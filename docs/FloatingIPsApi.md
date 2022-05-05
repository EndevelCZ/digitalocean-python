# digitalocean_client.FloatingIPsApi

All URIs are relative to *https://api.digitalocean.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_floating_ip**](FloatingIPsApi.md#create_floating_ip) | **POST** /v2/floating_ips | Create a New Floating IP
[**delete_floating_ip**](FloatingIPsApi.md#delete_floating_ip) | **DELETE** /v2/floating_ips/{floating_ip} | Delete a Floating IPs
[**get_floating_ip**](FloatingIPsApi.md#get_floating_ip) | **GET** /v2/floating_ips/{floating_ip} | Retrieve an Existing Floating IP
[**list_floating_ips**](FloatingIPsApi.md#list_floating_ips) | **GET** /v2/floating_ips | List All Floating IPs


# **create_floating_ip**
> InlineResponse202 create_floating_ip(floating_ip_create)

Create a New Floating IP

On creation, a floating IP must be either assigned to a Droplet or reserved to a region. * To create a new floating IP assigned to a Droplet, send a POST   request to `/v2/floating_ips` with the `droplet_id` attribute.  * To create a new floating IP reserved to a region, send a POST request to   `/v2/floating_ips` with the `region` attribute.  **Note**:  In addition to the standard rate limiting, only 12 floating IPs may be created per 60 seconds.

### Example

* Bearer Authentication (bearer_auth):

```python
import time
import digitalocean_client
from digitalocean_client.api import floating_ips_api
from digitalocean_client.model.error import Error
from digitalocean_client.model.floating_ip_create import FloatingIpCreate
from digitalocean_client.model.inline_response202 import InlineResponse202
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
    api_instance = floating_ips_api.FloatingIPsApi(api_client)
    floating_ip_create = FloatingIpCreate(None) # FloatingIpCreate | 

    # example passing only required values which don't have defaults set
    try:
        # Create a New Floating IP
        api_response = api_instance.create_floating_ip(floating_ip_create)
        pprint(api_response)
    except digitalocean_client.ApiException as e:
        print("Exception when calling FloatingIPsApi->create_floating_ip: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **floating_ip_create** | [**FloatingIpCreate**](FloatingIpCreate.md)|  |

### Return type

[**InlineResponse202**](InlineResponse202.md)

### Authorization

[bearer_auth](../README.md#bearer_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | The response will be a JSON object with a key called &#x60;floating_ip&#x60;. The value of this will be an object that contains the standard attributes associated with a floating IP. When assigning a floating IP to a Droplet at same time as it created, the response&#39;s &#x60;links&#x60; object will contain links to both the Droplet and the assignment action. The latter can be used to check the status of the action. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**401** | Unauthorized |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**429** | API Rate limit exceeded |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**500** | Server error. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**0** | Unexpected error |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_floating_ip**
> delete_floating_ip(floating_ip)

Delete a Floating IPs

To delete a floating IP and remove it from your account, send a DELETE request to `/v2/floating_ips/$FLOATING_IP_ADDR`.  A successful request will receive a 204 status code with no body in response. This indicates that the request was processed successfully. 

### Example

* Bearer Authentication (bearer_auth):

```python
import time
import digitalocean_client
from digitalocean_client.api import floating_ips_api
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
    api_instance = floating_ips_api.FloatingIPsApi(api_client)
    floating_ip = "45.55.96.47" # str | A floating IP address.

    # example passing only required values which don't have defaults set
    try:
        # Delete a Floating IPs
        api_instance.delete_floating_ip(floating_ip)
    except digitalocean_client.ApiException as e:
        print("Exception when calling FloatingIPsApi->delete_floating_ip: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **floating_ip** | **str**| A floating IP address. |

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

# **get_floating_ip**
> InlineResponse2003 get_floating_ip(floating_ip)

Retrieve an Existing Floating IP

To show information about a floating IP, send a GET request to `/v2/floating_ips/$FLOATING_IP_ADDR`.

### Example

* Bearer Authentication (bearer_auth):

```python
import time
import digitalocean_client
from digitalocean_client.api import floating_ips_api
from digitalocean_client.model.inline_response2003 import InlineResponse2003
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
    api_instance = floating_ips_api.FloatingIPsApi(api_client)
    floating_ip = "45.55.96.47" # str | A floating IP address.

    # example passing only required values which don't have defaults set
    try:
        # Retrieve an Existing Floating IP
        api_response = api_instance.get_floating_ip(floating_ip)
        pprint(api_response)
    except digitalocean_client.ApiException as e:
        print("Exception when calling FloatingIPsApi->get_floating_ip: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **floating_ip** | **str**| A floating IP address. |

### Return type

[**InlineResponse2003**](InlineResponse2003.md)

### Authorization

[bearer_auth](../README.md#bearer_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The response will be a JSON object with a key called &#x60;floating_ip&#x60;. The value of this will be an object that contains the standard attributes associated with a floating IP. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**401** | Unauthorized |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**404** | The resource was not found. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**429** | API Rate limit exceeded |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**500** | Server error. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**0** | Unexpected error |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_floating_ips**
> bool, date, datetime, dict, float, int, list, str, none_type list_floating_ips()

List All Floating IPs

To list all of the floating IPs available on your account, send a GET request to `/v2/floating_ips`.

### Example

* Bearer Authentication (bearer_auth):

```python
import time
import digitalocean_client
from digitalocean_client.api import floating_ips_api
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
    api_instance = floating_ips_api.FloatingIPsApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # List All Floating IPs
        api_response = api_instance.list_floating_ips()
        pprint(api_response)
    except digitalocean_client.ApiException as e:
        print("Exception when calling FloatingIPsApi->list_floating_ips: %s\n" % e)
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
**200** | The response will be a JSON object with a key called &#x60;floating_ips&#x60;. This will be set to an array of floating IP objects, each of which will contain the standard floating IP attributes |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**401** | Unauthorized |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**429** | API Rate limit exceeded |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**500** | Server error. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**0** | Unexpected error |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

