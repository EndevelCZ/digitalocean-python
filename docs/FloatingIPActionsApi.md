# digitalocean_client.FloatingIPActionsApi

All URIs are relative to *https://api.digitalocean.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_floating_ip_action**](FloatingIPActionsApi.md#get_floating_ip_action) | **GET** /v2/floating_ips/{floating_ip}/actions/{action_id} | Retrieve an Existing Floating IP Action
[**list_floating_ip_actions**](FloatingIPActionsApi.md#list_floating_ip_actions) | **GET** /v2/floating_ips/{floating_ip}/actions | List All Actions for a Floating IP
[**post_floating_ip_action**](FloatingIPActionsApi.md#post_floating_ip_action) | **POST** /v2/floating_ips/{floating_ip}/actions | Initiate a Floating IP Action


# **get_floating_ip_action**
> bool, date, datetime, dict, float, int, list, str, none_type get_floating_ip_action(floating_ip, action_id)

Retrieve an Existing Floating IP Action

To retrieve the status of a floating IP action, send a GET request to `/v2/floating_ips/$FLOATING_IP/actions/$ACTION_ID`.

### Example

* Bearer Authentication (bearer_auth):

```python
import time
import digitalocean_client
from digitalocean_client.api import floating_ip_actions_api
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
    api_instance = floating_ip_actions_api.FloatingIPActionsApi(api_client)
    floating_ip = "45.55.96.47" # str | A floating IP address.
    action_id = 36804636 # int | A unique numeric ID that can be used to identify and reference an action.

    # example passing only required values which don't have defaults set
    try:
        # Retrieve an Existing Floating IP Action
        api_response = api_instance.get_floating_ip_action(floating_ip, action_id)
        pprint(api_response)
    except digitalocean_client.ApiException as e:
        print("Exception when calling FloatingIPActionsApi->get_floating_ip_action: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **floating_ip** | **str**| A floating IP address. |
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
**200** | The response will be an object with a key called &#x60;action&#x60;. The value of this will be an object that contains the standard floating IP action attributes. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**401** | Unauthorized |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**404** | The resource was not found. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**429** | API Rate limit exceeded |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**500** | Server error. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**0** | Unexpected error |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_floating_ip_actions**
> bool, date, datetime, dict, float, int, list, str, none_type list_floating_ip_actions(floating_ip)

List All Actions for a Floating IP

To retrieve all actions that have been executed on a floating IP, send a GET request to `/v2/floating_ips/$FLOATING_IP/actions`.

### Example

* Bearer Authentication (bearer_auth):

```python
import time
import digitalocean_client
from digitalocean_client.api import floating_ip_actions_api
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
    api_instance = floating_ip_actions_api.FloatingIPActionsApi(api_client)
    floating_ip = "45.55.96.47" # str | A floating IP address.

    # example passing only required values which don't have defaults set
    try:
        # List All Actions for a Floating IP
        api_response = api_instance.list_floating_ip_actions(floating_ip)
        pprint(api_response)
    except digitalocean_client.ApiException as e:
        print("Exception when calling FloatingIPActionsApi->list_floating_ip_actions: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **floating_ip** | **str**| A floating IP address. |

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
**200** | The results will be returned as a JSON object with an &#x60;actions&#x60; key. This will be set to an array filled with action objects containing the standard floating IP action attributes. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**401** | Unauthorized |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**404** | The resource was not found. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**429** | API Rate limit exceeded |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**500** | Server error. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**0** | Unexpected error |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_floating_ip_action**
> bool, date, datetime, dict, float, int, list, str, none_type post_floating_ip_action(floating_ip)

Initiate a Floating IP Action

To initiate an action on a floating IP send a POST request to `/v2/floating_ips/$FLOATING_IP/actions`. In the JSON body to the request, set the `type` attribute to on of the supported action types:  | Action     | Details |------------|-------- | `assign`   | Assigns a floating IP to a Droplet | `unassign` | Unassign a floating IP from a Droplet 

### Example

* Bearer Authentication (bearer_auth):

```python
import time
import digitalocean_client
from digitalocean_client.api import floating_ip_actions_api
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
    api_instance = floating_ip_actions_api.FloatingIPActionsApi(api_client)
    floating_ip = "45.55.96.47" # str | A floating IP address.
    unknown_base_type = None # UNKNOWN_BASE_TYPE | The `type` attribute set in the request body will specify the action that will be taken on the floating IP.  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Initiate a Floating IP Action
        api_response = api_instance.post_floating_ip_action(floating_ip)
        pprint(api_response)
    except digitalocean_client.ApiException as e:
        print("Exception when calling FloatingIPActionsApi->post_floating_ip_action: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Initiate a Floating IP Action
        api_response = api_instance.post_floating_ip_action(floating_ip, unknown_base_type=unknown_base_type)
        pprint(api_response)
    except digitalocean_client.ApiException as e:
        print("Exception when calling FloatingIPActionsApi->post_floating_ip_action: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **floating_ip** | **str**| A floating IP address. |
 **unknown_base_type** | [**UNKNOWN_BASE_TYPE**](UNKNOWN_BASE_TYPE.md)| The &#x60;type&#x60; attribute set in the request body will specify the action that will be taken on the floating IP.  | [optional]

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
**201** | The response will be an object with a key called &#x60;action&#x60;. The value of this will be an object that contains the standard floating IP action attributes. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**401** | Unauthorized |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**404** | The resource was not found. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**429** | API Rate limit exceeded |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**500** | Server error. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**0** | Unexpected error |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

