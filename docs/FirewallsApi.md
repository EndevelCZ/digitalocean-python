# digitalocean_client.FirewallsApi

All URIs are relative to *https://api.digitalocean.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_firewall_droplets**](FirewallsApi.md#add_firewall_droplets) | **POST** /v2/firewalls/{firewall_id}/droplets | Add Droplets to a Firewall
[**add_firewall_rules**](FirewallsApi.md#add_firewall_rules) | **POST** /v2/firewalls/{firewall_id}/rules | Add Rules to a Firewall
[**add_firewall_tags**](FirewallsApi.md#add_firewall_tags) | **POST** /v2/firewalls/{firewall_id}/tags | Add Tags to a Firewall
[**create_firewall**](FirewallsApi.md#create_firewall) | **POST** /v2/firewalls | Create a New Firewall
[**delete_firewall**](FirewallsApi.md#delete_firewall) | **DELETE** /v2/firewalls/{firewall_id} | Delete a Firewall
[**delete_firewall_droplets**](FirewallsApi.md#delete_firewall_droplets) | **DELETE** /v2/firewalls/{firewall_id}/droplets | Remove Droplets from a Firewall
[**delete_firewall_rules**](FirewallsApi.md#delete_firewall_rules) | **DELETE** /v2/firewalls/{firewall_id}/rules | Remove Rules from a Firewall
[**delete_firewall_tags**](FirewallsApi.md#delete_firewall_tags) | **DELETE** /v2/firewalls/{firewall_id}/tags | Remove Tags from a Firewall
[**get_firewall**](FirewallsApi.md#get_firewall) | **GET** /v2/firewalls/{firewall_id} | Retrieve an Existing Firewall
[**list_firewalls**](FirewallsApi.md#list_firewalls) | **GET** /v2/firewalls | List All Firewalls
[**update_firewall**](FirewallsApi.md#update_firewall) | **PUT** /v2/firewalls/{firewall_id} | Update a Firewall


# **add_firewall_droplets**
> add_firewall_droplets(firewall_id)

Add Droplets to a Firewall

To assign a Droplet to a firewall, send a POST request to `/v2/firewalls/$FIREWALL_ID/droplets`. In the body of the request, there should be a `droplet_ids` attribute containing a list of Droplet IDs.  No response body will be sent back, but the response code will indicate success. Specifically, the response code will be a 204, which means that the action was successful with no returned body data. 

### Example

* Bearer Authentication (bearer_auth):

```python
import time
import digitalocean_client
from digitalocean_client.api import firewalls_api
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
    api_instance = firewalls_api.FirewallsApi(api_client)
    firewall_id = "bb4b2611-3d72-467b-8602-280330ecd65c" # str | A unique ID that can be used to identify and reference a firewall.
    unknown_base_type = None # UNKNOWN_BASE_TYPE |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Add Droplets to a Firewall
        api_instance.add_firewall_droplets(firewall_id)
    except digitalocean_client.ApiException as e:
        print("Exception when calling FirewallsApi->add_firewall_droplets: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Add Droplets to a Firewall
        api_instance.add_firewall_droplets(firewall_id, unknown_base_type=unknown_base_type)
    except digitalocean_client.ApiException as e:
        print("Exception when calling FirewallsApi->add_firewall_droplets: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **firewall_id** | **str**| A unique ID that can be used to identify and reference a firewall. |
 **unknown_base_type** | [**UNKNOWN_BASE_TYPE**](UNKNOWN_BASE_TYPE.md)|  | [optional]

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
**400** | Bad Request |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**401** | Unauthorized |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**404** | The resource was not found. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**429** | API Rate limit exceeded |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**500** | Server error. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**0** | Unexpected error |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_firewall_rules**
> add_firewall_rules(firewall_id)

Add Rules to a Firewall

To add additional access rules to a firewall, send a POST request to `/v2/firewalls/$FIREWALL_ID/rules`. The body of the request may include an inbound_rules and/or outbound_rules attribute containing an array of rules to be added.  No response body will be sent back, but the response code will indicate success. Specifically, the response code will be a 204, which means that the action was successful with no returned body data. 

### Example

* Bearer Authentication (bearer_auth):

```python
import time
import digitalocean_client
from digitalocean_client.api import firewalls_api
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
    api_instance = firewalls_api.FirewallsApi(api_client)
    firewall_id = "bb4b2611-3d72-467b-8602-280330ecd65c" # str | A unique ID that can be used to identify and reference a firewall.
    unknown_base_type = None # UNKNOWN_BASE_TYPE |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Add Rules to a Firewall
        api_instance.add_firewall_rules(firewall_id)
    except digitalocean_client.ApiException as e:
        print("Exception when calling FirewallsApi->add_firewall_rules: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Add Rules to a Firewall
        api_instance.add_firewall_rules(firewall_id, unknown_base_type=unknown_base_type)
    except digitalocean_client.ApiException as e:
        print("Exception when calling FirewallsApi->add_firewall_rules: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **firewall_id** | **str**| A unique ID that can be used to identify and reference a firewall. |
 **unknown_base_type** | [**UNKNOWN_BASE_TYPE**](UNKNOWN_BASE_TYPE.md)|  | [optional]

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
**400** | Bad Request |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**401** | Unauthorized |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**404** | The resource was not found. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**429** | API Rate limit exceeded |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**500** | Server error. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**0** | Unexpected error |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_firewall_tags**
> add_firewall_tags(firewall_id)

Add Tags to a Firewall

To assign a tag representing a group of Droplets to a firewall, send a POST request to `/v2/firewalls/$FIREWALL_ID/tags`. In the body of the request, there should be a `tags` attribute containing a list of tag names.  No response body will be sent back, but the response code will indicate success. Specifically, the response code will be a 204, which means that the action was successful with no returned body data. 

### Example

* Bearer Authentication (bearer_auth):

```python
import time
import digitalocean_client
from digitalocean_client.api import firewalls_api
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
    api_instance = firewalls_api.FirewallsApi(api_client)
    firewall_id = "bb4b2611-3d72-467b-8602-280330ecd65c" # str | A unique ID that can be used to identify and reference a firewall.
    unknown_base_type = None # UNKNOWN_BASE_TYPE |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Add Tags to a Firewall
        api_instance.add_firewall_tags(firewall_id)
    except digitalocean_client.ApiException as e:
        print("Exception when calling FirewallsApi->add_firewall_tags: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Add Tags to a Firewall
        api_instance.add_firewall_tags(firewall_id, unknown_base_type=unknown_base_type)
    except digitalocean_client.ApiException as e:
        print("Exception when calling FirewallsApi->add_firewall_tags: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **firewall_id** | **str**| A unique ID that can be used to identify and reference a firewall. |
 **unknown_base_type** | [**UNKNOWN_BASE_TYPE**](UNKNOWN_BASE_TYPE.md)|  | [optional]

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
**400** | Bad Request |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**401** | Unauthorized |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**404** | The resource was not found. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**429** | API Rate limit exceeded |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**500** | Server error. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**0** | Unexpected error |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_firewall**
> bool, date, datetime, dict, float, int, list, str, none_type create_firewall()

Create a New Firewall

To create a new firewall, send a POST request to `/v2/firewalls`. The request must contain at least one inbound or outbound access rule. 

### Example

* Bearer Authentication (bearer_auth):

```python
import time
import digitalocean_client
from digitalocean_client.api import firewalls_api
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
    api_instance = firewalls_api.FirewallsApi(api_client)
    unknown_base_type = None # UNKNOWN_BASE_TYPE |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create a New Firewall
        api_response = api_instance.create_firewall(unknown_base_type=unknown_base_type)
        pprint(api_response)
    except digitalocean_client.ApiException as e:
        print("Exception when calling FirewallsApi->create_firewall: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **unknown_base_type** | [**UNKNOWN_BASE_TYPE**](UNKNOWN_BASE_TYPE.md)|  | [optional]

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
**202** | The response will be a JSON object with a firewall key. This will be set to an object containing the standard firewall attributes |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**400** | Bad Request |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**401** | Unauthorized |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**429** | API Rate limit exceeded |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**500** | Server error. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**0** | Unexpected error |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_firewall**
> delete_firewall(firewall_id)

Delete a Firewall

To delete a firewall send a DELETE request to `/v2/firewalls/$FIREWALL_ID`.  No response body will be sent back, but the response code will indicate success. Specifically, the response code will be a 204, which means that the action was successful with no returned body data. 

### Example

* Bearer Authentication (bearer_auth):

```python
import time
import digitalocean_client
from digitalocean_client.api import firewalls_api
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
    api_instance = firewalls_api.FirewallsApi(api_client)
    firewall_id = "bb4b2611-3d72-467b-8602-280330ecd65c" # str | A unique ID that can be used to identify and reference a firewall.

    # example passing only required values which don't have defaults set
    try:
        # Delete a Firewall
        api_instance.delete_firewall(firewall_id)
    except digitalocean_client.ApiException as e:
        print("Exception when calling FirewallsApi->delete_firewall: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **firewall_id** | **str**| A unique ID that can be used to identify and reference a firewall. |

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

# **delete_firewall_droplets**
> delete_firewall_droplets(firewall_id)

Remove Droplets from a Firewall

To remove a Droplet from a firewall, send a DELETE request to `/v2/firewalls/$FIREWALL_ID/droplets`. In the body of the request, there should be a `droplet_ids` attribute containing a list of Droplet IDs.  No response body will be sent back, but the response code will indicate success. Specifically, the response code will be a 204, which means that the action was successful with no returned body data. 

### Example

* Bearer Authentication (bearer_auth):

```python
import time
import digitalocean_client
from digitalocean_client.api import firewalls_api
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
    api_instance = firewalls_api.FirewallsApi(api_client)
    firewall_id = "bb4b2611-3d72-467b-8602-280330ecd65c" # str | A unique ID that can be used to identify and reference a firewall.
    unknown_base_type = None # UNKNOWN_BASE_TYPE |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Remove Droplets from a Firewall
        api_instance.delete_firewall_droplets(firewall_id)
    except digitalocean_client.ApiException as e:
        print("Exception when calling FirewallsApi->delete_firewall_droplets: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Remove Droplets from a Firewall
        api_instance.delete_firewall_droplets(firewall_id, unknown_base_type=unknown_base_type)
    except digitalocean_client.ApiException as e:
        print("Exception when calling FirewallsApi->delete_firewall_droplets: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **firewall_id** | **str**| A unique ID that can be used to identify and reference a firewall. |
 **unknown_base_type** | [**UNKNOWN_BASE_TYPE**](UNKNOWN_BASE_TYPE.md)|  | [optional]

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
**400** | Bad Request |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**401** | Unauthorized |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**404** | The resource was not found. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**429** | API Rate limit exceeded |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**500** | Server error. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**0** | Unexpected error |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_firewall_rules**
> delete_firewall_rules(firewall_id)

Remove Rules from a Firewall

To remove access rules from a firewall, send a DELETE request to `/v2/firewalls/$FIREWALL_ID/rules`. The body of the request may include an `inbound_rules` and/or `outbound_rules` attribute containing an array of rules to be removed.  No response body will be sent back, but the response code will indicate success. Specifically, the response code will be a 204, which means that the action was successful with no returned body data. 

### Example

* Bearer Authentication (bearer_auth):

```python
import time
import digitalocean_client
from digitalocean_client.api import firewalls_api
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
    api_instance = firewalls_api.FirewallsApi(api_client)
    firewall_id = "bb4b2611-3d72-467b-8602-280330ecd65c" # str | A unique ID that can be used to identify and reference a firewall.
    unknown_base_type = None # UNKNOWN_BASE_TYPE |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Remove Rules from a Firewall
        api_instance.delete_firewall_rules(firewall_id)
    except digitalocean_client.ApiException as e:
        print("Exception when calling FirewallsApi->delete_firewall_rules: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Remove Rules from a Firewall
        api_instance.delete_firewall_rules(firewall_id, unknown_base_type=unknown_base_type)
    except digitalocean_client.ApiException as e:
        print("Exception when calling FirewallsApi->delete_firewall_rules: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **firewall_id** | **str**| A unique ID that can be used to identify and reference a firewall. |
 **unknown_base_type** | [**UNKNOWN_BASE_TYPE**](UNKNOWN_BASE_TYPE.md)|  | [optional]

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
**400** | Bad Request |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**401** | Unauthorized |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**404** | The resource was not found. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**429** | API Rate limit exceeded |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**500** | Server error. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**0** | Unexpected error |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_firewall_tags**
> delete_firewall_tags(firewall_id)

Remove Tags from a Firewall

To remove a tag representing a group of Droplets from a firewall, send a DELETE request to `/v2/firewalls/$FIREWALL_ID/tags`. In the body of the request, there should be a `tags` attribute containing a list of tag names.  No response body will be sent back, but the response code will indicate success. Specifically, the response code will be a 204, which means that the action was successful with no returned body data. 

### Example

* Bearer Authentication (bearer_auth):

```python
import time
import digitalocean_client
from digitalocean_client.api import firewalls_api
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
    api_instance = firewalls_api.FirewallsApi(api_client)
    firewall_id = "bb4b2611-3d72-467b-8602-280330ecd65c" # str | A unique ID that can be used to identify and reference a firewall.
    unknown_base_type = None # UNKNOWN_BASE_TYPE |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Remove Tags from a Firewall
        api_instance.delete_firewall_tags(firewall_id)
    except digitalocean_client.ApiException as e:
        print("Exception when calling FirewallsApi->delete_firewall_tags: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Remove Tags from a Firewall
        api_instance.delete_firewall_tags(firewall_id, unknown_base_type=unknown_base_type)
    except digitalocean_client.ApiException as e:
        print("Exception when calling FirewallsApi->delete_firewall_tags: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **firewall_id** | **str**| A unique ID that can be used to identify and reference a firewall. |
 **unknown_base_type** | [**UNKNOWN_BASE_TYPE**](UNKNOWN_BASE_TYPE.md)|  | [optional]

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
**400** | Bad Request |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**401** | Unauthorized |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**404** | The resource was not found. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**429** | API Rate limit exceeded |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**500** | Server error. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**0** | Unexpected error |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_firewall**
> bool, date, datetime, dict, float, int, list, str, none_type get_firewall(firewall_id)

Retrieve an Existing Firewall

To show information about an existing firewall, send a GET request to `/v2/firewalls/$FIREWALL_ID`.

### Example

* Bearer Authentication (bearer_auth):

```python
import time
import digitalocean_client
from digitalocean_client.api import firewalls_api
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
    api_instance = firewalls_api.FirewallsApi(api_client)
    firewall_id = "bb4b2611-3d72-467b-8602-280330ecd65c" # str | A unique ID that can be used to identify and reference a firewall.

    # example passing only required values which don't have defaults set
    try:
        # Retrieve an Existing Firewall
        api_response = api_instance.get_firewall(firewall_id)
        pprint(api_response)
    except digitalocean_client.ApiException as e:
        print("Exception when calling FirewallsApi->get_firewall: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **firewall_id** | **str**| A unique ID that can be used to identify and reference a firewall. |

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
**200** | The response will be a JSON object with a firewall key. This will be set to an object containing the standard firewall attributes. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**401** | Unauthorized |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**404** | The resource was not found. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**429** | API Rate limit exceeded |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**500** | Server error. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**0** | Unexpected error |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_firewalls**
> bool, date, datetime, dict, float, int, list, str, none_type list_firewalls()

List All Firewalls

To list all of the firewalls available on your account, send a GET request to `/v2/firewalls`.

### Example

* Bearer Authentication (bearer_auth):

```python
import time
import digitalocean_client
from digitalocean_client.api import firewalls_api
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
    api_instance = firewalls_api.FirewallsApi(api_client)
    per_page = 2 # int | Number of items returned per page (optional) if omitted the server will use the default value of 20
    page = 1 # int | Which 'page' of paginated results to return. (optional) if omitted the server will use the default value of 1

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List All Firewalls
        api_response = api_instance.list_firewalls(per_page=per_page, page=page)
        pprint(api_response)
    except digitalocean_client.ApiException as e:
        print("Exception when calling FirewallsApi->list_firewalls: %s\n" % e)
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
**200** | To list all of the firewalls available on your account, send a GET request to &#x60;/v2/firewalls&#x60;. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**401** | Unauthorized |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**429** | API Rate limit exceeded |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**500** | Server error. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**0** | Unexpected error |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_firewall**
> bool, date, datetime, dict, float, int, list, str, none_type update_firewall(firewall_id)

Update a Firewall

To update the configuration of an existing firewall, send a PUT request to `/v2/firewalls/$FIREWALL_ID`. The request should contain a full representation of the firewall including existing attributes. **Note that any attributes that are not provided will be reset to their default values.** 

### Example

* Bearer Authentication (bearer_auth):

```python
import time
import digitalocean_client
from digitalocean_client.api import firewalls_api
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
    api_instance = firewalls_api.FirewallsApi(api_client)
    firewall_id = "bb4b2611-3d72-467b-8602-280330ecd65c" # str | A unique ID that can be used to identify and reference a firewall.
    unknown_base_type = None # UNKNOWN_BASE_TYPE |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update a Firewall
        api_response = api_instance.update_firewall(firewall_id)
        pprint(api_response)
    except digitalocean_client.ApiException as e:
        print("Exception when calling FirewallsApi->update_firewall: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update a Firewall
        api_response = api_instance.update_firewall(firewall_id, unknown_base_type=unknown_base_type)
        pprint(api_response)
    except digitalocean_client.ApiException as e:
        print("Exception when calling FirewallsApi->update_firewall: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **firewall_id** | **str**| A unique ID that can be used to identify and reference a firewall. |
 **unknown_base_type** | [**UNKNOWN_BASE_TYPE**](UNKNOWN_BASE_TYPE.md)|  | [optional]

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
**200** | The response will be a JSON object with a &#x60;firewall&#x60; key. This will be set to an object containing the standard firewall attributes. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**400** | Bad Request |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**401** | Unauthorized |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**404** | The resource was not found. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**429** | API Rate limit exceeded |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**500** | Server error. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**0** | Unexpected error |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

