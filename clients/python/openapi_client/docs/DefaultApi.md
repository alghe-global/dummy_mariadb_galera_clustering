# openapi_client.DefaultApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_item_items_customer_id_delete**](DefaultApi.md#delete_item_items_customer_id_delete) | **DELETE** /items/{customer_id} | Delete Item
[**health_check_health_check_customer_id_get**](DefaultApi.md#health_check_health_check_customer_id_get) | **GET** /health-check/{customer_id} | Health Check
[**put_item_items_customer_id_put**](DefaultApi.md#put_item_items_customer_id_put) | **PUT** /items/{customer_id} | Put Item
[**read_cluster_status_cluster_get**](DefaultApi.md#read_cluster_status_cluster_get) | **GET** /cluster | Read Cluster Status
[**read_customer_cluster_status_cluster_customer_id_get**](DefaultApi.md#read_customer_cluster_status_cluster_customer_id_get) | **GET** /cluster/{customer_id} | Read Customer Cluster Status
[**read_item_item_customer_id_id_get**](DefaultApi.md#read_item_item_customer_id_id_get) | **GET** /item/{customer_id}/{id} | Read Item
[**read_items_items_customer_id_get**](DefaultApi.md#read_items_items_customer_id_get) | **GET** /items/{customer_id} | Read Items
[**register_cluster_node_cluster_customer_id_put**](DefaultApi.md#register_cluster_node_cluster_customer_id_put) | **PUT** /cluster/{customer_id} | Register Cluster Node
[**register_cluster_node_cluster_node_ip_delete**](DefaultApi.md#register_cluster_node_cluster_node_ip_delete) | **DELETE** /cluster/{node_ip} | Register Cluster Node
[**root_get**](DefaultApi.md#root_get) | **GET** / | Root


# **delete_item_items_customer_id_delete**
> object delete_item_items_customer_id_delete(customer_id, database, table, id_key, id)

Delete Item

Delete an item from **database** using table **table** with primary key **id_key** and id **id**

NOTE: Works only for tables with a primary key (id)

### Example


```python
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    customer_id = 'customer_id_example' # str | 
    database = 'database_example' # str | 
    table = 'table_example' # str | 
    id_key = 'id_key_example' # str | 
    id = 56 # int | 

    try:
        # Delete Item
        api_response = api_instance.delete_item_items_customer_id_delete(customer_id, database, table, id_key, id)
        print("The response of DefaultApi->delete_item_items_customer_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->delete_item_items_customer_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**|  | 
 **database** | **str**|  | 
 **table** | **str**|  | 
 **id_key** | **str**|  | 
 **id** | **int**|  | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **health_check_health_check_customer_id_get**
> object health_check_health_check_customer_id_get(customer_id, database)

Health Check

### Example


```python
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    customer_id = 'customer_id_example' # str | 
    database = 'database_example' # str | 

    try:
        # Health Check
        api_response = api_instance.health_check_health_check_customer_id_get(customer_id, database)
        print("The response of DefaultApi->health_check_health_check_customer_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->health_check_health_check_customer_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**|  | 
 **database** | **str**|  | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_item_items_customer_id_put**
> object put_item_items_customer_id_put(customer_id, database, table, id, value)

Put Item

Put an item in **database** using table **table** with values (**id**, **value**)

NOTE: Works only for tables with a primary key (id) and an additional key (with value **value**)

### Example


```python
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    customer_id = 'customer_id_example' # str | 
    database = 'database_example' # str | 
    table = 'table_example' # str | 
    id = 56 # int | 
    value = 'value_example' # str | 

    try:
        # Put Item
        api_response = api_instance.put_item_items_customer_id_put(customer_id, database, table, id, value)
        print("The response of DefaultApi->put_item_items_customer_id_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->put_item_items_customer_id_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**|  | 
 **database** | **str**|  | 
 **table** | **str**|  | 
 **id** | **int**|  | 
 **value** | **str**|  | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_cluster_status_cluster_get**
> object read_cluster_status_cluster_get()

Read Cluster Status

### Example


```python
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)

    try:
        # Read Cluster Status
        api_response = api_instance.read_cluster_status_cluster_get()
        print("The response of DefaultApi->read_cluster_status_cluster_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->read_cluster_status_cluster_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_customer_cluster_status_cluster_customer_id_get**
> object read_customer_cluster_status_cluster_customer_id_get(customer_id)

Read Customer Cluster Status

### Example


```python
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    customer_id = 'customer_id_example' # str | 

    try:
        # Read Customer Cluster Status
        api_response = api_instance.read_customer_cluster_status_cluster_customer_id_get(customer_id)
        print("The response of DefaultApi->read_customer_cluster_status_cluster_customer_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->read_customer_cluster_status_cluster_customer_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**|  | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_item_item_customer_id_id_get**
> object read_item_item_customer_id_id_get(customer_id, id, database, table, key)

Read Item

### Example


```python
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    customer_id = 'customer_id_example' # str | 
    id = 56 # int | 
    database = 'database_example' # str | 
    table = 'table_example' # str | 
    key = 'key_example' # str | 

    try:
        # Read Item
        api_response = api_instance.read_item_item_customer_id_id_get(customer_id, id, database, table, key)
        print("The response of DefaultApi->read_item_item_customer_id_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->read_item_item_customer_id_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**|  | 
 **id** | **int**|  | 
 **database** | **str**|  | 
 **table** | **str**|  | 
 **key** | **str**|  | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_items_items_customer_id_get**
> object read_items_items_customer_id_get(customer_id, database, table)

Read Items

### Example


```python
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    customer_id = 'customer_id_example' # str | 
    database = 'database_example' # str | 
    table = 'table_example' # str | 

    try:
        # Read Items
        api_response = api_instance.read_items_items_customer_id_get(customer_id, database, table)
        print("The response of DefaultApi->read_items_items_customer_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->read_items_items_customer_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**|  | 
 **database** | **str**|  | 
 **table** | **str**|  | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **register_cluster_node_cluster_customer_id_put**
> object register_cluster_node_cluster_customer_id_put(customer_id, node_ip)

Register Cluster Node

### Example


```python
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    customer_id = 'customer_id_example' # str | 
    node_ip = 'node_ip_example' # str | 

    try:
        # Register Cluster Node
        api_response = api_instance.register_cluster_node_cluster_customer_id_put(customer_id, node_ip)
        print("The response of DefaultApi->register_cluster_node_cluster_customer_id_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->register_cluster_node_cluster_customer_id_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**|  | 
 **node_ip** | **str**|  | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **register_cluster_node_cluster_node_ip_delete**
> object register_cluster_node_cluster_node_ip_delete(node_ip)

Register Cluster Node

Normally, there'd be an intermediary keeping a mapping of customer_id to
node_ip which would talk to this API acting as a sort of loadbalancer (healthcheck wise)

In absence of such middleware, we simply assume IP is unique per customer_id (cluster).
Thus, removing an IP would not remove any other node.

### Example


```python
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    node_ip = 'node_ip_example' # str | 

    try:
        # Register Cluster Node
        api_response = api_instance.register_cluster_node_cluster_node_ip_delete(node_ip)
        print("The response of DefaultApi->register_cluster_node_cluster_node_ip_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->register_cluster_node_cluster_node_ip_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **node_ip** | **str**|  | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **root_get**
> object root_get()

Root

### Example


```python
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)

    try:
        # Root
        api_response = api_instance.root_get()
        print("The response of DefaultApi->root_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->root_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

