# digitalocean_client.LoadBalancersApi

All URIs are relative to *https://api.digitalocean.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_load_balancer_droplets**](LoadBalancersApi.md#add_load_balancer_droplets) | **POST** /v2/load_balancers/{lb_id}/droplets | Add Droplets to a Load Balancer
[**add_load_balancer_forwarding_rules**](LoadBalancersApi.md#add_load_balancer_forwarding_rules) | **POST** /v2/load_balancers/{lb_id}/forwarding_rules | Add Forwarding Rules to a Load Balancer
[**create_load_balancer**](LoadBalancersApi.md#create_load_balancer) | **POST** /v2/load_balancers | Create a New Load Balancer
[**delete_load_balancer**](LoadBalancersApi.md#delete_load_balancer) | **DELETE** /v2/load_balancers/{lb_id} | Delete a Load Balancer
[**get_load_balancer**](LoadBalancersApi.md#get_load_balancer) | **GET** /v2/load_balancers/{lb_id} | Retrieve an Existing Load Balancer
[**list_all_load_balancers**](LoadBalancersApi.md#list_all_load_balancers) | **GET** /v2/load_balancers | List All Load Balancers
[**remove_load_balancer_droplets**](LoadBalancersApi.md#remove_load_balancer_droplets) | **DELETE** /v2/load_balancers/{lb_id}/droplets | Remove Droplets from a Load Balancer
[**remove_load_balancer_forwarding_rules**](LoadBalancersApi.md#remove_load_balancer_forwarding_rules) | **DELETE** /v2/load_balancers/{lb_id}/forwarding_rules | Remove Forwarding Rules from a Load Balancer
[**update_load_balancer**](LoadBalancersApi.md#update_load_balancer) | **PUT** /v2/load_balancers/{lb_id} | Update a Load Balancer


# **add_load_balancer_droplets**
> add_load_balancer_droplets(lb_id, unknown_base_type)

Add Droplets to a Load Balancer

To assign a Droplet to a load balancer instance, send a POST request to `/v2/load_balancers/$LOAD_BALANCER_ID/droplets`. In the body of the request, there should be a `droplet_ids` attribute containing a list of Droplet IDs. Individual Droplets can not be added to a load balancer configured with a Droplet tag. Attempting to do so will result in a \"422 Unprocessable Entity\" response from the API.  No response body will be sent back, but the response code will indicate success. Specifically, the response code will be a 204, which means that the action was successful with no returned body data. 

### Example

* Bearer Authentication (bearer_auth):

```python
import time
import digitalocean_client
from digitalocean_client.api import load_balancers_api
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
    api_instance = load_balancers_api.LoadBalancersApi(api_client)
    lb_id = "4de7ac8b-495b-4884-9a69-1050c6793cd6" # str | A unique identifier for a load balancer.
    unknown_base_type = None # UNKNOWN_BASE_TYPE | 

    # example passing only required values which don't have defaults set
    try:
        # Add Droplets to a Load Balancer
        api_instance.add_load_balancer_droplets(lb_id, unknown_base_type)
    except digitalocean_client.ApiException as e:
        print("Exception when calling LoadBalancersApi->add_load_balancer_droplets: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **lb_id** | **str**| A unique identifier for a load balancer. |
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
**204** | The action was successful and the response body is empty. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**401** | Unauthorized |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**404** | The resource was not found. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**429** | API Rate limit exceeded |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**500** | Server error. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**0** | Unexpected error |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_load_balancer_forwarding_rules**
> add_load_balancer_forwarding_rules(lb_id, unknown_base_type)

Add Forwarding Rules to a Load Balancer

To add an additional forwarding rule to a load balancer instance, send a POST request to `/v2/load_balancers/$LOAD_BALANCER_ID/forwarding_rules`. In the body of the request, there should be a `forwarding_rules` attribute containing an array of rules to be added.  No response body will be sent back, but the response code will indicate success. Specifically, the response code will be a 204, which means that the action was successful with no returned body data. 

### Example

* Bearer Authentication (bearer_auth):

```python
import time
import digitalocean_client
from digitalocean_client.api import load_balancers_api
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
    api_instance = load_balancers_api.LoadBalancersApi(api_client)
    lb_id = "4de7ac8b-495b-4884-9a69-1050c6793cd6" # str | A unique identifier for a load balancer.
    unknown_base_type = None # UNKNOWN_BASE_TYPE | 

    # example passing only required values which don't have defaults set
    try:
        # Add Forwarding Rules to a Load Balancer
        api_instance.add_load_balancer_forwarding_rules(lb_id, unknown_base_type)
    except digitalocean_client.ApiException as e:
        print("Exception when calling LoadBalancersApi->add_load_balancer_forwarding_rules: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **lb_id** | **str**| A unique identifier for a load balancer. |
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
**204** | The action was successful and the response body is empty. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**401** | Unauthorized |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**404** | The resource was not found. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**429** | API Rate limit exceeded |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**500** | Server error. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**0** | Unexpected error |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_load_balancer**
> bool, date, datetime, dict, float, int, list, str, none_type create_load_balancer(load_balancer_create)

Create a New Load Balancer

To create a new load balancer instance, send a POST request to `/v2/load_balancers`.  You can specify the Droplets that will sit behind the load balancer using one of two methods:  * Set `droplet_ids` to a list of specific Droplet IDs. * Set `tag` to the name of a tag. All Droplets with this tag applied will be   assigned to the load balancer. Additional Droplets will be automatically   assigned as they are tagged.  These methods are mutually exclusive. 

### Example

* Bearer Authentication (bearer_auth):

```python
import time
import digitalocean_client
from digitalocean_client.api import load_balancers_api
from digitalocean_client.model.error import Error
from digitalocean_client.model.load_balancer_create import LoadBalancerCreate
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
    api_instance = load_balancers_api.LoadBalancersApi(api_client)
    load_balancer_create = LoadBalancerCreate(None) # LoadBalancerCreate | 

    # example passing only required values which don't have defaults set
    try:
        # Create a New Load Balancer
        api_response = api_instance.create_load_balancer(load_balancer_create)
        pprint(api_response)
    except digitalocean_client.ApiException as e:
        print("Exception when calling LoadBalancersApi->create_load_balancer: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **load_balancer_create** | [**LoadBalancerCreate**](LoadBalancerCreate.md)|  |

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
**202** | Accepted |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**401** | Unauthorized |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**429** | API Rate limit exceeded |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**500** | Server error. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**0** | Unexpected error |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_load_balancer**
> delete_load_balancer(lb_id)

Delete a Load Balancer

To delete a load balancer instance, disassociating any Droplets assigned to it and removing it from your account, send a DELETE request to `/v2/load_balancers/$LOAD_BALANCER_ID`.  A successful request will receive a 204 status code with no body in response. This indicates that the request was processed successfully. 

### Example

* Bearer Authentication (bearer_auth):

```python
import time
import digitalocean_client
from digitalocean_client.api import load_balancers_api
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
    api_instance = load_balancers_api.LoadBalancersApi(api_client)
    lb_id = "4de7ac8b-495b-4884-9a69-1050c6793cd6" # str | A unique identifier for a load balancer.

    # example passing only required values which don't have defaults set
    try:
        # Delete a Load Balancer
        api_instance.delete_load_balancer(lb_id)
    except digitalocean_client.ApiException as e:
        print("Exception when calling LoadBalancersApi->delete_load_balancer: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **lb_id** | **str**| A unique identifier for a load balancer. |

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

# **get_load_balancer**
> bool, date, datetime, dict, float, int, list, str, none_type get_load_balancer(lb_id)

Retrieve an Existing Load Balancer

To show information about a load balancer instance, send a GET request to `/v2/load_balancers/$LOAD_BALANCER_ID`. 

### Example

* Bearer Authentication (bearer_auth):

```python
import time
import digitalocean_client
from digitalocean_client.api import load_balancers_api
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
    api_instance = load_balancers_api.LoadBalancersApi(api_client)
    lb_id = "4de7ac8b-495b-4884-9a69-1050c6793cd6" # str | A unique identifier for a load balancer.

    # example passing only required values which don't have defaults set
    try:
        # Retrieve an Existing Load Balancer
        api_response = api_instance.get_load_balancer(lb_id)
        pprint(api_response)
    except digitalocean_client.ApiException as e:
        print("Exception when calling LoadBalancersApi->get_load_balancer: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **lb_id** | **str**| A unique identifier for a load balancer. |

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
**200** | The response will be a JSON object with a key called &#x60;load_balancer&#x60;. The value of this will be an object that contains the standard attributes associated with a load balancer  |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**401** | Unauthorized |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**404** | The resource was not found. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**429** | API Rate limit exceeded |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**500** | Server error. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**0** | Unexpected error |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_all_load_balancers**
> bool, date, datetime, dict, float, int, list, str, none_type list_all_load_balancers()

List All Load Balancers

To list all of the load balancer instances on your account, send a GET request to `/v2/load_balancers`. 

### Example

* Bearer Authentication (bearer_auth):

```python
import time
import digitalocean_client
from digitalocean_client.api import load_balancers_api
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
    api_instance = load_balancers_api.LoadBalancersApi(api_client)
    per_page = 2 # int | Number of items returned per page (optional) if omitted the server will use the default value of 20
    page = 1 # int | Which 'page' of paginated results to return. (optional) if omitted the server will use the default value of 1

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List All Load Balancers
        api_response = api_instance.list_all_load_balancers(per_page=per_page, page=page)
        pprint(api_response)
    except digitalocean_client.ApiException as e:
        print("Exception when calling LoadBalancersApi->list_all_load_balancers: %s\n" % e)
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
**200** | A JSON object with a key of &#x60;load_balancers&#x60;. This will be set to an array of objects, each of which will contain the standard load balancer attributes. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**401** | Unauthorized |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**429** | API Rate limit exceeded |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**500** | Server error. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**0** | Unexpected error |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_load_balancer_droplets**
> remove_load_balancer_droplets(lb_id, unknown_base_type)

Remove Droplets from a Load Balancer

To remove a Droplet from a load balancer instance, send a DELETE request to `/v2/load_balancers/$LOAD_BALANCER_ID/droplets`. In the body of the request, there should be a `droplet_ids` attribute containing a list of Droplet IDs.  No response body will be sent back, but the response code will indicate success. Specifically, the response code will be a 204, which means that the action was successful with no returned body data. 

### Example

* Bearer Authentication (bearer_auth):

```python
import time
import digitalocean_client
from digitalocean_client.api import load_balancers_api
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
    api_instance = load_balancers_api.LoadBalancersApi(api_client)
    lb_id = "4de7ac8b-495b-4884-9a69-1050c6793cd6" # str | A unique identifier for a load balancer.
    unknown_base_type = None # UNKNOWN_BASE_TYPE | 

    # example passing only required values which don't have defaults set
    try:
        # Remove Droplets from a Load Balancer
        api_instance.remove_load_balancer_droplets(lb_id, unknown_base_type)
    except digitalocean_client.ApiException as e:
        print("Exception when calling LoadBalancersApi->remove_load_balancer_droplets: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **lb_id** | **str**| A unique identifier for a load balancer. |
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
**204** | The action was successful and the response body is empty. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**401** | Unauthorized |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**404** | The resource was not found. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**429** | API Rate limit exceeded |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**500** | Server error. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**0** | Unexpected error |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_load_balancer_forwarding_rules**
> remove_load_balancer_forwarding_rules(lb_id, unknown_base_type)

Remove Forwarding Rules from a Load Balancer

To remove forwarding rules from a load balancer instance, send a DELETE request to `/v2/load_balancers/$LOAD_BALANCER_ID/forwarding_rules`. In the body of the request, there should be a `forwarding_rules` attribute containing an array of rules to be removed.  No response body will be sent back, but the response code will indicate success. Specifically, the response code will be a 204, which means that the action was successful with no returned body data. 

### Example

* Bearer Authentication (bearer_auth):

```python
import time
import digitalocean_client
from digitalocean_client.api import load_balancers_api
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
    api_instance = load_balancers_api.LoadBalancersApi(api_client)
    lb_id = "4de7ac8b-495b-4884-9a69-1050c6793cd6" # str | A unique identifier for a load balancer.
    unknown_base_type = None # UNKNOWN_BASE_TYPE | 

    # example passing only required values which don't have defaults set
    try:
        # Remove Forwarding Rules from a Load Balancer
        api_instance.remove_load_balancer_forwarding_rules(lb_id, unknown_base_type)
    except digitalocean_client.ApiException as e:
        print("Exception when calling LoadBalancersApi->remove_load_balancer_forwarding_rules: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **lb_id** | **str**| A unique identifier for a load balancer. |
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
**204** | The action was successful and the response body is empty. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**401** | Unauthorized |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**404** | The resource was not found. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**429** | API Rate limit exceeded |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**500** | Server error. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**0** | Unexpected error |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_load_balancer**
> bool, date, datetime, dict, float, int, list, str, none_type update_load_balancer(lb_id, load_balancer_create)

Update a Load Balancer

To update a load balancer's settings, send a PUT request to `/v2/load_balancers/$LOAD_BALANCER_ID`. The request should contain a full representation of the load balancer including existing attributes. It may contain _one of_ the `droplets_ids` or `tag` attributes as they are mutually exclusive. **Note that any attribute that is not provided will be reset to its default value.** 

### Example

* Bearer Authentication (bearer_auth):

```python
import time
import digitalocean_client
from digitalocean_client.api import load_balancers_api
from digitalocean_client.model.error import Error
from digitalocean_client.model.load_balancer_create import LoadBalancerCreate
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
    api_instance = load_balancers_api.LoadBalancersApi(api_client)
    lb_id = "4de7ac8b-495b-4884-9a69-1050c6793cd6" # str | A unique identifier for a load balancer.
    load_balancer_create = LoadBalancerCreate(None) # LoadBalancerCreate | 

    # example passing only required values which don't have defaults set
    try:
        # Update a Load Balancer
        api_response = api_instance.update_load_balancer(lb_id, load_balancer_create)
        pprint(api_response)
    except digitalocean_client.ApiException as e:
        print("Exception when calling LoadBalancersApi->update_load_balancer: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **lb_id** | **str**| A unique identifier for a load balancer. |
 **load_balancer_create** | [**LoadBalancerCreate**](LoadBalancerCreate.md)|  |

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
**200** | The response will be a JSON object with a key called &#x60;load_balancer&#x60;. The value of this will be an object containing the standard attributes of a load balancer.  |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**401** | Unauthorized |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**404** | The resource was not found. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**429** | API Rate limit exceeded |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**500** | Server error. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**0** | Unexpected error |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

