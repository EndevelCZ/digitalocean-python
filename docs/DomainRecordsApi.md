# digitalocean_client.DomainRecordsApi

All URIs are relative to *https://api.digitalocean.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_domain_record**](DomainRecordsApi.md#create_domain_record) | **POST** /v2/domains/{domain_name}/records | Create a New Domain Record
[**delete_domain_record**](DomainRecordsApi.md#delete_domain_record) | **DELETE** /v2/domains/{domain_name}/records/{domain_record_id} | Delete a Domain Record
[**get_domain_record**](DomainRecordsApi.md#get_domain_record) | **GET** /v2/domains/{domain_name}/records/{domain_record_id} | Retrieve an Existing Domain Record
[**list_all_domain_records**](DomainRecordsApi.md#list_all_domain_records) | **GET** /v2/domains/{domain_name}/records | List All Domain Records
[**patch_update_domain_record**](DomainRecordsApi.md#patch_update_domain_record) | **PATCH** /v2/domains/{domain_name}/records/{domain_record_id} | Update a Domain Record
[**update_domain_record**](DomainRecordsApi.md#update_domain_record) | **PUT** /v2/domains/{domain_name}/records/{domain_record_id} | Update a Domain Record


# **create_domain_record**
> bool, date, datetime, dict, float, int, list, str, none_type create_domain_record(domain_name)

Create a New Domain Record

To create a new record to a domain, send a POST request to `/v2/domains/$DOMAIN_NAME/records`.  The request must include all of the required fields for the domain record type being added.  See the [attribute table](#tag/Domain-Records) for details regarding record types and their respective required attributes. 

### Example

* Bearer Authentication (bearer_auth):

```python
import time
import digitalocean_client
from digitalocean_client.api import domain_records_api
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
    api_instance = domain_records_api.DomainRecordsApi(api_client)
    domain_name = "example.com" # str | The name of the domain itself.
    unknown_base_type = None # UNKNOWN_BASE_TYPE |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Create a New Domain Record
        api_response = api_instance.create_domain_record(domain_name)
        pprint(api_response)
    except digitalocean_client.ApiException as e:
        print("Exception when calling DomainRecordsApi->create_domain_record: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create a New Domain Record
        api_response = api_instance.create_domain_record(domain_name, unknown_base_type=unknown_base_type)
        pprint(api_response)
    except digitalocean_client.ApiException as e:
        print("Exception when calling DomainRecordsApi->create_domain_record: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain_name** | **str**| The name of the domain itself. |
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
**201** | The response body will be a JSON object with a key called &#x60;domain_record&#x60;. The value of this will be an object representing the new record. Attributes that are not applicable for the record type will be set to &#x60;null&#x60;. An &#x60;id&#x60; attribute is generated for each record as part of the object. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**401** | Unauthorized |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**404** | The resource was not found. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**429** | API Rate limit exceeded |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**500** | Server error. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**0** | Unexpected error |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_domain_record**
> delete_domain_record(domain_name, domain_record_id)

Delete a Domain Record

To delete a record for a domain, send a DELETE request to `/v2/domains/$DOMAIN_NAME/records/$DOMAIN_RECORD_ID`.  The record will be deleted and the response status will be a 204. This indicates a successful request with no body returned. 

### Example

* Bearer Authentication (bearer_auth):

```python
import time
import digitalocean_client
from digitalocean_client.api import domain_records_api
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
    api_instance = domain_records_api.DomainRecordsApi(api_client)
    domain_name = "example.com" # str | The name of the domain itself.
    domain_record_id = 3352896 # int | The unique identifier of the domain record.

    # example passing only required values which don't have defaults set
    try:
        # Delete a Domain Record
        api_instance.delete_domain_record(domain_name, domain_record_id)
    except digitalocean_client.ApiException as e:
        print("Exception when calling DomainRecordsApi->delete_domain_record: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain_name** | **str**| The name of the domain itself. |
 **domain_record_id** | **int**| The unique identifier of the domain record. |

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

# **get_domain_record**
> bool, date, datetime, dict, float, int, list, str, none_type get_domain_record(domain_name, domain_record_id)

Retrieve an Existing Domain Record

To retrieve a specific domain record, send a GET request to `/v2/domains/$DOMAIN_NAME/records/$RECORD_ID`.

### Example

* Bearer Authentication (bearer_auth):

```python
import time
import digitalocean_client
from digitalocean_client.api import domain_records_api
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
    api_instance = domain_records_api.DomainRecordsApi(api_client)
    domain_name = "example.com" # str | The name of the domain itself.
    domain_record_id = 3352896 # int | The unique identifier of the domain record.

    # example passing only required values which don't have defaults set
    try:
        # Retrieve an Existing Domain Record
        api_response = api_instance.get_domain_record(domain_name, domain_record_id)
        pprint(api_response)
    except digitalocean_client.ApiException as e:
        print("Exception when calling DomainRecordsApi->get_domain_record: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain_name** | **str**| The name of the domain itself. |
 **domain_record_id** | **int**| The unique identifier of the domain record. |

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
**200** | The response will be a JSON object with a key called &#x60;domain_record&#x60;. The value of this will be a domain record object which contains the standard domain record attributes. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**401** | Unauthorized |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**404** | The resource was not found. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**429** | API Rate limit exceeded |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**500** | Server error. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**0** | Unexpected error |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_all_domain_records**
> bool, date, datetime, dict, float, int, list, str, none_type list_all_domain_records(domain_name)

List All Domain Records

To get a listing of all records configured for a domain, send a GET request to `/v2/domains/$DOMAIN_NAME/records`. The list of records returned can be filtered by using the `name` and `type` query parameters. For example, to only include A records for a domain, send a GET request to `/v2/domains/$DOMAIN_NAME/records?type=A`. `name` must be a fully qualified record name. For example, to only include records matching `sub.example.com`, send a GET request to `/v2/domains/$DOMAIN_NAME/records?name=sub.example.com`. Both name and type may be used together.  

### Example

* Bearer Authentication (bearer_auth):

```python
import time
import digitalocean_client
from digitalocean_client.api import domain_records_api
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
    api_instance = domain_records_api.DomainRecordsApi(api_client)
    domain_name = "example.com" # str | The name of the domain itself.
    name = "sub.example.com" # str | A fully qualified record name. For example, to only include records matching sub.example.com, send a GET request to `/v2/domains/$DOMAIN_NAME/records?name=sub.example.com`. (optional)
    type = "A" # str | The type of the DNS record. For example: A, CNAME, TXT, ... (optional)

    # example passing only required values which don't have defaults set
    try:
        # List All Domain Records
        api_response = api_instance.list_all_domain_records(domain_name)
        pprint(api_response)
    except digitalocean_client.ApiException as e:
        print("Exception when calling DomainRecordsApi->list_all_domain_records: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List All Domain Records
        api_response = api_instance.list_all_domain_records(domain_name, name=name, type=type)
        pprint(api_response)
    except digitalocean_client.ApiException as e:
        print("Exception when calling DomainRecordsApi->list_all_domain_records: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain_name** | **str**| The name of the domain itself. |
 **name** | **str**| A fully qualified record name. For example, to only include records matching sub.example.com, send a GET request to &#x60;/v2/domains/$DOMAIN_NAME/records?name&#x3D;sub.example.com&#x60;. | [optional]
 **type** | **str**| The type of the DNS record. For example: A, CNAME, TXT, ... | [optional]

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
**200** | The response will be a JSON object with a key called &#x60;domain_records&#x60;. The value of this will be an array of domain record objects, each of which contains the standard domain record attributes. For attributes that are not used by a specific record type, a value of &#x60;null&#x60; will be returned. For instance, all records other than SRV will have &#x60;null&#x60; for the &#x60;weight&#x60; and &#x60;port&#x60; attributes. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**401** | Unauthorized |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**404** | The resource was not found. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**429** | API Rate limit exceeded |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**500** | Server error. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**0** | Unexpected error |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_update_domain_record**
> bool, date, datetime, dict, float, int, list, str, none_type patch_update_domain_record(domain_name, domain_record_id)

Update a Domain Record

To update an existing record, send a PATCH request to `/v2/domains/$DOMAIN_NAME/records/$DOMAIN_RECORD_ID`. Any attribute valid for the record type can be set to a new value for the record.  See the [attribute table](#tag/Domain-Records) for details regarding record types and their respective attributes. 

### Example

* Bearer Authentication (bearer_auth):

```python
import time
import digitalocean_client
from digitalocean_client.api import domain_records_api
from digitalocean_client.model.error import Error
from digitalocean_client.model.domain_record import DomainRecord
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
    api_instance = domain_records_api.DomainRecordsApi(api_client)
    domain_name = "example.com" # str | The name of the domain itself.
    domain_record_id = 3352896 # int | The unique identifier of the domain record.
    domain_record = DomainRecord(
        type="NS",
        name="@",
        data="ns1.digitalocean.com",
        priority=1,
        port=1,
        ttl=1800,
        weight=1,
        flags=1,
        tag="tag_example",
    ) # DomainRecord |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update a Domain Record
        api_response = api_instance.patch_update_domain_record(domain_name, domain_record_id)
        pprint(api_response)
    except digitalocean_client.ApiException as e:
        print("Exception when calling DomainRecordsApi->patch_update_domain_record: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update a Domain Record
        api_response = api_instance.patch_update_domain_record(domain_name, domain_record_id, domain_record=domain_record)
        pprint(api_response)
    except digitalocean_client.ApiException as e:
        print("Exception when calling DomainRecordsApi->patch_update_domain_record: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain_name** | **str**| The name of the domain itself. |
 **domain_record_id** | **int**| The unique identifier of the domain record. |
 **domain_record** | [**DomainRecord**](DomainRecord.md)|  | [optional]

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
**200** | The response will be a JSON object with a key called &#x60;domain_record&#x60;. The value of this will be a domain record object which contains the standard domain record attributes. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**401** | Unauthorized |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**404** | The resource was not found. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**429** | API Rate limit exceeded |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**500** | Server error. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**0** | Unexpected error |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_domain_record**
> bool, date, datetime, dict, float, int, list, str, none_type update_domain_record(domain_name, domain_record_id)

Update a Domain Record

To update an existing record, send a PUT request to `/v2/domains/$DOMAIN_NAME/records/$DOMAIN_RECORD_ID`. Any attribute valid for the record type can be set to a new value for the record.  See the [attribute table](#tag/Domain-Records) for details regarding record types and their respective attributes. 

### Example

* Bearer Authentication (bearer_auth):

```python
import time
import digitalocean_client
from digitalocean_client.api import domain_records_api
from digitalocean_client.model.error import Error
from digitalocean_client.model.domain_record import DomainRecord
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
    api_instance = domain_records_api.DomainRecordsApi(api_client)
    domain_name = "example.com" # str | The name of the domain itself.
    domain_record_id = 3352896 # int | The unique identifier of the domain record.
    domain_record = DomainRecord(
        type="NS",
        name="@",
        data="ns1.digitalocean.com",
        priority=1,
        port=1,
        ttl=1800,
        weight=1,
        flags=1,
        tag="tag_example",
    ) # DomainRecord |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update a Domain Record
        api_response = api_instance.update_domain_record(domain_name, domain_record_id)
        pprint(api_response)
    except digitalocean_client.ApiException as e:
        print("Exception when calling DomainRecordsApi->update_domain_record: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update a Domain Record
        api_response = api_instance.update_domain_record(domain_name, domain_record_id, domain_record=domain_record)
        pprint(api_response)
    except digitalocean_client.ApiException as e:
        print("Exception when calling DomainRecordsApi->update_domain_record: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain_name** | **str**| The name of the domain itself. |
 **domain_record_id** | **int**| The unique identifier of the domain record. |
 **domain_record** | [**DomainRecord**](DomainRecord.md)|  | [optional]

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
**200** | The response will be a JSON object with a key called &#x60;domain_record&#x60;. The value of this will be a domain record object which contains the standard domain record attributes. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**401** | Unauthorized |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**404** | The resource was not found. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**429** | API Rate limit exceeded |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**500** | Server error. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**0** | Unexpected error |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

