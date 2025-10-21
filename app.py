#!/usr/bin/env python

import os
import json
import random

from fastapi import FastAPI
from fastapi import HTTPException

from collections import defaultdict

import aiofiles
import aiomysql
from async_lru import alru_cache

MARIADB_USER = os.getenv("MARIADB_USER")
MARIADB_PASSWORD = os.getenv("MARIADB_PASSWORD")
MAPPING_FILE = os.getenv("MAPPING_FILE") or "customer_to_cluster_mapping.json"

app = FastAPI()

customer_to_cluster_mapping = json.load(open(MAPPING_FILE, "rb"))

@alru_cache()
async def get_mariadb_client(host: str):
    """
    Gets a client for MariaDB and returns it (cached)

    :return: client
    """
    client = await aiomysql.create_pool(
        host=host,
        port=3306,
        user=MARIADB_USER,
        password=MARIADB_PASSWORD
    )

    return client

@app.get("/")
async def root():
    return {"message": "Hello, world"}

@app.get("/health-check/{customer_id}")
async def health_check(customer_id: str, database: str):
    if customer_id not in customer_to_cluster_mapping.keys():
        return HTTPException(status_code=404, detail="Customer not found")

    registered_hosts = len(customer_to_cluster_mapping[customer_id]["cluster"])
    host = list(customer_to_cluster_mapping[customer_id]["cluster"])[random.randint(0, registered_hosts-1)]
    pool = await get_mariadb_client(host)
    async with pool.acquire() as conn:
        async with conn.cursor() as cursor:
            await cursor.execute("USE {0};".format(database))
            await cursor.execute("SHOW STATUS LIKE 'wsrep_connected';")
            row = await cursor.fetchone()

            if isinstance(row, tuple) and "ON" in row:
                return {"status": "Healthy"}

    return HTTPException(status_code=502)

@app.get("/items/{customer_id}")
async def read_items(customer_id: str, database: str, table: str):
    if customer_id not in customer_to_cluster_mapping.keys():
        return HTTPException(status_code=404, detail="Customer not found")

    registered_hosts = len(customer_to_cluster_mapping[customer_id]["cluster"])
    host = list(customer_to_cluster_mapping[customer_id]["cluster"])[random.randint(0, registered_hosts-1)]

    pool = await get_mariadb_client(host)
    async with pool.acquire() as conn:
        async with conn.cursor() as cursor:
            await cursor.execute("USE {0};".format(database))
            await cursor.execute("SELECT * FROM {0};".format(table))
            rows = await cursor.fetchall()

            return rows

    return HTTPException(status_code=502)

@app.get("/item/{customer_id}/{id}")
async def read_item(customer_id: str, id: int, database: str, table: str, key: str):
    if customer_id not in customer_to_cluster_mapping.keys():
        return HTTPException(status_code=404, detail="Customer not found")

    registered_hosts = len(customer_to_cluster_mapping[customer_id]["cluster"])
    host = list(customer_to_cluster_mapping[customer_id]["cluster"])[random.randint(0, registered_hosts-1)]

    pool = await get_mariadb_client(host)
    async with pool.acquire() as conn:
        async with conn.cursor() as cursor:
            await cursor.execute("USE {0};".format(database))
            await cursor.execute("SELECT * FROM {0} WHERE {1}='{2}';".format(
                table,
                key,
                id
            ))
            rows = await cursor.fetchall()

            if isinstance(rows, tuple) and len(rows) > 0:
                return rows
            elif isinstance(rows, tuple) and len(rows) == 0:
                return HTTPException(status_code=404)

    return HTTPException(status_code=502)

@app.put("/items/{customer_id}")
async def put_item(
    customer_id: str,
    database: str,
    table: str,
    id: int,
    value: str
):
    """
    Put an item in **database** using table **table** with values (**id**, **value**)

    NOTE: Works only for tables with a primary key (id) and an additional key (with value **value**)
    """

    if customer_id not in customer_to_cluster_mapping.keys():
        return HTTPException(status_code=404, detail="Customer not found")

    registered_hosts = len(customer_to_cluster_mapping[customer_id]["cluster"])
    host = list(customer_to_cluster_mapping[customer_id]["cluster"])[random.randint(0, registered_hosts-1)]

    pool = await get_mariadb_client(host)
    async with pool.acquire() as conn:
        async with conn.cursor() as cursor:
            await cursor.execute("USE {0};".format(database))
            await cursor.execute("INSERT INTO {0} VALUES ({1}, '{2}');".format(
                table,
                id,
                value
            ))
            await conn.commit()

            return {"success": True}

    return HTTPException(status_code=502)

@app.delete("/items/{customer_id}")
async def delete_item(
    customer_id: str,
    database: str,
    table: str,
    id_key: str,
    id: int
):
    """
    Delete an item from **database** using table **table** with primary key **id_key** and id **id**

    NOTE: Works only for tables with a primary key (id)
    """

    if customer_id not in customer_to_cluster_mapping.keys():
        return HTTPException(status_code=404, detail="Customer not found")

    registered_hosts = len(customer_to_cluster_mapping[customer_id]["cluster"])
    host = list(customer_to_cluster_mapping[customer_id]["cluster"])[random.randint(0, registered_hosts-1)]

    pool = await get_mariadb_client(host)
    async with pool.acquire() as conn:
        async with conn.cursor() as cursor:
            await cursor.execute("USE {0};".format(database))
            await cursor.execute("DELETE FROM {0} WHERE {1}='{2}';".format(
                table,
                id_key,
                id
            ))
            await conn.commit()

            return {"success": True}

    return HTTPException(status_code=502)

################################################
# Customer to MariaDB Galera cluster mapping API
################################################

async def flush_state_to_disk(file: str, state: dict) -> bool:
    """
    Utility to asynchronously write to disk API cluster mapping state

    NOTE: Normally, a better datastore would be used here (such as a database)

    :param file: The file to write to
    :type file: str
    :param state: The state to write to disk
    :type state: dict
    """

    async with aiofiles.open(file, "w") as fobj:
        await fobj.write(json.dumps(state))
        await fobj.flush()
        return True

    return False

@app.get("/cluster")
async def read_cluster_status():
    return customer_to_cluster_mapping

@app.get("/cluster/{customer_id}")
async def read_customer_cluster_status(customer_id: str):
    ret = customer_to_cluster_mapping.get(customer_id)
    if ret is None:
        return HTTPException(status_code=404, detail="Customer not found")

    return ret

@app.put("/cluster/{customer_id}")
async def register_cluster_node(customer_id: str, node_ip: str):
    ret = customer_to_cluster_mapping.get(customer_id)
    if ret is None:
        customer_to_cluster_mapping[customer_id] = {"cluster": []}

    if node_ip not in customer_to_cluster_mapping[customer_id].get("cluster", []):
        customer_to_cluster_mapping[customer_id]["cluster"].append(node_ip)
        await flush_state_to_disk(MAPPING_FILE, customer_to_cluster_mapping)

    return node_ip

@app.delete("/cluster/{node_ip}")
async def deregister_cluster_node(node_ip: str):
    """
    Normally, there'd be an intermediary keeping a mapping of customer_id to
    node_ip which would talk to this API acting as a sort of loadbalancer (healthcheck wise)

    In absence of such middleware, we simply assume IP is unique per customer_id (cluster).
    Thus, removing an IP would not remove any other node.
    """

    for customer_id in customer_to_cluster_mapping.keys():
        if node_ip in customer_to_cluster_mapping[customer_id].get("cluster", []):
            customer_to_cluster_mapping[customer_id]["cluster"].remove(node_ip)
            await flush_state_to_disk(MAPPING_FILE, customer_to_cluster_mapping)

            return node_ip

    return HTTPException(status_code=404, detail="Customer not found")
