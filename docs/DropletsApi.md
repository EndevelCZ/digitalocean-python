# openapi_client.DropletsApi

All URIs are relative to *https://api.digitalocean.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_droplet**](DropletsApi.md#create_droplet) | **POST** /v2/droplets | Create a New Droplet
[**destroy_droplet**](DropletsApi.md#destroy_droplet) | **DELETE** /v2/droplets/{droplet_id} | Delete an Existing Droplet
[**destroy_droplets_by_tag**](DropletsApi.md#destroy_droplets_by_tag) | **DELETE** /v2/droplets | Deleting Droplets by Tag
[**destroy_with_associated_resources_dangerous**](DropletsApi.md#destroy_with_associated_resources_dangerous) | **DELETE** /v2/droplets/{droplet_id}/destroy_with_associated_resources/dangerous | Destroy a Droplet and All of its Associated Resources (Dangerous)
[**destroy_with_associated_resources_selective**](DropletsApi.md#destroy_with_associated_resources_selective) | **DELETE** /v2/droplets/{droplet_id}/destroy_with_associated_resources/selective | Selectively Destroy a Droplet and its Associated Resources
[**get_destroy_with_associated_resources_status**](DropletsApi.md#get_destroy_with_associated_resources_status) | **GET** /v2/droplets/{droplet_id}/destroy_with_associated_resources/status | Check Status of a Droplet Destroy with Associated Resources Request
[**get_droplet**](DropletsApi.md#get_droplet) | **GET** /v2/droplets/{droplet_id} | Retrieve an Existing Droplet
[**list_all_droplet_neighbors_ids**](DropletsApi.md#list_all_droplet_neighbors_ids) | **GET** /v2/reports/droplet_neighbors_ids | List All Droplet Neighbors
[**list_all_droplets**](DropletsApi.md#list_all_droplets) | **GET** /v2/droplets | List All Droplets
[**list_droplet_associated_resources**](DropletsApi.md#list_droplet_associated_resources) | **GET** /v2/droplets/{droplet_id}/destroy_with_associated_resources | List Associated Resources for a Droplet
[**list_droplet_backups**](DropletsApi.md#list_droplet_backups) | **GET** /v2/droplets/{droplet_id}/backups | List Backups for a Droplet
[**list_droplet_firewalls**](DropletsApi.md#list_droplet_firewalls) | **GET** /v2/droplets/{droplet_id}/firewalls | List all Firewalls Applied to a Droplet
[**list_droplet_kernels**](DropletsApi.md#list_droplet_kernels) | **GET** /v2/droplets/{droplet_id}/kernels | List All Available Kernels for a Droplet
[**list_droplet_neighbors**](DropletsApi.md#list_droplet_neighbors) | **GET** /v2/droplets/{droplet_id}/neighbors | List Neighbors for a Droplet
[**list_droplet_snapshots**](DropletsApi.md#list_droplet_snapshots) | **GET** /v2/droplets/{droplet_id}/snapshots | List Snapshots for a Droplet
[**retry_destroy_with_associated_resource**](DropletsApi.md#retry_destroy_with_associated_resource) | **POST** /v2/droplets/{droplet_id}/destroy_with_associated_resources/retry | Retry a Droplet Destroy with Associated Resources Request


# **create_droplet**
> bool, date, datetime, dict, float, int, list, str, none_type create_droplet()

Create a New Droplet

To create a new Droplet, send a POST request to `/v2/droplets` setting the required attributes.  A Droplet will be created using the provided information. The response body will contain a JSON object with a key called `droplet`. The value will be an object containing the standard attributes for your new Droplet. The response code, 202 Accepted, does not indicate the success or failure of the operation, just that the request has been accepted for processing. The `actions` returned as part of the response's `links` object can be used to check the status of the Droplet create event.  ### Create Multiple Droplets  Creating multiple Droplets is very similar to creating a single Droplet. Instead of sending `name` as a string, send `names` as an array of strings. A Droplet will be created for each name you send using the associated information. Up to ten Droplets may be created this way at a time.  Rather than returning a single Droplet, the response body will contain a JSON array with a key called `droplets`. This will be set to an array of JSON objects, each of which will contain the standard Droplet attributes. The response code, 202 Accepted, does not indicate the success or failure of any operation, just that the request has been accepted for processing. The array of `actions` returned as part of the response's `links` object can be used to check the status of each individual Droplet create event. 

### Example

* Bearer Authentication (bearer_auth):

```python
import time
import openapi_client
from openapi_client.api import droplets_api
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
    api_instance = droplets_api.DropletsApi(api_client)
    unknown_base_type = None # UNKNOWN_BASE_TYPE |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create a New Droplet
        api_response = api_instance.create_droplet(unknown_base_type=unknown_base_type)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DropletsApi->create_droplet: %s\n" % e)
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
**202** | Accepted |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**401** | Unauthorized |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**429** | API Rate limit exceeded |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**500** | Server error. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**0** | Unexpected error |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **destroy_droplet**
> destroy_droplet(droplet_id)

Delete an Existing Droplet

To delete a Droplet, send a DELETE request to `/v2/droplets/$DROPLET_ID`.  A successful request will receive a 204 status code with no body in response. This indicates that the request was processed successfully. 

### Example

* Bearer Authentication (bearer_auth):

```python
import time
import openapi_client
from openapi_client.api import droplets_api
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
    api_instance = droplets_api.DropletsApi(api_client)
    droplet_id = 3164444 # int | A unique identifier for a Droplet instance.

    # example passing only required values which don't have defaults set
    try:
        # Delete an Existing Droplet
        api_instance.destroy_droplet(droplet_id)
    except openapi_client.ApiException as e:
        print("Exception when calling DropletsApi->destroy_droplet: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **droplet_id** | **int**| A unique identifier for a Droplet instance. |

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

# **destroy_droplets_by_tag**
> destroy_droplets_by_tag(tag_name)

Deleting Droplets by Tag

To delete **all** Droplets assigned to a specific tag, include the `tag_name` query parameter set to the name of the tag in your DELETE request. For example,  `/v2/droplets?tag_name=$TAG_NAME`.  A successful request will receive a 204 status code with no body in response. This indicates that the request was processed successfully. 

### Example

* Bearer Authentication (bearer_auth):

```python
import time
import openapi_client
from openapi_client.api import droplets_api
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
    api_instance = droplets_api.DropletsApi(api_client)
    tag_name = "env:test" # str | Specifies Droplets to be deleted by tag.

    # example passing only required values which don't have defaults set
    try:
        # Deleting Droplets by Tag
        api_instance.destroy_droplets_by_tag(tag_name)
    except openapi_client.ApiException as e:
        print("Exception when calling DropletsApi->destroy_droplets_by_tag: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tag_name** | **str**| Specifies Droplets to be deleted by tag. |

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

# **destroy_with_associated_resources_dangerous**
> destroy_with_associated_resources_dangerous(droplet_id, x_dangerous)

Destroy a Droplet and All of its Associated Resources (Dangerous)

To destroy a Droplet along with all of its associated resources, send a DELETE request to the `/v2/droplets/$DROPLET_ID/destroy_with_associated_resources/dangerous` endpoint. The headers of this request must include an `X-Dangerous` key set to `true`. To preview which resources will be destroyed, first query the Droplet's associated resources. This operation _can not_ be reverse and should be used with caution.  A successful response will include a 202 response code and no content. Use the status endpoint to check on the success or failure of the destruction of the individual resources. 

### Example

* Bearer Authentication (bearer_auth):

```python
import time
import openapi_client
from openapi_client.api import droplets_api
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
    api_instance = droplets_api.DropletsApi(api_client)
    droplet_id = 3164444 # int | A unique identifier for a Droplet instance.
    x_dangerous = True # bool | Acknowledge this action will destroy the Droplet and all associated resources and _can not_ be reversed.

    # example passing only required values which don't have defaults set
    try:
        # Destroy a Droplet and All of its Associated Resources (Dangerous)
        api_instance.destroy_with_associated_resources_dangerous(droplet_id, x_dangerous)
    except openapi_client.ApiException as e:
        print("Exception when calling DropletsApi->destroy_with_associated_resources_dangerous: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **droplet_id** | **int**| A unique identifier for a Droplet instance. |
 **x_dangerous** | **bool**| Acknowledge this action will destroy the Droplet and all associated resources and _can not_ be reversed. |

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
**202** | The does not indicate the success or failure of any operation, just that the request has been accepted for processing. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**401** | Unauthorized |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**404** | The resource was not found. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**429** | API Rate limit exceeded |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**500** | Server error. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**0** | Unexpected error |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **destroy_with_associated_resources_selective**
> destroy_with_associated_resources_selective(droplet_id)

Selectively Destroy a Droplet and its Associated Resources

To destroy a Droplet along with a sub-set of its associated resources, send a DELETE request to the `/v2/droplets/$DROPLET_ID/destroy_with_associated_resources/selective` endpoint. The JSON body of the request should include `floating_ips`, `snapshots`, `volumes`, or `volume_snapshots` keys each set to an array of IDs for the associated resources to be destroyed. The IDs can be found by querying the Droplet's associated resources. Any associated resource not included in the request will remain and continue to accrue changes on your account.  A successful response will include a 202 response code and no content. Use the status endpoint to check on the success or failure of the destruction of the individual resources. 

### Example

* Bearer Authentication (bearer_auth):

```python
import time
import openapi_client
from openapi_client.api import droplets_api
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
    api_instance = droplets_api.DropletsApi(api_client)
    droplet_id = 3164444 # int | A unique identifier for a Droplet instance.

    # example passing only required values which don't have defaults set
    try:
        # Selectively Destroy a Droplet and its Associated Resources
        api_instance.destroy_with_associated_resources_selective(droplet_id)
    except openapi_client.ApiException as e:
        print("Exception when calling DropletsApi->destroy_with_associated_resources_selective: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **droplet_id** | **int**| A unique identifier for a Droplet instance. |

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
**202** | The does not indicate the success or failure of any operation, just that the request has been accepted for processing. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**401** | Unauthorized |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**404** | The resource was not found. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**429** | API Rate limit exceeded |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**500** | Server error. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**0** | Unexpected error |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_destroy_with_associated_resources_status**
> AssociatedResourceStatus get_destroy_with_associated_resources_status(droplet_id)

Check Status of a Droplet Destroy with Associated Resources Request

To check on the status of a request to destroy a Droplet with its associated resources, send a GET request to the `/v2/droplets/$DROPLET_ID/destroy_with_associated_resources/status` endpoint. 

### Example

* Bearer Authentication (bearer_auth):

```python
import time
import openapi_client
from openapi_client.api import droplets_api
from openapi_client.model.associated_resource_status import AssociatedResourceStatus
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
    api_instance = droplets_api.DropletsApi(api_client)
    droplet_id = 3164444 # int | A unique identifier for a Droplet instance.

    # example passing only required values which don't have defaults set
    try:
        # Check Status of a Droplet Destroy with Associated Resources Request
        api_response = api_instance.get_destroy_with_associated_resources_status(droplet_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DropletsApi->get_destroy_with_associated_resources_status: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **droplet_id** | **int**| A unique identifier for a Droplet instance. |

### Return type

[**AssociatedResourceStatus**](AssociatedResourceStatus.md)

### Authorization

[bearer_auth](../README.md#bearer_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A JSON object containing containing the status of a request to destroy a Droplet and its associated resources. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**401** | Unauthorized |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**404** | The resource was not found. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**429** | API Rate limit exceeded |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**500** | Server error. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**0** | Unexpected error |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_droplet**
> bool, date, datetime, dict, float, int, list, str, none_type get_droplet(droplet_id)

Retrieve an Existing Droplet

To show information about an individual Droplet, send a GET request to `/v2/droplets/$DROPLET_ID`. 

### Example

* Bearer Authentication (bearer_auth):

```python
import time
import openapi_client
from openapi_client.api import droplets_api
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
    api_instance = droplets_api.DropletsApi(api_client)
    droplet_id = 3164444 # int | A unique identifier for a Droplet instance.

    # example passing only required values which don't have defaults set
    try:
        # Retrieve an Existing Droplet
        api_response = api_instance.get_droplet(droplet_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DropletsApi->get_droplet: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **droplet_id** | **int**| A unique identifier for a Droplet instance. |

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
**200** | The response will be a JSON object with a key called &#x60;droplet&#x60;. This will be set to a JSON object that contains the standard Droplet attributes.  |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**401** | Unauthorized |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**404** | The resource was not found. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**429** | API Rate limit exceeded |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**500** | Server error. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**0** | Unexpected error |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_all_droplet_neighbors_ids**
> NeighborIds list_all_droplet_neighbors_ids()

List All Droplet Neighbors

To retrieve a list of all Droplets that are co-located on the same physical hardware, send a GET request to `/v2/reports/droplet_neighbors_ids`.  The results will be returned as a JSON object with a key of `neighbor_ids`. This will be set to an array of arrays. Each array will contain a set of Droplet IDs for Droplets that share a physical server. An empty array indicates that all Droplets associated with your account are located on separate physical hardware. 

### Example

* Bearer Authentication (bearer_auth):

```python
import time
import openapi_client
from openapi_client.api import droplets_api
from openapi_client.model.neighbor_ids import NeighborIds
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
    api_instance = droplets_api.DropletsApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # List All Droplet Neighbors
        api_response = api_instance.list_all_droplet_neighbors_ids()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DropletsApi->list_all_droplet_neighbors_ids: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**NeighborIds**](NeighborIds.md)

### Authorization

[bearer_auth](../README.md#bearer_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A JSON object with an &#x60;neighbor_ids&#x60; key. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**401** | Unauthorized |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**404** | The resource was not found. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**429** | API Rate limit exceeded |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**500** | Server error. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**0** | Unexpected error |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_all_droplets**
> bool, date, datetime, dict, float, int, list, str, none_type list_all_droplets()

List All Droplets

To list all Droplets in your account, send a GET request to `/v2/droplets`.  The response body will be a JSON object with a key of `droplets`. This will be set to an array containing objects each representing a Droplet. These will contain the standard Droplet attributes.  ### Filtering Results by Tag  It's possible to request filtered results by including certain query parameters. To only list Droplets assigned to a specific tag, include the `tag_name` query parameter set to the name of the tag in your GET request. For example, `/v2/droplets?tag_name=$TAG_NAME`. 

### Example

* Bearer Authentication (bearer_auth):

```python
import time
import openapi_client
from openapi_client.api import droplets_api
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
    api_instance = droplets_api.DropletsApi(api_client)
    per_page = 2 # int | Number of items returned per page (optional) if omitted the server will use the default value of 20
    page = 1 # int | Which 'page' of paginated results to return. (optional) if omitted the server will use the default value of 1
    tag_name = "env:prod" # str | Used to filter Droplets by a specific tag. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List All Droplets
        api_response = api_instance.list_all_droplets(per_page=per_page, page=page, tag_name=tag_name)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DropletsApi->list_all_droplets: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **per_page** | **int**| Number of items returned per page | [optional] if omitted the server will use the default value of 20
 **page** | **int**| Which &#39;page&#39; of paginated results to return. | [optional] if omitted the server will use the default value of 1
 **tag_name** | **str**| Used to filter Droplets by a specific tag. | [optional]

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
**200** | A JSON object with a key of &#x60;droplets&#x60;. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**401** | Unauthorized |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**429** | API Rate limit exceeded |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**500** | Server error. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**0** | Unexpected error |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_droplet_associated_resources**
> bool, date, datetime, dict, float, int, list, str, none_type list_droplet_associated_resources(droplet_id)

List Associated Resources for a Droplet

To list the associated billable resources that can be destroyed along with a Droplet, send a GET request to the `/v2/droplets/$DROPLET_ID/destroy_with_associated_resources` endpoint.  The response will be a JSON object containing `snapshots`, `volumes`, and `volume_snapshots` keys. Each will be set to an array of objects containing information about the associated resources. 

### Example

* Bearer Authentication (bearer_auth):

```python
import time
import openapi_client
from openapi_client.api import droplets_api
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
    api_instance = droplets_api.DropletsApi(api_client)
    droplet_id = 3164444 # int | A unique identifier for a Droplet instance.

    # example passing only required values which don't have defaults set
    try:
        # List Associated Resources for a Droplet
        api_response = api_instance.list_droplet_associated_resources(droplet_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DropletsApi->list_droplet_associated_resources: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **droplet_id** | **int**| A unique identifier for a Droplet instance. |

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
**200** | A JSON object containing &#x60;snapshots&#x60;, &#x60;volumes&#x60;, and &#x60;volume_snapshots&#x60; keys. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**401** | Unauthorized |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**404** | The resource was not found. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**429** | API Rate limit exceeded |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**500** | Server error. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**0** | Unexpected error |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_droplet_backups**
> bool, date, datetime, dict, float, int, list, str, none_type list_droplet_backups(droplet_id)

List Backups for a Droplet

To retrieve any backups associated with a Droplet, send a GET request to `/v2/droplets/$DROPLET_ID/backups`.  You will get back a JSON object that has a `backups` key. This will be set to an array of backup objects, each of which contain the standard Droplet backup attributes. 

### Example

* Bearer Authentication (bearer_auth):

```python
import time
import openapi_client
from openapi_client.api import droplets_api
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
    api_instance = droplets_api.DropletsApi(api_client)
    droplet_id = 3164444 # int | A unique identifier for a Droplet instance.
    per_page = 2 # int | Number of items returned per page (optional) if omitted the server will use the default value of 20
    page = 1 # int | Which 'page' of paginated results to return. (optional) if omitted the server will use the default value of 1

    # example passing only required values which don't have defaults set
    try:
        # List Backups for a Droplet
        api_response = api_instance.list_droplet_backups(droplet_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DropletsApi->list_droplet_backups: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List Backups for a Droplet
        api_response = api_instance.list_droplet_backups(droplet_id, per_page=per_page, page=page)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DropletsApi->list_droplet_backups: %s\n" % e)
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
**200** | A JSON object with an &#x60;backups&#x60; key. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**401** | Unauthorized |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**404** | The resource was not found. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**429** | API Rate limit exceeded |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**500** | Server error. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**0** | Unexpected error |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_droplet_firewalls**
> bool, date, datetime, dict, float, int, list, str, none_type list_droplet_firewalls(droplet_id)

List all Firewalls Applied to a Droplet

To retrieve a list of all firewalls available to a Droplet, send a GET request to `/v2/droplets/$DROPLET_ID/firewalls`  The response will be a JSON object that has a key called `firewalls`. This will be set to an array of `firewall` objects, each of which contain the standard `firewall` attributes. 

### Example

* Bearer Authentication (bearer_auth):

```python
import time
import openapi_client
from openapi_client.api import droplets_api
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
    api_instance = droplets_api.DropletsApi(api_client)
    droplet_id = 3164444 # int | A unique identifier for a Droplet instance.
    per_page = 2 # int | Number of items returned per page (optional) if omitted the server will use the default value of 20
    page = 1 # int | Which 'page' of paginated results to return. (optional) if omitted the server will use the default value of 1

    # example passing only required values which don't have defaults set
    try:
        # List all Firewalls Applied to a Droplet
        api_response = api_instance.list_droplet_firewalls(droplet_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DropletsApi->list_droplet_firewalls: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List all Firewalls Applied to a Droplet
        api_response = api_instance.list_droplet_firewalls(droplet_id, per_page=per_page, page=page)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DropletsApi->list_droplet_firewalls: %s\n" % e)
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
**200** | A JSON object that has a key called &#x60;firewalls&#x60;. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**401** | Unauthorized |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**404** | The resource was not found. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**429** | API Rate limit exceeded |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**500** | Server error. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**0** | Unexpected error |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_droplet_kernels**
> bool, date, datetime, dict, float, int, list, str, none_type list_droplet_kernels(droplet_id)

List All Available Kernels for a Droplet

To retrieve a list of all kernels available to a Droplet, send a GET request to `/v2/droplets/$DROPLET_ID/kernels`  The response will be a JSON object that has a key called `kernels`. This will be set to an array of `kernel` objects, each of which contain the standard `kernel` attributes. 

### Example

* Bearer Authentication (bearer_auth):

```python
import time
import openapi_client
from openapi_client.api import droplets_api
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
    api_instance = droplets_api.DropletsApi(api_client)
    droplet_id = 3164444 # int | A unique identifier for a Droplet instance.
    per_page = 2 # int | Number of items returned per page (optional) if omitted the server will use the default value of 20
    page = 1 # int | Which 'page' of paginated results to return. (optional) if omitted the server will use the default value of 1

    # example passing only required values which don't have defaults set
    try:
        # List All Available Kernels for a Droplet
        api_response = api_instance.list_droplet_kernels(droplet_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DropletsApi->list_droplet_kernels: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List All Available Kernels for a Droplet
        api_response = api_instance.list_droplet_kernels(droplet_id, per_page=per_page, page=page)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DropletsApi->list_droplet_kernels: %s\n" % e)
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
**200** | A JSON object that has a key called &#x60;kernels&#x60;. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**401** | Unauthorized |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**404** | The resource was not found. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**429** | API Rate limit exceeded |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**500** | Server error. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**0** | Unexpected error |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_droplet_neighbors**
> bool, date, datetime, dict, float, int, list, str, none_type list_droplet_neighbors(droplet_id)

List Neighbors for a Droplet

To retrieve a list of any \"neighbors\" (i.e. Droplets that are co-located on the same physical hardware) for a specific Droplet, send a GET request to `/v2/droplets/$DROPLET_ID/neighbors`.  The results will be returned as a JSON object with a key of `droplets`. This will be set to an array containing objects representing any other Droplets that share the same physical hardware. An empty array indicates that the Droplet is not co-located any other Droplets associated with your account. 

### Example

* Bearer Authentication (bearer_auth):

```python
import time
import openapi_client
from openapi_client.api import droplets_api
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
    api_instance = droplets_api.DropletsApi(api_client)
    droplet_id = 3164444 # int | A unique identifier for a Droplet instance.

    # example passing only required values which don't have defaults set
    try:
        # List Neighbors for a Droplet
        api_response = api_instance.list_droplet_neighbors(droplet_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DropletsApi->list_droplet_neighbors: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **droplet_id** | **int**| A unique identifier for a Droplet instance. |

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
**200** | A JSON object with an &#x60;droplets&#x60; key. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**401** | Unauthorized |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**404** | The resource was not found. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**429** | API Rate limit exceeded |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**500** | Server error. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**0** | Unexpected error |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_droplet_snapshots**
> bool, date, datetime, dict, float, int, list, str, none_type list_droplet_snapshots(droplet_id)

List Snapshots for a Droplet

To retrieve the snapshots that have been created from a Droplet, send a GET request to `/v2/droplets/$DROPLET_ID/snapshots`.  You will get back a JSON object that has a `snapshots` key. This will be set to an array of snapshot objects, each of which contain the standard Droplet snapshot attributes. 

### Example

* Bearer Authentication (bearer_auth):

```python
import time
import openapi_client
from openapi_client.api import droplets_api
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
    api_instance = droplets_api.DropletsApi(api_client)
    droplet_id = 3164444 # int | A unique identifier for a Droplet instance.
    per_page = 2 # int | Number of items returned per page (optional) if omitted the server will use the default value of 20
    page = 1 # int | Which 'page' of paginated results to return. (optional) if omitted the server will use the default value of 1

    # example passing only required values which don't have defaults set
    try:
        # List Snapshots for a Droplet
        api_response = api_instance.list_droplet_snapshots(droplet_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DropletsApi->list_droplet_snapshots: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List Snapshots for a Droplet
        api_response = api_instance.list_droplet_snapshots(droplet_id, per_page=per_page, page=page)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DropletsApi->list_droplet_snapshots: %s\n" % e)
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
**200** | A JSON object with an &#x60;snapshots&#x60; key. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**401** | Unauthorized |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**404** | The resource was not found. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**429** | API Rate limit exceeded |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**500** | Server error. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**0** | Unexpected error |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retry_destroy_with_associated_resource**
> retry_destroy_with_associated_resource(droplet_id)

Retry a Droplet Destroy with Associated Resources Request

If the status of a request to destroy a Droplet with its associated resources reported any errors, it can be retried by sending a POST request to the `/v2/droplets/$DROPLET_ID/destroy_with_associated_resources/retry` endpoint.  Only one destroy can be active at a time per Droplet. If a retry is issued while another destroy is in progress for the Droplet a 409 status code will be returned. A successful response will include a 202 response code and no content. 

### Example

* Bearer Authentication (bearer_auth):

```python
import time
import openapi_client
from openapi_client.api import droplets_api
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
    api_instance = droplets_api.DropletsApi(api_client)
    droplet_id = 3164444 # int | A unique identifier for a Droplet instance.

    # example passing only required values which don't have defaults set
    try:
        # Retry a Droplet Destroy with Associated Resources Request
        api_instance.retry_destroy_with_associated_resource(droplet_id)
    except openapi_client.ApiException as e:
        print("Exception when calling DropletsApi->retry_destroy_with_associated_resource: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **droplet_id** | **int**| A unique identifier for a Droplet instance. |

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
**202** | The does not indicate the success or failure of any operation, just that the request has been accepted for processing. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**401** | Unauthorized |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**404** | The resource was not found. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**409** | Conflict |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**429** | API Rate limit exceeded |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**500** | Server error. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**0** | Unexpected error |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

