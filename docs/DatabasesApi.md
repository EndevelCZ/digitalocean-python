# digitalocean_client.DatabasesApi

All URIs are relative to *https://api.digitalocean.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_connection_pool**](DatabasesApi.md#add_connection_pool) | **POST** /v2/databases/{database_cluster_uuid}/pools | Add a New Connection Pool (PostgreSQL)
[**add_database**](DatabasesApi.md#add_database) | **POST** /v2/databases/{database_cluster_uuid}/dbs | Add a New Database
[**add_user**](DatabasesApi.md#add_user) | **POST** /v2/databases/{database_cluster_uuid}/users | Add a Database User
[**create_database_cluster**](DatabasesApi.md#create_database_cluster) | **POST** /v2/databases | Create a New Database Cluster
[**create_replica**](DatabasesApi.md#create_replica) | **POST** /v2/databases/{database_cluster_uuid}/replicas | Create a Read-only Replica
[**delete_connection_pool**](DatabasesApi.md#delete_connection_pool) | **DELETE** /v2/databases/{database_cluster_uuid}/pools/{pool_name} | Delete a Connection Pool (PostgreSQL)
[**delete_database**](DatabasesApi.md#delete_database) | **DELETE** /v2/databases/{database_cluster_uuid}/dbs/{database_name} | Delete a Database
[**delete_online_migration**](DatabasesApi.md#delete_online_migration) | **DELETE** /v2/databases/{database_cluster_uuid}/online-migration/{migration_id} | Stop an Online Migration
[**delete_user**](DatabasesApi.md#delete_user) | **DELETE** /v2/databases/{database_cluster_uuid}/users/{username} | Remove a Database User
[**destroy_cluster**](DatabasesApi.md#destroy_cluster) | **DELETE** /v2/databases/{database_cluster_uuid} | Destroy a Database Cluster
[**destroy_replica**](DatabasesApi.md#destroy_replica) | **DELETE** /v2/databases/{database_cluster_uuid}/replicas/{replica_name} | Destroy a Read-only Replica
[**get_ca**](DatabasesApi.md#get_ca) | **GET** /v2/databases/{database_cluster_uuid}/ca | Retrieve the Public Certificate
[**get_connection_pool**](DatabasesApi.md#get_connection_pool) | **GET** /v2/databases/{database_cluster_uuid}/pools/{pool_name} | Retrieve Existing Connection Pool (PostgreSQL)
[**get_database**](DatabasesApi.md#get_database) | **GET** /v2/databases/{database_cluster_uuid}/dbs/{database_name} | Retrieve an Existing Database
[**get_database_cluster**](DatabasesApi.md#get_database_cluster) | **GET** /v2/databases/{database_cluster_uuid} | Retrieve an Existing Database Cluster
[**get_eviction_policy**](DatabasesApi.md#get_eviction_policy) | **GET** /v2/databases/{database_cluster_uuid}/eviction_policy | Retrieve the Eviction Policy for a Redis Cluster
[**get_migration_status**](DatabasesApi.md#get_migration_status) | **GET** /v2/databases/{database_cluster_uuid}/online-migration | Retrieve the Status of an Online Migration
[**get_replica**](DatabasesApi.md#get_replica) | **GET** /v2/databases/{database_cluster_uuid}/replicas/{replica_name} | Retrieve an Existing Read-only Replica
[**get_sql_mode**](DatabasesApi.md#get_sql_mode) | **GET** /v2/databases/{database_cluster_uuid}/sql_mode | Retrieve the SQL Modes for a MySQL Cluster
[**get_user**](DatabasesApi.md#get_user) | **GET** /v2/databases/{database_cluster_uuid}/users/{username} | Retrieve an Existing Database User
[**list_connection_pools**](DatabasesApi.md#list_connection_pools) | **GET** /v2/databases/{database_cluster_uuid}/pools | List Connection Pools (PostgreSQL)
[**list_database_backups**](DatabasesApi.md#list_database_backups) | **GET** /v2/databases/{database_cluster_uuid}/backups | List Backups for a Database Cluster
[**list_database_clusters**](DatabasesApi.md#list_database_clusters) | **GET** /v2/databases | List All Database Clusters
[**list_database_firewalls**](DatabasesApi.md#list_database_firewalls) | **GET** /v2/databases/{database_cluster_uuid}/firewall | List Firewall Rules (Trusted Sources) for a Database Cluster
[**list_databases**](DatabasesApi.md#list_databases) | **GET** /v2/databases/{database_cluster_uuid}/dbs | List All Databases
[**list_replicas**](DatabasesApi.md#list_replicas) | **GET** /v2/databases/{database_cluster_uuid}/replicas | List All Read-only Replicas
[**list_users**](DatabasesApi.md#list_users) | **GET** /v2/databases/{database_cluster_uuid}/users | List all Database Users
[**reset_auth**](DatabasesApi.md#reset_auth) | **POST** /v2/databases/{database_cluster_uuid}/users/{username}/reset_auth | Reset a Database User&#39;s Password or Authentication Method
[**update_database_cluster**](DatabasesApi.md#update_database_cluster) | **PUT** /v2/databases/{database_cluster_uuid}/migrate | Migrate a Database Cluster to a New Region
[**update_database_cluster_size**](DatabasesApi.md#update_database_cluster_size) | **PUT** /v2/databases/{database_cluster_uuid}/resize | Resize a Database Cluster
[**update_database_firewall**](DatabasesApi.md#update_database_firewall) | **PUT** /v2/databases/{database_cluster_uuid}/firewall | Update Firewall Rules (Trusted Sources) for a Database
[**update_eviction_policy**](DatabasesApi.md#update_eviction_policy) | **PUT** /v2/databases/{database_cluster_uuid}/eviction_policy | Configure the Eviction Policy for a Redis Cluster
[**update_maintenance_window**](DatabasesApi.md#update_maintenance_window) | **PUT** /v2/databases/{database_cluster_uuid}/maintenance | Configure a Database Cluster&#39;s Maintenance Window
[**update_online_migration**](DatabasesApi.md#update_online_migration) | **PUT** /v2/databases/{database_cluster_uuid}/online-migration | Start an Online Migration
[**update_sql_mode**](DatabasesApi.md#update_sql_mode) | **PUT** /v2/databases/{database_cluster_uuid}/sql_mode | Update SQL Mode for a Cluster


# **add_connection_pool**
> InlineResponse2015 add_connection_pool(database_cluster_uuid, connection_pool)

Add a New Connection Pool (PostgreSQL)

For PostgreSQL database clusters, connection pools can be used to allow a database to share its idle connections. The popular PostgreSQL connection pooling utility PgBouncer is used to provide this service. [See here for more information](https://www.digitalocean.com/docs/databases/postgresql/how-to/manage-connection-pools/) about how and why to use PgBouncer connection pooling including details about the available transaction modes.  To add a new connection pool to a PostgreSQL database cluster, send a POST request to `/v2/databases/$DATABASE_ID/pools` specifying a name for the pool, the user to connect with, the database to connect to, as well as its desired size and transaction mode. 

### Example

* Bearer Authentication (bearer_auth):

```python
import time
import digitalocean_client
from digitalocean_client.api import databases_api
from digitalocean_client.model.connection_pool import ConnectionPool
from digitalocean_client.model.error import Error
from digitalocean_client.model.inline_response2015 import InlineResponse2015
from pprint import pprint
# Defining the host is optional and defaults to https://api.digitalocean.com
# See configuration.py for a list of all supported configuration parameters.
configuration = digitalocean_client.Configuration(
    host = "https://api.digitalocean.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: bearer_auth
configuration = digitalocean_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with digitalocean_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = databases_api.DatabasesApi(api_client)
    database_cluster_uuid = "9cc10173-e9ea-4176-9dbc-a4cee4c4ff30" # str | A unique identifier for a database cluster.
    connection_pool = ConnectionPool(
        name="backend-pool",
        mode="transaction",
        size=10,
        db="defaultdb",
        user="doadmin",
        connection=None,
        private_connection=None,
    ) # ConnectionPool | 

    # example passing only required values which don't have defaults set
    try:
        # Add a New Connection Pool (PostgreSQL)
        api_response = api_instance.add_connection_pool(database_cluster_uuid, connection_pool)
        pprint(api_response)
    except digitalocean_client.ApiException as e:
        print("Exception when calling DatabasesApi->add_connection_pool: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **database_cluster_uuid** | **str**| A unique identifier for a database cluster. |
 **connection_pool** | [**ConnectionPool**](ConnectionPool.md)|  |

### Return type

[**InlineResponse2015**](InlineResponse2015.md)

### Authorization

[bearer_auth](../README.md#bearer_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | A JSON object with a key of &#x60;pool&#x60;. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**401** | Unauthorized |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**404** | The resource was not found. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**429** | API Rate limit exceeded |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**500** | Server error. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**0** | Unexpected error |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_database**
> InlineResponse2014 add_database(database_cluster_uuid, database)

Add a New Database

To add a new database to an existing cluster, send a POST request to `/v2/databases/$DATABASE_ID/dbs`.  Note: Database management is not supported for Redis clusters.  The response will be a JSON object with a key called `db`. The value of this will be an object that contains the standard attributes associated with a database. 

### Example

* Bearer Authentication (bearer_auth):

```python
import time
import digitalocean_client
from digitalocean_client.api import databases_api
from digitalocean_client.model.inline_response2014 import InlineResponse2014
from digitalocean_client.model.error import Error
from digitalocean_client.model.database import Database
from pprint import pprint
# Defining the host is optional and defaults to https://api.digitalocean.com
# See configuration.py for a list of all supported configuration parameters.
configuration = digitalocean_client.Configuration(
    host = "https://api.digitalocean.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: bearer_auth
configuration = digitalocean_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with digitalocean_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = databases_api.DatabasesApi(api_client)
    database_cluster_uuid = "9cc10173-e9ea-4176-9dbc-a4cee4c4ff30" # str | A unique identifier for a database cluster.
    database = Database(
        name="alpha",
    ) # Database | 

    # example passing only required values which don't have defaults set
    try:
        # Add a New Database
        api_response = api_instance.add_database(database_cluster_uuid, database)
        pprint(api_response)
    except digitalocean_client.ApiException as e:
        print("Exception when calling DatabasesApi->add_database: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **database_cluster_uuid** | **str**| A unique identifier for a database cluster. |
 **database** | [**Database**](Database.md)|  |

### Return type

[**InlineResponse2014**](InlineResponse2014.md)

### Authorization

[bearer_auth](../README.md#bearer_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | A JSON object with a key of &#x60;db&#x60;. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**401** | Unauthorized |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**404** | The resource was not found. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**429** | API Rate limit exceeded |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**500** | Server error. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**0** | Unexpected error |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_user**
> InlineResponse2013 add_user(database_cluster_uuid, database_user)

Add a Database User

To add a new database user, send a POST request to `/v2/databases/$DATABASE_ID/users` with the desired username.  Note: User management is not supported for Redis clusters.  When adding a user to a MySQL cluster, additional options can be configured in the `mysql_settings` object.  The response will be a JSON object with a key called `user`. The value of this will be an object that contains the standard attributes associated with a database user including its randomly generated password. 

### Example

* Bearer Authentication (bearer_auth):

```python
import time
import digitalocean_client
from digitalocean_client.api import databases_api
from digitalocean_client.model.inline_response2013 import InlineResponse2013
from digitalocean_client.model.database_user import DatabaseUser
from digitalocean_client.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to https://api.digitalocean.com
# See configuration.py for a list of all supported configuration parameters.
configuration = digitalocean_client.Configuration(
    host = "https://api.digitalocean.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: bearer_auth
configuration = digitalocean_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with digitalocean_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = databases_api.DatabasesApi(api_client)
    database_cluster_uuid = "9cc10173-e9ea-4176-9dbc-a4cee4c4ff30" # str | A unique identifier for a database cluster.
    database_user = DatabaseUser(
        name="app-01",
        mysql_settings=MysqlSettings(
            auth_plugin="mysql_native_password",
        ),
    ) # DatabaseUser | 

    # example passing only required values which don't have defaults set
    try:
        # Add a Database User
        api_response = api_instance.add_user(database_cluster_uuid, database_user)
        pprint(api_response)
    except digitalocean_client.ApiException as e:
        print("Exception when calling DatabasesApi->add_user: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **database_cluster_uuid** | **str**| A unique identifier for a database cluster. |
 **database_user** | [**DatabaseUser**](DatabaseUser.md)|  |

### Return type

[**InlineResponse2013**](InlineResponse2013.md)

### Authorization

[bearer_auth](../README.md#bearer_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | A JSON object with a key of &#x60;user&#x60;. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**401** | Unauthorized |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**404** | The resource was not found. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**429** | API Rate limit exceeded |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**500** | Server error. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**0** | Unexpected error |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_database_cluster**
> InlineResponse2011 create_database_cluster(unknown_base_type)

Create a New Database Cluster

To create a database cluster, send a POST request to `/v2/databases`. The response will be a JSON object with a key called `database`. The value of this will be an object that contains the standard attributes associated with a database cluster. The initial value of the database cluster's `status` attribute will be `creating`. When the cluster is ready to receive traffic, this will transition to `online`. The embedded `connection` and `private_connection` objects will contain the information needed to access the database cluster. DigitalOcean managed PostgreSQL and MySQL database clusters take automated daily backups. To create a new database cluster based on a backup of an exising cluster, send a POST request to `/v2/databases`. In addition to the standard database cluster attributes, the JSON body must include a key named `backup_restore` with the name of the original database cluster and the timestamp of the backup to be restored. Note: Backups are not supported for Redis clusters.

### Example

* Bearer Authentication (bearer_auth):

```python
import time
import digitalocean_client
from digitalocean_client.api import databases_api
from digitalocean_client.model.inline_response2011 import InlineResponse2011
from digitalocean_client.model.unknownbasetype import UNKNOWNBASETYPE
from digitalocean_client.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to https://api.digitalocean.com
# See configuration.py for a list of all supported configuration parameters.
configuration = digitalocean_client.Configuration(
    host = "https://api.digitalocean.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: bearer_auth
configuration = digitalocean_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with digitalocean_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = databases_api.DatabasesApi(api_client)
    unknown_base_type = None # UNKNOWN_BASE_TYPE | 

    # example passing only required values which don't have defaults set
    try:
        # Create a New Database Cluster
        api_response = api_instance.create_database_cluster(unknown_base_type)
        pprint(api_response)
    except digitalocean_client.ApiException as e:
        print("Exception when calling DatabasesApi->create_database_cluster: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **unknown_base_type** | [**UNKNOWN_BASE_TYPE**](UNKNOWN_BASE_TYPE.md)|  |

### Return type

[**InlineResponse2011**](InlineResponse2011.md)

### Authorization

[bearer_auth](../README.md#bearer_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | A JSON object with a key of &#x60;database&#x60;. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**401** | Unauthorized |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**404** | The resource was not found. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**429** | API Rate limit exceeded |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**500** | Server error. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**0** | Unexpected error |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_replica**
> InlineResponse2012 create_replica(database_cluster_uuid)

Create a Read-only Replica

To create a read-only replica for a PostgreSQL or MySQL database cluster, send a POST request to `/v2/databases/$DATABASE_ID/replicas` specifying the name it should be given, the size of the node to be used, and the region where it will be located. **Note**: Read-only replicas are not supported for Redis clusters. The response will be a JSON object with a key called `replica`. The value of this will be an object that contains the standard attributes associated with a database replica. The initial value of the read-only replica's `status` attribute will be `forking`. When the replica is ready to receive traffic, this will transition to `active`.

### Example

* Bearer Authentication (bearer_auth):

```python
import time
import digitalocean_client
from digitalocean_client.api import databases_api
from digitalocean_client.model.inline_response2012 import InlineResponse2012
from digitalocean_client.model.unknownbasetype import UNKNOWNBASETYPE
from digitalocean_client.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to https://api.digitalocean.com
# See configuration.py for a list of all supported configuration parameters.
configuration = digitalocean_client.Configuration(
    host = "https://api.digitalocean.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: bearer_auth
configuration = digitalocean_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with digitalocean_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = databases_api.DatabasesApi(api_client)
    database_cluster_uuid = "9cc10173-e9ea-4176-9dbc-a4cee4c4ff30" # str | A unique identifier for a database cluster.
    unknown_base_type = None # UNKNOWN_BASE_TYPE |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Create a Read-only Replica
        api_response = api_instance.create_replica(database_cluster_uuid)
        pprint(api_response)
    except digitalocean_client.ApiException as e:
        print("Exception when calling DatabasesApi->create_replica: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create a Read-only Replica
        api_response = api_instance.create_replica(database_cluster_uuid, unknown_base_type=unknown_base_type)
        pprint(api_response)
    except digitalocean_client.ApiException as e:
        print("Exception when calling DatabasesApi->create_replica: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **database_cluster_uuid** | **str**| A unique identifier for a database cluster. |
 **unknown_base_type** | [**UNKNOWN_BASE_TYPE**](UNKNOWN_BASE_TYPE.md)|  | [optional]

### Return type

[**InlineResponse2012**](InlineResponse2012.md)

### Authorization

[bearer_auth](../README.md#bearer_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | A JSON object with a key of &#x60;replica&#x60;. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**401** | Unauthorized |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**404** | The resource was not found. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**429** | API Rate limit exceeded |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**500** | Server error. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**0** | Unexpected error |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_connection_pool**
> delete_connection_pool(database_cluster_uuid, pool_name)

Delete a Connection Pool (PostgreSQL)

To delete a specific connection pool for a PostgreSQL database cluster, send a DELETE request to `/v2/databases/$DATABASE_ID/pools/$POOL_NAME`.  A status of 204 will be given. This indicates that the request was processed successfully, but that no response body is needed. 

### Example

* Bearer Authentication (bearer_auth):

```python
import time
import digitalocean_client
from digitalocean_client.api import databases_api
from digitalocean_client.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to https://api.digitalocean.com
# See configuration.py for a list of all supported configuration parameters.
configuration = digitalocean_client.Configuration(
    host = "https://api.digitalocean.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: bearer_auth
configuration = digitalocean_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with digitalocean_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = databases_api.DatabasesApi(api_client)
    database_cluster_uuid = "9cc10173-e9ea-4176-9dbc-a4cee4c4ff30" # str | A unique identifier for a database cluster.
    pool_name = "backend-pool" # str | The name used to identify the connection pool.

    # example passing only required values which don't have defaults set
    try:
        # Delete a Connection Pool (PostgreSQL)
        api_instance.delete_connection_pool(database_cluster_uuid, pool_name)
    except digitalocean_client.ApiException as e:
        print("Exception when calling DatabasesApi->delete_connection_pool: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **database_cluster_uuid** | **str**| A unique identifier for a database cluster. |
 **pool_name** | **str**| The name used to identify the connection pool. |

### Return type

void (empty response body)

### Authorization

[bearer_auth](../README.md#bearer_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | The action was successful and the response body is empty. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**401** | Unauthorized |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**404** | The resource was not found. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**429** | API Rate limit exceeded |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**500** | Server error. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**0** | Unexpected error |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_database**
> delete_database(database_cluster_uuid, database_name)

Delete a Database

To delete a specific database, send a DELETE request to `/v2/databases/$DATABASE_ID/dbs/$DB_NAME`.  A status of 204 will be given. This indicates that the request was processed successfully, but that no response body is needed.  Note: Database management is not supported for Redis clusters. 

### Example

* Bearer Authentication (bearer_auth):

```python
import time
import digitalocean_client
from digitalocean_client.api import databases_api
from digitalocean_client.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to https://api.digitalocean.com
# See configuration.py for a list of all supported configuration parameters.
configuration = digitalocean_client.Configuration(
    host = "https://api.digitalocean.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: bearer_auth
configuration = digitalocean_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with digitalocean_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = databases_api.DatabasesApi(api_client)
    database_cluster_uuid = "9cc10173-e9ea-4176-9dbc-a4cee4c4ff30" # str | A unique identifier for a database cluster.
    database_name = "alpha" # str | The name of the database.

    # example passing only required values which don't have defaults set
    try:
        # Delete a Database
        api_instance.delete_database(database_cluster_uuid, database_name)
    except digitalocean_client.ApiException as e:
        print("Exception when calling DatabasesApi->delete_database: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **database_cluster_uuid** | **str**| A unique identifier for a database cluster. |
 **database_name** | **str**| The name of the database. |

### Return type

void (empty response body)

### Authorization

[bearer_auth](../README.md#bearer_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | The action was successful and the response body is empty. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**401** | Unauthorized |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**404** | The resource was not found. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**429** | API Rate limit exceeded |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**500** | Server error. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**0** | Unexpected error |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_online_migration**
> delete_online_migration(database_cluster_uuid, migration_id)

Stop an Online Migration

To stop an online migration, send a DELETE request to `/v2/databases/$DATABASE_ID/online-migration/$MIGRATION_ID`.  A status of 204 will be given. This indicates that the request was processed successfully, but that no response body is needed. 

### Example

* Bearer Authentication (bearer_auth):

```python
import time
import digitalocean_client
from digitalocean_client.api import databases_api
from digitalocean_client.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to https://api.digitalocean.com
# See configuration.py for a list of all supported configuration parameters.
configuration = digitalocean_client.Configuration(
    host = "https://api.digitalocean.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: bearer_auth
configuration = digitalocean_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with digitalocean_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = databases_api.DatabasesApi(api_client)
    database_cluster_uuid = "9cc10173-e9ea-4176-9dbc-a4cee4c4ff30" # str | A unique identifier for a database cluster.
    migration_id = "77b28fc8-19ff-11eb-8c9c-c68e24557488" # str | A unique identifier assigned to the online migration.

    # example passing only required values which don't have defaults set
    try:
        # Stop an Online Migration
        api_instance.delete_online_migration(database_cluster_uuid, migration_id)
    except digitalocean_client.ApiException as e:
        print("Exception when calling DatabasesApi->delete_online_migration: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **database_cluster_uuid** | **str**| A unique identifier for a database cluster. |
 **migration_id** | **str**| A unique identifier assigned to the online migration. |

### Return type

void (empty response body)

### Authorization

[bearer_auth](../README.md#bearer_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | The action was successful and the response body is empty. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**401** | Unauthorized |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**404** | The resource was not found. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**429** | API Rate limit exceeded |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**500** | Server error. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**0** | Unexpected error |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_user**
> delete_user(database_cluster_uuid, username)

Remove a Database User

To remove a specific database user, send a DELETE request to `/v2/databases/$DATABASE_ID/users/$USERNAME`.  A status of 204 will be given. This indicates that the request was processed successfully, but that no response body is needed.  Note: User management is not supported for Redis clusters. 

### Example

* Bearer Authentication (bearer_auth):

```python
import time
import digitalocean_client
from digitalocean_client.api import databases_api
from digitalocean_client.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to https://api.digitalocean.com
# See configuration.py for a list of all supported configuration parameters.
configuration = digitalocean_client.Configuration(
    host = "https://api.digitalocean.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: bearer_auth
configuration = digitalocean_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with digitalocean_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = databases_api.DatabasesApi(api_client)
    database_cluster_uuid = "9cc10173-e9ea-4176-9dbc-a4cee4c4ff30" # str | A unique identifier for a database cluster.
    username = "app-01" # str | The name of the database user.

    # example passing only required values which don't have defaults set
    try:
        # Remove a Database User
        api_instance.delete_user(database_cluster_uuid, username)
    except digitalocean_client.ApiException as e:
        print("Exception when calling DatabasesApi->delete_user: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **database_cluster_uuid** | **str**| A unique identifier for a database cluster. |
 **username** | **str**| The name of the database user. |

### Return type

void (empty response body)

### Authorization

[bearer_auth](../README.md#bearer_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | The action was successful and the response body is empty. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**401** | Unauthorized |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**404** | The resource was not found. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**429** | API Rate limit exceeded |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**500** | Server error. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**0** | Unexpected error |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **destroy_cluster**
> destroy_cluster(database_cluster_uuid)

Destroy a Database Cluster

To destroy a specific database, send a DELETE request to `/v2/databases/$DATABASE_ID`. A status of 204 will be given. This indicates that the request was processed successfully, but that no response body is needed.

### Example

* Bearer Authentication (bearer_auth):

```python
import time
import digitalocean_client
from digitalocean_client.api import databases_api
from digitalocean_client.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to https://api.digitalocean.com
# See configuration.py for a list of all supported configuration parameters.
configuration = digitalocean_client.Configuration(
    host = "https://api.digitalocean.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: bearer_auth
configuration = digitalocean_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with digitalocean_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = databases_api.DatabasesApi(api_client)
    database_cluster_uuid = "9cc10173-e9ea-4176-9dbc-a4cee4c4ff30" # str | A unique identifier for a database cluster.

    # example passing only required values which don't have defaults set
    try:
        # Destroy a Database Cluster
        api_instance.destroy_cluster(database_cluster_uuid)
    except digitalocean_client.ApiException as e:
        print("Exception when calling DatabasesApi->destroy_cluster: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **database_cluster_uuid** | **str**| A unique identifier for a database cluster. |

### Return type

void (empty response body)

### Authorization

[bearer_auth](../README.md#bearer_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | The action was successful and the response body is empty. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**401** | Unauthorized |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**404** | The resource was not found. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**429** | API Rate limit exceeded |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**500** | Server error. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**0** | Unexpected error |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **destroy_replica**
> destroy_replica(database_cluster_uuid, replica_name)

Destroy a Read-only Replica

To destroy a specific read-only replica, send a DELETE request to `/v2/databases/$DATABASE_ID/replicas/$REPLICA_NAME`. **Note**: Read-only replicas are not supported for Redis clusters. A status of 204 will be given. This indicates that the request was processed successfully, but that no response body is needed.

### Example

* Bearer Authentication (bearer_auth):

```python
import time
import digitalocean_client
from digitalocean_client.api import databases_api
from digitalocean_client.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to https://api.digitalocean.com
# See configuration.py for a list of all supported configuration parameters.
configuration = digitalocean_client.Configuration(
    host = "https://api.digitalocean.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: bearer_auth
configuration = digitalocean_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with digitalocean_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = databases_api.DatabasesApi(api_client)
    database_cluster_uuid = "9cc10173-e9ea-4176-9dbc-a4cee4c4ff30" # str | A unique identifier for a database cluster.
    replica_name = "read-nyc3-01" # str | The name of the database replica.

    # example passing only required values which don't have defaults set
    try:
        # Destroy a Read-only Replica
        api_instance.destroy_replica(database_cluster_uuid, replica_name)
    except digitalocean_client.ApiException as e:
        print("Exception when calling DatabasesApi->destroy_replica: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **database_cluster_uuid** | **str**| A unique identifier for a database cluster. |
 **replica_name** | **str**| The name of the database replica. |

### Return type

void (empty response body)

### Authorization

[bearer_auth](../README.md#bearer_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | The action was successful and the response body is empty. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**401** | Unauthorized |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**404** | The resource was not found. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**429** | API Rate limit exceeded |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**500** | Server error. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**0** | Unexpected error |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_ca**
> InlineResponse2001 get_ca(database_cluster_uuid)

Retrieve the Public Certificate

To retrieve the public certificate used to secure the connection to the database cluster send a GET request to `/v2/databases/$DATABASE_ID/ca`.  The response will be a JSON object with a `ca` key. This will be set to an object containing the base64 encoding of the public key certificate. 

### Example

* Bearer Authentication (bearer_auth):

```python
import time
import digitalocean_client
from digitalocean_client.api import databases_api
from digitalocean_client.model.inline_response2001 import InlineResponse2001
from digitalocean_client.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to https://api.digitalocean.com
# See configuration.py for a list of all supported configuration parameters.
configuration = digitalocean_client.Configuration(
    host = "https://api.digitalocean.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: bearer_auth
configuration = digitalocean_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with digitalocean_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = databases_api.DatabasesApi(api_client)
    database_cluster_uuid = "9cc10173-e9ea-4176-9dbc-a4cee4c4ff30" # str | A unique identifier for a database cluster.

    # example passing only required values which don't have defaults set
    try:
        # Retrieve the Public Certificate
        api_response = api_instance.get_ca(database_cluster_uuid)
        pprint(api_response)
    except digitalocean_client.ApiException as e:
        print("Exception when calling DatabasesApi->get_ca: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **database_cluster_uuid** | **str**| A unique identifier for a database cluster. |

### Return type

[**InlineResponse2001**](InlineResponse2001.md)

### Authorization

[bearer_auth](../README.md#bearer_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A JSON object with a key of &#x60;ca&#x60;. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**401** | Unauthorized |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**404** | The resource was not found. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**429** | API Rate limit exceeded |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**500** | Server error. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**0** | Unexpected error |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_connection_pool**
> InlineResponse2015 get_connection_pool(database_cluster_uuid, pool_name)

Retrieve Existing Connection Pool (PostgreSQL)

To show information about an existing connection pool for a PostgreSQL database cluster, send a GET request to `/v2/databases/$DATABASE_ID/pools/$POOL_NAME`. The response will be a JSON object with a `pool` key.

### Example

* Bearer Authentication (bearer_auth):

```python
import time
import digitalocean_client
from digitalocean_client.api import databases_api
from digitalocean_client.model.error import Error
from digitalocean_client.model.inline_response2015 import InlineResponse2015
from pprint import pprint
# Defining the host is optional and defaults to https://api.digitalocean.com
# See configuration.py for a list of all supported configuration parameters.
configuration = digitalocean_client.Configuration(
    host = "https://api.digitalocean.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: bearer_auth
configuration = digitalocean_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with digitalocean_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = databases_api.DatabasesApi(api_client)
    database_cluster_uuid = "9cc10173-e9ea-4176-9dbc-a4cee4c4ff30" # str | A unique identifier for a database cluster.
    pool_name = "backend-pool" # str | The name used to identify the connection pool.

    # example passing only required values which don't have defaults set
    try:
        # Retrieve Existing Connection Pool (PostgreSQL)
        api_response = api_instance.get_connection_pool(database_cluster_uuid, pool_name)
        pprint(api_response)
    except digitalocean_client.ApiException as e:
        print("Exception when calling DatabasesApi->get_connection_pool: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **database_cluster_uuid** | **str**| A unique identifier for a database cluster. |
 **pool_name** | **str**| The name used to identify the connection pool. |

### Return type

[**InlineResponse2015**](InlineResponse2015.md)

### Authorization

[bearer_auth](../README.md#bearer_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A JSON object with a key of &#x60;pool&#x60;. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**401** | Unauthorized |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**404** | The resource was not found. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**429** | API Rate limit exceeded |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**500** | Server error. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**0** | Unexpected error |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_database**
> InlineResponse2014 get_database(database_cluster_uuid, database_name)

Retrieve an Existing Database

To show information about an existing database cluster, send a GET request to `/v2/databases/$DATABASE_ID/dbs/$DB_NAME`.  Note: Database management is not supported for Redis clusters.  The response will be a JSON object with a `db` key. This will be set to an object containing the standard database attributes. 

### Example

* Bearer Authentication (bearer_auth):

```python
import time
import digitalocean_client
from digitalocean_client.api import databases_api
from digitalocean_client.model.inline_response2014 import InlineResponse2014
from digitalocean_client.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to https://api.digitalocean.com
# See configuration.py for a list of all supported configuration parameters.
configuration = digitalocean_client.Configuration(
    host = "https://api.digitalocean.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: bearer_auth
configuration = digitalocean_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with digitalocean_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = databases_api.DatabasesApi(api_client)
    database_cluster_uuid = "9cc10173-e9ea-4176-9dbc-a4cee4c4ff30" # str | A unique identifier for a database cluster.
    database_name = "alpha" # str | The name of the database.

    # example passing only required values which don't have defaults set
    try:
        # Retrieve an Existing Database
        api_response = api_instance.get_database(database_cluster_uuid, database_name)
        pprint(api_response)
    except digitalocean_client.ApiException as e:
        print("Exception when calling DatabasesApi->get_database: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **database_cluster_uuid** | **str**| A unique identifier for a database cluster. |
 **database_name** | **str**| The name of the database. |

### Return type

[**InlineResponse2014**](InlineResponse2014.md)

### Authorization

[bearer_auth](../README.md#bearer_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A JSON object with a key of &#x60;db&#x60;. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**401** | Unauthorized |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**404** | The resource was not found. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**429** | API Rate limit exceeded |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**500** | Server error. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**0** | Unexpected error |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_database_cluster**
> InlineResponse2011 get_database_cluster(database_cluster_uuid)

Retrieve an Existing Database Cluster

To show information about an existing database cluster, send a GET request to `/v2/databases/$DATABASE_ID`. The response will be a JSON object with a database key. This will be set to an object containing the standard database cluster attributes. The embedded connection and private_connection objects will contain the information needed to access the database cluster. The embedded maintenance_window object will contain information about any scheduled maintenance for the database cluster.

### Example

* Bearer Authentication (bearer_auth):

```python
import time
import digitalocean_client
from digitalocean_client.api import databases_api
from digitalocean_client.model.inline_response2011 import InlineResponse2011
from digitalocean_client.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to https://api.digitalocean.com
# See configuration.py for a list of all supported configuration parameters.
configuration = digitalocean_client.Configuration(
    host = "https://api.digitalocean.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: bearer_auth
configuration = digitalocean_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with digitalocean_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = databases_api.DatabasesApi(api_client)
    database_cluster_uuid = "9cc10173-e9ea-4176-9dbc-a4cee4c4ff30" # str | A unique identifier for a database cluster.

    # example passing only required values which don't have defaults set
    try:
        # Retrieve an Existing Database Cluster
        api_response = api_instance.get_database_cluster(database_cluster_uuid)
        pprint(api_response)
    except digitalocean_client.ApiException as e:
        print("Exception when calling DatabasesApi->get_database_cluster: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **database_cluster_uuid** | **str**| A unique identifier for a database cluster. |

### Return type

[**InlineResponse2011**](InlineResponse2011.md)

### Authorization

[bearer_auth](../README.md#bearer_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A JSON object with a key of &#x60;database&#x60;. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**401** | Unauthorized |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**404** | The resource was not found. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**429** | API Rate limit exceeded |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**500** | Server error. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**0** | Unexpected error |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_eviction_policy**
> EvictionPolicy get_eviction_policy(database_cluster_uuid)

Retrieve the Eviction Policy for a Redis Cluster

To retrieve the configured eviction policy for an existing Redis cluster, send a GET request to `/v2/databases/$DATABASE_ID/eviction_policy`. The response will be a JSON object with an `eviction_policy` key. This will be set to a string representing the eviction policy.

### Example

* Bearer Authentication (bearer_auth):

```python
import time
import digitalocean_client
from digitalocean_client.api import databases_api
from digitalocean_client.model.eviction_policy import EvictionPolicy
from digitalocean_client.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to https://api.digitalocean.com
# See configuration.py for a list of all supported configuration parameters.
configuration = digitalocean_client.Configuration(
    host = "https://api.digitalocean.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: bearer_auth
configuration = digitalocean_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with digitalocean_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = databases_api.DatabasesApi(api_client)
    database_cluster_uuid = "9cc10173-e9ea-4176-9dbc-a4cee4c4ff30" # str | A unique identifier for a database cluster.

    # example passing only required values which don't have defaults set
    try:
        # Retrieve the Eviction Policy for a Redis Cluster
        api_response = api_instance.get_eviction_policy(database_cluster_uuid)
        pprint(api_response)
    except digitalocean_client.ApiException as e:
        print("Exception when calling DatabasesApi->get_eviction_policy: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **database_cluster_uuid** | **str**| A unique identifier for a database cluster. |

### Return type

[**EvictionPolicy**](EvictionPolicy.md)

### Authorization

[bearer_auth](../README.md#bearer_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A JSON string with a key of &#x60;eviction_policy&#x60;. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**401** | Unauthorized |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**404** | The resource was not found. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**429** | API Rate limit exceeded |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**500** | Server error. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**0** | Unexpected error |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_migration_status**
> OnlineMigration get_migration_status(database_cluster_uuid)

Retrieve the Status of an Online Migration

To retrieve the status of an online migration, send a GET request to `/v2/databases/$DATABASE_ID/online-migration`. If a migration has completed, a 200 OK status is returned with no response body.

### Example

* Bearer Authentication (bearer_auth):

```python
import time
import digitalocean_client
from digitalocean_client.api import databases_api
from digitalocean_client.model.error import Error
from digitalocean_client.model.online_migration import OnlineMigration
from pprint import pprint
# Defining the host is optional and defaults to https://api.digitalocean.com
# See configuration.py for a list of all supported configuration parameters.
configuration = digitalocean_client.Configuration(
    host = "https://api.digitalocean.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: bearer_auth
configuration = digitalocean_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with digitalocean_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = databases_api.DatabasesApi(api_client)
    database_cluster_uuid = "9cc10173-e9ea-4176-9dbc-a4cee4c4ff30" # str | A unique identifier for a database cluster.

    # example passing only required values which don't have defaults set
    try:
        # Retrieve the Status of an Online Migration
        api_response = api_instance.get_migration_status(database_cluster_uuid)
        pprint(api_response)
    except digitalocean_client.ApiException as e:
        print("Exception when calling DatabasesApi->get_migration_status: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **database_cluster_uuid** | **str**| A unique identifier for a database cluster. |

### Return type

[**OnlineMigration**](OnlineMigration.md)

### Authorization

[bearer_auth](../README.md#bearer_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A JSON object. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**401** | Unauthorized |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**404** | The resource was not found. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**429** | API Rate limit exceeded |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**500** | Server error. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**0** | Unexpected error |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_replica**
> InlineResponse2012 get_replica(database_cluster_uuid, replica_name)

Retrieve an Existing Read-only Replica

To show information about an existing database replica, send a GET request to `/v2/databases/$DATABASE_ID/replicas/$REPLICA_NAME`. **Note**: Read-only replicas are not supported for Redis clusters. The response will be a JSON object with a `replica key`. This will be set to an object containing the standard database replica attributes.

### Example

* Bearer Authentication (bearer_auth):

```python
import time
import digitalocean_client
from digitalocean_client.api import databases_api
from digitalocean_client.model.inline_response2012 import InlineResponse2012
from digitalocean_client.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to https://api.digitalocean.com
# See configuration.py for a list of all supported configuration parameters.
configuration = digitalocean_client.Configuration(
    host = "https://api.digitalocean.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: bearer_auth
configuration = digitalocean_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with digitalocean_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = databases_api.DatabasesApi(api_client)
    database_cluster_uuid = "9cc10173-e9ea-4176-9dbc-a4cee4c4ff30" # str | A unique identifier for a database cluster.
    replica_name = "read-nyc3-01" # str | The name of the database replica.

    # example passing only required values which don't have defaults set
    try:
        # Retrieve an Existing Read-only Replica
        api_response = api_instance.get_replica(database_cluster_uuid, replica_name)
        pprint(api_response)
    except digitalocean_client.ApiException as e:
        print("Exception when calling DatabasesApi->get_replica: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **database_cluster_uuid** | **str**| A unique identifier for a database cluster. |
 **replica_name** | **str**| The name of the database replica. |

### Return type

[**InlineResponse2012**](InlineResponse2012.md)

### Authorization

[bearer_auth](../README.md#bearer_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A JSON object with a key of &#x60;replica&#x60;. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**401** | Unauthorized |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**404** | The resource was not found. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**429** | API Rate limit exceeded |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**500** | Server error. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**0** | Unexpected error |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sql_mode**
> SqlMode get_sql_mode(database_cluster_uuid)

Retrieve the SQL Modes for a MySQL Cluster

To retrieve the configured SQL modes for an existing MySQL cluster, send a GET request to `/v2/databases/$DATABASE_ID/sql_mode`. The response will be a JSON object with a `sql_mode` key. This will be set to a string representing the configured SQL modes.

### Example

* Bearer Authentication (bearer_auth):

```python
import time
import digitalocean_client
from digitalocean_client.api import databases_api
from digitalocean_client.model.error import Error
from digitalocean_client.model.sql_mode import SqlMode
from pprint import pprint
# Defining the host is optional and defaults to https://api.digitalocean.com
# See configuration.py for a list of all supported configuration parameters.
configuration = digitalocean_client.Configuration(
    host = "https://api.digitalocean.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: bearer_auth
configuration = digitalocean_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with digitalocean_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = databases_api.DatabasesApi(api_client)
    database_cluster_uuid = "9cc10173-e9ea-4176-9dbc-a4cee4c4ff30" # str | A unique identifier for a database cluster.

    # example passing only required values which don't have defaults set
    try:
        # Retrieve the SQL Modes for a MySQL Cluster
        api_response = api_instance.get_sql_mode(database_cluster_uuid)
        pprint(api_response)
    except digitalocean_client.ApiException as e:
        print("Exception when calling DatabasesApi->get_sql_mode: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **database_cluster_uuid** | **str**| A unique identifier for a database cluster. |

### Return type

[**SqlMode**](SqlMode.md)

### Authorization

[bearer_auth](../README.md#bearer_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A JSON string with a key of &#x60;sql_mode&#x60;. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**401** | Unauthorized |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**404** | The resource was not found. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**429** | API Rate limit exceeded |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**500** | Server error. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**0** | Unexpected error |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user**
> InlineResponse2013 get_user(database_cluster_uuid, username)

Retrieve an Existing Database User

To show information about an existing database user, send a GET request to `/v2/databases/$DATABASE_ID/users/$USERNAME`.  Note: User management is not supported for Redis clusters.  The response will be a JSON object with a `user` key. This will be set to an object containing the standard database user attributes.  For MySQL clusters, additional options will be contained in the mysql_settings object. 

### Example

* Bearer Authentication (bearer_auth):

```python
import time
import digitalocean_client
from digitalocean_client.api import databases_api
from digitalocean_client.model.inline_response2013 import InlineResponse2013
from digitalocean_client.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to https://api.digitalocean.com
# See configuration.py for a list of all supported configuration parameters.
configuration = digitalocean_client.Configuration(
    host = "https://api.digitalocean.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: bearer_auth
configuration = digitalocean_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with digitalocean_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = databases_api.DatabasesApi(api_client)
    database_cluster_uuid = "9cc10173-e9ea-4176-9dbc-a4cee4c4ff30" # str | A unique identifier for a database cluster.
    username = "app-01" # str | The name of the database user.

    # example passing only required values which don't have defaults set
    try:
        # Retrieve an Existing Database User
        api_response = api_instance.get_user(database_cluster_uuid, username)
        pprint(api_response)
    except digitalocean_client.ApiException as e:
        print("Exception when calling DatabasesApi->get_user: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **database_cluster_uuid** | **str**| A unique identifier for a database cluster. |
 **username** | **str**| The name of the database user. |

### Return type

[**InlineResponse2013**](InlineResponse2013.md)

### Authorization

[bearer_auth](../README.md#bearer_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A JSON object with a key of &#x60;user&#x60;. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**401** | Unauthorized |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**404** | The resource was not found. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**429** | API Rate limit exceeded |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**500** | Server error. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**0** | Unexpected error |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_connection_pools**
> ConnectionPools list_connection_pools(database_cluster_uuid)

List Connection Pools (PostgreSQL)

To list all of the connection pools available to a PostgreSQL database cluster, send a GET request to `/v2/databases/$DATABASE_ID/pools`. The result will be a JSON object with a `pools` key. This will be set to an array of connection pool objects.

### Example

* Bearer Authentication (bearer_auth):

```python
import time
import digitalocean_client
from digitalocean_client.api import databases_api
from digitalocean_client.model.connection_pools import ConnectionPools
from digitalocean_client.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to https://api.digitalocean.com
# See configuration.py for a list of all supported configuration parameters.
configuration = digitalocean_client.Configuration(
    host = "https://api.digitalocean.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: bearer_auth
configuration = digitalocean_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with digitalocean_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = databases_api.DatabasesApi(api_client)
    database_cluster_uuid = "9cc10173-e9ea-4176-9dbc-a4cee4c4ff30" # str | A unique identifier for a database cluster.

    # example passing only required values which don't have defaults set
    try:
        # List Connection Pools (PostgreSQL)
        api_response = api_instance.list_connection_pools(database_cluster_uuid)
        pprint(api_response)
    except digitalocean_client.ApiException as e:
        print("Exception when calling DatabasesApi->list_connection_pools: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **database_cluster_uuid** | **str**| A unique identifier for a database cluster. |

### Return type

[**ConnectionPools**](ConnectionPools.md)

### Authorization

[bearer_auth](../README.md#bearer_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A JSON object with a key of &#x60;pools&#x60;. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**401** | Unauthorized |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**404** | The resource was not found. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**429** | API Rate limit exceeded |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**500** | Server error. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**0** | Unexpected error |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_database_backups**
> InlineResponse2002 list_database_backups(database_cluster_uuid)

List Backups for a Database Cluster

To list all of the available backups of a PostgreSQL or MySQL database cluster, send a GET request to `/v2/databases/$DATABASE_ID/backups`. **Note**: Backups are not supported for Redis clusters. The result will be a JSON object with a `backups key`. This will be set to an array of backup objects, each of which will contain the size of the backup and the timestamp at which it was created.

### Example

* Bearer Authentication (bearer_auth):

```python
import time
import digitalocean_client
from digitalocean_client.api import databases_api
from digitalocean_client.model.error import Error
from digitalocean_client.model.inline_response2002 import InlineResponse2002
from pprint import pprint
# Defining the host is optional and defaults to https://api.digitalocean.com
# See configuration.py for a list of all supported configuration parameters.
configuration = digitalocean_client.Configuration(
    host = "https://api.digitalocean.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: bearer_auth
configuration = digitalocean_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with digitalocean_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = databases_api.DatabasesApi(api_client)
    database_cluster_uuid = "9cc10173-e9ea-4176-9dbc-a4cee4c4ff30" # str | A unique identifier for a database cluster.

    # example passing only required values which don't have defaults set
    try:
        # List Backups for a Database Cluster
        api_response = api_instance.list_database_backups(database_cluster_uuid)
        pprint(api_response)
    except digitalocean_client.ApiException as e:
        print("Exception when calling DatabasesApi->list_database_backups: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **database_cluster_uuid** | **str**| A unique identifier for a database cluster. |

### Return type

[**InlineResponse2002**](InlineResponse2002.md)

### Authorization

[bearer_auth](../README.md#bearer_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A JSON object with a key of &#x60;database_backups&#x60;. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**401** | Unauthorized |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**404** | The resource was not found. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**429** | API Rate limit exceeded |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**500** | Server error. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**0** | Unexpected error |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_database_clusters**
> bool, date, datetime, dict, float, int, list, str, none_type list_database_clusters()

List All Database Clusters

To list all of the database clusters available on your account, send a GET request to `/v2/databases`. To limit the results to database clusters with a specific tag, include the `tag_name` query parameter set to the name of the tag. For example, `/v2/databases?tag_name=$TAG_NAME`. The result will be a JSON object with a `databases` key. This will be set to an array of database objects, each of which will contain the standard database attributes. The embedded `connection` and `private_connection` objects will contain the information needed to access the database cluster: The embedded `maintenance_window` object will contain information about any scheduled maintenance for the database cluster.

### Example

* Bearer Authentication (bearer_auth):

```python
import time
import digitalocean_client
from digitalocean_client.api import databases_api
from digitalocean_client.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to https://api.digitalocean.com
# See configuration.py for a list of all supported configuration parameters.
configuration = digitalocean_client.Configuration(
    host = "https://api.digitalocean.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: bearer_auth
configuration = digitalocean_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with digitalocean_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = databases_api.DatabasesApi(api_client)
    tag_name = "production" # str | Limits the results to database clusters with a specific tag. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List All Database Clusters
        api_response = api_instance.list_database_clusters(tag_name=tag_name)
        pprint(api_response)
    except digitalocean_client.ApiException as e:
        print("Exception when calling DatabasesApi->list_database_clusters: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tag_name** | **str**| Limits the results to database clusters with a specific tag. | [optional]

### Return type

**bool, date, datetime, dict, float, int, list, str, none_type**

### Authorization

[bearer_auth](../README.md#bearer_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A JSON object with a key of &#x60;databases&#x60;. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**401** | Unauthorized |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**404** | The resource was not found. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**429** | API Rate limit exceeded |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**500** | Server error. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**0** | Unexpected error |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_database_firewalls**
> bool, date, datetime, dict, float, int, list, str, none_type list_database_firewalls(database_cluster_uuid)

List Firewall Rules (Trusted Sources) for a Database Cluster

To list all of a database cluster's firewall rules (known as \"trusted sources\" in the control panel), send a GET request to `/v2/databases/$DATABASE_ID/firewall`. The result will be a JSON object with a `rules` key.

### Example

* Bearer Authentication (bearer_auth):

```python
import time
import digitalocean_client
from digitalocean_client.api import databases_api
from digitalocean_client.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to https://api.digitalocean.com
# See configuration.py for a list of all supported configuration parameters.
configuration = digitalocean_client.Configuration(
    host = "https://api.digitalocean.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: bearer_auth
configuration = digitalocean_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with digitalocean_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = databases_api.DatabasesApi(api_client)
    database_cluster_uuid = "9cc10173-e9ea-4176-9dbc-a4cee4c4ff30" # str | A unique identifier for a database cluster.

    # example passing only required values which don't have defaults set
    try:
        # List Firewall Rules (Trusted Sources) for a Database Cluster
        api_response = api_instance.list_database_firewalls(database_cluster_uuid)
        pprint(api_response)
    except digitalocean_client.ApiException as e:
        print("Exception when calling DatabasesApi->list_database_firewalls: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **database_cluster_uuid** | **str**| A unique identifier for a database cluster. |

### Return type

**bool, date, datetime, dict, float, int, list, str, none_type**

### Authorization

[bearer_auth](../README.md#bearer_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A JSON object with a key of &#x60;rules&#x60;. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**401** | Unauthorized |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**404** | The resource was not found. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**429** | API Rate limit exceeded |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**500** | Server error. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**0** | Unexpected error |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_databases**
> bool, date, datetime, dict, float, int, list, str, none_type list_databases(database_cluster_uuid)

List All Databases

To list all of the databases in a clusters, send a GET request to `/v2/databases/$DATABASE_ID/dbs`.  The result will be a JSON object with a `dbs` key. This will be set to an array of database objects, each of which will contain the standard database attributes.  Note: Database management is not supported for Redis clusters. 

### Example

* Bearer Authentication (bearer_auth):

```python
import time
import digitalocean_client
from digitalocean_client.api import databases_api
from digitalocean_client.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to https://api.digitalocean.com
# See configuration.py for a list of all supported configuration parameters.
configuration = digitalocean_client.Configuration(
    host = "https://api.digitalocean.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: bearer_auth
configuration = digitalocean_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with digitalocean_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = databases_api.DatabasesApi(api_client)
    database_cluster_uuid = "9cc10173-e9ea-4176-9dbc-a4cee4c4ff30" # str | A unique identifier for a database cluster.

    # example passing only required values which don't have defaults set
    try:
        # List All Databases
        api_response = api_instance.list_databases(database_cluster_uuid)
        pprint(api_response)
    except digitalocean_client.ApiException as e:
        print("Exception when calling DatabasesApi->list_databases: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **database_cluster_uuid** | **str**| A unique identifier for a database cluster. |

### Return type

**bool, date, datetime, dict, float, int, list, str, none_type**

### Authorization

[bearer_auth](../README.md#bearer_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A JSON object with a key of &#x60;databases&#x60;. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**401** | Unauthorized |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**404** | The resource was not found. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**429** | API Rate limit exceeded |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**500** | Server error. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**0** | Unexpected error |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_replicas**
> bool, date, datetime, dict, float, int, list, str, none_type list_replicas(database_cluster_uuid)

List All Read-only Replicas

To list all of the read-only replicas associated with a database cluster, send a GET request to `/v2/databases/$DATABASE_ID/replicas`. **Note**: Read-only replicas are not supported for Redis clusters. The result will be a JSON object with a `replicas` key. This will be set to an array of database replica objects, each of which will contain the standard database replica attributes.

### Example

* Bearer Authentication (bearer_auth):

```python
import time
import digitalocean_client
from digitalocean_client.api import databases_api
from digitalocean_client.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to https://api.digitalocean.com
# See configuration.py for a list of all supported configuration parameters.
configuration = digitalocean_client.Configuration(
    host = "https://api.digitalocean.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: bearer_auth
configuration = digitalocean_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with digitalocean_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = databases_api.DatabasesApi(api_client)
    database_cluster_uuid = "9cc10173-e9ea-4176-9dbc-a4cee4c4ff30" # str | A unique identifier for a database cluster.

    # example passing only required values which don't have defaults set
    try:
        # List All Read-only Replicas
        api_response = api_instance.list_replicas(database_cluster_uuid)
        pprint(api_response)
    except digitalocean_client.ApiException as e:
        print("Exception when calling DatabasesApi->list_replicas: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **database_cluster_uuid** | **str**| A unique identifier for a database cluster. |

### Return type

**bool, date, datetime, dict, float, int, list, str, none_type**

### Authorization

[bearer_auth](../README.md#bearer_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A JSON object with a key of &#x60;replicas&#x60;. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**401** | Unauthorized |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**404** | The resource was not found. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**429** | API Rate limit exceeded |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**500** | Server error. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**0** | Unexpected error |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_users**
> bool, date, datetime, dict, float, int, list, str, none_type list_users(database_cluster_uuid)

List all Database Users

To list all of the users for your database cluster, send a GET request to `/v2/databases/$DATABASE_ID/users`.  Note: User management is not supported for Redis clusters.  The result will be a JSON object with a `users` key. This will be set to an array of database user objects, each of which will contain the standard database user attributes.  For MySQL clusters, additional options will be contained in the mysql_settings object. 

### Example

* Bearer Authentication (bearer_auth):

```python
import time
import digitalocean_client
from digitalocean_client.api import databases_api
from digitalocean_client.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to https://api.digitalocean.com
# See configuration.py for a list of all supported configuration parameters.
configuration = digitalocean_client.Configuration(
    host = "https://api.digitalocean.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: bearer_auth
configuration = digitalocean_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with digitalocean_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = databases_api.DatabasesApi(api_client)
    database_cluster_uuid = "9cc10173-e9ea-4176-9dbc-a4cee4c4ff30" # str | A unique identifier for a database cluster.

    # example passing only required values which don't have defaults set
    try:
        # List all Database Users
        api_response = api_instance.list_users(database_cluster_uuid)
        pprint(api_response)
    except digitalocean_client.ApiException as e:
        print("Exception when calling DatabasesApi->list_users: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **database_cluster_uuid** | **str**| A unique identifier for a database cluster. |

### Return type

**bool, date, datetime, dict, float, int, list, str, none_type**

### Authorization

[bearer_auth](../README.md#bearer_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A JSON object with a key of &#x60;users&#x60;. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**401** | Unauthorized |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**404** | The resource was not found. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**429** | API Rate limit exceeded |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**500** | Server error. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**0** | Unexpected error |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reset_auth**
> InlineResponse2013 reset_auth(database_cluster_uuid, username, inline_object3)

Reset a Database User's Password or Authentication Method

To reset the password for a database user, send a POST request to `/v2/databases/$DATABASE_ID/users/$USERNAME/reset_auth`.   For `mysql` databases, the authentication method can be specifying by including a key in the JSON body called `mysql_settings` with the `auth_plugin` value specified.  The response will be a JSON object with a `user` key. This will be set to an object containing the standard database user attributes. 

### Example

* Bearer Authentication (bearer_auth):

```python
import time
import digitalocean_client
from digitalocean_client.api import databases_api
from digitalocean_client.model.inline_response2013 import InlineResponse2013
from digitalocean_client.model.inline_object3 import InlineObject3
from digitalocean_client.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to https://api.digitalocean.com
# See configuration.py for a list of all supported configuration parameters.
configuration = digitalocean_client.Configuration(
    host = "https://api.digitalocean.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: bearer_auth
configuration = digitalocean_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with digitalocean_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = databases_api.DatabasesApi(api_client)
    database_cluster_uuid = "9cc10173-e9ea-4176-9dbc-a4cee4c4ff30" # str | A unique identifier for a database cluster.
    username = "app-01" # str | The name of the database user.
    inline_object3 = InlineObject3(
        mysql_settings=MysqlSettings(
            auth_plugin="mysql_native_password",
        ),
    ) # InlineObject3 | 

    # example passing only required values which don't have defaults set
    try:
        # Reset a Database User's Password or Authentication Method
        api_response = api_instance.reset_auth(database_cluster_uuid, username, inline_object3)
        pprint(api_response)
    except digitalocean_client.ApiException as e:
        print("Exception when calling DatabasesApi->reset_auth: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **database_cluster_uuid** | **str**| A unique identifier for a database cluster. |
 **username** | **str**| The name of the database user. |
 **inline_object3** | [**InlineObject3**](InlineObject3.md)|  |

### Return type

[**InlineResponse2013**](InlineResponse2013.md)

### Authorization

[bearer_auth](../README.md#bearer_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A JSON object with a key of &#x60;user&#x60;. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**401** | Unauthorized |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**404** | The resource was not found. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**429** | API Rate limit exceeded |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**500** | Server error. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**0** | Unexpected error |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_database_cluster**
> update_database_cluster(database_cluster_uuid, inline_object1)

Migrate a Database Cluster to a New Region

To migrate a database cluster to a new region, send a `PUT` request to `/v2/databases/$DATABASE_ID/migrate`. The body of the request must specify a `region` attribute.  A successful request will receive a 202 Accepted status code with no body in response. Querying the database cluster will show that its `status` attribute will now be set to `migrating`. This will transition back to `online` when the migration has completed. 

### Example

* Bearer Authentication (bearer_auth):

```python
import time
import digitalocean_client
from digitalocean_client.api import databases_api
from digitalocean_client.model.error import Error
from digitalocean_client.model.inline_object1 import InlineObject1
from pprint import pprint
# Defining the host is optional and defaults to https://api.digitalocean.com
# See configuration.py for a list of all supported configuration parameters.
configuration = digitalocean_client.Configuration(
    host = "https://api.digitalocean.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: bearer_auth
configuration = digitalocean_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with digitalocean_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = databases_api.DatabasesApi(api_client)
    database_cluster_uuid = "9cc10173-e9ea-4176-9dbc-a4cee4c4ff30" # str | A unique identifier for a database cluster.
    inline_object1 = InlineObject1(
        region="lon1",
    ) # InlineObject1 | 

    # example passing only required values which don't have defaults set
    try:
        # Migrate a Database Cluster to a New Region
        api_instance.update_database_cluster(database_cluster_uuid, inline_object1)
    except digitalocean_client.ApiException as e:
        print("Exception when calling DatabasesApi->update_database_cluster: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **database_cluster_uuid** | **str**| A unique identifier for a database cluster. |
 **inline_object1** | [**InlineObject1**](InlineObject1.md)|  |

### Return type

void (empty response body)

### Authorization

[bearer_auth](../README.md#bearer_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | The does not indicate the success or failure of any operation, just that the request has been accepted for processing. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**401** | Unauthorized |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**404** | The resource was not found. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**429** | API Rate limit exceeded |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**500** | Server error. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**0** | Unexpected error |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_database_cluster_size**
> update_database_cluster_size(database_cluster_uuid, database_cluster_resize)

Resize a Database Cluster

To resize a database cluster, send a PUT request to `/v2/databases/$DATABASE_ID/resize`. The body of the request must specify both the size and num_nodes attributes. A successful request will receive a 202 Accepted status code with no body in response. Querying the database cluster will show that its status attribute will now be set to resizing. This will transition back to online when the resize operation has completed.

### Example

* Bearer Authentication (bearer_auth):

```python
import time
import digitalocean_client
from digitalocean_client.api import databases_api
from digitalocean_client.model.database_cluster_resize import DatabaseClusterResize
from digitalocean_client.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to https://api.digitalocean.com
# See configuration.py for a list of all supported configuration parameters.
configuration = digitalocean_client.Configuration(
    host = "https://api.digitalocean.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: bearer_auth
configuration = digitalocean_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with digitalocean_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = databases_api.DatabasesApi(api_client)
    database_cluster_uuid = "9cc10173-e9ea-4176-9dbc-a4cee4c4ff30" # str | A unique identifier for a database cluster.
    database_cluster_resize = DatabaseClusterResize(
        size="db-s-4vcpu-8gb",
        num_nodes=3,
    ) # DatabaseClusterResize | 

    # example passing only required values which don't have defaults set
    try:
        # Resize a Database Cluster
        api_instance.update_database_cluster_size(database_cluster_uuid, database_cluster_resize)
    except digitalocean_client.ApiException as e:
        print("Exception when calling DatabasesApi->update_database_cluster_size: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **database_cluster_uuid** | **str**| A unique identifier for a database cluster. |
 **database_cluster_resize** | [**DatabaseClusterResize**](DatabaseClusterResize.md)|  |

### Return type

void (empty response body)

### Authorization

[bearer_auth](../README.md#bearer_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | The action was successful and the response body is empty. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**401** | Unauthorized |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**404** | The resource was not found. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**429** | API Rate limit exceeded |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**500** | Server error. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**0** | Unexpected error |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_database_firewall**
> update_database_firewall(database_cluster_uuid, inline_object2)

Update Firewall Rules (Trusted Sources) for a Database

To update a database cluster's firewall rules (known as \"trusted sources\" in the control panel), send a PUT request to `/v2/databases/$DATABASE_ID/firewall` specifying which resources should be able to open connections to the database. You may limit connections to specific Droplets, Kubernetes clusters, or IP addresses. When a tag is provided, any Droplet or Kubernetes node with that tag applied to it will have access. The firewall is limited to 100 rules (or trusted sources). When possible, we recommend [placing your databases into a VPC network](https://www.digitalocean.com/docs/networking/vpc/) to limit access to them instead of using a firewall. A successful

### Example

* Bearer Authentication (bearer_auth):

```python
import time
import digitalocean_client
from digitalocean_client.api import databases_api
from digitalocean_client.model.error import Error
from digitalocean_client.model.inline_object2 import InlineObject2
from pprint import pprint
# Defining the host is optional and defaults to https://api.digitalocean.com
# See configuration.py for a list of all supported configuration parameters.
configuration = digitalocean_client.Configuration(
    host = "https://api.digitalocean.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: bearer_auth
configuration = digitalocean_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with digitalocean_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = databases_api.DatabasesApi(api_client)
    database_cluster_uuid = "9cc10173-e9ea-4176-9dbc-a4cee4c4ff30" # str | A unique identifier for a database cluster.
    inline_object2 = InlineObject2(
        rules=[
            FirewallRule(
                uuid="79f26d28-ea8a-41f2-8ad8-8cfcdd020095",
                cluster_uuid="9cc10173-e9ea-4176-9dbc-a4cee4c4ff30",
                type="droplet",
                value="ff2a6c52-5a44-4b63-b99c-0e98e7a63d61",
            ),
        ],
    ) # InlineObject2 | 

    # example passing only required values which don't have defaults set
    try:
        # Update Firewall Rules (Trusted Sources) for a Database
        api_instance.update_database_firewall(database_cluster_uuid, inline_object2)
    except digitalocean_client.ApiException as e:
        print("Exception when calling DatabasesApi->update_database_firewall: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **database_cluster_uuid** | **str**| A unique identifier for a database cluster. |
 **inline_object2** | [**InlineObject2**](InlineObject2.md)|  |

### Return type

void (empty response body)

### Authorization

[bearer_auth](../README.md#bearer_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | The action was successful and the response body is empty. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**401** | Unauthorized |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**404** | The resource was not found. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**429** | API Rate limit exceeded |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**500** | Server error. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**0** | Unexpected error |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_eviction_policy**
> update_eviction_policy(database_cluster_uuid, eviction_policy)

Configure the Eviction Policy for a Redis Cluster

To configure an eviction policy for an existing Redis cluster, send a PUT request to `/v2/databases/$DATABASE_ID/eviction_policy` specifying the desired policy.

### Example

* Bearer Authentication (bearer_auth):

```python
import time
import digitalocean_client
from digitalocean_client.api import databases_api
from digitalocean_client.model.eviction_policy import EvictionPolicy
from digitalocean_client.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to https://api.digitalocean.com
# See configuration.py for a list of all supported configuration parameters.
configuration = digitalocean_client.Configuration(
    host = "https://api.digitalocean.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: bearer_auth
configuration = digitalocean_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with digitalocean_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = databases_api.DatabasesApi(api_client)
    database_cluster_uuid = "9cc10173-e9ea-4176-9dbc-a4cee4c4ff30" # str | A unique identifier for a database cluster.
    eviction_policy = EvictionPolicy(
        eviction_policy="noeviction",
    ) # EvictionPolicy | 

    # example passing only required values which don't have defaults set
    try:
        # Configure the Eviction Policy for a Redis Cluster
        api_instance.update_eviction_policy(database_cluster_uuid, eviction_policy)
    except digitalocean_client.ApiException as e:
        print("Exception when calling DatabasesApi->update_eviction_policy: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **database_cluster_uuid** | **str**| A unique identifier for a database cluster. |
 **eviction_policy** | [**EvictionPolicy**](EvictionPolicy.md)|  |

### Return type

void (empty response body)

### Authorization

[bearer_auth](../README.md#bearer_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | The action was successful and the response body is empty. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**401** | Unauthorized |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**404** | The resource was not found. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**429** | API Rate limit exceeded |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**500** | Server error. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**0** | Unexpected error |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_maintenance_window**
> update_maintenance_window(database_cluster_uuid, database_maintenance_window)

Configure a Database Cluster's Maintenance Window

To configure the window when automatic maintenance should be performed for a database cluster, send a PUT request to `/v2/databases/$DATABASE_ID/maintenance`. A successful request will receive a 204 No Content status code with no body in response.

### Example

* Bearer Authentication (bearer_auth):

```python
import time
import digitalocean_client
from digitalocean_client.api import databases_api
from digitalocean_client.model.database_maintenance_window import DatabaseMaintenanceWindow
from digitalocean_client.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to https://api.digitalocean.com
# See configuration.py for a list of all supported configuration parameters.
configuration = digitalocean_client.Configuration(
    host = "https://api.digitalocean.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: bearer_auth
configuration = digitalocean_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with digitalocean_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = databases_api.DatabasesApi(api_client)
    database_cluster_uuid = "9cc10173-e9ea-4176-9dbc-a4cee4c4ff30" # str | A unique identifier for a database cluster.
    database_maintenance_window = DatabaseMaintenanceWindow(
        day="tuesday",
        hour="14:00",
    ) # DatabaseMaintenanceWindow | 

    # example passing only required values which don't have defaults set
    try:
        # Configure a Database Cluster's Maintenance Window
        api_instance.update_maintenance_window(database_cluster_uuid, database_maintenance_window)
    except digitalocean_client.ApiException as e:
        print("Exception when calling DatabasesApi->update_maintenance_window: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **database_cluster_uuid** | **str**| A unique identifier for a database cluster. |
 **database_maintenance_window** | [**DatabaseMaintenanceWindow**](DatabaseMaintenanceWindow.md)|  |

### Return type

void (empty response body)

### Authorization

[bearer_auth](../README.md#bearer_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | The action was successful and the response body is empty. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**401** | Unauthorized |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**404** | The resource was not found. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**429** | API Rate limit exceeded |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**500** | Server error. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**0** | Unexpected error |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_online_migration**
> OnlineMigration update_online_migration(database_cluster_uuid, source_database)

Start an Online Migration

To start an online migration, send a PUT request to `/v2/databases/$DATABASE_ID/online-migration` endpoint. Migrating a cluster establishes a connection with an existing cluster and replicates its contents to the target cluster. Online migration is only available for PostgreSQL and Redis clusters.

### Example

* Bearer Authentication (bearer_auth):

```python
import time
import digitalocean_client
from digitalocean_client.api import databases_api
from digitalocean_client.model.error import Error
from digitalocean_client.model.source_database import SourceDatabase
from digitalocean_client.model.online_migration import OnlineMigration
from pprint import pprint
# Defining the host is optional and defaults to https://api.digitalocean.com
# See configuration.py for a list of all supported configuration parameters.
configuration = digitalocean_client.Configuration(
    host = "https://api.digitalocean.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: bearer_auth
configuration = digitalocean_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with digitalocean_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = databases_api.DatabasesApi(api_client)
    database_cluster_uuid = "9cc10173-e9ea-4176-9dbc-a4cee4c4ff30" # str | A unique identifier for a database cluster.
    source_database = SourceDatabase(
        source=None,
        disable_ssl=False,
    ) # SourceDatabase | 

    # example passing only required values which don't have defaults set
    try:
        # Start an Online Migration
        api_response = api_instance.update_online_migration(database_cluster_uuid, source_database)
        pprint(api_response)
    except digitalocean_client.ApiException as e:
        print("Exception when calling DatabasesApi->update_online_migration: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **database_cluster_uuid** | **str**| A unique identifier for a database cluster. |
 **source_database** | [**SourceDatabase**](SourceDatabase.md)|  |

### Return type

[**OnlineMigration**](OnlineMigration.md)

### Authorization

[bearer_auth](../README.md#bearer_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A JSON object. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**401** | Unauthorized |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**404** | The resource was not found. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**429** | API Rate limit exceeded |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**500** | Server error. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**0** | Unexpected error |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_sql_mode**
> update_sql_mode(database_cluster_uuid, sql_mode)

Update SQL Mode for a Cluster

To configure the SQL modes for an existing MySQL cluster, send a PUT request to `/v2/databases/$DATABASE_ID/sql_mode` specifying the desired modes. See the official MySQL 8 documentation for a [full list of supported SQL modes](https://dev.mysql.com/doc/refman/8.0/en/sql-mode.html#sql-mode-full). A successful request will receive a 204 No Content status code with no body in response.

### Example

* Bearer Authentication (bearer_auth):

```python
import time
import digitalocean_client
from digitalocean_client.api import databases_api
from digitalocean_client.model.error import Error
from digitalocean_client.model.sql_mode import SqlMode
from pprint import pprint
# Defining the host is optional and defaults to https://api.digitalocean.com
# See configuration.py for a list of all supported configuration parameters.
configuration = digitalocean_client.Configuration(
    host = "https://api.digitalocean.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: bearer_auth
configuration = digitalocean_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with digitalocean_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = databases_api.DatabasesApi(api_client)
    database_cluster_uuid = "9cc10173-e9ea-4176-9dbc-a4cee4c4ff30" # str | A unique identifier for a database cluster.
    sql_mode = SqlMode(
        sql_mode="ANSI,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION,NO_ZERO_DATE,NO_ZERO_IN_DATE,STRICT_ALL_TABLES",
    ) # SqlMode | 

    # example passing only required values which don't have defaults set
    try:
        # Update SQL Mode for a Cluster
        api_instance.update_sql_mode(database_cluster_uuid, sql_mode)
    except digitalocean_client.ApiException as e:
        print("Exception when calling DatabasesApi->update_sql_mode: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **database_cluster_uuid** | **str**| A unique identifier for a database cluster. |
 **sql_mode** | [**SqlMode**](SqlMode.md)|  |

### Return type

void (empty response body)

### Authorization

[bearer_auth](../README.md#bearer_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | The action was successful and the response body is empty. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**401** | Unauthorized |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**404** | The resource was not found. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**429** | API Rate limit exceeded |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**500** | Server error. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**0** | Unexpected error |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

