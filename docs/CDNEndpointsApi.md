# openapi_client.CDNEndpointsApi

All URIs are relative to *https://api.digitalocean.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_cdn_endpoint**](CDNEndpointsApi.md#create_cdn_endpoint) | **POST** /v2/cdn/endpoints | Create a New CDN Endpoint
[**delete_cdn_endpoint**](CDNEndpointsApi.md#delete_cdn_endpoint) | **DELETE** /v2/cdn/endpoints/{cdn_id} | Delete a CDN Endpoint
[**get_cdn_endpoint**](CDNEndpointsApi.md#get_cdn_endpoint) | **GET** /v2/cdn/endpoints/{cdn_id} | Retrieve an Existing CDN Endpoint
[**list_cdn_endpoints**](CDNEndpointsApi.md#list_cdn_endpoints) | **GET** /v2/cdn/endpoints | List All CDN Endpoints
[**purge_cdn_cache**](CDNEndpointsApi.md#purge_cdn_cache) | **DELETE** /v2/cdn/endpoints/{cdn_id}/cache | Purge the Cache for an Existing CDN Endpoint
[**update_cdn_endpoint**](CDNEndpointsApi.md#update_cdn_endpoint) | **PUT** /v2/cdn/endpoints/{cdn_id} | Update a CDN Endpoint


# **create_cdn_endpoint**
> bool, date, datetime, dict, float, int, list, str, none_type create_cdn_endpoint(cdn_endpoint)

Create a New CDN Endpoint

To create a new CDN endpoint, send a POST request to `/v2/cdn/endpoints`. The origin attribute must be set to the fully qualified domain name (FQDN) of a DigitalOcean Space. Optionally, the TTL may be configured by setting the `ttl` attribute.  A custom subdomain may be configured by specifying the `custom_domain` and `certificate_id` attributes. 

### Example

* Bearer Authentication (bearer_auth):

```python
import time
import openapi_client
from openapi_client.api import cdn_endpoints_api
from openapi_client.model.error import Error
from openapi_client.model.cdn_endpoint import CdnEndpoint
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
    api_instance = cdn_endpoints_api.CDNEndpointsApi(api_client)
    cdn_endpoint = CdnEndpoint(
        origin="static-images.nyc3.digitaloceanspaces.com",
        ttl=3600,
        certificate_id="892071a0-bb95-49bc-8021-3afd67a210bf",
        custom_domain="static.example.com",
    ) # CdnEndpoint | 

    # example passing only required values which don't have defaults set
    try:
        # Create a New CDN Endpoint
        api_response = api_instance.create_cdn_endpoint(cdn_endpoint)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling CDNEndpointsApi->create_cdn_endpoint: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cdn_endpoint** | [**CdnEndpoint**](CdnEndpoint.md)|  |

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
**201** | The response will be a JSON object with an &#x60;endpoint&#x60; key. This will be set to an object containing the standard CDN endpoint attributes. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**401** | Unauthorized |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**429** | API Rate limit exceeded |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**500** | Server error. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**0** | Unexpected error |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_cdn_endpoint**
> delete_cdn_endpoint(cdn_id)

Delete a CDN Endpoint

To delete a specific CDN endpoint, send a DELETE request to `/v2/cdn/endpoints/$ENDPOINT_ID`.  A status of 204 will be given. This indicates that the request was processed successfully, but that no response body is needed. 

### Example

* Bearer Authentication (bearer_auth):

```python
import time
import openapi_client
from openapi_client.api import cdn_endpoints_api
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
    api_instance = cdn_endpoints_api.CDNEndpointsApi(api_client)
    cdn_id = "19f06b6a-3ace-4315-b086-499a0e521b76" # str | A unique identifier for a CDN endpoint.

    # example passing only required values which don't have defaults set
    try:
        # Delete a CDN Endpoint
        api_instance.delete_cdn_endpoint(cdn_id)
    except openapi_client.ApiException as e:
        print("Exception when calling CDNEndpointsApi->delete_cdn_endpoint: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cdn_id** | **str**| A unique identifier for a CDN endpoint. |

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

# **get_cdn_endpoint**
> bool, date, datetime, dict, float, int, list, str, none_type get_cdn_endpoint(cdn_id)

Retrieve an Existing CDN Endpoint

To show information about an existing CDN endpoint, send a GET request to `/v2/cdn/endpoints/$ENDPOINT_ID`.

### Example

* Bearer Authentication (bearer_auth):

```python
import time
import openapi_client
from openapi_client.api import cdn_endpoints_api
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
    api_instance = cdn_endpoints_api.CDNEndpointsApi(api_client)
    cdn_id = "19f06b6a-3ace-4315-b086-499a0e521b76" # str | A unique identifier for a CDN endpoint.

    # example passing only required values which don't have defaults set
    try:
        # Retrieve an Existing CDN Endpoint
        api_response = api_instance.get_cdn_endpoint(cdn_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling CDNEndpointsApi->get_cdn_endpoint: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cdn_id** | **str**| A unique identifier for a CDN endpoint. |

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
**200** | The response will be a JSON object with an &#x60;endpoint&#x60; key. This will be set to an object containing the standard CDN endpoint attributes. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**401** | Unauthorized |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**404** | The resource was not found. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**429** | API Rate limit exceeded |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**500** | Server error. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**0** | Unexpected error |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_cdn_endpoints**
> bool, date, datetime, dict, float, int, list, str, none_type list_cdn_endpoints()

List All CDN Endpoints

To list all of the CDN endpoints available on your account, send a GET request to `/v2/cdn/endpoints`.

### Example

* Bearer Authentication (bearer_auth):

```python
import time
import openapi_client
from openapi_client.api import cdn_endpoints_api
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
    api_instance = cdn_endpoints_api.CDNEndpointsApi(api_client)
    per_page = 2 # int | Number of items returned per page (optional) if omitted the server will use the default value of 20
    page = 1 # int | Which 'page' of paginated results to return. (optional) if omitted the server will use the default value of 1

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List All CDN Endpoints
        api_response = api_instance.list_cdn_endpoints(per_page=per_page, page=page)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling CDNEndpointsApi->list_cdn_endpoints: %s\n" % e)
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
**200** | The result will be a JSON object with an &#x60;endpoints&#x60; key. This will be set to an array of endpoint objects, each of which will contain the standard CDN endpoint attributes. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**401** | Unauthorized |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**429** | API Rate limit exceeded |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**500** | Server error. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**0** | Unexpected error |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **purge_cdn_cache**
> purge_cdn_cache(cdn_id, purge_cache)

Purge the Cache for an Existing CDN Endpoint

To purge cached content from a CDN endpoint, send a DELETE request to `/v2/cdn/endpoints/$ENDPOINT_ID/cache`. The body of the request should include a `files` attribute containing a list of cached file paths to be purged. A path may be for a single file or may contain a wildcard (`*`) to recursively purge all files under a directory. When only a wildcard is provided, all cached files will be purged. 

### Example

* Bearer Authentication (bearer_auth):

```python
import time
import openapi_client
from openapi_client.api import cdn_endpoints_api
from openapi_client.model.purge_cache import PurgeCache
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
    api_instance = cdn_endpoints_api.CDNEndpointsApi(api_client)
    cdn_id = "19f06b6a-3ace-4315-b086-499a0e521b76" # str | A unique identifier for a CDN endpoint.
    purge_cache = PurgeCache(
        files=["path/to/image.png","path/to/css/*"],
    ) # PurgeCache | 

    # example passing only required values which don't have defaults set
    try:
        # Purge the Cache for an Existing CDN Endpoint
        api_instance.purge_cdn_cache(cdn_id, purge_cache)
    except openapi_client.ApiException as e:
        print("Exception when calling CDNEndpointsApi->purge_cdn_cache: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cdn_id** | **str**| A unique identifier for a CDN endpoint. |
 **purge_cache** | [**PurgeCache**](PurgeCache.md)|  |

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

# **update_cdn_endpoint**
> bool, date, datetime, dict, float, int, list, str, none_type update_cdn_endpoint(cdn_id, update_endpoint)

Update a CDN Endpoint

To update the TTL, certificate ID, or the FQDN of the custom subdomain for an existing CDN endpoint, send a PUT request to `/v2/cdn/endpoints/$ENDPOINT_ID`. 

### Example

* Bearer Authentication (bearer_auth):

```python
import time
import openapi_client
from openapi_client.api import cdn_endpoints_api
from openapi_client.model.update_endpoint import UpdateEndpoint
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
    api_instance = cdn_endpoints_api.CDNEndpointsApi(api_client)
    cdn_id = "19f06b6a-3ace-4315-b086-499a0e521b76" # str | A unique identifier for a CDN endpoint.
    update_endpoint = UpdateEndpoint(
        ttl=3600,
        certificate_id="892071a0-bb95-49bc-8021-3afd67a210bf",
        custom_domain="static.example.com",
    ) # UpdateEndpoint | 

    # example passing only required values which don't have defaults set
    try:
        # Update a CDN Endpoint
        api_response = api_instance.update_cdn_endpoint(cdn_id, update_endpoint)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling CDNEndpointsApi->update_cdn_endpoint: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cdn_id** | **str**| A unique identifier for a CDN endpoint. |
 **update_endpoint** | [**UpdateEndpoint**](UpdateEndpoint.md)|  |

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
**202** | The response will be a JSON object with an &#x60;endpoint&#x60; key. This will be set to an object containing the standard CDN endpoint attributes. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**401** | Unauthorized |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**404** | The resource was not found. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**429** | API Rate limit exceeded |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**500** | Server error. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**0** | Unexpected error |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

