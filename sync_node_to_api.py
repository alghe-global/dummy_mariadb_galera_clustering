#!/usr/bin/env python3

import os
import sys
import time
import socket
import logging

import asyncio
import aiomysql

import openapi_client
from openapi_client.api.default_api import DefaultApi
from openapi_client.api_client import ApiClient

API_HOST = os.getenv("API_HOST")
MARIADB_USERNAME = os.getenv("MARIADB_USERNAME")
MARIADB_PASSWORD = os.getenv("MARIADB_PASSWORD")

LOG_PATH="/var/log"
LOG_FILENAME="sync_node_to_api"
LOG_FORMATTER = logging.Formatter(
    '[%(asctime)s.%(msecs)06dZ] [%(levelname)s] %(message)s',
    datefmt="%Y-%m-%dT%H:%M:%S")

logger = logging.getLogger(__name__)

fileHandler = logging.FileHandler("{0}/{1}.log".format(LOG_PATH, LOG_FILENAME))
fileHandler.setFormatter(LOG_FORMATTER)
logger.addHandler(fileHandler)

streamHandler = logging.StreamHandler(sys.stdout)
streamHandler.setFormatter(LOG_FORMATTER)
logger.addHandler(streamHandler)

logger.setLevel(logging.DEBUG)

if not all([API_HOST, MARIADB_USERNAME, MARIADB_PASSWORD]):
    logger.critical("One or more nvironment variable(s) not defined, exiting...")
    sys.exit(1)

def get_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.settimeout(0)
    try:
        # doesn't even have to be reachable
        s.connect(("10.254.254.254", 1))
        IP = s.getsockname()[0]
    except Exception as e:
        logger.critical(f"Failed to get IP: {e}")
        raise Exception("Failed to get IP", e)
    finally:
        s.close()
    return IP

async def get_mariadb_client():
    try:
        client = await aiomysql.create_pool(
            host="localhost",
            port=3306,
            user=MARIADB_USERNAME,
            password=MARIADB_PASSWORD
        )

        return client
    except Exception as e:
        logger.critical(f"Failed to connect to local MariaDB instance: {e}")
        return None

async def ping_db(client, retry=5):
    row = []

    async with client.acquire() as conn:
        async with conn.cursor() as cursor:
            await cursor.execute("SHOW STATUS LIKE 'wsrep_ready';")
            row = await cursor.fetchall()
            await cursor.close()
            conn.close()

            if row is None or len(row) == 0:
                logger.critical("Failed to get healthcheck status from node...")
                return False

    for i in range(retry):
        if row[0][-1] == "ON":
            logger.debug("Healthcheck succeeded")
            return True

        logger.info(f"{i}/{retry-1} Waiting for node to be ready...")
        time.sleep(1)

    logger.critical("Failed healthcheck due to node not being ready...")
    return False

async def get_cluster_state_uuid(client):
    async with client.acquire() as conn:
        async with conn.cursor() as cursor:
            await cursor.execute("SHOW STATUS LIKE 'wsrep_cluster_state_uuid';")
            row = await cursor.fetchall()
            await cursor.close()
            conn.close()

            if row is None or len(row) == 0:
                logger.critical("Failed to get cluster state UUID...")
                return None

            return row[0][-1]

async def synchronize_node_ip_to_api(ip, api_client, mysql_client):
    try:
        healthcheck = await ping_db(mysql_client)

        if healthcheck:
            cluster_state_uuid = await get_cluster_state_uuid(mysql_client)

            if cluster_state_uuid is not None:
                api_client.register_cluster_node_cluster_customer_id_put(cluster_state_uuid, ip)
                logger.debug(f"Successfully registered node with cluster_state_uuid: {cluster_state_uuid} and ip: {ip}")
                return True
            else:
                api_client.deregister_cluster_node_cluster_node_ip_delete(ip)
                logger.critical(f"Couldn't get cluster state UUID. Deregistered node (ip: {ip})")
                return False
        else:
            logger.critical("Healthcheck failed... Deregistering node.")
            api_client.deregister_cluster_node_cluster_node_ip_delete(ip)
            return False
    except Exception as e:
        logger.info(f"Unable to register node ip: {ip} to API ({e}). Deregistering node")
        api_client.deregister_cluster_node_cluster_node_ip_delete(ip)
        return False

    return False

async def main(api_client):
    ip = get_ip()

    mysql_client = await get_mariadb_client()
    if mysql_client:
        logger.debug("Instantiated MySQL client")
    else:
        logger.critical("Failed to instantiate MySQL client. Deregistering node.")
        api_client.deregister_cluster_node_cluster_node_ip_delete(ip)
        sys.exit(1)

    result = await synchronize_node_ip_to_api(ip, api_service, mysql_client)

    if result:
        logger.info("Successfully registered node to API")
        sys.exit(0)
    else:
        logger.critical("Failed to register node to API")
        sys.exit(1)

if __name__ == "__main__":
    configuration = openapi_client.configuration.Configuration()
    configuration.host = API_HOST
    api_client = openapi_client.ApiClient(configuration)
    api_service = DefaultApi(api_client)
    logging.debug(f"Instantiated API client to host: {API_HOST}")

    asyncio.run(main(api_service))
