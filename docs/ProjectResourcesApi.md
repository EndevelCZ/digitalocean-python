# openapi_client.ProjectResourcesApi

All URIs are relative to *https://api.digitalocean.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**assign_default_project_resources**](ProjectResourcesApi.md#assign_default_project_resources) | **POST** /v2/projects/default/resources | Assign Resources to Default Project
[**assign_project_resources**](ProjectResourcesApi.md#assign_project_resources) | **POST** /v2/projects/{project_id}/resources | Assign Resources to a Project
[**list_default_project_resources**](ProjectResourcesApi.md#list_default_project_resources) | **GET** /v2/projects/default/resources | List Default Project Resources
[**list_project_resources**](ProjectResourcesApi.md#list_project_resources) | **GET** /v2/projects/{project_id}/resources | List Project Resources


# **assign_default_project_resources**
> InlineResponse2006 assign_default_project_resources(project_assignment)

Assign Resources to Default Project

To assign resources to your default project, send a POST request to `/v2/projects/default/resources`.

### Example

* Bearer Authentication (bearer_auth):

```python
import time
import openapi_client
from openapi_client.api import project_resources_api
from openapi_client.model.error import Error
from openapi_client.model.project_assignment import ProjectAssignment
from openapi_client.model.inline_response2006 import InlineResponse2006
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
    api_instance = project_resources_api.ProjectResourcesApi(api_client)
    project_assignment = ProjectAssignment(
        resources=[
            Urn("["do:droplet:13457723"]"),
        ],
    ) # ProjectAssignment | 

    # example passing only required values which don't have defaults set
    try:
        # Assign Resources to Default Project
        api_response = api_instance.assign_default_project_resources(project_assignment)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ProjectResourcesApi->assign_default_project_resources: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_assignment** | [**ProjectAssignment**](ProjectAssignment.md)|  |

### Return type

[**InlineResponse2006**](InlineResponse2006.md)

### Authorization

[bearer_auth](../README.md#bearer_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The response will be a JSON object with a key called &#x60;resources&#x60;. The value of this will be an object with the standard resource attributes. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**401** | Unauthorized |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**404** | The resource was not found. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**429** | API Rate limit exceeded |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**500** | Server error. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**0** | Unexpected error |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **assign_project_resources**
> InlineResponse2006 assign_project_resources(project_id, project_assignment)

Assign Resources to a Project

To assign resources to a project, send a POST request to `/v2/projects/$PROJECT_ID/resources`.

### Example

* Bearer Authentication (bearer_auth):

```python
import time
import openapi_client
from openapi_client.api import project_resources_api
from openapi_client.model.error import Error
from openapi_client.model.project_assignment import ProjectAssignment
from openapi_client.model.inline_response2006 import InlineResponse2006
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
    api_instance = project_resources_api.ProjectResourcesApi(api_client)
    project_id = "4de7ac8b-495b-4884-9a69-1050c6793cd6" # str | A unique identifier for a project.
    project_assignment = ProjectAssignment(
        resources=[
            Urn("["do:droplet:13457723"]"),
        ],
    ) # ProjectAssignment | 

    # example passing only required values which don't have defaults set
    try:
        # Assign Resources to a Project
        api_response = api_instance.assign_project_resources(project_id, project_assignment)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ProjectResourcesApi->assign_project_resources: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| A unique identifier for a project. |
 **project_assignment** | [**ProjectAssignment**](ProjectAssignment.md)|  |

### Return type

[**InlineResponse2006**](InlineResponse2006.md)

### Authorization

[bearer_auth](../README.md#bearer_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The response will be a JSON object with a key called &#x60;resources&#x60;. The value of this will be an object with the standard resource attributes. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**401** | Unauthorized |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**404** | The resource was not found. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**429** | API Rate limit exceeded |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**500** | Server error. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**0** | Unexpected error |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_default_project_resources**
> bool, date, datetime, dict, float, int, list, str, none_type list_default_project_resources()

List Default Project Resources

To list all your resources in your default project, send a GET request to `/v2/projects/default/resources`.

### Example

* Bearer Authentication (bearer_auth):

```python
import time
import openapi_client
from openapi_client.api import project_resources_api
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
    api_instance = project_resources_api.ProjectResourcesApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # List Default Project Resources
        api_response = api_instance.list_default_project_resources()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ProjectResourcesApi->list_default_project_resources: %s\n" % e)
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
**200** | The response will be a JSON object with a key called &#x60;resources&#x60;. The value of this will be an object with the standard resource attributes. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**401** | Unauthorized |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**404** | The resource was not found. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**429** | API Rate limit exceeded |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**500** | Server error. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**0** | Unexpected error |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_project_resources**
> bool, date, datetime, dict, float, int, list, str, none_type list_project_resources(project_id)

List Project Resources

To list all your resources in a project, send a GET request to `/v2/projects/$PROJECT_ID/resources`.

### Example

* Bearer Authentication (bearer_auth):

```python
import time
import openapi_client
from openapi_client.api import project_resources_api
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
    api_instance = project_resources_api.ProjectResourcesApi(api_client)
    project_id = "4de7ac8b-495b-4884-9a69-1050c6793cd6" # str | A unique identifier for a project.

    # example passing only required values which don't have defaults set
    try:
        # List Project Resources
        api_response = api_instance.list_project_resources(project_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ProjectResourcesApi->list_project_resources: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| A unique identifier for a project. |

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
**200** | The response will be a JSON object with a key called &#x60;resources&#x60;. The value of this will be an object with the standard resource attributes. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**401** | Unauthorized |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**404** | The resource was not found. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**429** | API Rate limit exceeded |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**500** | Server error. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**0** | Unexpected error |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

