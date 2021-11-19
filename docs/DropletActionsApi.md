# openapi_client.DropletActionsApi

All URIs are relative to *https://api.digitalocean.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_droplet_action**](DropletActionsApi.md#get_droplet_action) | **GET** /v2/droplets/{droplet_id}/actions/{action_id} | Retrieve a Droplet Action
[**list_droplet_actions**](DropletActionsApi.md#list_droplet_actions) | **GET** /v2/droplets/{droplet_id}/actions | List Actions for a Droplet
[**post_droplet_action**](DropletActionsApi.md#post_droplet_action) | **POST** /v2/droplets/{droplet_id}/actions | Initiate a Droplet Action
[**post_droplet_action_by_tag**](DropletActionsApi.md#post_droplet_action_by_tag) | **POST** /v2/droplets/actions | Acting on Tagged Droplets


# **get_droplet_action**
> bool, date, datetime, dict, float, int, list, str, none_type get_droplet_action(droplet_id, action_id)

Retrieve a Droplet Action

To retrieve a Droplet action, send a GET request to `/v2/droplets/$DROPLET_ID/actions/$ACTION_ID`.  The response will be a JSON object with a key called `action`. The value will be a Droplet action object. 

### Example

* Bearer Authentication (bearer_auth):

```python
import time
import openapi_client
from openapi_client.api import droplet_actions_api
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
    api_instance = droplet_actions_api.DropletActionsApi(api_client)
    droplet_id = 3164444 # int | A unique identifier for a Droplet instance.
    action_id = 36804636 # int | A unique numeric ID that can be used to identify and reference an action.

    # example passing only required values which don't have defaults set
    try:
        # Retrieve a Droplet Action
        api_response = api_instance.get_droplet_action(droplet_id, action_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DropletActionsApi->get_droplet_action: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **droplet_id** | **int**| A unique identifier for a Droplet instance. |
 **action_id** | **int**| A unique numeric ID that can be used to identify and reference an action. |

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
**200** | The result will be a JSON object with an action key.  This will be set to an action object containing the standard action attributes. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**401** | Unauthorized |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**404** | The resource was not found. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**429** | API Rate limit exceeded |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**500** | Server error. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**0** | Unexpected error |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_droplet_actions**
> bool, date, datetime, dict, float, int, list, str, none_type list_droplet_actions(droplet_id)

List Actions for a Droplet

To retrieve a list of all actions that have been executed for a Droplet, send a GET request to `/v2/droplets/$DROPLET_ID/actions`.  The results will be returned as a JSON object with an `actions` key. This will be set to an array filled with `action` objects containing the standard `action` attributes. 

### Example

* Bearer Authentication (bearer_auth):

```python
import time
import openapi_client
from openapi_client.api import droplet_actions_api
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
    api_instance = droplet_actions_api.DropletActionsApi(api_client)
    droplet_id = 3164444 # int | A unique identifier for a Droplet instance.
    per_page = 2 # int | Number of items returned per page (optional) if omitted the server will use the default value of 20
    page = 1 # int | Which 'page' of paginated results to return. (optional) if omitted the server will use the default value of 1

    # example passing only required values which don't have defaults set
    try:
        # List Actions for a Droplet
        api_response = api_instance.list_droplet_actions(droplet_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DropletActionsApi->list_droplet_actions: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List Actions for a Droplet
        api_response = api_instance.list_droplet_actions(droplet_id, per_page=per_page, page=page)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DropletActionsApi->list_droplet_actions: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **droplet_id** | **int**| A unique identifier for a Droplet instance. |
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
**200** | A JSON object with an &#x60;actions&#x60; key. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**401** | Unauthorized |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**404** | The resource was not found. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**429** | API Rate limit exceeded |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**500** | Server error. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**0** | Unexpected error |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_droplet_action**
> bool, date, datetime, dict, float, int, list, str, none_type post_droplet_action(droplet_id)

Initiate a Droplet Action

To initiate an action on a Droplet send a POST request to `/v2/droplets/$DROPLET_ID/actions`. In the JSON body to the request, set the `type` attribute to on of the supported action types:  | Action                                   | Details | | ---------------------------------------- | ----------- | | <nobr>`enable_backups`</nobr>            | Enables backups for a Droplet | | <nobr>`disable_backups`</nobr>           | Disables backups for a Droplet | | <nobr>`reboot`</nobr>                    | Reboots a Droplet. A `reboot` action is an attempt to reboot the Droplet in a graceful way, similar to using the `reboot` command from the console. | | <nobr>`power_cycle`</nobr>               | Power cycles a Droplet. A `powercycle` action is similar to pushing the reset button on a physical machine, it's similar to booting from scratch. | | <nobr>`shutdown`</nobr>                  | Shutsdown a Droplet. A shutdown action is an attempt to shutdown the Droplet in a graceful way, similar to using the `shutdown` command from the console. Since a `shutdown` command can fail, this action guarantees that the command is issued, not that it succeeds. The preferred way to turn off a Droplet is to attempt a shutdown, with a reasonable timeout, followed by a `power_off` action to ensure the Droplet is off. | | <nobr>`power_off`</nobr>                 | Powers off a Droplet. A `power_off` event is a hard shutdown and should only be used if the `shutdown` action is not successful. It is similar to cutting the power on a server and could lead to complications. | | <nobr>`power_on`</nobr>                  | Powers on a Droplet. | | <nobr>`restore`</nobr>                   | Restore a Droplet using a backup image. The image ID that is passed in must be a backup of the current Droplet instance. The operation will leave any embedded SSH keys intact. | | <nobr>`password_reset`</nobr>            | Resets the root password for a Droplet. A new password will be provided via email. It must be changed after first use. | | <nobr>`resize`</nobr>                    | Resizes a Droplet. Set the `size` attribute to a size slug. If a permanent resize with disk changes included is desired, set the `disk` attribute to `true`. | | <nobr>`rebuild`</nobr>                   | Rebuilds a Droplet from a new base image. Set the `image` attribute to an image ID or slug. | | <nobr>`rename`</nobr>                    | Renames a Droplet. | | <nobr>`change_kernel`</nobr>             | Changes a Droplet's kernel. Only applies to Droplets with externally managed kernels. All Droplets created after March 2017 use internal kernels by default. | | <nobr>`enable_ipv6`</nobr>               | Enables IPv6 for a Droplet. | | <nobr>`snapshot`</nobr>                  | Takes a snapshot of a Droplet. | 

### Example

* Bearer Authentication (bearer_auth):

```python
import time
import openapi_client
from openapi_client.api import droplet_actions_api
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
    api_instance = droplet_actions_api.DropletActionsApi(api_client)
    droplet_id = 3164444 # int | A unique identifier for a Droplet instance.
    unknown_base_type = None # UNKNOWN_BASE_TYPE | The `type` attribute set in the request body will specify the  action that will be taken on the Droplet. Some actions will require additional attributes to be set as well.  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Initiate a Droplet Action
        api_response = api_instance.post_droplet_action(droplet_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DropletActionsApi->post_droplet_action: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Initiate a Droplet Action
        api_response = api_instance.post_droplet_action(droplet_id, unknown_base_type=unknown_base_type)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DropletActionsApi->post_droplet_action: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **droplet_id** | **int**| A unique identifier for a Droplet instance. |
 **unknown_base_type** | [**UNKNOWN_BASE_TYPE**](UNKNOWN_BASE_TYPE.md)| The &#x60;type&#x60; attribute set in the request body will specify the  action that will be taken on the Droplet. Some actions will require additional attributes to be set as well.  | [optional]

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
**201** | The response will be a JSON object with a key called &#x60;action&#x60;. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**401** | Unauthorized |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**404** | The resource was not found. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**429** | API Rate limit exceeded |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**500** | Server error. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**0** | Unexpected error |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_droplet_action_by_tag**
> bool, date, datetime, dict, float, int, list, str, none_type post_droplet_action_by_tag()

Acting on Tagged Droplets

Some actions can be performed in bulk on tagged Droplets. The actions can be initiated by sending a POST to `/v2/droplets/actions?tag_name=$TAG_NAME` with the action arguments.  Only a sub-set of action types are supported:  - `power_cycle` - `power_on` - `power_off` - `shutdown` - `enable_ipv6` - `enable_backups` - `disable_backups` - `snapshot` 

### Example

* Bearer Authentication (bearer_auth):

```python
import time
import openapi_client
from openapi_client.api import droplet_actions_api
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
    api_instance = droplet_actions_api.DropletActionsApi(api_client)
    tag_name = "env:prod" # str | Used to filter Droplets by a specific tag. (optional)
    unknown_base_type = None # UNKNOWN_BASE_TYPE | The `type` attribute set in the request body will specify the  action that will be taken on the Droplet. Some actions will require additional attributes to be set as well.  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Acting on Tagged Droplets
        api_response = api_instance.post_droplet_action_by_tag(tag_name=tag_name, unknown_base_type=unknown_base_type)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DropletActionsApi->post_droplet_action_by_tag: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tag_name** | **str**| Used to filter Droplets by a specific tag. | [optional]
 **unknown_base_type** | [**UNKNOWN_BASE_TYPE**](UNKNOWN_BASE_TYPE.md)| The &#x60;type&#x60; attribute set in the request body will specify the  action that will be taken on the Droplet. Some actions will require additional attributes to be set as well.  | [optional]

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
**201** | The response will be a JSON object with a key called &#x60;actions&#x60;. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**401** | Unauthorized |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**429** | API Rate limit exceeded |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**500** | Server error. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**0** | Unexpected error |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

