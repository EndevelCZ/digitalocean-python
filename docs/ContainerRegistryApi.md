# openapi_client.ContainerRegistryApi

All URIs are relative to *https://api.digitalocean.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_registry**](ContainerRegistryApi.md#create_registry) | **POST** /v2/registry | Create Container Registry
[**delete_registry**](ContainerRegistryApi.md#delete_registry) | **DELETE** /v2/registry | Delete Container Registry
[**delete_repository_manifest**](ContainerRegistryApi.md#delete_repository_manifest) | **DELETE** /v2/registry/{registry_name}/{repository_name}/digests/{manifest_digest} | Delete Container Registry Repository Manifest
[**delete_repository_tag**](ContainerRegistryApi.md#delete_repository_tag) | **DELETE** /v2/registry/{registry_name}/{repository_name}/tags/{repository_tag} | Delete Container Registry Repository Tag
[**get_docker_credentials**](ContainerRegistryApi.md#get_docker_credentials) | **GET** /v2/registry/docker-credentials | Get Docker Credentials for Container Registry
[**get_garbage_collection**](ContainerRegistryApi.md#get_garbage_collection) | **GET** /v2/registry/{registry_name}/garbage-collection | Get Active Garbage Collection
[**get_registry**](ContainerRegistryApi.md#get_registry) | **GET** /v2/registry | Get Container Registry Information
[**get_registry_options**](ContainerRegistryApi.md#get_registry_options) | **GET** /v2/registry/options | List Available Subscription Tiers
[**get_registry_subscription**](ContainerRegistryApi.md#get_registry_subscription) | **GET** /v2/registry/subscription | Get Subscription Information
[**list_garbage_collections**](ContainerRegistryApi.md#list_garbage_collections) | **GET** /v2/registry/{registry_name}/garbage-collections | List Garbage Collections
[**list_registry_repositories**](ContainerRegistryApi.md#list_registry_repositories) | **GET** /v2/registry/{registry_name} | List All Container Registry Repositories
[**list_repository_tags**](ContainerRegistryApi.md#list_repository_tags) | **GET** /v2/registry/{registry_name}/{repository_name}/tags | List All Container Registry Repository Tags
[**post_registry_subscription**](ContainerRegistryApi.md#post_registry_subscription) | **POST** /v2/registry/subscription | Update Subscription Tier
[**run_garbage_collection**](ContainerRegistryApi.md#run_garbage_collection) | **POST** /v2/registry/{registry_name}/garbage-collection | Start Garbage Collection
[**update_garbage_collection**](ContainerRegistryApi.md#update_garbage_collection) | **PUT** /v2/registry/{registry_name}/garbage-collection/{garbage_collection_uuid} | Update Garbage Collection
[**validate_registry_name**](ContainerRegistryApi.md#validate_registry_name) | **POST** /v2/registry/validate-name | Validate a Container Registry Name


# **create_registry**
> bool, date, datetime, dict, float, int, list, str, none_type create_registry(registry_create)

Create Container Registry

To create your container registry, send a POST request to `/v2/registry`.  The `name` becomes part of the URL for images stored in the registry. For example, if your registry is called `example`, an image in it will have the URL `registry.digitalocean.com/example/image:tag`. 

### Example

* Bearer Authentication (bearer_auth):

```python
import time
import openapi_client
from openapi_client.api import container_registry_api
from openapi_client.model.registry_create import RegistryCreate
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
    api_instance = container_registry_api.ContainerRegistryApi(api_client)
    registry_create = RegistryCreate(
        name="example",
        subscription_tier_slug="basic",
    ) # RegistryCreate | 

    # example passing only required values which don't have defaults set
    try:
        # Create Container Registry
        api_response = api_instance.create_registry(registry_create)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ContainerRegistryApi->create_registry: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **registry_create** | [**RegistryCreate**](RegistryCreate.md)|  |

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
**201** | The response will be a JSON object with the key &#x60;registry&#x60; containing information about your registry. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**401** | Unauthorized |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**429** | API Rate limit exceeded |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**500** | Server error. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**0** | Unexpected error |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_registry**
> delete_registry()

Delete Container Registry

To delete your container registry, destroying all container image data stored in it, send a DELETE request to `/v2/registry`.

### Example

* Bearer Authentication (bearer_auth):

```python
import time
import openapi_client
from openapi_client.api import container_registry_api
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
    api_instance = container_registry_api.ContainerRegistryApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Delete Container Registry
        api_instance.delete_registry()
    except openapi_client.ApiException as e:
        print("Exception when calling ContainerRegistryApi->delete_registry: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

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

# **delete_repository_manifest**
> delete_repository_manifest(registry_name, repository_name, manifest_digest)

Delete Container Registry Repository Manifest

To delete a container repository manifest by digest, send a DELETE request to `/v2/registry/$REGISTRY_NAME/repositories/$REPOSITORY_NAME/digests/$MANIFEST_DIGEST`.  Note that if your repository name contains `/` characters, it must be URL-encoded in the request URL. For example, to delete `registry.digitalocean.com/example/my/repo@sha256:abcd`, the path would be `/v2/registry/example/repositories/my%2Frepo/digests/sha256:abcd`.  A successful request will receive a 204 status code with no body in response. This indicates that the request was processed successfully. 

### Example

* Bearer Authentication (bearer_auth):

```python
import time
import openapi_client
from openapi_client.api import container_registry_api
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
    api_instance = container_registry_api.ContainerRegistryApi(api_client)
    registry_name = "example" # str | The name of a container registry.
    repository_name = "repo-1" # str | The name of a container registry repository. If the name contains `/` characters, they must be URL-encoded, e.g. `%2F`.
    manifest_digest = "sha256:cb8a924afdf0229ef7515d9e5b3024e23b3eb03ddbba287f4a19c6ac90b8d221" # str | The manifest digest of a container registry repository tag.

    # example passing only required values which don't have defaults set
    try:
        # Delete Container Registry Repository Manifest
        api_instance.delete_repository_manifest(registry_name, repository_name, manifest_digest)
    except openapi_client.ApiException as e:
        print("Exception when calling ContainerRegistryApi->delete_repository_manifest: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **registry_name** | **str**| The name of a container registry. |
 **repository_name** | **str**| The name of a container registry repository. If the name contains &#x60;/&#x60; characters, they must be URL-encoded, e.g. &#x60;%2F&#x60;. |
 **manifest_digest** | **str**| The manifest digest of a container registry repository tag. |

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

# **delete_repository_tag**
> delete_repository_tag(registry_name, repository_name, repository_tag)

Delete Container Registry Repository Tag

To delete a container repository tag, send a DELETE request to `/v2/registry/$REGISTRY_NAME/repositories/$REPOSITORY_NAME/tags/$TAG`.  Note that if your repository name contains `/` characters, it must be URL-encoded in the request URL. For example, to delete `registry.digitalocean.com/example/my/repo:mytag`, the path would be `/v2/registry/example/repositories/my%2Frepo/tags/mytag`.  A successful request will receive a 204 status code with no body in response. This indicates that the request was processed successfully. 

### Example

* Bearer Authentication (bearer_auth):

```python
import time
import openapi_client
from openapi_client.api import container_registry_api
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
    api_instance = container_registry_api.ContainerRegistryApi(api_client)
    registry_name = "example" # str | The name of a container registry.
    repository_name = "repo-1" # str | The name of a container registry repository. If the name contains `/` characters, they must be URL-encoded, e.g. `%2F`.
    repository_tag = "06a447a" # str | The name of a container registry repository tag.

    # example passing only required values which don't have defaults set
    try:
        # Delete Container Registry Repository Tag
        api_instance.delete_repository_tag(registry_name, repository_name, repository_tag)
    except openapi_client.ApiException as e:
        print("Exception when calling ContainerRegistryApi->delete_repository_tag: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **registry_name** | **str**| The name of a container registry. |
 **repository_name** | **str**| The name of a container registry repository. If the name contains &#x60;/&#x60; characters, they must be URL-encoded, e.g. &#x60;%2F&#x60;. |
 **repository_tag** | **str**| The name of a container registry repository tag. |

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

# **get_docker_credentials**
> DockerCredentials get_docker_credentials()

Get Docker Credentials for Container Registry

In order to access your container registry with the Docker client or from a Kubernetes cluster, you will need to configure authentication. The necessary JSON configuration can be retrieved by sending a GET request to `/v2/registry/docker-credentials`.  The response will be in the format of a Docker `config.json` file. To use the config in your Kubernetes cluster, create a Secret with:      kubectl create secret generic docr \\       --from-file=.dockerconfigjson=config.json \\       --type=kubernetes.io/dockerconfigjson  By default, the returned credentials have read-only access to your registry and cannot be used to push images. This is appropriate for most Kubernetes clusters. To retrieve read/write credentials, suitable for use with the Docker client or in a CI system, read_write may be provided as query parameter. For example: `/v2/registry/docker-credentials?read_write=true`  By default, the returned credentials will not expire. To retrieve credentials with an expiry set, expiry_seconds may be provided as a query parameter. For example: `/v2/registry/docker-credentials?expiry_seconds=3600` will return credentials that expire after one hour. 

### Example

* Bearer Authentication (bearer_auth):

```python
import time
import openapi_client
from openapi_client.api import container_registry_api
from openapi_client.model.error import Error
from openapi_client.model.docker_credentials import DockerCredentials
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
    api_instance = container_registry_api.ContainerRegistryApi(api_client)
    expiry_seconds = 3600 # int | The duration in seconds that the returned registry credentials will be valid. If not set or 0, the credentials will not expire. (optional) if omitted the server will use the default value of 0
    read_write = True # bool | By default, the registry credentials allow for read-only access. Set this query parameter to `true` to obtain read-write credentials. (optional) if omitted the server will use the default value of False

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get Docker Credentials for Container Registry
        api_response = api_instance.get_docker_credentials(expiry_seconds=expiry_seconds, read_write=read_write)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ContainerRegistryApi->get_docker_credentials: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **expiry_seconds** | **int**| The duration in seconds that the returned registry credentials will be valid. If not set or 0, the credentials will not expire. | [optional] if omitted the server will use the default value of 0
 **read_write** | **bool**| By default, the registry credentials allow for read-only access. Set this query parameter to &#x60;true&#x60; to obtain read-write credentials. | [optional] if omitted the server will use the default value of False

### Return type

[**DockerCredentials**](DockerCredentials.md)

### Authorization

[bearer_auth](../README.md#bearer_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A Docker &#x60;config.json&#x60; file for the container registry. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**401** | Unauthorized |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**429** | API Rate limit exceeded |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**500** | Server error. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**0** | Unexpected error |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_garbage_collection**
> InlineResponse2007 get_garbage_collection(registry_name)

Get Active Garbage Collection

To get information about the currently-active garbage collection for a registry, send a GET request to `/v2/registry/$REGISTRY_NAME/garbage-collection`.

### Example

* Bearer Authentication (bearer_auth):

```python
import time
import openapi_client
from openapi_client.api import container_registry_api
from openapi_client.model.error import Error
from openapi_client.model.inline_response2007 import InlineResponse2007
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
    api_instance = container_registry_api.ContainerRegistryApi(api_client)
    registry_name = "example" # str | The name of a container registry.

    # example passing only required values which don't have defaults set
    try:
        # Get Active Garbage Collection
        api_response = api_instance.get_garbage_collection(registry_name)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ContainerRegistryApi->get_garbage_collection: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **registry_name** | **str**| The name of a container registry. |

### Return type

[**InlineResponse2007**](InlineResponse2007.md)

### Authorization

[bearer_auth](../README.md#bearer_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The response will be a JSON object with a key of &#x60;garbage_collection&#x60;. This will be a json object with attributes representing the currently-active garbage collection. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**401** | Unauthorized |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**404** | The resource was not found. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**429** | API Rate limit exceeded |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**500** | Server error. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**0** | Unexpected error |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_registry**
> bool, date, datetime, dict, float, int, list, str, none_type get_registry()

Get Container Registry Information

To get information about your container registry, send a GET request to `/v2/registry`.

### Example

* Bearer Authentication (bearer_auth):

```python
import time
import openapi_client
from openapi_client.api import container_registry_api
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
    api_instance = container_registry_api.ContainerRegistryApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Get Container Registry Information
        api_response = api_instance.get_registry()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ContainerRegistryApi->get_registry: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

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
**200** | The response will be a JSON object with the key &#x60;registry&#x60; containing information about your registry. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**401** | Unauthorized |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**429** | API Rate limit exceeded |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**500** | Server error. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**0** | Unexpected error |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_registry_options**
> InlineResponse2009 get_registry_options()

List Available Subscription Tiers

There are multiple subscription tiers available for container registry. Each tier allows a different number of image repositories to be created in your registry, and has a different amount of storage and transfer included. To list the available subscription tiers, send a GET request to `/v2/registry/options`.

### Example

* Bearer Authentication (bearer_auth):

```python
import time
import openapi_client
from openapi_client.api import container_registry_api
from openapi_client.model.error import Error
from openapi_client.model.inline_response2009 import InlineResponse2009
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
    api_instance = container_registry_api.ContainerRegistryApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # List Available Subscription Tiers
        api_response = api_instance.get_registry_options()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ContainerRegistryApi->get_registry_options: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse2009**](InlineResponse2009.md)

### Authorization

[bearer_auth](../README.md#bearer_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The response will be a JSON object with a key called &#x60;options&#x60; which contains a key called &#x60;subscription_tiers&#x60; listing the available tiers. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**401** | Unauthorized |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**429** | API Rate limit exceeded |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**500** | Server error. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**0** | Unexpected error |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_registry_subscription**
> Subscription get_registry_subscription()

Get Subscription Information

A subscription is automatically created when you configure your container registry. To get information about your subscription, send a GET request to `/v2/registry/subscription`.

### Example

* Bearer Authentication (bearer_auth):

```python
import time
import openapi_client
from openapi_client.api import container_registry_api
from openapi_client.model.subscription import Subscription
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
    api_instance = container_registry_api.ContainerRegistryApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Get Subscription Information
        api_response = api_instance.get_registry_subscription()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ContainerRegistryApi->get_registry_subscription: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**Subscription**](Subscription.md)

### Authorization

[bearer_auth](../README.md#bearer_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The response will be a JSON object with a key called &#x60;subscription&#x60; containing information about your subscription. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**401** | Unauthorized |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**429** | API Rate limit exceeded |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**500** | Server error. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**0** | Unexpected error |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_garbage_collections**
> InlineResponse2008 list_garbage_collections(registry_name)

List Garbage Collections

To get information about past garbage collections for a registry, send a GET request to `/v2/registry/$REGISTRY_NAME/garbage-collections`.

### Example

* Bearer Authentication (bearer_auth):

```python
import time
import openapi_client
from openapi_client.api import container_registry_api
from openapi_client.model.error import Error
from openapi_client.model.inline_response2008 import InlineResponse2008
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
    api_instance = container_registry_api.ContainerRegistryApi(api_client)
    registry_name = "example" # str | The name of a container registry.
    per_page = 2 # int | Number of items returned per page (optional) if omitted the server will use the default value of 20
    page = 1 # int | Which 'page' of paginated results to return. (optional) if omitted the server will use the default value of 1

    # example passing only required values which don't have defaults set
    try:
        # List Garbage Collections
        api_response = api_instance.list_garbage_collections(registry_name)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ContainerRegistryApi->list_garbage_collections: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List Garbage Collections
        api_response = api_instance.list_garbage_collections(registry_name, per_page=per_page, page=page)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ContainerRegistryApi->list_garbage_collections: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **registry_name** | **str**| The name of a container registry. |
 **per_page** | **int**| Number of items returned per page | [optional] if omitted the server will use the default value of 20
 **page** | **int**| Which &#39;page&#39; of paginated results to return. | [optional] if omitted the server will use the default value of 1

### Return type

[**InlineResponse2008**](InlineResponse2008.md)

### Authorization

[bearer_auth](../README.md#bearer_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The response will be a JSON object with a key of &#x60;garbage_collections&#x60;. This will be set to an array containing objects representing each past garbage collection. Each will contain the standard Garbage Collection attributes. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**401** | Unauthorized |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**404** | The resource was not found. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**429** | API Rate limit exceeded |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**500** | Server error. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**0** | Unexpected error |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_registry_repositories**
> bool, date, datetime, dict, float, int, list, str, none_type list_registry_repositories(registry_name)

List All Container Registry Repositories

To list all repositories in your container registry, send a GET request to `/v2/registry/$REGISTRY_NAME/repositories`.

### Example

* Bearer Authentication (bearer_auth):

```python
import time
import openapi_client
from openapi_client.api import container_registry_api
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
    api_instance = container_registry_api.ContainerRegistryApi(api_client)
    registry_name = "example" # str | The name of a container registry.
    per_page = 2 # int | Number of items returned per page (optional) if omitted the server will use the default value of 20
    page = 1 # int | Which 'page' of paginated results to return. (optional) if omitted the server will use the default value of 1

    # example passing only required values which don't have defaults set
    try:
        # List All Container Registry Repositories
        api_response = api_instance.list_registry_repositories(registry_name)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ContainerRegistryApi->list_registry_repositories: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List All Container Registry Repositories
        api_response = api_instance.list_registry_repositories(registry_name, per_page=per_page, page=page)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ContainerRegistryApi->list_registry_repositories: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **registry_name** | **str**| The name of a container registry. |
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
**200** | The response body will be a JSON object with a key of &#x60;repositories&#x60;. This will be set to an array containing objects each representing a repository. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**401** | Unauthorized |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**404** | The resource was not found. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**429** | API Rate limit exceeded |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**500** | Server error. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**0** | Unexpected error |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_repository_tags**
> bool, date, datetime, dict, float, int, list, str, none_type list_repository_tags(registry_name, repository_name)

List All Container Registry Repository Tags

To list all tags in your container registry repository, send a GET request to `/v2/registry/$REGISTRY_NAME/repositories/$REPOSITORY_NAME/tags`.  Note that if your repository name contains `/` characters, it must be URL-encoded in the request URL. For example, to list tags for `registry.digitalocean.com/example/my/repo`, the path would be `/v2/registry/example/repositories/my%2Frepo/tags`. 

### Example

* Bearer Authentication (bearer_auth):

```python
import time
import openapi_client
from openapi_client.api import container_registry_api
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
    api_instance = container_registry_api.ContainerRegistryApi(api_client)
    registry_name = "example" # str | The name of a container registry.
    repository_name = "repo-1" # str | The name of a container registry repository. If the name contains `/` characters, they must be URL-encoded, e.g. `%2F`.
    per_page = 2 # int | Number of items returned per page (optional) if omitted the server will use the default value of 20
    page = 1 # int | Which 'page' of paginated results to return. (optional) if omitted the server will use the default value of 1

    # example passing only required values which don't have defaults set
    try:
        # List All Container Registry Repository Tags
        api_response = api_instance.list_repository_tags(registry_name, repository_name)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ContainerRegistryApi->list_repository_tags: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List All Container Registry Repository Tags
        api_response = api_instance.list_repository_tags(registry_name, repository_name, per_page=per_page, page=page)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ContainerRegistryApi->list_repository_tags: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **registry_name** | **str**| The name of a container registry. |
 **repository_name** | **str**| The name of a container registry repository. If the name contains &#x60;/&#x60; characters, they must be URL-encoded, e.g. &#x60;%2F&#x60;. |
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
**200** | The response body will be a JSON object with a key of &#x60;tags&#x60;. This will be set to an array containing objects each representing a tag. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**401** | Unauthorized |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**404** | The resource was not found. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**429** | API Rate limit exceeded |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**500** | Server error. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**0** | Unexpected error |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_registry_subscription**
> Subscription post_registry_subscription()

Update Subscription Tier

After creating your registry, you can switch to a different subscription tier to better suit your needs. To do this, send a POST request to `/v2/registry/subscription`.

### Example

* Bearer Authentication (bearer_auth):

```python
import time
import openapi_client
from openapi_client.api import container_registry_api
from openapi_client.model.subscription import Subscription
from openapi_client.model.error import Error
from openapi_client.model.inline_object4 import InlineObject4
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
    api_instance = container_registry_api.ContainerRegistryApi(api_client)
    inline_object4 = InlineObject4(
        tier_slug="basic",
    ) # InlineObject4 |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update Subscription Tier
        api_response = api_instance.post_registry_subscription(inline_object4=inline_object4)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ContainerRegistryApi->post_registry_subscription: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inline_object4** | [**InlineObject4**](InlineObject4.md)|  | [optional]

### Return type

[**Subscription**](Subscription.md)

### Authorization

[bearer_auth](../README.md#bearer_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The response will be a JSON object with a key called &#x60;subscription&#x60; containing information about your subscription. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**401** | Unauthorized |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**429** | API Rate limit exceeded |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**500** | Server error. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**0** | Unexpected error |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **run_garbage_collection**
> InlineResponse2007 run_garbage_collection(registry_name)

Start Garbage Collection

Garbage collection enables users to clear out unreferenced blobs (layer & manifest data) after deleting one or more manifests from a repository. If there are no unreferenced blobs resulting from the deletion of one or more manifests, garbage collection is effectively a noop. [See here for more information](https://www.digitalocean.com/docs/container-registry/how-to/clean-up-container-registry/) about how and why you should clean up your container registry periodically.  To request a garbage collection run on your registry, send a POST request to `/v2/registry/$REGISTRY_NAME/garbage-collection`. This will initiate the following sequence of events on your registry.  * Set the registry to read-only mode, meaning no further write-scoped   JWTs will be issued to registry clients. Existing write-scoped JWTs will   continue to work until they expire which can take up to 15 minutes. * Wait until all existing write-scoped JWTs have expired. * Scan all registry manifests to determine which blobs are unreferenced. * Delete all unreferenced blobs from the registry. * Record the number of blobs deleted and bytes freed, mark the garbage   collection status as `success`. * Remove the read-only mode restriction from the registry, meaning write-scoped   JWTs will once again be issued to registry clients. 

### Example

* Bearer Authentication (bearer_auth):

```python
import time
import openapi_client
from openapi_client.api import container_registry_api
from openapi_client.model.error import Error
from openapi_client.model.inline_response2007 import InlineResponse2007
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
    api_instance = container_registry_api.ContainerRegistryApi(api_client)
    registry_name = "example" # str | The name of a container registry.

    # example passing only required values which don't have defaults set
    try:
        # Start Garbage Collection
        api_response = api_instance.run_garbage_collection(registry_name)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ContainerRegistryApi->run_garbage_collection: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **registry_name** | **str**| The name of a container registry. |

### Return type

[**InlineResponse2007**](InlineResponse2007.md)

### Authorization

[bearer_auth](../README.md#bearer_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The response will be a JSON object with a key of &#x60;garbage_collection&#x60;. This will be a json object with attributes representing the currently-active garbage collection. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**401** | Unauthorized |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**404** | The resource was not found. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**429** | API Rate limit exceeded |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**500** | Server error. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**0** | Unexpected error |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_garbage_collection**
> InlineResponse2007 update_garbage_collection(registry_name, garbage_collection_uuid, update_registry)

Update Garbage Collection

To cancel the currently-active garbage collection for a registry, send a PUT request to `/v2/registry/$REGISTRY_NAME/garbage-collection/$GC_UUID` and specify one or more of the attributes below.

### Example

* Bearer Authentication (bearer_auth):

```python
import time
import openapi_client
from openapi_client.api import container_registry_api
from openapi_client.model.update_registry import UpdateRegistry
from openapi_client.model.error import Error
from openapi_client.model.inline_response2007 import InlineResponse2007
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
    api_instance = container_registry_api.ContainerRegistryApi(api_client)
    registry_name = "example" # str | The name of a container registry.
    garbage_collection_uuid = "eff0feee-49c7-4e8f-ba5c-a320c109c8a8" # str | The UUID of a garbage collection run.
    update_registry = UpdateRegistry(
        cancel=True,
    ) # UpdateRegistry | 

    # example passing only required values which don't have defaults set
    try:
        # Update Garbage Collection
        api_response = api_instance.update_garbage_collection(registry_name, garbage_collection_uuid, update_registry)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ContainerRegistryApi->update_garbage_collection: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **registry_name** | **str**| The name of a container registry. |
 **garbage_collection_uuid** | **str**| The UUID of a garbage collection run. |
 **update_registry** | [**UpdateRegistry**](UpdateRegistry.md)|  |

### Return type

[**InlineResponse2007**](InlineResponse2007.md)

### Authorization

[bearer_auth](../README.md#bearer_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The response will be a JSON object with a key of &#x60;garbage_collection&#x60;. This will be a json object with attributes representing the currently-active garbage collection. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**401** | Unauthorized |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**404** | The resource was not found. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**429** | API Rate limit exceeded |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**500** | Server error. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**0** | Unexpected error |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **validate_registry_name**
> validate_registry_name(validate_registry)

Validate a Container Registry Name

To validate that a container registry name is available for use, send a POST request to `/v2/registry/validate-name`.  If the name is both formatted correctly and available, the response code will be 204 and contain no body. If the name is already in use, the response will be a 409 Conflict. 

### Example

* Bearer Authentication (bearer_auth):

```python
import time
import openapi_client
from openapi_client.api import container_registry_api
from openapi_client.model.error import Error
from openapi_client.model.validate_registry import ValidateRegistry
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
    api_instance = container_registry_api.ContainerRegistryApi(api_client)
    validate_registry = ValidateRegistry(
        name="example",
    ) # ValidateRegistry | 

    # example passing only required values which don't have defaults set
    try:
        # Validate a Container Registry Name
        api_instance.validate_registry_name(validate_registry)
    except openapi_client.ApiException as e:
        print("Exception when calling ContainerRegistryApi->validate_registry_name: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **validate_registry** | [**ValidateRegistry**](ValidateRegistry.md)|  |

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
**409** | Conflict |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**429** | API Rate limit exceeded |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**500** | Server error. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**0** | Unexpected error |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

