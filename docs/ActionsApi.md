# digitalocean_client.ActionsApi

All URIs are relative to *https://api.digitalocean.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_action**](ActionsApi.md#get_action) | **GET** /v2/actions/{action_id} | Retrieve an Existing Action
[**list_all_actions**](ActionsApi.md#list_all_actions) | **GET** /v2/actions | List All Actions


# **get_action**
> bool, date, datetime, dict, float, int, list, str, none_type get_action(action_id)

Retrieve an Existing Action

To retrieve a specific action object, send a GET request to `/v2/actions/$ACTION_ID`.

### Example

* Bearer Authentication (bearer_auth):

```python
import time
import digitalocean_client
from digitalocean_client.api import actions_api
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
    api_instance = actions_api.ActionsApi(api_client)
    action_id = 36804636 # int | A unique numeric ID that can be used to identify and reference an action.

    # example passing only required values which don't have defaults set
    try:
        # Retrieve an Existing Action
        api_response = api_instance.get_action(action_id)
        pprint(api_response)
    except digitalocean_client.ApiException as e:
        print("Exception when calling ActionsApi->get_action: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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

# **list_all_actions**
> bool, date, datetime, dict, float, int, list, str, none_type list_all_actions()

List All Actions

This will be the entire list of actions taken on your account, so it will be quite large. As with any large collection returned by the API, the results will be paginated with only 20 on each page by default.

### Example

* Bearer Authentication (bearer_auth):

```python
import time
import digitalocean_client
from digitalocean_client.api import actions_api
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
    api_instance = actions_api.ActionsApi(api_client)
    per_page = 2 # int | Number of items returned per page (optional) if omitted the server will use the default value of 20
    page = 1 # int | Which 'page' of paginated results to return. (optional) if omitted the server will use the default value of 1

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List All Actions
        api_response = api_instance.list_all_actions(per_page=per_page, page=page)
        pprint(api_response)
    except digitalocean_client.ApiException as e:
        print("Exception when calling ActionsApi->list_all_actions: %s\n" % e)
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
**200** | The results will be returned as a JSON object with an actions key.  This will be set to an array filled with action objects containing the standard action attributes |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**401** | Unauthorized |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**429** | API Rate limit exceeded |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**500** | Server error. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**0** | Unexpected error |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

