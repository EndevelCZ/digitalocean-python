# openapi_client.SnapshotsApi

All URIs are relative to *https://api.digitalocean.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_snapshot**](SnapshotsApi.md#delete_snapshot) | **DELETE** /v2/snapshots/{snapshot_id} | Delete a Snapshot
[**get_snapshot**](SnapshotsApi.md#get_snapshot) | **GET** /v2/snapshots/{snapshot_id} | Retrieve an Existing Snapshot
[**list_all_snapshots**](SnapshotsApi.md#list_all_snapshots) | **GET** /v2/snapshots | List All Snapshots


# **delete_snapshot**
> delete_snapshot(snapshot_id)

Delete a Snapshot

Both Droplet and volume snapshots are managed through the `/v2/snapshots/` endpoint. To delete a snapshot, send a DELETE request to `/v2/snapshots/$SNAPSHOT_ID`.  A status of 204 will be given. This indicates that the request was processed successfully, but that no response body is needed. 

### Example

* Bearer Authentication (bearer_auth):

```python
import time
import openapi_client
from openapi_client.api import snapshots_api
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
    api_instance = snapshots_api.SnapshotsApi(api_client)
    snapshot_id = None # bool, date, datetime, dict, float, int, list, str, none_type | Either the ID of an existing snapshot. This will be an integer for a Droplet snapshot or a string for a volume snapshot.

    # example passing only required values which don't have defaults set
    try:
        # Delete a Snapshot
        api_instance.delete_snapshot(snapshot_id)
    except openapi_client.ApiException as e:
        print("Exception when calling SnapshotsApi->delete_snapshot: %s\n" % e)
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

# **get_snapshot**
> bool, date, datetime, dict, float, int, list, str, none_type get_snapshot(snapshot_id)

Retrieve an Existing Snapshot

To retrieve information about a snapshot, send a GET request to `/v2/snapshots/$SNAPSHOT_ID`.  The response will be a JSON object with a key called `snapshot`. The value of this will be an snapshot object containing the standard snapshot attributes. 

### Example

* Bearer Authentication (bearer_auth):

```python
import time
import openapi_client
from openapi_client.api import snapshots_api
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
    api_instance = snapshots_api.SnapshotsApi(api_client)
    snapshot_id = None # bool, date, datetime, dict, float, int, list, str, none_type | Either the ID of an existing snapshot. This will be an integer for a Droplet snapshot or a string for a volume snapshot.

    # example passing only required values which don't have defaults set
    try:
        # Retrieve an Existing Snapshot
        api_response = api_instance.get_snapshot(snapshot_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling SnapshotsApi->get_snapshot: %s\n" % e)
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
**200** | A JSON object with a key called &#x60;snapshot&#x60;.  |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**401** | Unauthorized |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**404** | The resource was not found. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**429** | API Rate limit exceeded |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**500** | Server error. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**0** | Unexpected error |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_all_snapshots**
> bool, date, datetime, dict, float, int, list, str, none_type list_all_snapshots()

List All Snapshots

To list all of the snapshots available on your account, send a GET request to `/v2/snapshots`.  The response will be a JSON object with a key called `snapshots`. This will be set to an array of `snapshot` objects, each of which will contain the standard snapshot attributes.  ### Filtering Results by Resource Type  It's possible to request filtered results by including certain query parameters.  #### List Droplet Snapshots  To retrieve only snapshots based on Droplets, include the `resource_type` query parameter set to `droplet`. For example, `/v2/snapshots?resource_type=droplet`.  #### List Volume Snapshots  To retrieve only snapshots based on volumes, include the `resource_type` query parameter set to `volume`. For example, `/v2/snapshots?resource_type=volume`. 

### Example

* Bearer Authentication (bearer_auth):

```python
import time
import openapi_client
from openapi_client.api import snapshots_api
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
    api_instance = snapshots_api.SnapshotsApi(api_client)
    per_page = 2 # int | Number of items returned per page (optional) if omitted the server will use the default value of 20
    page = 1 # int | Which 'page' of paginated results to return. (optional) if omitted the server will use the default value of 1
    resource_type = "droplet" # str | Used to filter snapshots by a resource type. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List All Snapshots
        api_response = api_instance.list_all_snapshots(per_page=per_page, page=page, resource_type=resource_type)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling SnapshotsApi->list_all_snapshots: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **per_page** | **int**| Number of items returned per page | [optional] if omitted the server will use the default value of 20
 **page** | **int**| Which &#39;page&#39; of paginated results to return. | [optional] if omitted the server will use the default value of 1
 **resource_type** | **str**| Used to filter snapshots by a resource type. | [optional]

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
**200** | A JSON object with a key of &#x60;snapshots&#x60;. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**401** | Unauthorized |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**429** | API Rate limit exceeded |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**500** | Server error. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**0** | Unexpected error |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

