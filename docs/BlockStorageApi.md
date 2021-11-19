# openapi_client.BlockStorageApi

All URIs are relative to *https://api.digitalocean.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_new_volume**](BlockStorageApi.md#create_new_volume) | **POST** /v2/volumes | Create a New Block Storage Volume
[**create_volume_snapshot**](BlockStorageApi.md#create_volume_snapshot) | **POST** /v2/volumes/{volume_id}/snapshots | Create Snapshot from a Volume
[**delete_volume**](BlockStorageApi.md#delete_volume) | **DELETE** /v2/volumes/{volume_id} | Delete a Block Storage Volume
[**delete_volume_by_name**](BlockStorageApi.md#delete_volume_by_name) | **DELETE** /v2/volumes | Delete a Block Storage Volume by Name
[**delete_volume_snapshot_by_id**](BlockStorageApi.md#delete_volume_snapshot_by_id) | **DELETE** /v2/volumes/snapshot/{snapshot_id} | Delete a Volume Snapshot
[**get_volume**](BlockStorageApi.md#get_volume) | **GET** /v2/volumes/{volume_id} | Retrieve an Existing Block Storage Volume
[**get_volume_snapshot_by_id**](BlockStorageApi.md#get_volume_snapshot_by_id) | **GET** /v2/volumes/snapshot/{snapshot_id} | Retreive an Existing Volume Snapshot
[**list_all_volumes**](BlockStorageApi.md#list_all_volumes) | **GET** /v2/volumes | List All Block Storage Volumes
[**list_volume_snapshots**](BlockStorageApi.md#list_volume_snapshots) | **GET** /v2/volumes/{volume_id}/snapshots | List Snapshots for a Volume


# **create_new_volume**
> bool, date, datetime, dict, float, int, list, str, none_type create_new_volume(unknown_base_type)

Create a New Block Storage Volume

To create a new volume, send a POST request to `/v2/volumes`. Optionally, a `filesystem_type` attribute may be provided in order to automatically format the volume's filesystem. Pre-formatted volumes are automatically mounted when attached to Ubuntu, Debian, Fedora, Fedora Atomic, and CentOS Droplets created on or after April 26, 2018. Attaching pre-formatted volumes to Droplets without support for auto-mounting is not recommended.

### Example

* Bearer Authentication (bearer_auth):

```python
import time
import openapi_client
from openapi_client.api import block_storage_api
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
    api_instance = block_storage_api.BlockStorageApi(api_client)
    unknown_base_type = None # UNKNOWN_BASE_TYPE | 

    # example passing only required values which don't have defaults set
    try:
        # Create a New Block Storage Volume
        api_response = api_instance.create_new_volume(unknown_base_type)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling BlockStorageApi->create_new_volume: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **unknown_base_type** | [**UNKNOWN_BASE_TYPE**](UNKNOWN_BASE_TYPE.md)|  |

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
**201** | The response will be a JSON object with a key called &#x60;volume&#x60;. The value will be an object containing the standard attributes associated with a volume. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**400** | Bad Request |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**401** | Unauthorized |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**404** | The resource was not found. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**429** | API Rate limit exceeded |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**500** | Server error. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**0** | Unexpected error |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_volume_snapshot**
> bool, date, datetime, dict, float, int, list, str, none_type create_volume_snapshot(volume_id, unknown_base_type)

Create Snapshot from a Volume

To create a snapshot from a volume, sent a POST request to `/v2/volumes/$VOLUME_ID/snapshots`.

### Example

* Bearer Authentication (bearer_auth):

```python
import time
import openapi_client
from openapi_client.api import block_storage_api
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
    api_instance = block_storage_api.BlockStorageApi(api_client)
    volume_id = "7724db7c-e098-11e5-b522-000f53304e51" # str | The ID of the block storage volume.
    unknown_base_type = None # UNKNOWN_BASE_TYPE | 

    # example passing only required values which don't have defaults set
    try:
        # Create Snapshot from a Volume
        api_response = api_instance.create_volume_snapshot(volume_id, unknown_base_type)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling BlockStorageApi->create_volume_snapshot: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **volume_id** | **str**| The ID of the block storage volume. |
 **unknown_base_type** | [**UNKNOWN_BASE_TYPE**](UNKNOWN_BASE_TYPE.md)|  |

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
**201** | You will get back a JSON object that has a &#x60;snapshot&#x60; key. This will contain the standard snapshot attributes |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**400** | Bad Request |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**401** | Unauthorized |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**404** | The resource was not found. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**429** | API Rate limit exceeded |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**500** | Server error. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**0** | Unexpected error |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_volume**
> delete_volume(volume_id)

Delete a Block Storage Volume

To delete a block storage volume, destroying all data and removing it from your account, send a DELETE request to `/v2/volumes/$VOLUME_ID`. No response body will be sent back, but the response code will indicate success. Specifically, the response code will be a 204, which means that the action was successful with no returned body data.  

### Example

* Bearer Authentication (bearer_auth):

```python
import time
import openapi_client
from openapi_client.api import block_storage_api
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
    api_instance = block_storage_api.BlockStorageApi(api_client)
    volume_id = "7724db7c-e098-11e5-b522-000f53304e51" # str | The ID of the block storage volume.

    # example passing only required values which don't have defaults set
    try:
        # Delete a Block Storage Volume
        api_instance.delete_volume(volume_id)
    except openapi_client.ApiException as e:
        print("Exception when calling BlockStorageApi->delete_volume: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **volume_id** | **str**| The ID of the block storage volume. |

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

# **delete_volume_by_name**
> delete_volume_by_name()

Delete a Block Storage Volume by Name

Block storage volumes may also be deleted by name by sending a DELETE request with the volume's **name** and the **region slug** for the region it is located in as query parameters to `/v2/volumes?name=$VOLUME_NAME&region=nyc1`. No response body will be sent back, but the response code will indicate success. Specifically, the response code will be a 204, which means that the action was successful with no returned body data.  

### Example

* Bearer Authentication (bearer_auth):

```python
import time
import openapi_client
from openapi_client.api import block_storage_api
from openapi_client.model.error import Error
from openapi_client.model.region_slug import RegionSlug
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
    api_instance = block_storage_api.BlockStorageApi(api_client)
    name = "example" # str | The block storage volume's name. (optional)
    region = RegionSlug("nyc3") # RegionSlug | The slug identifier for the region where the resource is available. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Delete a Block Storage Volume by Name
        api_instance.delete_volume_by_name(name=name, region=region)
    except openapi_client.ApiException as e:
        print("Exception when calling BlockStorageApi->delete_volume_by_name: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The block storage volume&#39;s name. | [optional]
 **region** | **RegionSlug**| The slug identifier for the region where the resource is available. | [optional]

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

# **delete_volume_snapshot_by_id**
> delete_volume_snapshot_by_id(snapshot_id)

Delete a Volume Snapshot

To delete a volume snapshot, send a DELETE request to `/v2/snapshots/$SNAPSHOT_ID`.  A status of 204 will be given. This indicates that the request was processed successfully, but that no response body is needed. 

### Example

* Bearer Authentication (bearer_auth):

```python
import time
import openapi_client
from openapi_client.api import block_storage_api
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
    api_instance = block_storage_api.BlockStorageApi(api_client)
    snapshot_id = None # bool, date, datetime, dict, float, int, list, str, none_type | Either the ID of an existing snapshot. This will be an integer for a Droplet snapshot or a string for a volume snapshot.

    # example passing only required values which don't have defaults set
    try:
        # Delete a Volume Snapshot
        api_instance.delete_volume_snapshot_by_id(snapshot_id)
    except openapi_client.ApiException as e:
        print("Exception when calling BlockStorageApi->delete_volume_snapshot_by_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **snapshot_id** | **bool, date, datetime, dict, float, int, list, str, none_type**| Either the ID of an existing snapshot. This will be an integer for a Droplet snapshot or a string for a volume snapshot. |

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

# **get_volume**
> bool, date, datetime, dict, float, int, list, str, none_type get_volume(volume_id)

Retrieve an Existing Block Storage Volume

To show information about a block storage volume, send a GET request to `/v2/volumes/$VOLUME_ID`.  

### Example

* Bearer Authentication (bearer_auth):

```python
import time
import openapi_client
from openapi_client.api import block_storage_api
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
    api_instance = block_storage_api.BlockStorageApi(api_client)
    volume_id = "7724db7c-e098-11e5-b522-000f53304e51" # str | The ID of the block storage volume.

    # example passing only required values which don't have defaults set
    try:
        # Retrieve an Existing Block Storage Volume
        api_response = api_instance.get_volume(volume_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling BlockStorageApi->get_volume: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **volume_id** | **str**| The ID of the block storage volume. |

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
**200** | The response will be a JSON object with a key called &#x60;volume&#x60;. The value will be an object containing the standard attributes associated with a volume. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**401** | Unauthorized |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**404** | The resource was not found. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**429** | API Rate limit exceeded |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**500** | Server error. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**0** | Unexpected error |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_volume_snapshot_by_id**
> bool, date, datetime, dict, float, int, list, str, none_type get_volume_snapshot_by_id(snapshot_id)

Retreive an Existing Volume Snapshot

To retrieve the details of a snapshot that has been created from a volume, send a GET request to `/v2/volumes/snapshots/$SNAPSHOT_ID`.  

### Example

* Bearer Authentication (bearer_auth):

```python
import time
import openapi_client
from openapi_client.api import block_storage_api
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
    api_instance = block_storage_api.BlockStorageApi(api_client)
    snapshot_id = None # bool, date, datetime, dict, float, int, list, str, none_type | Either the ID of an existing snapshot. This will be an integer for a Droplet snapshot or a string for a volume snapshot.

    # example passing only required values which don't have defaults set
    try:
        # Retreive an Existing Volume Snapshot
        api_response = api_instance.get_volume_snapshot_by_id(snapshot_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling BlockStorageApi->get_volume_snapshot_by_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **snapshot_id** | **bool, date, datetime, dict, float, int, list, str, none_type**| Either the ID of an existing snapshot. This will be an integer for a Droplet snapshot or a string for a volume snapshot. |

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
**200** | You will get back a JSON object that has a &#x60;snapshot&#x60; key. This will contain the standard snapshot attributes |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**401** | Unauthorized |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**404** | The resource was not found. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**429** | API Rate limit exceeded |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**500** | Server error. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**0** | Unexpected error |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_all_volumes**
> bool, date, datetime, dict, float, int, list, str, none_type list_all_volumes()

List All Block Storage Volumes

To list all of the block storage volumes available on your account, send a GET request to `/v2/volumes`. ## Filtering Results ### By Region The `region` may be provided as query paramater in order to restrict results to volumes available in a specific region. For example: `/v2/volumes?region=nyc1` ### By Name It is also possible to list volumes on your account that match a specified name. To do so, send a GET request with the volume's name as a query parameter to `/v2/volumes?name=$VOLUME_NAME`. **Note:** You can only create one volume per region with the same name. ### By Name and Region It is also possible to retrieve information about a block storage volume by name. To do so, send a GET request with the volume's name and the region slug for the region it is located in as query parameters to `/v2/volumes?name=$VOLUME_NAME&region=nyc1`.   

### Example

* Bearer Authentication (bearer_auth):

```python
import time
import openapi_client
from openapi_client.api import block_storage_api
from openapi_client.model.error import Error
from openapi_client.model.region_slug import RegionSlug
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
    api_instance = block_storage_api.BlockStorageApi(api_client)
    name = "example" # str | The block storage volume's name. (optional)
    region = RegionSlug("nyc3") # RegionSlug | The slug identifier for the region where the resource is available. (optional)
    per_page = 2 # int | Number of items returned per page (optional) if omitted the server will use the default value of 20
    page = 1 # int | Which 'page' of paginated results to return. (optional) if omitted the server will use the default value of 1

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List All Block Storage Volumes
        api_response = api_instance.list_all_volumes(name=name, region=region, per_page=per_page, page=page)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling BlockStorageApi->list_all_volumes: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The block storage volume&#39;s name. | [optional]
 **region** | **RegionSlug**| The slug identifier for the region where the resource is available. | [optional]
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
**200** | The response will be a JSON object with a key called &#x60;volumes&#x60;. This will be set to an array of volume objects, each of which will contain the standard volume attributes. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**401** | Unauthorized |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**429** | API Rate limit exceeded |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**500** | Server error. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**0** | Unexpected error |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_volume_snapshots**
> bool, date, datetime, dict, float, int, list, str, none_type list_volume_snapshots(volume_id)

List Snapshots for a Volume

To retrieve the snapshots that have been created from a volume, send a GET request to `/v2/volumes/$VOLUME_ID/snapshots`.  

### Example

* Bearer Authentication (bearer_auth):

```python
import time
import openapi_client
from openapi_client.api import block_storage_api
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
    api_instance = block_storage_api.BlockStorageApi(api_client)
    volume_id = "7724db7c-e098-11e5-b522-000f53304e51" # str | The ID of the block storage volume.
    per_page = 2 # int | Number of items returned per page (optional) if omitted the server will use the default value of 20
    page = 1 # int | Which 'page' of paginated results to return. (optional) if omitted the server will use the default value of 1

    # example passing only required values which don't have defaults set
    try:
        # List Snapshots for a Volume
        api_response = api_instance.list_volume_snapshots(volume_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling BlockStorageApi->list_volume_snapshots: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List Snapshots for a Volume
        api_response = api_instance.list_volume_snapshots(volume_id, per_page=per_page, page=page)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling BlockStorageApi->list_volume_snapshots: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **volume_id** | **str**| The ID of the block storage volume. |
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
**200** | You will get back a JSON object that has a &#x60;snapshots&#x60; key. This will be set to an array of snapshot objects, each of which contain the standard snapshot attributes |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**401** | Unauthorized |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**404** | The resource was not found. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**429** | API Rate limit exceeded |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**500** | Server error. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**0** | Unexpected error |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

