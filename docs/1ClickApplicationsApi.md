# openapi_client.1ClickApplicationsApi

All URIs are relative to *https://api.digitalocean.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**install_kubernetes**](1ClickApplicationsApi.md#install_kubernetes) | **POST** /v2/1-clicks/kubernetes | Install Kubernetes 1-Click Applications
[**list**](1ClickApplicationsApi.md#list) | **GET** /v2/1-clicks | List 1-Click Applications


# **install_kubernetes**
> InlineResponse200 install_kubernetes(model1_click_create)

Install Kubernetes 1-Click Applications

To install a Kubernetes 1-Click application on a cluster, send a POST request to `/v2/1-clicks/kubernetes`. The `addon_slugs` and `cluster_uuid` must be provided as body parameter in order to specify which 1-Click application(s) to install. To list all available 1-Click Kubernetes applications, send a request to `/v2/1-clicks?type=kubernetes`. 

### Example

* Bearer Authentication (bearer_auth):

```python
import time
import openapi_client
from openapi_client.api import 1_click_applications_api
from openapi_client.model.model1_click_create import Model1ClickCreate
from openapi_client.model.error import Error
from openapi_client.model.inline_response200 import InlineResponse200
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
    api_instance = 1_click_applications_api.1ClickApplicationsApi(api_client)
    model1_click_create = Model1ClickCreate(
        addon_slugs=["kube-state-metrics","loki"],
        cluster_uuid="50a994b6-c303-438f-9495-7e896cfe6b08",
    ) # Model1ClickCreate | 

    # example passing only required values which don't have defaults set
    try:
        # Install Kubernetes 1-Click Applications
        api_response = api_instance.install_kubernetes(model1_click_create)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling 1ClickApplicationsApi->install_kubernetes: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **model1_click_create** | [**Model1ClickCreate**](Model1ClickCreate.md)|  |

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

[bearer_auth](../README.md#bearer_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The response will verify that a job has been successfully created to install a 1-Click. The post-installation lifecycle of a 1-Click application can not be managed via the DigitalOcean API. For additional details specific to the 1-Click, find and view its [DigitalOcean Marketplace](https://marketplace.digitalocean.com) page.  |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**401** | Unauthorized |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**429** | API Rate limit exceeded |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**500** | Server error. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**0** | Unexpected error |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list**
> bool, date, datetime, dict, float, int, list, str, none_type list()

List 1-Click Applications

To list all available 1-Click applications, send a GET request to `/v2/1-clicks`. The `type` may be provided as query paramater in order to restrict results to a certain type of 1-Click, for example: `/v2/1-clicks?type=droplet`. Current supported types are `kubernetes` and `droplet`.  The response will be a JSON object with a key called `1_clicks`. This will be set to an array of 1-Click application data, each of which will contain the the slug and type for the 1-Click. 

### Example

* Bearer Authentication (bearer_auth):

```python
import time
import openapi_client
from openapi_client.api import 1_click_applications_api
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
    api_instance = 1_click_applications_api.1ClickApplicationsApi(api_client)
    type = "kubernetes" # str | Restrict results to a certain type of 1-Click. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List 1-Click Applications
        api_response = api_instance.list(type=type)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling 1ClickApplicationsApi->list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**| Restrict results to a certain type of 1-Click. | [optional]

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
**200** | A JSON object with a key of &#x60;1_clicks&#x60;. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**401** | Unauthorized |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**429** | API Rate limit exceeded |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**500** | Server error. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**0** | Unexpected error |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

