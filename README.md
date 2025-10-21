# Dummy MariaDB Galera Cluster partitioning

This repository contains code to map a given customer to a particular MariaDB galera cluster in order to provide API functionality to write to their respective cluster.

## Installation

### API

API contains code to write to the database (using generic keys and values[1]) as well as list cluster nodes and register and deregister cluster nodes. Docker can be used to build and run the container. It takes the following environment variables:

* `MARIADB_USER` - this is the user to use to connect to the MariaDB node
* `MARIADB_PASSWORD` - this is the password used to connect to the MariaDB node

Note that OpenAPI Python client is provided.

### Synchronize node to API script

This script (`sync_node_to_api.py`) was tested on a Ubuntu 24.04 machine. It connects to the local MariaDB node (where it is intended to run) and checks the status of the node. If healthcheck and cluster UUID are ready, it registers the node (with the cluster UUID) to the API. In case these fail, the node deregisters (using IP[2]) from the API.

In order to install the script, make sure that:
1. Your cluster is setup correctly (openssh-server, rsync, cluster status)
2. You've installed the script into a location from which the cronjob can execute and that it meets the `requirements.txt` provided and can successfully run against the API and have linked it in `/usr/local/bin`

The script writes logs to `stdout` as well as `/var/log/sync_node_to_api.log`.

> NOTE: The API uses a random node to write to as MariaDB Galera runs in peer-to-peer mode.

#### Cronjob

The cronjob `sync_node_to_api` is intended to be ran every minute on each of the nodes where the above mentioned script runs.

Make sure to replace the `API_HOST_IP`, `DB_USERNAME` and `DB_PASSWORD` with the respective values to be able to connect to the API and the MariaDB local node.

You can create a dedicated user on the MariaDB nodes to have the script be able to read status.

## Execute against the API

If you want to execute against the API with your local machine (e.g. if you are running the MariaDB clusters with Docker and in a separate container you're running the API), you can use the OpenAPI server itself (available at `{{IP}}:{{PORT}}/docs`) or the client provided.

```python
import openapi_client
from openapi_client.api.default_api import DefaultApi
from openapi_client.api_client import ApiClient
configuration = openapi_client.configuration.Configuration()
configuration.host = "{{API_SERVER_IP}}"  # the server needs to run on port 80, mandatory
client = openapi_client.ApiClient(configuration)
api_service = DefaultApi(client)
```

### List all entries for a given cluster ID (customer)

```python
api_service.read_items_items_customer_id_get("efc4b73f-ab28-11f0-9cdd-7aca9ae0a672", "test", "customers")
```
```python
[]
```

### Add an entry for a given cluster ID

```python
api_service.put_item_items_customer_id_put("efc4b73f-ab28-11f0-9cdd-7aca9ae0a672", "test", "customers", 1, "test")
```
```python
{'success': True}
```

### Read an entry from a given cluster ID

```python
api_service.read_item_item_customer_id_id_get("efc4b73f-ab28-11f0-9cdd-7aca9ae0a672", 1, "test", "customers", "CustomerID")
```
```python
[[1, 'test']]
```

### Delete an entry from a given cluster ID

```python
api_service.delete_item_items_customer_id_delete("efc4b73f-ab28-11f0-9cdd-7aca9ae0a672", "test", "customers", "CustomerID", 1)
```
```python
{'success': True}
```

## Recommendations

Keep your MariaDB nodes in UTC time.

## Notes

This is really just a simple example of how a mapping would take place. In real life, there'd be dedicated APIs with their own storage that's offering the data store required to keep the mapping between the customers, their clusters and the respective cluster nodes by adding further functionality resembling that of a load balancer.

In this demo, I wanted to show how scaling clusters to match their users can be done. While it is not strict partitioning (sharding) that we see with NoSQL databases, it offers isolation from other clusters and minimizes latency due to synchronous replication in peer-to-peer mode with the other nodes to cluster level, enabling other customers to maintain performance.

## References

[1] In a real world scenario, this would be much more complex than what has been implemented here. Either by providing specific API calls for specific requests/actions to be completed, or offering a complete schema so that the user can use complex queries.

[2] In this model, we assume each IP is unique. In a real-world scenario, we'd want to have NAT going between clusters so that the scaling of cluster nodes won't be hindered by IP space exhaustion.

## License

[Apache-2.0 license](https://raw.githubusercontent.com/alghe-global/dummy_mariadb_galera_clustering/refs/heads/master/LICENSE)
