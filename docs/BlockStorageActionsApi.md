# digitalocean_client.BlockStorageActionsApi

All URIs are relative to *https://api.digitalocean.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_volume_action**](BlockStorageActionsApi.md#get_volume_action) | **GET** /v2/volumes/{volume_id}/actions/{action_id} | Retrieve an Existing Volume Action
[**list_all_volume_actions**](BlockStorageActionsApi.md#list_all_volume_actions) | **GET** /v2/volumes/{volume_id}/actions | List All Actions for a Volume
[**post_volume_action_by_id**](BlockStorageActionsApi.md#post_volume_action_by_id) | **POST** /v2/volumes/{volume_id}/actions | Initiate A Block Storage Action By Volume Id
[**post_volume_action_by_name**](BlockStorageActionsApi.md#post_volume_action_by_name) | **POST** /v2/volumes/actions | Initiate A Block Storage Action By Volume Name


# **get_volume_action**
> bool, date, datetime, dict, float, int, list, str, none_type get_volume_action(volume_id, action_id)

Retrieve an Existing Volume Action

To retrieve the status of a volume action, send a GET request to `/v2/volumes/$VOLUME_ID/actions/$ACTION_ID`.  

### Example

* Bearer Authentication (bearer_auth):

```python
import time
import digitalocean_client
from digitalocean_client.api import block_storage_actions_api
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
    api_instance = block_storage_actions_api.BlockStorageActionsApi(api_client)
    volume_id = "7724db7c-e098-11e5-b522-000f53304e51" # str | The ID of the block storage volume.
    action_id = 36804636 # int | A unique numeric ID that can be used to identify and reference an action.
    per_page = 2 # int | Number of items returned per page (optional) if omitted the server will use the default value of 20
    page = 1 # int | Which 'page' of paginated results to return. (optional) if omitted the server will use the default value of 1

    # example passing only required values which don't have defaults set
    try:
        # Retrieve an Existing Volume Action
        api_response = api_instance.get_volume_action(volume_id, action_id)
        pprint(api_response)
    except digitalocean_client.ApiException as e:
        print("Exception when calling BlockStorageActionsApi->get_volume_action: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Retrieve an Existing Volume Action
        api_response = api_instance.get_volume_action(volume_id, action_id, per_page=per_page, page=page)
        pprint(api_response)
    except digitalocean_client.ApiException as e:
        print("Exception when calling BlockStorageActionsApi->get_volume_action: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **volume_id** | **str**| The ID of the block storage volume. |
 **action_id** | **int**| A unique numeric ID that can be used to identify and reference an action. |
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
**200** | The response will be an object with a key called &#x60;action&#x60;. The value of this will be an object that contains the standard volume action attributes |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**401** | Unauthorized |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**404** | The resource was not found. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**429** | API Rate limit exceeded |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**500** | Server error. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**0** | Unexpected error |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_all_volume_actions**
> bool, date, datetime, dict, float, int, list, str, none_type list_all_volume_actions(volume_id)

List All Actions for a Volume

To retrieve all actions that have been executed on a volume, send a GET request to `/v2/volumes/$VOLUME_ID/actions`.  

### Example

* Bearer Authentication (bearer_auth):

```python
import time
import digitalocean_client
from digitalocean_client.api import block_storage_actions_api
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
    api_instance = block_storage_actions_api.BlockStorageActionsApi(api_client)
    volume_id = "7724db7c-e098-11e5-b522-000f53304e51" # str | The ID of the block storage volume.
    per_page = 2 # int | Number of items returned per page (optional) if omitted the server will use the default value of 20
    page = 1 # int | Which 'page' of paginated results to return. (optional) if omitted the server will use the default value of 1

    # example passing only required values which don't have defaults set
    try:
        # List All Actions for a Volume
        api_response = api_instance.list_all_volume_actions(volume_id)
        pprint(api_response)
    except digitalocean_client.ApiException as e:
        print("Exception when calling BlockStorageActionsApi->list_all_volume_actions: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List All Actions for a Volume
        api_response = api_instance.list_all_volume_actions(volume_id, per_page=per_page, page=page)
        pprint(api_response)
    except digitalocean_client.ApiException as e:
        print("Exception when calling BlockStorageActionsApi->list_all_volume_actions: %s\n" % e)
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
**200** | The response will be an object with a key called &#x60;action&#x60;. The value of this will be an object that contains the standard volume action attributes. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**401** | Unauthorized |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**404** | The resource was not found. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**429** | API Rate limit exceeded |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**500** | Server error. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**0** | Unexpected error |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_volume_action_by_id**
> bool, date, datetime, dict, float, int, list, str, none_type post_volume_action_by_id(volume_id, unknown_base_type)

Initiate A Block Storage Action By Volume Id

To initiate an action on a block storage volume by Id, send a POST request to `~/v2/volumes/$VOLUME_ID/actions`. The body should contain the appropriate attributes for the respective action.  ## Attach a Block Storage Volume to a Droplet  | Attribute  | Details                                                             | | ---------- | ------------------------------------------------------------------- | | type       | This must be `attach`                                               | | droplet_id | Set to the Droplet's ID                                             | | region     | Set to the slug representing the region where the volume is located |  Each volume may only be attached to a single Droplet. However, up to five volumes may be attached to a Droplet at a time. Pre-formatted volumes will be automatically mounted to Ubuntu, Debian, Fedora, Fedora Atomic, and CentOS Droplets created on or after April 26, 2018 when attached. On older Droplets, [additional configuration](https://www.digitalocean.com/community/tutorials/how-to-partition-and-format-digitalocean-block-storage-volumes-in-linux#mounting-the-filesystems) is required.  ## Remove a Block Storage Volume from a Droplet  | Attribute  | Details                                                             | | ---------- | ------------------------------------------------------------------- | | type       | This must be `detach`                                               | | droplet_id | Set to the Droplet's ID                                             | | region     | Set to the slug representing the region where the volume is located |  ## Resize a Volume  | Attribute      | Details                                                             | | -------------- | ------------------------------------------------------------------- | | type           | This must be `resize`                                               | | size_gigabytes | The new size of the block storage volume in GiB (1024^3)            | | region         | Set to the slug representing the region where the volume is located |  Volumes may only be resized upwards. The maximum size for a volume is 16TiB. 

### Example

* Bearer Authentication (bearer_auth):

```python
import time
import digitalocean_client
from digitalocean_client.api import block_storage_actions_api
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
    api_instance = block_storage_actions_api.BlockStorageActionsApi(api_client)
    volume_id = "7724db7c-e098-11e5-b522-000f53304e51" # str | The ID of the block storage volume.
    unknown_base_type = None # UNKNOWN_BASE_TYPE | 
    per_page = 2 # int | Number of items returned per page (optional) if omitted the server will use the default value of 20
    page = 1 # int | Which 'page' of paginated results to return. (optional) if omitted the server will use the default value of 1

    # example passing only required values which don't have defaults set
    try:
        # Initiate A Block Storage Action By Volume Id
        api_response = api_instance.post_volume_action_by_id(volume_id, unknown_base_type)
        pprint(api_response)
    except digitalocean_client.ApiException as e:
        print("Exception when calling BlockStorageActionsApi->post_volume_action_by_id: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Initiate A Block Storage Action By Volume Id
        api_response = api_instance.post_volume_action_by_id(volume_id, unknown_base_type, per_page=per_page, page=page)
        pprint(api_response)
    except digitalocean_client.ApiException as e:
        print("Exception when calling BlockStorageActionsApi->post_volume_action_by_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **volume_id** | **str**| The ID of the block storage volume. |
 **unknown_base_type** | [**UNKNOWN_BASE_TYPE**](UNKNOWN_BASE_TYPE.md)|  |
 **per_page** | **int**| Number of items returned per page | [optional] if omitted the server will use the default value of 20
 **page** | **int**| Which &#39;page&#39; of paginated results to return. | [optional] if omitted the server will use the default value of 1

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
**202** | The response will be an object with a key called &#x60;action&#x60;. The value of this will be an object that contains the standard volume action attributes |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**401** | Unauthorized |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**404** | The resource was not found. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**429** | API Rate limit exceeded |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**500** | Server error. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**0** | Unexpected error |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_volume_action_by_name**
> bool, date, datetime, dict, float, int, list, str, none_type post_volume_action_by_name(unknown_base_type)

Initiate A Block Storage Action By Volume Name

To initiate an action on a block storage volume by Id, send a POST request to `~/v2/volumes/actions`. The body should contain the appropriate attributes for the respective action.  ## Attach a Block Storage Volume to a Droplet  | Attribute   | Details                                                             | | ----------- | ------------------------------------------------------------------- | | type        | This must be `attach`                                               | | volume_name | The name of the block storage volume                                | | droplet_id  | Set to the Droplet's ID                                             | | region      | Set to the slug representing the region where the volume is located |  Each volume may only be attached to a single Droplet. However, up to five volumes may be attached to a Droplet at a time. Pre-formatted volumes will be automatically mounted to Ubuntu, Debian, Fedora, Fedora Atomic, and CentOS Droplets created on or after April 26, 2018 when attached. On older Droplets, [additional configuration](https://www.digitalocean.com/community/tutorials/how-to-partition-and-format-digitalocean-block-storage-volumes-in-linux#mounting-the-filesystems) is required.  ## Remove a Block Storage Volume from a Droplet  | Attribute   | Details                                                             | | ----------- | ------------------------------------------------------------------- | | type        | This must be `detach`                                               | | volume_name | The name of the block storage volume                                | | droplet_id  | Set to the Droplet's ID                                             | | region      | Set to the slug representing the region where the volume is located | 

### Example

* Bearer Authentication (bearer_auth):

```python
import time
import digitalocean_client
from digitalocean_client.api import block_storage_actions_api
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
    api_instance = block_storage_actions_api.BlockStorageActionsApi(api_client)
    unknown_base_type = None # UNKNOWN_BASE_TYPE | 
    per_page = 2 # int | Number of items returned per page (optional) if omitted the server will use the default value of 20
    page = 1 # int | Which 'page' of paginated results to return. (optional) if omitted the server will use the default value of 1

    # example passing only required values which don't have defaults set
    try:
        # Initiate A Block Storage Action By Volume Name
        api_response = api_instance.post_volume_action_by_name(unknown_base_type)
        pprint(api_response)
    except digitalocean_client.ApiException as e:
        print("Exception when calling BlockStorageActionsApi->post_volume_action_by_name: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Initiate A Block Storage Action By Volume Name
        api_response = api_instance.post_volume_action_by_name(unknown_base_type, per_page=per_page, page=page)
        pprint(api_response)
    except digitalocean_client.ApiException as e:
        print("Exception when calling BlockStorageActionsApi->post_volume_action_by_name: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **unknown_base_type** | [**UNKNOWN_BASE_TYPE**](UNKNOWN_BASE_TYPE.md)|  |
 **per_page** | **int**| Number of items returned per page | [optional] if omitted the server will use the default value of 20
 **page** | **int**| Which &#39;page&#39; of paginated results to return. | [optional] if omitted the server will use the default value of 1

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
**202** | The response will be an object with a key called &#x60;action&#x60;. The value of this will be an object that contains the standard volume action attributes |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**401** | Unauthorized |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**404** | The resource was not found. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**429** | API Rate limit exceeded |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**500** | Server error. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**0** | Unexpected error |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

