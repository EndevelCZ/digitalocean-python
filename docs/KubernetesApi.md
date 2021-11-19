# openapi_client.KubernetesApi

All URIs are relative to *https://api.digitalocean.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_kubernetes_node_pool**](KubernetesApi.md#add_kubernetes_node_pool) | **POST** /v2/kubernetes/clusters/{cluster_id}/node_pools | Add a Node Pool to a Kubernetes Cluster
[**add_registry**](KubernetesApi.md#add_registry) | **POST** /v2/kubernetes/registry | Add Container Registry to Kubernetes Clusters
[**create_kubernetes_cluster**](KubernetesApi.md#create_kubernetes_cluster) | **POST** /v2/kubernetes/clusters | Create a New Kubernetes Cluster
[**delete_kubernetes_cluster**](KubernetesApi.md#delete_kubernetes_cluster) | **DELETE** /v2/kubernetes/clusters/{cluster_id} | Delete a Kubernetes Cluster
[**delete_kubernetes_node**](KubernetesApi.md#delete_kubernetes_node) | **DELETE** /v2/kubernetes/clusters/{cluster_id}/node_pools/{node_pool_id}/nodes/{node_id} | Delete a Node in a Kubernetes Cluster
[**delete_kubernetes_node_pool**](KubernetesApi.md#delete_kubernetes_node_pool) | **DELETE** /v2/kubernetes/clusters/{cluster_id}/node_pools/{node_pool_id} | Delete a Node Pool in a Kubernetes Cluster
[**destroy_kubernetes_associated_resources_dangerous**](KubernetesApi.md#destroy_kubernetes_associated_resources_dangerous) | **DELETE** /v2/kubernetes/clusters/{cluster_id}/destroy_with_associated_resources/dangerous | Delete a Cluster and All of its Associated Resources (Dangerous)
[**destroy_kubernetes_associated_resources_selective**](KubernetesApi.md#destroy_kubernetes_associated_resources_selective) | **DELETE** /v2/kubernetes/clusters/{cluster_id}/destroy_with_associated_resources/selective | Selectively Delete a Cluster and its Associated Resources
[**get_available_upgrades**](KubernetesApi.md#get_available_upgrades) | **GET** /v2/kubernetes/clusters/{cluster_id}/upgrades | Retrieve Available Upgrades for an Existing Kubernetes Cluster
[**get_cluster_user**](KubernetesApi.md#get_cluster_user) | **GET** /v2/kubernetes/clusters/{cluster_id}/user | Retrieve User Information for a Kubernetes Cluster
[**get_clusterlint_results**](KubernetesApi.md#get_clusterlint_results) | **GET** /v2/kubernetes/clusters/{cluster_id}/clusterlint | Fetch Clusterlint Diagnostics for a Kubernetes Cluster
[**get_credentials**](KubernetesApi.md#get_credentials) | **GET** /v2/kubernetes/clusters/{cluster_id}/credentials | Retrieve Credentials for a Kubernetes Cluster
[**get_kubeconfig**](KubernetesApi.md#get_kubeconfig) | **GET** /v2/kubernetes/clusters/{cluster_id}/kubeconfig | Retrieve the kubeconfig for a Kubernetes Cluster
[**get_kubernetes_cluster**](KubernetesApi.md#get_kubernetes_cluster) | **GET** /v2/kubernetes/clusters/{cluster_id} | Retrieve an Existing Kubernetes Cluster
[**get_node_pool**](KubernetesApi.md#get_node_pool) | **GET** /v2/kubernetes/clusters/{cluster_id}/node_pools/{node_pool_id} | Retrieve a Node Pool for a Kubernetes Cluster
[**list_all_kubernetes_clusters**](KubernetesApi.md#list_all_kubernetes_clusters) | **GET** /v2/kubernetes/clusters | List All Kubernetes Clusters
[**list_kubernetes_associated_resources**](KubernetesApi.md#list_kubernetes_associated_resources) | **GET** /v2/kubernetes/clusters/{cluster_id}/destroy_with_associated_resources | List Associated Resources for Cluster Deletion
[**list_kubernetes_options**](KubernetesApi.md#list_kubernetes_options) | **GET** /v2/kubernetes/options | List Available Regions, Node Sizes, and Versions of Kubernetes
[**list_node_pools**](KubernetesApi.md#list_node_pools) | **GET** /v2/kubernetes/clusters/{cluster_id}/node_pools | List All Node Pools in a Kubernetes Clusters
[**recycle_kubernetes_node_pool**](KubernetesApi.md#recycle_kubernetes_node_pool) | **POST** /v2/kubernetes/clusters/{cluster_id}/node_pools/{node_pool_id}/recycle | Recycle a Kubernetes Node Pool
[**remove_registry**](KubernetesApi.md#remove_registry) | **DELETE** /v2/kubernetes/registry | Remove Container Registry from Kubernetes Clusters
[**run_clusterlint**](KubernetesApi.md#run_clusterlint) | **POST** /v2/kubernetes/clusters/{cluster_id}/clusterlint | Run Clusterlint Checks on a Kubernetes Cluster
[**update_kubernetes_cluster**](KubernetesApi.md#update_kubernetes_cluster) | **PUT** /v2/kubernetes/clusters/{cluster_id} | Update a Kubernetes Cluster
[**update_kubernetes_node_pool**](KubernetesApi.md#update_kubernetes_node_pool) | **PUT** /v2/kubernetes/clusters/{cluster_id}/node_pools/{node_pool_id} | Update a Node Pool in a Kubernetes Cluster
[**upgrade_kubernetes_cluster**](KubernetesApi.md#upgrade_kubernetes_cluster) | **POST** /v2/kubernetes/clusters/{cluster_id}/upgrade | Upgrade a Kubernetes Cluster


# **add_kubernetes_node_pool**
> bool, date, datetime, dict, float, int, list, str, none_type add_kubernetes_node_pool(cluster_id, kubernetes_node_pool)

Add a Node Pool to a Kubernetes Cluster

To add an additional node pool to a Kubernetes clusters, send a POST request to `/v2/kubernetes/clusters/$K8S_CLUSTER_ID/node_pools` with the following attributes. 

### Example

* Bearer Authentication (bearer_auth):

```python
import time
import openapi_client
from openapi_client.api import kubernetes_api
from openapi_client.model.error import Error
from openapi_client.model.kubernetes_node_pool import KubernetesNodePool
from pprint import pprint
# Defining the host is optional and defaults to https://api.digitalocean.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.digitalocean.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: bearer_auth
configuration = openapi_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = kubernetes_api.KubernetesApi(api_client)
    cluster_id = "bd5f5959-5e1e-4205-a714-a914373942af" # str | A unique ID that can be used to reference a Kubernetes cluster.
    kubernetes_node_pool = KubernetesNodePool() # KubernetesNodePool | 

    # example passing only required values which don't have defaults set
    try:
        # Add a Node Pool to a Kubernetes Cluster
        api_response = api_instance.add_kubernetes_node_pool(cluster_id, kubernetes_node_pool)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling KubernetesApi->add_kubernetes_node_pool: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**| A unique ID that can be used to reference a Kubernetes cluster. |
 **kubernetes_node_pool** | [**KubernetesNodePool**](KubernetesNodePool.md)|  |

### Return type

**bool, date, datetime, dict, float, int, list, str, none_type**

### Authorization

[bearer_auth](../README.md#bearer_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The response will be a JSON object with a key called &#x60;node_pool&#x60;. The value of this will be an object containing the standard attributes of a node pool.  |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**401** | Unauthorized |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**404** | The resource was not found. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**429** | API Rate limit exceeded |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**500** | Server error. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**0** | Unexpected error |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_registry**
> add_registry()

Add Container Registry to Kubernetes Clusters

To integrate the container registry with Kubernetes clusters, send a POST request to `/v2/kubernetes/registry`.

### Example

* Bearer Authentication (bearer_auth):

```python
import time
import openapi_client
from openapi_client.api import kubernetes_api
from openapi_client.model.cluster_registries import ClusterRegistries
from openapi_client.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to https://api.digitalocean.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.digitalocean.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: bearer_auth
configuration = openapi_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = kubernetes_api.KubernetesApi(api_client)
    cluster_registries = ClusterRegistries(
        cluster_uuids=["bd5f5959-5e1e-4205-a714-a914373942af","50c2f44c-011d-493e-aee5-361a4a0d1844"],
    ) # ClusterRegistries |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Add Container Registry to Kubernetes Clusters
        api_instance.add_registry(cluster_registries=cluster_registries)
    except openapi_client.ApiException as e:
        print("Exception when calling KubernetesApi->add_registry: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_registries** | [**ClusterRegistries**](ClusterRegistries.md)|  | [optional]

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
**429** | API Rate limit exceeded |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**500** | Server error. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**0** | Unexpected error |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_kubernetes_cluster**
> bool, date, datetime, dict, float, int, list, str, none_type create_kubernetes_cluster(cluster)

Create a New Kubernetes Cluster

To create a new Kubernetes cluster, send a POST request to `/v2/kubernetes/clusters`. The request must contain at least one node pool with at least one worker.  The request may contain a maintenance window policy describing a time period when disruptive maintenance tasks may be carried out. Omitting the policy implies that a window will be chosen automatically. See [here](https://www.digitalocean.com/docs/kubernetes/how-to/upgrade-cluster/) for details. 

### Example

* Bearer Authentication (bearer_auth):

```python
import time
import openapi_client
from openapi_client.api import kubernetes_api
from openapi_client.model.error import Error
from openapi_client.model.cluster import Cluster
from pprint import pprint
# Defining the host is optional and defaults to https://api.digitalocean.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.digitalocean.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: bearer_auth
configuration = openapi_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = kubernetes_api.KubernetesApi(api_client)
    cluster = Cluster(
        name="prod-cluster-01",
        region="nyc1",
        version="1.18.6-do.0",
        vpc_uuid="c33931f2-a26a-4e61-b85c-4e95a2ec431b",
        tags=["k8s","k8s:bd5f5959-5e1e-4205-a714-a914373942af","production","web-team"],
        node_pools=[
            KubernetesNodePool(),
        ],
        maintenance_policy=MaintenancePolicy(
            start_time="12:00",
            day="any",
        ),
        auto_upgrade=True,
        surge_upgrade=True,
        ha=True,
    ) # Cluster | 

    # example passing only required values which don't have defaults set
    try:
        # Create a New Kubernetes Cluster
        api_response = api_instance.create_kubernetes_cluster(cluster)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling KubernetesApi->create_kubernetes_cluster: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster** | [**Cluster**](Cluster.md)|  |

### Return type

**bool, date, datetime, dict, float, int, list, str, none_type**

### Authorization

[bearer_auth](../README.md#bearer_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The response will be a JSON object with a key called &#x60;kubernetes_cluster&#x60;. The value of this will be an object containing the standard attributes of a Kubernetes cluster.  The IP address and cluster API server endpoint will not be available until the cluster has finished provisioning. The initial value of the cluster&#39;s &#x60;status.state&#x60; attribute will be &#x60;provisioning&#x60;. When the cluster is ready, this will transition to &#x60;running&#x60;.  |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**401** | Unauthorized |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**429** | API Rate limit exceeded |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**500** | Server error. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**0** | Unexpected error |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_kubernetes_cluster**
> delete_kubernetes_cluster(cluster_id)

Delete a Kubernetes Cluster

To delete a Kubernetes cluster and all services deployed to it, send a DELETE request to `/v2/kubernetes/clusters/$K8S_CLUSTER_ID`.  A 204 status code with no body will be returned in response to a successful request. 

### Example

* Bearer Authentication (bearer_auth):

```python
import time
import openapi_client
from openapi_client.api import kubernetes_api
from openapi_client.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to https://api.digitalocean.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.digitalocean.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: bearer_auth
configuration = openapi_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = kubernetes_api.KubernetesApi(api_client)
    cluster_id = "bd5f5959-5e1e-4205-a714-a914373942af" # str | A unique ID that can be used to reference a Kubernetes cluster.

    # example passing only required values which don't have defaults set
    try:
        # Delete a Kubernetes Cluster
        api_instance.delete_kubernetes_cluster(cluster_id)
    except openapi_client.ApiException as e:
        print("Exception when calling KubernetesApi->delete_kubernetes_cluster: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**| A unique ID that can be used to reference a Kubernetes cluster. |

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

# **delete_kubernetes_node**
> delete_kubernetes_node(cluster_id, node_pool_id, node_id)

Delete a Node in a Kubernetes Cluster

To delete a single node in a pool, send a DELETE request to `/v2/kubernetes/clusters/$K8S_CLUSTER_ID/node_pools/$NODE_POOL_ID/nodes/$NODE_ID`.  Appending the `skip_drain=1` query parameter to the request causes node draining to be skipped. Omitting the query parameter or setting its value to `0` carries out draining prior to deletion.  Appending the `replace=1` query parameter to the request causes the node to be replaced by a new one after deletion. Omitting the query parameter or setting its value to `0` deletes without replacement. 

### Example

* Bearer Authentication (bearer_auth):

```python
import time
import openapi_client
from openapi_client.api import kubernetes_api
from openapi_client.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to https://api.digitalocean.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.digitalocean.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: bearer_auth
configuration = openapi_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = kubernetes_api.KubernetesApi(api_client)
    cluster_id = "bd5f5959-5e1e-4205-a714-a914373942af" # str | A unique ID that can be used to reference a Kubernetes cluster.
    node_pool_id = "cdda885e-7663-40c8-bc74-3a036c66545d" # str | A unique ID that can be used to reference a Kubernetes node pool.
    node_id = "478247f8-b1bb-4f7a-8db9-2a5f8d4b8f8f" # str | A unique ID that can be used to reference a node in a Kubernetes node pool.
    skip_drain = 1 # int | Specifies whether or not to drain workloads from a node before it is deleted. Setting it to `1` causes node draining to be skipped. Omitting the query parameter or setting its value to `0` carries out draining prior to deletion. (optional) if omitted the server will use the default value of 0
    replace = 1 # int | Specifies whether or not to replace a node after it has been deleted. Setting it to `1` causes the node to be replaced by a new one after deletion. Omitting the query parameter or setting its value to `0` deletes without replacement. (optional) if omitted the server will use the default value of 0

    # example passing only required values which don't have defaults set
    try:
        # Delete a Node in a Kubernetes Cluster
        api_instance.delete_kubernetes_node(cluster_id, node_pool_id, node_id)
    except openapi_client.ApiException as e:
        print("Exception when calling KubernetesApi->delete_kubernetes_node: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Delete a Node in a Kubernetes Cluster
        api_instance.delete_kubernetes_node(cluster_id, node_pool_id, node_id, skip_drain=skip_drain, replace=replace)
    except openapi_client.ApiException as e:
        print("Exception when calling KubernetesApi->delete_kubernetes_node: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**| A unique ID that can be used to reference a Kubernetes cluster. |
 **node_pool_id** | **str**| A unique ID that can be used to reference a Kubernetes node pool. |
 **node_id** | **str**| A unique ID that can be used to reference a node in a Kubernetes node pool. |
 **skip_drain** | **int**| Specifies whether or not to drain workloads from a node before it is deleted. Setting it to &#x60;1&#x60; causes node draining to be skipped. Omitting the query parameter or setting its value to &#x60;0&#x60; carries out draining prior to deletion. | [optional] if omitted the server will use the default value of 0
 **replace** | **int**| Specifies whether or not to replace a node after it has been deleted. Setting it to &#x60;1&#x60; causes the node to be replaced by a new one after deletion. Omitting the query parameter or setting its value to &#x60;0&#x60; deletes without replacement. | [optional] if omitted the server will use the default value of 0

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
**202** | The does not indicate the success or failure of any operation, just that the request has been accepted for processing. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**401** | Unauthorized |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**404** | The resource was not found. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**429** | API Rate limit exceeded |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**500** | Server error. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**0** | Unexpected error |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_kubernetes_node_pool**
> delete_kubernetes_node_pool(cluster_id, node_pool_id)

Delete a Node Pool in a Kubernetes Cluster

To delete a node pool, send a DELETE request to `/v2/kubernetes/clusters/$K8S_CLUSTER_ID/node_pools/$NODE_POOL_ID`.  A 204 status code with no body will be returned in response to a successful request. Nodes in the pool will subsequently be drained and deleted. 

### Example

* Bearer Authentication (bearer_auth):

```python
import time
import openapi_client
from openapi_client.api import kubernetes_api
from openapi_client.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to https://api.digitalocean.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.digitalocean.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: bearer_auth
configuration = openapi_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = kubernetes_api.KubernetesApi(api_client)
    cluster_id = "bd5f5959-5e1e-4205-a714-a914373942af" # str | A unique ID that can be used to reference a Kubernetes cluster.
    node_pool_id = "cdda885e-7663-40c8-bc74-3a036c66545d" # str | A unique ID that can be used to reference a Kubernetes node pool.

    # example passing only required values which don't have defaults set
    try:
        # Delete a Node Pool in a Kubernetes Cluster
        api_instance.delete_kubernetes_node_pool(cluster_id, node_pool_id)
    except openapi_client.ApiException as e:
        print("Exception when calling KubernetesApi->delete_kubernetes_node_pool: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**| A unique ID that can be used to reference a Kubernetes cluster. |
 **node_pool_id** | **str**| A unique ID that can be used to reference a Kubernetes node pool. |

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

# **destroy_kubernetes_associated_resources_dangerous**
> destroy_kubernetes_associated_resources_dangerous(cluster_id)

Delete a Cluster and All of its Associated Resources (Dangerous)

To delete a Kubernetes cluster with all of its associated resources, send a DELETE request to `/v2/kubernetes/clusters/$K8S_CLUSTER_ID/destroy_with_associated_resources/dangerous`. A 204 status code with no body will be returned in response to a successful request. 

### Example

* Bearer Authentication (bearer_auth):

```python
import time
import openapi_client
from openapi_client.api import kubernetes_api
from openapi_client.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to https://api.digitalocean.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.digitalocean.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: bearer_auth
configuration = openapi_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = kubernetes_api.KubernetesApi(api_client)
    cluster_id = "bd5f5959-5e1e-4205-a714-a914373942af" # str | A unique ID that can be used to reference a Kubernetes cluster.

    # example passing only required values which don't have defaults set
    try:
        # Delete a Cluster and All of its Associated Resources (Dangerous)
        api_instance.destroy_kubernetes_associated_resources_dangerous(cluster_id)
    except openapi_client.ApiException as e:
        print("Exception when calling KubernetesApi->destroy_kubernetes_associated_resources_dangerous: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**| A unique ID that can be used to reference a Kubernetes cluster. |

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

# **destroy_kubernetes_associated_resources_selective**
> destroy_kubernetes_associated_resources_selective(cluster_id, destroy_associated_kubernetes_resources)

Selectively Delete a Cluster and its Associated Resources

To delete a Kubernetes cluster along with a subset of its associated resources, send a DELETE request to `/v2/kubernetes/clusters/$K8S_CLUSTER_ID/destroy_with_associated_resources/selective`.  The JSON body of the request should include `load_balancers`, `volumes`, or `volume_snapshots` keys each set to an array of IDs for the associated resources to be destroyed.  The IDs can be found by querying the cluster's associated resources endpoint. Any associated resource not included in the request will remain and continue to accrue changes on your account. 

### Example

* Bearer Authentication (bearer_auth):

```python
import time
import openapi_client
from openapi_client.api import kubernetes_api
from openapi_client.model.error import Error
from openapi_client.model.destroy_associated_kubernetes_resources import DestroyAssociatedKubernetesResources
from pprint import pprint
# Defining the host is optional and defaults to https://api.digitalocean.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.digitalocean.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: bearer_auth
configuration = openapi_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = kubernetes_api.KubernetesApi(api_client)
    cluster_id = "bd5f5959-5e1e-4205-a714-a914373942af" # str | A unique ID that can be used to reference a Kubernetes cluster.
    destroy_associated_kubernetes_resources = DestroyAssociatedKubernetesResources(
        load_balancers=["4de7ac8b-495b-4884-9a69-1050c6793cd6"],
        volumes=["ba49449a-7435-11ea-b89e-0a58ac14480f"],
        volume_snapshots=["edb0478d-7436-11ea-86e6-0a58ac144b91"],
    ) # DestroyAssociatedKubernetesResources | 

    # example passing only required values which don't have defaults set
    try:
        # Selectively Delete a Cluster and its Associated Resources
        api_instance.destroy_kubernetes_associated_resources_selective(cluster_id, destroy_associated_kubernetes_resources)
    except openapi_client.ApiException as e:
        print("Exception when calling KubernetesApi->destroy_kubernetes_associated_resources_selective: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**| A unique ID that can be used to reference a Kubernetes cluster. |
 **destroy_associated_kubernetes_resources** | [**DestroyAssociatedKubernetesResources**](DestroyAssociatedKubernetesResources.md)|  |

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

# **get_available_upgrades**
> InlineResponse2005 get_available_upgrades(cluster_id)

Retrieve Available Upgrades for an Existing Kubernetes Cluster

To determine whether a cluster can be upgraded, and the versions to which it can be upgraded, send a GET request to `/v2/kubernetes/clusters/$K8S_CLUSTER_ID/upgrades`. 

### Example

* Bearer Authentication (bearer_auth):

```python
import time
import openapi_client
from openapi_client.api import kubernetes_api
from openapi_client.model.inline_response2005 import InlineResponse2005
from openapi_client.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to https://api.digitalocean.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.digitalocean.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: bearer_auth
configuration = openapi_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = kubernetes_api.KubernetesApi(api_client)
    cluster_id = "bd5f5959-5e1e-4205-a714-a914373942af" # str | A unique ID that can be used to reference a Kubernetes cluster.

    # example passing only required values which don't have defaults set
    try:
        # Retrieve Available Upgrades for an Existing Kubernetes Cluster
        api_response = api_instance.get_available_upgrades(cluster_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling KubernetesApi->get_available_upgrades: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**| A unique ID that can be used to reference a Kubernetes cluster. |

### Return type

[**InlineResponse2005**](InlineResponse2005.md)

### Authorization

[bearer_auth](../README.md#bearer_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The response will be a JSON object with a key called &#x60;available_upgrade_versions&#x60;. The value of this will be an array of objects, representing the upgrade versions currently available for this cluster.  If the cluster is up-to-date (i.e. there are no upgrades currently available) &#x60;available_upgrade_versions&#x60; will be &#x60;null&#x60;.  |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**401** | Unauthorized |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**404** | The resource was not found. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**429** | API Rate limit exceeded |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**500** | Server error. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**0** | Unexpected error |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cluster_user**
> User get_cluster_user(cluster_id)

Retrieve User Information for a Kubernetes Cluster

To show information the user associated with a Kubernetes cluster, send a GET request to `/v2/kubernetes/clusters/$K8S_CLUSTER_ID/user`. 

### Example

* Bearer Authentication (bearer_auth):

```python
import time
import openapi_client
from openapi_client.api import kubernetes_api
from openapi_client.model.user import User
from openapi_client.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to https://api.digitalocean.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.digitalocean.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: bearer_auth
configuration = openapi_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = kubernetes_api.KubernetesApi(api_client)
    cluster_id = "bd5f5959-5e1e-4205-a714-a914373942af" # str | A unique ID that can be used to reference a Kubernetes cluster.

    # example passing only required values which don't have defaults set
    try:
        # Retrieve User Information for a Kubernetes Cluster
        api_response = api_instance.get_cluster_user(cluster_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling KubernetesApi->get_cluster_user: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**| A unique ID that can be used to reference a Kubernetes cluster. |

### Return type

[**User**](User.md)

### Authorization

[bearer_auth](../README.md#bearer_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The response will be a JSON object with a key called &#x60;kubernetes_cluster_user&#x60; containing the username and in-cluster groups that it belongs to.  |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**401** | Unauthorized |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**404** | The resource was not found. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**429** | API Rate limit exceeded |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**500** | Server error. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**0** | Unexpected error |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_clusterlint_results**
> ClusterlintResults get_clusterlint_results(cluster_id)

Fetch Clusterlint Diagnostics for a Kubernetes Cluster

To request clusterlint diagnostics for your cluster, send a GET request to `/v2/kubernetes/clusters/$K8S_CLUSTER_ID/clusterlint`. If the `run_id` query parameter is provided, then the diagnostics for the specific run is fetched. By default, the latest results are shown.  To find out how to address clusterlint feedback, please refer to [the clusterlint check documentation](https://github.com/digitalocean/clusterlint/blob/master/checks.md). 

### Example

* Bearer Authentication (bearer_auth):

```python
import time
import openapi_client
from openapi_client.api import kubernetes_api
from openapi_client.model.clusterlint_results import ClusterlintResults
from openapi_client.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to https://api.digitalocean.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.digitalocean.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: bearer_auth
configuration = openapi_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = kubernetes_api.KubernetesApi(api_client)
    cluster_id = "bd5f5959-5e1e-4205-a714-a914373942af" # str | A unique ID that can be used to reference a Kubernetes cluster.
    run_id = "50c2f44c-011d-493e-aee5-361a4a0d1844" # str | Specifies the clusterlint run whose results will be retrieved. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Fetch Clusterlint Diagnostics for a Kubernetes Cluster
        api_response = api_instance.get_clusterlint_results(cluster_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling KubernetesApi->get_clusterlint_results: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Fetch Clusterlint Diagnostics for a Kubernetes Cluster
        api_response = api_instance.get_clusterlint_results(cluster_id, run_id=run_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling KubernetesApi->get_clusterlint_results: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**| A unique ID that can be used to reference a Kubernetes cluster. |
 **run_id** | **str**| Specifies the clusterlint run whose results will be retrieved. | [optional]

### Return type

[**ClusterlintResults**](ClusterlintResults.md)

### Authorization

[bearer_auth](../README.md#bearer_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The response is a JSON object which contains the diagnostics on Kubernetes objects in the cluster. Each diagnostic will contain some metadata information about the object and feedback for users to act upon.  |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**401** | Unauthorized |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**404** | The resource was not found. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**429** | API Rate limit exceeded |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**500** | Server error. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**0** | Unexpected error |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_credentials**
> Credentials get_credentials(cluster_id)

Retrieve Credentials for a Kubernetes Cluster

This endpoint returns a JSON object . It can be used to programmatically construct Kubernetes clients which cannot parse kubeconfig files.  The resulting JSON object contains token-based authentication for clusters supporting it, and certificate-based authentication otherwise. For a list of supported versions and more information, see \"[How to Connect to a DigitalOcean Kubernetes Cluster with kubectl](https://www.digitalocean.com/docs/kubernetes/how-to/connect-with-kubectl/)\".  To retrieve credentials for accessing a Kubernetes cluster, send a GET request to `/v2/kubernetes/clusters/$K8S_CLUSTER_ID/credentials`.  Clusters supporting token-based authentication may define an expiration by passing a duration in seconds as a query parameter to `/v2/kubernetes/clusters/$K8S_CLUSTER_ID/kubeconfig?expiry_seconds=$DURATION_IN_SECONDS`. If not set or 0, then the token will have a 7 day expiry. The query parameter has no impact in certificate-based authentication. 

### Example

* Bearer Authentication (bearer_auth):

```python
import time
import openapi_client
from openapi_client.api import kubernetes_api
from openapi_client.model.error import Error
from openapi_client.model.credentials import Credentials
from pprint import pprint
# Defining the host is optional and defaults to https://api.digitalocean.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.digitalocean.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: bearer_auth
configuration = openapi_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = kubernetes_api.KubernetesApi(api_client)
    cluster_id = "bd5f5959-5e1e-4205-a714-a914373942af" # str | A unique ID that can be used to reference a Kubernetes cluster.
    expiry_seconds = 300 # int | The duration in seconds that the returned Kubernetes credentials will be valid. If not set or 0, the credentials will have a 7 day expiry. (optional) if omitted the server will use the default value of 0

    # example passing only required values which don't have defaults set
    try:
        # Retrieve Credentials for a Kubernetes Cluster
        api_response = api_instance.get_credentials(cluster_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling KubernetesApi->get_credentials: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Retrieve Credentials for a Kubernetes Cluster
        api_response = api_instance.get_credentials(cluster_id, expiry_seconds=expiry_seconds)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling KubernetesApi->get_credentials: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**| A unique ID that can be used to reference a Kubernetes cluster. |
 **expiry_seconds** | **int**| The duration in seconds that the returned Kubernetes credentials will be valid. If not set or 0, the credentials will have a 7 day expiry. | [optional] if omitted the server will use the default value of 0

### Return type

[**Credentials**](Credentials.md)

### Authorization

[bearer_auth](../README.md#bearer_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A JSON object containing credentials for a cluster. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**401** | Unauthorized |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**404** | The resource was not found. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**429** | API Rate limit exceeded |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**500** | Server error. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**0** | Unexpected error |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_kubeconfig**
> str get_kubeconfig(cluster_id)

Retrieve the kubeconfig for a Kubernetes Cluster

This endpoint returns a kubeconfig file in YAML format. It can be used to connect to and administer the cluster using the Kubernetes command line tool, `kubectl`, or other programs supporting kubeconfig files (e.g., client libraries).  The resulting kubeconfig file uses token-based authentication for clusters supporting it, and certificate-based authentication otherwise. For a list of supported versions and more information, see \"[How to Connect to a DigitalOcean Kubernetes Cluster with kubectl](https://www.digitalocean.com/docs/kubernetes/how-to/connect-with-kubectl/)\".  To retrieve a kubeconfig file for use with a Kubernetes cluster, send a GET request to `/v2/kubernetes/clusters/$K8S_CLUSTER_ID/kubeconfig`.  Clusters supporting token-based authentication may define an expiration by passing a duration in seconds as a query parameter to `/v2/kubernetes/clusters/$K8S_CLUSTER_ID/kubeconfig?expiry_seconds=$DURATION_IN_SECONDS`. If not set or 0, then the token will have a 7 day expiry. The query parameter has no impact in certificate-based authentication. 

### Example

* Bearer Authentication (bearer_auth):

```python
import time
import openapi_client
from openapi_client.api import kubernetes_api
from openapi_client.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to https://api.digitalocean.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.digitalocean.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: bearer_auth
configuration = openapi_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = kubernetes_api.KubernetesApi(api_client)
    cluster_id = "bd5f5959-5e1e-4205-a714-a914373942af" # str | A unique ID that can be used to reference a Kubernetes cluster.
    expiry_seconds = 300 # int | The duration in seconds that the returned Kubernetes credentials will be valid. If not set or 0, the credentials will have a 7 day expiry. (optional) if omitted the server will use the default value of 0

    # example passing only required values which don't have defaults set
    try:
        # Retrieve the kubeconfig for a Kubernetes Cluster
        api_response = api_instance.get_kubeconfig(cluster_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling KubernetesApi->get_kubeconfig: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Retrieve the kubeconfig for a Kubernetes Cluster
        api_response = api_instance.get_kubeconfig(cluster_id, expiry_seconds=expiry_seconds)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling KubernetesApi->get_kubeconfig: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**| A unique ID that can be used to reference a Kubernetes cluster. |
 **expiry_seconds** | **int**| The duration in seconds that the returned Kubernetes credentials will be valid. If not set or 0, the credentials will have a 7 day expiry. | [optional] if omitted the server will use the default value of 0

### Return type

**str**

### Authorization

[bearer_auth](../README.md#bearer_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/yaml, application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A kubeconfig file for the cluster in YAML format. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**401** | Unauthorized |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**404** | The resource was not found. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**429** | API Rate limit exceeded |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**500** | Server error. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**0** | Unexpected error |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_kubernetes_cluster**
> bool, date, datetime, dict, float, int, list, str, none_type get_kubernetes_cluster(cluster_id)

Retrieve an Existing Kubernetes Cluster

To show information about an existing Kubernetes cluster, send a GET request to `/v2/kubernetes/clusters/$K8S_CLUSTER_ID`. 

### Example

* Bearer Authentication (bearer_auth):

```python
import time
import openapi_client
from openapi_client.api import kubernetes_api
from openapi_client.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to https://api.digitalocean.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.digitalocean.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: bearer_auth
configuration = openapi_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = kubernetes_api.KubernetesApi(api_client)
    cluster_id = "bd5f5959-5e1e-4205-a714-a914373942af" # str | A unique ID that can be used to reference a Kubernetes cluster.

    # example passing only required values which don't have defaults set
    try:
        # Retrieve an Existing Kubernetes Cluster
        api_response = api_instance.get_kubernetes_cluster(cluster_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling KubernetesApi->get_kubernetes_cluster: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**| A unique ID that can be used to reference a Kubernetes cluster. |

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
**200** | The response will be a JSON object with a key called &#x60;kubernetes_cluster&#x60;. The value of this will be an object containing the standard attributes of a Kubernetes cluster.  |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**401** | Unauthorized |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**404** | The resource was not found. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**429** | API Rate limit exceeded |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**500** | Server error. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**0** | Unexpected error |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_node_pool**
> bool, date, datetime, dict, float, int, list, str, none_type get_node_pool(cluster_id, node_pool_id)

Retrieve a Node Pool for a Kubernetes Cluster

To show information about a specific node pool in a Kubernetes cluster, send a GET request to `/v2/kubernetes/clusters/$K8S_CLUSTER_ID/node_pools/$NODE_POOL_ID`. 

### Example

* Bearer Authentication (bearer_auth):

```python
import time
import openapi_client
from openapi_client.api import kubernetes_api
from openapi_client.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to https://api.digitalocean.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.digitalocean.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: bearer_auth
configuration = openapi_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = kubernetes_api.KubernetesApi(api_client)
    cluster_id = "bd5f5959-5e1e-4205-a714-a914373942af" # str | A unique ID that can be used to reference a Kubernetes cluster.
    node_pool_id = "cdda885e-7663-40c8-bc74-3a036c66545d" # str | A unique ID that can be used to reference a Kubernetes node pool.

    # example passing only required values which don't have defaults set
    try:
        # Retrieve a Node Pool for a Kubernetes Cluster
        api_response = api_instance.get_node_pool(cluster_id, node_pool_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling KubernetesApi->get_node_pool: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**| A unique ID that can be used to reference a Kubernetes cluster. |
 **node_pool_id** | **str**| A unique ID that can be used to reference a Kubernetes node pool. |

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
**200** | The response will be a JSON object with a key called &#x60;node_pool&#x60;. The value of this will be an object containing the standard attributes of a node pool.  |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**401** | Unauthorized |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**404** | The resource was not found. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**429** | API Rate limit exceeded |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**500** | Server error. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**0** | Unexpected error |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_all_kubernetes_clusters**
> bool, date, datetime, dict, float, int, list, str, none_type list_all_kubernetes_clusters()

List All Kubernetes Clusters

To list all of the Kubernetes clusters on your account, send a GET request to `/v2/kubernetes/clusters`. 

### Example

* Bearer Authentication (bearer_auth):

```python
import time
import openapi_client
from openapi_client.api import kubernetes_api
from openapi_client.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to https://api.digitalocean.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.digitalocean.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: bearer_auth
configuration = openapi_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = kubernetes_api.KubernetesApi(api_client)
    per_page = 2 # int | Number of items returned per page (optional) if omitted the server will use the default value of 20
    page = 1 # int | Which 'page' of paginated results to return. (optional) if omitted the server will use the default value of 1

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List All Kubernetes Clusters
        api_response = api_instance.list_all_kubernetes_clusters(per_page=per_page, page=page)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling KubernetesApi->list_all_kubernetes_clusters: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **per_page** | **int**| Number of items returned per page | [optional] if omitted the server will use the default value of 20
 **page** | **int**| Which &#39;page&#39; of paginated results to return. | [optional] if omitted the server will use the default value of 1

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
**200** | The response will be a JSON object with a key called &#x60;kubernetes_clusters&#x60;. This will be set to an array of objects, each of which will contain the standard Kubernetes cluster attributes.  |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**401** | Unauthorized |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**429** | API Rate limit exceeded |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**500** | Server error. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**0** | Unexpected error |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_kubernetes_associated_resources**
> AssociatedKubernetesResources list_kubernetes_associated_resources(cluster_id)

List Associated Resources for Cluster Deletion

To list the associated billable resources that can be destroyed along with a cluster, send a GET request to the `/v2/kubernetes/clusters/$K8S_CLUSTER_ID/destroy_with_associated_resources` endpoint.

### Example

* Bearer Authentication (bearer_auth):

```python
import time
import openapi_client
from openapi_client.api import kubernetes_api
from openapi_client.model.error import Error
from openapi_client.model.associated_kubernetes_resources import AssociatedKubernetesResources
from pprint import pprint
# Defining the host is optional and defaults to https://api.digitalocean.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.digitalocean.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: bearer_auth
configuration = openapi_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = kubernetes_api.KubernetesApi(api_client)
    cluster_id = "bd5f5959-5e1e-4205-a714-a914373942af" # str | A unique ID that can be used to reference a Kubernetes cluster.

    # example passing only required values which don't have defaults set
    try:
        # List Associated Resources for Cluster Deletion
        api_response = api_instance.list_kubernetes_associated_resources(cluster_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling KubernetesApi->list_kubernetes_associated_resources: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**| A unique ID that can be used to reference a Kubernetes cluster. |

### Return type

[**AssociatedKubernetesResources**](AssociatedKubernetesResources.md)

### Authorization

[bearer_auth](../README.md#bearer_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The response will be a JSON object containing &#x60;load_balancers&#x60;, &#x60;volumes&#x60;, and &#x60;volume_snapshots&#x60; keys. Each will be set to an array of objects containing the standard attributes for associated resources. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**401** | Unauthorized |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**404** | The resource was not found. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**429** | API Rate limit exceeded |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**500** | Server error. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**0** | Unexpected error |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_kubernetes_options**
> KubernetesOptions list_kubernetes_options()

List Available Regions, Node Sizes, and Versions of Kubernetes

To list the versions of Kubernetes available for use, the regions that support Kubernetes, and the available node sizes, send a GET request to `/v2/kubernetes/options`.

### Example

* Bearer Authentication (bearer_auth):

```python
import time
import openapi_client
from openapi_client.api import kubernetes_api
from openapi_client.model.kubernetes_options import KubernetesOptions
from openapi_client.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to https://api.digitalocean.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.digitalocean.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: bearer_auth
configuration = openapi_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = kubernetes_api.KubernetesApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # List Available Regions, Node Sizes, and Versions of Kubernetes
        api_response = api_instance.list_kubernetes_options()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling KubernetesApi->list_kubernetes_options: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**KubernetesOptions**](KubernetesOptions.md)

### Authorization

[bearer_auth](../README.md#bearer_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The response will be a JSON object with a key called &#x60;options&#x60; which contains &#x60;regions&#x60;, &#x60;versions&#x60;, and &#x60;sizes&#x60; objects listing the available options and the matching slugs for use when creating a new cluster.  |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**401** | Unauthorized |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**404** | The resource was not found. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**429** | API Rate limit exceeded |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**500** | Server error. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**0** | Unexpected error |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_node_pools**
> bool, date, datetime, dict, float, int, list, str, none_type list_node_pools(cluster_id)

List All Node Pools in a Kubernetes Clusters

To list all of the node pools in a Kubernetes clusters, send a GET request to `/v2/kubernetes/clusters/$K8S_CLUSTER_ID/node_pools`. 

### Example

* Bearer Authentication (bearer_auth):

```python
import time
import openapi_client
from openapi_client.api import kubernetes_api
from openapi_client.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to https://api.digitalocean.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.digitalocean.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: bearer_auth
configuration = openapi_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = kubernetes_api.KubernetesApi(api_client)
    cluster_id = "bd5f5959-5e1e-4205-a714-a914373942af" # str | A unique ID that can be used to reference a Kubernetes cluster.

    # example passing only required values which don't have defaults set
    try:
        # List All Node Pools in a Kubernetes Clusters
        api_response = api_instance.list_node_pools(cluster_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling KubernetesApi->list_node_pools: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**| A unique ID that can be used to reference a Kubernetes cluster. |

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
**200** | The response will be a JSON object with a key called &#x60;node_pools&#x60;. This will be set to an array of objects, each of which will contain the standard node pool attributes.  |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**401** | Unauthorized |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**404** | The resource was not found. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**429** | API Rate limit exceeded |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**500** | Server error. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**0** | Unexpected error |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **recycle_kubernetes_node_pool**
> recycle_kubernetes_node_pool(cluster_id, node_pool_id, unknown_base_type)

Recycle a Kubernetes Node Pool

The endpoint has been deprecated. Please use the DELETE `/v2/kubernetes/clusters/$K8S_CLUSTER_ID/node_pools/$NODE_POOL_ID/nodes/$NODE_ID` method instead. 

### Example

* Bearer Authentication (bearer_auth):

```python
import time
import openapi_client
from openapi_client.api import kubernetes_api
from openapi_client.model.unknownbasetype import UNKNOWNBASETYPE
from openapi_client.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to https://api.digitalocean.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.digitalocean.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: bearer_auth
configuration = openapi_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = kubernetes_api.KubernetesApi(api_client)
    cluster_id = "bd5f5959-5e1e-4205-a714-a914373942af" # str | A unique ID that can be used to reference a Kubernetes cluster.
    node_pool_id = "cdda885e-7663-40c8-bc74-3a036c66545d" # str | A unique ID that can be used to reference a Kubernetes node pool.
    unknown_base_type = None # UNKNOWN_BASE_TYPE | 

    # example passing only required values which don't have defaults set
    try:
        # Recycle a Kubernetes Node Pool
        api_instance.recycle_kubernetes_node_pool(cluster_id, node_pool_id, unknown_base_type)
    except openapi_client.ApiException as e:
        print("Exception when calling KubernetesApi->recycle_kubernetes_node_pool: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**| A unique ID that can be used to reference a Kubernetes cluster. |
 **node_pool_id** | **str**| A unique ID that can be used to reference a Kubernetes node pool. |
 **unknown_base_type** | [**UNKNOWN_BASE_TYPE**](UNKNOWN_BASE_TYPE.md)|  |

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

# **remove_registry**
> remove_registry()

Remove Container Registry from Kubernetes Clusters

To remove the container registry from Kubernetes clusters, send a DELETE request to `/v2/kubernetes/registry`.

### Example

* Bearer Authentication (bearer_auth):

```python
import time
import openapi_client
from openapi_client.api import kubernetes_api
from openapi_client.model.cluster_registries import ClusterRegistries
from openapi_client.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to https://api.digitalocean.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.digitalocean.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: bearer_auth
configuration = openapi_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = kubernetes_api.KubernetesApi(api_client)
    cluster_registries = ClusterRegistries(
        cluster_uuids=["bd5f5959-5e1e-4205-a714-a914373942af","50c2f44c-011d-493e-aee5-361a4a0d1844"],
    ) # ClusterRegistries |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Remove Container Registry from Kubernetes Clusters
        api_instance.remove_registry(cluster_registries=cluster_registries)
    except openapi_client.ApiException as e:
        print("Exception when calling KubernetesApi->remove_registry: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_registries** | [**ClusterRegistries**](ClusterRegistries.md)|  | [optional]

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
**429** | API Rate limit exceeded |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**500** | Server error. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**0** | Unexpected error |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **run_clusterlint**
> bool, date, datetime, dict, float, int, list, str, none_type run_clusterlint(cluster_id)

Run Clusterlint Checks on a Kubernetes Cluster

Clusterlint helps operators conform to Kubernetes best practices around resources, security and reliability to avoid common problems while operating or upgrading the clusters.  To request a clusterlint run on your cluster, send a POST request to `/v2/kubernetes/clusters/$K8S_CLUSTER_ID/clusterlint`. This will run all checks present in the `doks` group by default, if a request body is not specified. Optionally specify the below attributes.  For information about the available checks, please refer to [the clusterlint check documentation](https://github.com/digitalocean/clusterlint/blob/master/checks.md). 

### Example

* Bearer Authentication (bearer_auth):

```python
import time
import openapi_client
from openapi_client.api import kubernetes_api
from openapi_client.model.clusterlint_request import ClusterlintRequest
from openapi_client.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to https://api.digitalocean.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.digitalocean.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: bearer_auth
configuration = openapi_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = kubernetes_api.KubernetesApi(api_client)
    cluster_id = "bd5f5959-5e1e-4205-a714-a914373942af" # str | A unique ID that can be used to reference a Kubernetes cluster.
    clusterlint_request = ClusterlintRequest(
        include_groups=["basic","doks","security"],
        include_checks=["bare-pods","resource-requirements"],
        exclude_groups=["workload-health"],
        exclude_checks=["default-namespace"],
    ) # ClusterlintRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Run Clusterlint Checks on a Kubernetes Cluster
        api_response = api_instance.run_clusterlint(cluster_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling KubernetesApi->run_clusterlint: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Run Clusterlint Checks on a Kubernetes Cluster
        api_response = api_instance.run_clusterlint(cluster_id, clusterlint_request=clusterlint_request)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling KubernetesApi->run_clusterlint: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**| A unique ID that can be used to reference a Kubernetes cluster. |
 **clusterlint_request** | [**ClusterlintRequest**](ClusterlintRequest.md)|  | [optional]

### Return type

**bool, date, datetime, dict, float, int, list, str, none_type**

### Authorization

[bearer_auth](../README.md#bearer_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | The response is a JSON object with a key called &#x60;run_id&#x60; that you can later use to fetch the run results. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**401** | Unauthorized |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**404** | The resource was not found. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**429** | API Rate limit exceeded |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**500** | Server error. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**0** | Unexpected error |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_kubernetes_cluster**
> bool, date, datetime, dict, float, int, list, str, none_type update_kubernetes_cluster(cluster_id, cluster_update)

Update a Kubernetes Cluster

To update a Kubernetes cluster, send a PUT request to `/v2/kubernetes/clusters/$K8S_CLUSTER_ID` and specify one or more of the attributes below. 

### Example

* Bearer Authentication (bearer_auth):

```python
import time
import openapi_client
from openapi_client.api import kubernetes_api
from openapi_client.model.error import Error
from openapi_client.model.cluster_update import ClusterUpdate
from pprint import pprint
# Defining the host is optional and defaults to https://api.digitalocean.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.digitalocean.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: bearer_auth
configuration = openapi_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = kubernetes_api.KubernetesApi(api_client)
    cluster_id = "bd5f5959-5e1e-4205-a714-a914373942af" # str | A unique ID that can be used to reference a Kubernetes cluster.
    cluster_update = ClusterUpdate(
        name="prod-cluster-01",
        tags=["k8s","k8s:bd5f5959-5e1e-4205-a714-a914373942af","production","web-team"],
        maintenance_policy=MaintenancePolicy(
            start_time="12:00",
            day="any",
        ),
        auto_upgrade=True,
        surge_upgrade=True,
    ) # ClusterUpdate | 

    # example passing only required values which don't have defaults set
    try:
        # Update a Kubernetes Cluster
        api_response = api_instance.update_kubernetes_cluster(cluster_id, cluster_update)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling KubernetesApi->update_kubernetes_cluster: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**| A unique ID that can be used to reference a Kubernetes cluster. |
 **cluster_update** | [**ClusterUpdate**](ClusterUpdate.md)|  |

### Return type

**bool, date, datetime, dict, float, int, list, str, none_type**

### Authorization

[bearer_auth](../README.md#bearer_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | The response will be a JSON object with a key called &#x60;kubernetes_cluster&#x60;. The value of this will be an object containing the standard attributes of a Kubernetes cluster.  |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**401** | Unauthorized |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**404** | The resource was not found. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**429** | API Rate limit exceeded |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**500** | Server error. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**0** | Unexpected error |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_kubernetes_node_pool**
> bool, date, datetime, dict, float, int, list, str, none_type update_kubernetes_node_pool(cluster_id, node_pool_id, kubernetes_node_pool_update)

Update a Node Pool in a Kubernetes Cluster

To update the name of a node pool, edit the tags applied to it, or adjust its number of nodes, send a PUT request to `/v2/kubernetes/clusters/$K8S_CLUSTER_ID/node_pools/$NODE_POOL_ID` with the following attributes. 

### Example

* Bearer Authentication (bearer_auth):

```python
import time
import openapi_client
from openapi_client.api import kubernetes_api
from openapi_client.model.kubernetes_node_pool_update import KubernetesNodePoolUpdate
from openapi_client.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to https://api.digitalocean.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.digitalocean.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: bearer_auth
configuration = openapi_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = kubernetes_api.KubernetesApi(api_client)
    cluster_id = "bd5f5959-5e1e-4205-a714-a914373942af" # str | A unique ID that can be used to reference a Kubernetes cluster.
    node_pool_id = "cdda885e-7663-40c8-bc74-3a036c66545d" # str | A unique ID that can be used to reference a Kubernetes node pool.
    kubernetes_node_pool_update = KubernetesNodePoolUpdate() # KubernetesNodePoolUpdate | 

    # example passing only required values which don't have defaults set
    try:
        # Update a Node Pool in a Kubernetes Cluster
        api_response = api_instance.update_kubernetes_node_pool(cluster_id, node_pool_id, kubernetes_node_pool_update)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling KubernetesApi->update_kubernetes_node_pool: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**| A unique ID that can be used to reference a Kubernetes cluster. |
 **node_pool_id** | **str**| A unique ID that can be used to reference a Kubernetes node pool. |
 **kubernetes_node_pool_update** | [**KubernetesNodePoolUpdate**](KubernetesNodePoolUpdate.md)|  |

### Return type

**bool, date, datetime, dict, float, int, list, str, none_type**

### Authorization

[bearer_auth](../README.md#bearer_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | The response will be a JSON object with a key called &#x60;node_pool&#x60;. The value of this will be an object containing the standard attributes of a node pool.  |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**401** | Unauthorized |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**404** | The resource was not found. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**429** | API Rate limit exceeded |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**500** | Server error. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**0** | Unexpected error |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upgrade_kubernetes_cluster**
> upgrade_kubernetes_cluster(cluster_id, unknown_base_type)

Upgrade a Kubernetes Cluster

To immediately upgrade a Kubernetes cluster to a newer patch release of Kubernetes, send a POST request to `/v2/kubernetes/clusters/$K8S_CLUSTER_ID/upgrade`. The body of the request must specify a version attribute.  Available upgrade versions for a cluster can be fetched from `/v2/kubernetes/clusters/$K8S_CLUSTER_ID/upgrades`. 

### Example

* Bearer Authentication (bearer_auth):

```python
import time
import openapi_client
from openapi_client.api import kubernetes_api
from openapi_client.model.unknownbasetype import UNKNOWNBASETYPE
from openapi_client.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to https://api.digitalocean.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.digitalocean.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: bearer_auth
configuration = openapi_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = kubernetes_api.KubernetesApi(api_client)
    cluster_id = "bd5f5959-5e1e-4205-a714-a914373942af" # str | A unique ID that can be used to reference a Kubernetes cluster.
    unknown_base_type = None # UNKNOWN_BASE_TYPE | 

    # example passing only required values which don't have defaults set
    try:
        # Upgrade a Kubernetes Cluster
        api_instance.upgrade_kubernetes_cluster(cluster_id, unknown_base_type)
    except openapi_client.ApiException as e:
        print("Exception when calling KubernetesApi->upgrade_kubernetes_cluster: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**| A unique ID that can be used to reference a Kubernetes cluster. |
 **unknown_base_type** | [**UNKNOWN_BASE_TYPE**](UNKNOWN_BASE_TYPE.md)|  |

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

