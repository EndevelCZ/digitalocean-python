# digitalocean_client.AppsApi

All URIs are relative to *https://api.digitalocean.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**assign_alert_destinations**](AppsApi.md#assign_alert_destinations) | **POST** /v2/apps/{app_id}/alerts/{alert_id}/destinations | Update destinations for alerts
[**create_app**](AppsApi.md#create_app) | **POST** /v2/apps | Create a New App
[**create_deployment**](AppsApi.md#create_deployment) | **POST** /v2/apps/{app_id}/deployments | Create an App Deployment
[**delete_app**](AppsApi.md#delete_app) | **DELETE** /v2/apps/{id} | Delete an App
[**get_app**](AppsApi.md#get_app) | **GET** /v2/apps/{id} | Retrieve an Existing App
[**get_deployment**](AppsApi.md#get_deployment) | **GET** /v2/apps/{app_id}/deployments/{deployment_id} | Retrieve an App Deployment
[**get_instance_size**](AppsApi.md#get_instance_size) | **GET** /v2/apps/tiers/instance_sizes/{slug} | Retrieve an Instance Size
[**get_logs**](AppsApi.md#get_logs) | **GET** /v2/apps/{app_id}/deployments/{deployment_id}/components/{component_name}/logs | Retrieve Deployment Logs
[**get_logs_aggregate**](AppsApi.md#get_logs_aggregate) | **GET** /v2/apps/{app_id}/deployments/{deployment_id}/logs | Retrieve Aggregate Deployment Logs
[**get_tier**](AppsApi.md#get_tier) | **GET** /v2/apps/tiers/{slug} | Retrieve an App Tier
[**list_alerts**](AppsApi.md#list_alerts) | **GET** /v2/apps/{app_id}/alerts | List all app alerts
[**list_apps**](AppsApi.md#list_apps) | **GET** /v2/apps | List All Apps
[**list_deployments**](AppsApi.md#list_deployments) | **GET** /v2/apps/{app_id}/deployments | List App Deployments
[**list_instance_sizes**](AppsApi.md#list_instance_sizes) | **GET** /v2/apps/tiers/instance_sizes | List Instance Sizes
[**list_regions**](AppsApi.md#list_regions) | **GET** /v2/apps/regions | List App Regions
[**list_tiers**](AppsApi.md#list_tiers) | **GET** /v2/apps/tiers | List App Tiers
[**post_cancel_deployment**](AppsApi.md#post_cancel_deployment) | **POST** /v2/apps/{app_id}/deployments/{deployment_id}/cancel | Cancel a Deployment
[**update_app**](AppsApi.md#update_app) | **PUT** /v2/apps/{id} | Update an App
[**validate_app_spec**](AppsApi.md#validate_app_spec) | **POST** /v2/apps/propose | Propose an App Spec


# **assign_alert_destinations**
> AppsAlertResponse assign_alert_destinations(app_id, alert_id, apps_assign_app_alert_destinations_request)

Update destinations for alerts

Updates the emails and slack webhook destinations for app alerts. Emails must be associated to a user with access to the app.

### Example

* Bearer Authentication (bearer_auth):

```python
import time
import digitalocean_client
from digitalocean_client.api import apps_api
from digitalocean_client.model.error import Error
from digitalocean_client.model.apps_assign_app_alert_destinations_request import AppsAssignAppAlertDestinationsRequest
from digitalocean_client.model.apps_alert_response import AppsAlertResponse
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
    api_instance = apps_api.AppsApi(api_client)
    app_id = "4f6c71e2-1e90-4762-9fee-6cc4a0a9f2cf" # str | The app ID
    alert_id = "5a624ab5-dd58-4b39-b7dd-8b7c36e8a91d" # str | The alert ID
    apps_assign_app_alert_destinations_request = AppsAssignAppAlertDestinationsRequest(
        emails=["sammy@digitalocean.com"],
        slack_webhooks=[
            AppAlertSlackWebhook(
                url="https://hooks.slack.com/services/T00000000/B00000000/XXXXXXXXXXXXXXXXXXXXXXXX",
                channel="Channel Name",
            ),
        ],
    ) # AppsAssignAppAlertDestinationsRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Update destinations for alerts
        api_response = api_instance.assign_alert_destinations(app_id, alert_id, apps_assign_app_alert_destinations_request)
        pprint(api_response)
    except digitalocean_client.ApiException as e:
        print("Exception when calling AppsApi->assign_alert_destinations: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**| The app ID |
 **alert_id** | **str**| The alert ID |
 **apps_assign_app_alert_destinations_request** | [**AppsAssignAppAlertDestinationsRequest**](AppsAssignAppAlertDestinationsRequest.md)|  |

### Return type

[**AppsAlertResponse**](AppsAlertResponse.md)

### Authorization

[bearer_auth](../README.md#bearer_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A JSON object with an &#x60;alert&#x60; key. This is an object of type &#x60;alert&#x60;. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**401** | Unauthorized |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**404** | The resource was not found. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**429** | API Rate limit exceeded |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**500** | Server error. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**0** | Unexpected error |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_app**
> AppResponse create_app(apps_create_app_request)

Create a New App

Create a new app by submitting an app specification. For documentation on app specifications (`AppSpec` objects), please refer to [the product documentation](https://www.digitalocean.com/docs/app-platform/references/app-specification-reference/).

### Example

* Bearer Authentication (bearer_auth):

```python
import time
import digitalocean_client
from digitalocean_client.api import apps_api
from digitalocean_client.model.app_response import AppResponse
from digitalocean_client.model.error import Error
from digitalocean_client.model.apps_create_app_request import AppsCreateAppRequest
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
    api_instance = apps_api.AppsApi(api_client)
    apps_create_app_request = AppsCreateAppRequest(
        spec=AppSpec(
            name="web-app-01",
            region="nyc",
            domains=[
                AppDomainSpec(
                    domain="app.example.com",
                    type="DEFAULT",
                    wildcard=True,
                    zone="example.com",
                ),
            ],
            services=[
                AppServiceSpec(None),
            ],
            static_sites=[
                AppStaticSiteSpec(None),
            ],
            jobs=[
                AppJobSpec(None),
            ],
            workers=[
                AppWorkerSpec(None),
            ],
            databases=[
                AppDatabaseSpec(
                    cluster_name="cluster_name",
                    db_name="my_db",
                    db_user="superuser",
                    engine="PG",
                    name="prod-db",
                    production=True,
                    version="12",
                ),
            ],
        ),
    ) # AppsCreateAppRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Create a New App
        api_response = api_instance.create_app(apps_create_app_request)
        pprint(api_response)
    except digitalocean_client.ApiException as e:
        print("Exception when calling AppsApi->create_app: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **apps_create_app_request** | [**AppsCreateAppRequest**](AppsCreateAppRequest.md)|  |

### Return type

[**AppResponse**](AppResponse.md)

### Authorization

[bearer_auth](../README.md#bearer_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A JSON of a &#x60;spec&#x60; object. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**401** | Unauthorized |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**429** | API Rate limit exceeded |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**500** | Server error. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**0** | Unexpected error |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_deployment**
> AppsDeploymentResponse create_deployment(app_id, apps_create_deployment_request)

Create an App Deployment

Creating an app deployment will pull the latest changes from your repository and schedule a new deployment for your app.

### Example

* Bearer Authentication (bearer_auth):

```python
import time
import digitalocean_client
from digitalocean_client.api import apps_api
from digitalocean_client.model.apps_create_deployment_request import AppsCreateDeploymentRequest
from digitalocean_client.model.error import Error
from digitalocean_client.model.apps_deployment_response import AppsDeploymentResponse
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
    api_instance = apps_api.AppsApi(api_client)
    app_id = "4f6c71e2-1e90-4762-9fee-6cc4a0a9f2cf" # str | The app ID
    apps_create_deployment_request = AppsCreateDeploymentRequest(
        force_build=True,
    ) # AppsCreateDeploymentRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Create an App Deployment
        api_response = api_instance.create_deployment(app_id, apps_create_deployment_request)
        pprint(api_response)
    except digitalocean_client.ApiException as e:
        print("Exception when calling AppsApi->create_deployment: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**| The app ID |
 **apps_create_deployment_request** | [**AppsCreateDeploymentRequest**](AppsCreateDeploymentRequest.md)|  |

### Return type

[**AppsDeploymentResponse**](AppsDeploymentResponse.md)

### Authorization

[bearer_auth](../README.md#bearer_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A JSON object with a &#x60;deployment&#x60; key. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**401** | Unauthorized |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**404** | The resource was not found. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**429** | API Rate limit exceeded |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**500** | Server error. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**0** | Unexpected error |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_app**
> AppsDeleteAppResponse delete_app(id)

Delete an App

Delete an existing app. Once deleted, all active deployments will be permanently shut down and the app deleted. If needed, be sure to back up your app specification so that you may re-create it at a later time.

### Example

* Bearer Authentication (bearer_auth):

```python
import time
import digitalocean_client
from digitalocean_client.api import apps_api
from digitalocean_client.model.error import Error
from digitalocean_client.model.apps_delete_app_response import AppsDeleteAppResponse
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
    api_instance = apps_api.AppsApi(api_client)
    id = "4f6c71e2-1e90-4762-9fee-6cc4a0a9f2cf" # str | The ID of the app

    # example passing only required values which don't have defaults set
    try:
        # Delete an App
        api_response = api_instance.delete_app(id)
        pprint(api_response)
    except digitalocean_client.ApiException as e:
        print("Exception when calling AppsApi->delete_app: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the app |

### Return type

[**AppsDeleteAppResponse**](AppsDeleteAppResponse.md)

### Authorization

[bearer_auth](../README.md#bearer_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | the ID of the app deleted. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**401** | Unauthorized |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**404** | The resource was not found. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**429** | API Rate limit exceeded |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**500** | Server error. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**0** | Unexpected error |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_app**
> AppResponse get_app(id)

Retrieve an Existing App

Retrieve details about an existing app by either its ID or name. To retrieve an app by its name, do not include an ID in the request path. Information about the current active deployment as well as any in progress ones will also be included in the response.

### Example

* Bearer Authentication (bearer_auth):

```python
import time
import digitalocean_client
from digitalocean_client.api import apps_api
from digitalocean_client.model.app_response import AppResponse
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
    api_instance = apps_api.AppsApi(api_client)
    id = "4f6c71e2-1e90-4762-9fee-6cc4a0a9f2cf" # str | The ID of the app
    name = "myApp" # str | The name of the app to retrieve. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Retrieve an Existing App
        api_response = api_instance.get_app(id)
        pprint(api_response)
    except digitalocean_client.ApiException as e:
        print("Exception when calling AppsApi->get_app: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Retrieve an Existing App
        api_response = api_instance.get_app(id, name=name)
        pprint(api_response)
    except digitalocean_client.ApiException as e:
        print("Exception when calling AppsApi->get_app: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the app |
 **name** | **str**| The name of the app to retrieve. | [optional]

### Return type

[**AppResponse**](AppResponse.md)

### Authorization

[bearer_auth](../README.md#bearer_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A JSON with key &#x60;app&#x60; |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**401** | Unauthorized |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**404** | The resource was not found. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**429** | API Rate limit exceeded |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**500** | Server error. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**0** | Unexpected error |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_deployment**
> AppsDeploymentResponse get_deployment(app_id, deployment_id)

Retrieve an App Deployment

Retrieve information about an app deployment.

### Example

* Bearer Authentication (bearer_auth):

```python
import time
import digitalocean_client
from digitalocean_client.api import apps_api
from digitalocean_client.model.error import Error
from digitalocean_client.model.apps_deployment_response import AppsDeploymentResponse
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
    api_instance = apps_api.AppsApi(api_client)
    app_id = "4f6c71e2-1e90-4762-9fee-6cc4a0a9f2cf" # str | The app ID
    deployment_id = "3aa4d20e-5527-4c00-b496-601fbd22520a" # str | The deployment ID

    # example passing only required values which don't have defaults set
    try:
        # Retrieve an App Deployment
        api_response = api_instance.get_deployment(app_id, deployment_id)
        pprint(api_response)
    except digitalocean_client.ApiException as e:
        print("Exception when calling AppsApi->get_deployment: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**| The app ID |
 **deployment_id** | **str**| The deployment ID |

### Return type

[**AppsDeploymentResponse**](AppsDeploymentResponse.md)

### Authorization

[bearer_auth](../README.md#bearer_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A JSON of the requested deployment |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**401** | Unauthorized |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**404** | The resource was not found. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**429** | API Rate limit exceeded |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**500** | Server error. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**0** | Unexpected error |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_instance_size**
> AppsGetInstanceSizeResponse get_instance_size(slug)

Retrieve an Instance Size

Retrieve information about a specific instance size for `service`, `worker`, and `job` components.

### Example

* Bearer Authentication (bearer_auth):

```python
import time
import digitalocean_client
from digitalocean_client.api import apps_api
from digitalocean_client.model.error import Error
from digitalocean_client.model.apps_get_instance_size_response import AppsGetInstanceSizeResponse
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
    api_instance = apps_api.AppsApi(api_client)
    slug = "basic-xxs" # str | The slug of the instance size

    # example passing only required values which don't have defaults set
    try:
        # Retrieve an Instance Size
        api_response = api_instance.get_instance_size(slug)
        pprint(api_response)
    except digitalocean_client.ApiException as e:
        print("Exception when calling AppsApi->get_instance_size: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **slug** | **str**| The slug of the instance size |

### Return type

[**AppsGetInstanceSizeResponse**](AppsGetInstanceSizeResponse.md)

### Authorization

[bearer_auth](../README.md#bearer_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A JSON with key &#x60;instance_size&#x60; |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**401** | Unauthorized |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**404** | The resource was not found. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**429** | API Rate limit exceeded |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**500** | Server error. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**0** | Unexpected error |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_logs**
> AppsGetLogsResponse get_logs(app_id, deployment_id, component_name, )

Retrieve Deployment Logs

Retrieve the logs of a past, in-progress, or active deployment. If a component name is specified, the logs will be limited to only that component. The response will include links to either real-time logs of an in-progress or active deployment or archived logs of a past deployment.

### Example

* Bearer Authentication (bearer_auth):

```python
import time
import digitalocean_client
from digitalocean_client.api import apps_api
from digitalocean_client.model.apps_get_logs_response import AppsGetLogsResponse
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
    api_instance = apps_api.AppsApi(api_client)
    app_id = "4f6c71e2-1e90-4762-9fee-6cc4a0a9f2cf" # str | The app ID
    deployment_id = "3aa4d20e-5527-4c00-b496-601fbd22520a" # str | The deployment ID
    component_name = "component" # str | An optional component name. If set, logs will be limited to this component only.
    follow = True # bool | Whether the logs should follow live updates. (optional)
    pod_connection_timeout = "3m" # str | An optional time duration to wait if the underlying component instance is not immediately available. Default: `3m`. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Retrieve Deployment Logs
        api_response = api_instance.get_logs(app_id, deployment_id, component_name, )
        pprint(api_response)
    except digitalocean_client.ApiException as e:
        print("Exception when calling AppsApi->get_logs: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Retrieve Deployment Logs
        api_response = api_instance.get_logs(app_id, deployment_id, component_name, follow=follow, pod_connection_timeout=pod_connection_timeout)
        pprint(api_response)
    except digitalocean_client.ApiException as e:
        print("Exception when calling AppsApi->get_logs: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**| The app ID |
 **deployment_id** | **str**| The deployment ID |
 **component_name** | **str**| An optional component name. If set, logs will be limited to this component only. |
 **type** | **str**| The type of logs to retrieve - BUILD: Build-time logs - DEPLOY: Deploy-time logs - RUN: Live run-time logs | defaults to "UNSPECIFIED"
 **follow** | **bool**| Whether the logs should follow live updates. | [optional]
 **pod_connection_timeout** | **str**| An optional time duration to wait if the underlying component instance is not immediately available. Default: &#x60;3m&#x60;. | [optional]

### Return type

[**AppsGetLogsResponse**](AppsGetLogsResponse.md)

### Authorization

[bearer_auth](../README.md#bearer_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A JSON object with urls that point to archived logs |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**401** | Unauthorized |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**404** | The resource was not found. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**429** | API Rate limit exceeded |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**500** | Server error. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**0** | Unexpected error |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_logs_aggregate**
> AppsGetLogsResponse get_logs_aggregate(app_id, deployment_id, )

Retrieve Aggregate Deployment Logs

Retrieve the logs of a past, in-progress, or active deployment. If a component name is specified, the logs will be limited to only that component. The response will include links to either real-time logs of an in-progress or active deployment or archived logs of a past deployment.

### Example

* Bearer Authentication (bearer_auth):

```python
import time
import digitalocean_client
from digitalocean_client.api import apps_api
from digitalocean_client.model.apps_get_logs_response import AppsGetLogsResponse
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
    api_instance = apps_api.AppsApi(api_client)
    app_id = "4f6c71e2-1e90-4762-9fee-6cc4a0a9f2cf" # str | The app ID
    deployment_id = "3aa4d20e-5527-4c00-b496-601fbd22520a" # str | The deployment ID
    follow = True # bool | Whether the logs should follow live updates. (optional)
    pod_connection_timeout = "3m" # str | An optional time duration to wait if the underlying component instance is not immediately available. Default: `3m`. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Retrieve Aggregate Deployment Logs
        api_response = api_instance.get_logs_aggregate(app_id, deployment_id, )
        pprint(api_response)
    except digitalocean_client.ApiException as e:
        print("Exception when calling AppsApi->get_logs_aggregate: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Retrieve Aggregate Deployment Logs
        api_response = api_instance.get_logs_aggregate(app_id, deployment_id, follow=follow, pod_connection_timeout=pod_connection_timeout)
        pprint(api_response)
    except digitalocean_client.ApiException as e:
        print("Exception when calling AppsApi->get_logs_aggregate: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**| The app ID |
 **deployment_id** | **str**| The deployment ID |
 **type** | **str**| The type of logs to retrieve - BUILD: Build-time logs - DEPLOY: Deploy-time logs - RUN: Live run-time logs | defaults to "UNSPECIFIED"
 **follow** | **bool**| Whether the logs should follow live updates. | [optional]
 **pod_connection_timeout** | **str**| An optional time duration to wait if the underlying component instance is not immediately available. Default: &#x60;3m&#x60;. | [optional]

### Return type

[**AppsGetLogsResponse**](AppsGetLogsResponse.md)

### Authorization

[bearer_auth](../README.md#bearer_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A JSON object with urls that point to archived logs |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**401** | Unauthorized |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**404** | The resource was not found. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**429** | API Rate limit exceeded |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**500** | Server error. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**0** | Unexpected error |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tier**
> AppsGetTierResponse get_tier(slug)

Retrieve an App Tier

Retrieve information about a specific app tier.

### Example

* Bearer Authentication (bearer_auth):

```python
import time
import digitalocean_client
from digitalocean_client.api import apps_api
from digitalocean_client.model.apps_get_tier_response import AppsGetTierResponse
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
    api_instance = apps_api.AppsApi(api_client)
    slug = "basic" # str | The slug of the tier

    # example passing only required values which don't have defaults set
    try:
        # Retrieve an App Tier
        api_response = api_instance.get_tier(slug)
        pprint(api_response)
    except digitalocean_client.ApiException as e:
        print("Exception when calling AppsApi->get_tier: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **slug** | **str**| The slug of the tier |

### Return type

[**AppsGetTierResponse**](AppsGetTierResponse.md)

### Authorization

[bearer_auth](../README.md#bearer_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A JSON with the key &#x60;tier&#x60; |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**401** | Unauthorized |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**404** | The resource was not found. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**429** | API Rate limit exceeded |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**500** | Server error. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**0** | Unexpected error |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_alerts**
> AppsListAlertsResponse list_alerts(app_id)

List all app alerts

List alerts associated to the app and any components. This includes configuration information about the alerts including emails, slack webhooks, and triggering events or conditions.

### Example

* Bearer Authentication (bearer_auth):

```python
import time
import digitalocean_client
from digitalocean_client.api import apps_api
from digitalocean_client.model.error import Error
from digitalocean_client.model.apps_list_alerts_response import AppsListAlertsResponse
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
    api_instance = apps_api.AppsApi(api_client)
    app_id = "4f6c71e2-1e90-4762-9fee-6cc4a0a9f2cf" # str | The app ID

    # example passing only required values which don't have defaults set
    try:
        # List all app alerts
        api_response = api_instance.list_alerts(app_id)
        pprint(api_response)
    except digitalocean_client.ApiException as e:
        print("Exception when calling AppsApi->list_alerts: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**| The app ID |

### Return type

[**AppsListAlertsResponse**](AppsListAlertsResponse.md)

### Authorization

[bearer_auth](../README.md#bearer_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A JSON object with a &#x60;alerts&#x60; key. This is list of object &#x60;alerts&#x60;. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**401** | Unauthorized |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**404** | The resource was not found. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**429** | API Rate limit exceeded |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**500** | Server error. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**0** | Unexpected error |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_apps**
> AppsResponse list_apps()

List All Apps

List all apps on your account. Information about the current active deployment as well as any in progress ones will also be included for each app.

### Example

* Bearer Authentication (bearer_auth):

```python
import time
import digitalocean_client
from digitalocean_client.api import apps_api
from digitalocean_client.model.error import Error
from digitalocean_client.model.apps_response import AppsResponse
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
    api_instance = apps_api.AppsApi(api_client)
    page = 1 # int | Which 'page' of paginated results to return. (optional) if omitted the server will use the default value of 1
    per_page = 2 # int | Number of items returned per page (optional) if omitted the server will use the default value of 20

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List All Apps
        api_response = api_instance.list_apps(page=page, per_page=per_page)
        pprint(api_response)
    except digitalocean_client.ApiException as e:
        print("Exception when calling AppsApi->list_apps: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Which &#39;page&#39; of paginated results to return. | [optional] if omitted the server will use the default value of 1
 **per_page** | **int**| Number of items returned per page | [optional] if omitted the server will use the default value of 20

### Return type

[**AppsResponse**](AppsResponse.md)

### Authorization

[bearer_auth](../README.md#bearer_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A JSON object with a &#x60;apps&#x60; key. This is list of object &#x60;apps&#x60;. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**401** | Unauthorized |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**429** | API Rate limit exceeded |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**500** | Server error. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**0** | Unexpected error |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_deployments**
> AppsDeploymentsResponse list_deployments(app_id)

List App Deployments

List all deployments of an app.

### Example

* Bearer Authentication (bearer_auth):

```python
import time
import digitalocean_client
from digitalocean_client.api import apps_api
from digitalocean_client.model.apps_deployments_response import AppsDeploymentsResponse
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
    api_instance = apps_api.AppsApi(api_client)
    app_id = "4f6c71e2-1e90-4762-9fee-6cc4a0a9f2cf" # str | The app ID
    page = 1 # int | Which 'page' of paginated results to return. (optional) if omitted the server will use the default value of 1
    per_page = 2 # int | Number of items returned per page (optional) if omitted the server will use the default value of 20

    # example passing only required values which don't have defaults set
    try:
        # List App Deployments
        api_response = api_instance.list_deployments(app_id)
        pprint(api_response)
    except digitalocean_client.ApiException as e:
        print("Exception when calling AppsApi->list_deployments: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List App Deployments
        api_response = api_instance.list_deployments(app_id, page=page, per_page=per_page)
        pprint(api_response)
    except digitalocean_client.ApiException as e:
        print("Exception when calling AppsApi->list_deployments: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**| The app ID |
 **page** | **int**| Which &#39;page&#39; of paginated results to return. | [optional] if omitted the server will use the default value of 1
 **per_page** | **int**| Number of items returned per page | [optional] if omitted the server will use the default value of 20

### Return type

[**AppsDeploymentsResponse**](AppsDeploymentsResponse.md)

### Authorization

[bearer_auth](../README.md#bearer_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A JSON object with a &#x60;deployments&#x60; key. This will be a list of all app deployments |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**401** | Unauthorized |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**404** | The resource was not found. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**429** | API Rate limit exceeded |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**500** | Server error. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**0** | Unexpected error |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_instance_sizes**
> AppsListInstanceSizesResponse list_instance_sizes()

List Instance Sizes

List all instance sizes for `service`, `worker`, and `job` components.

### Example

* Bearer Authentication (bearer_auth):

```python
import time
import digitalocean_client
from digitalocean_client.api import apps_api
from digitalocean_client.model.error import Error
from digitalocean_client.model.apps_list_instance_sizes_response import AppsListInstanceSizesResponse
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
    api_instance = apps_api.AppsApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # List Instance Sizes
        api_response = api_instance.list_instance_sizes()
        pprint(api_response)
    except digitalocean_client.ApiException as e:
        print("Exception when calling AppsApi->list_instance_sizes: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**AppsListInstanceSizesResponse**](AppsListInstanceSizesResponse.md)

### Authorization

[bearer_auth](../README.md#bearer_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A JSON with key &#x60;instance_sizes&#x60; |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**401** | Unauthorized |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**429** | API Rate limit exceeded |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**500** | Server error. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**0** | Unexpected error |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_regions**
> AppsListRegionsResponse list_regions()

List App Regions

List all regions supported by App Platform.

### Example

* Bearer Authentication (bearer_auth):

```python
import time
import digitalocean_client
from digitalocean_client.api import apps_api
from digitalocean_client.model.error import Error
from digitalocean_client.model.apps_list_regions_response import AppsListRegionsResponse
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
    api_instance = apps_api.AppsApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # List App Regions
        api_response = api_instance.list_regions()
        pprint(api_response)
    except digitalocean_client.ApiException as e:
        print("Exception when calling AppsApi->list_regions: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**AppsListRegionsResponse**](AppsListRegionsResponse.md)

### Authorization

[bearer_auth](../README.md#bearer_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A JSON object with key &#x60;regions&#x60; |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**401** | Unauthorized |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**429** | API Rate limit exceeded |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**500** | Server error. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**0** | Unexpected error |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_tiers**
> AppsListTiersResponse list_tiers()

List App Tiers

List all app tiers.

### Example

* Bearer Authentication (bearer_auth):

```python
import time
import digitalocean_client
from digitalocean_client.api import apps_api
from digitalocean_client.model.apps_list_tiers_response import AppsListTiersResponse
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
    api_instance = apps_api.AppsApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # List App Tiers
        api_response = api_instance.list_tiers()
        pprint(api_response)
    except digitalocean_client.ApiException as e:
        print("Exception when calling AppsApi->list_tiers: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**AppsListTiersResponse**](AppsListTiersResponse.md)

### Authorization

[bearer_auth](../README.md#bearer_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A JSON object with a &#x60;tiers&#x60; key. This will be a list of all app tiers |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**401** | Unauthorized |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**429** | API Rate limit exceeded |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**500** | Server error. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**0** | Unexpected error |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_cancel_deployment**
> AppsDeploymentResponse post_cancel_deployment(app_id, deployment_id)

Cancel a Deployment

Immediately cancel an in-progress deployment.

### Example

* Bearer Authentication (bearer_auth):

```python
import time
import digitalocean_client
from digitalocean_client.api import apps_api
from digitalocean_client.model.error import Error
from digitalocean_client.model.apps_deployment_response import AppsDeploymentResponse
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
    api_instance = apps_api.AppsApi(api_client)
    app_id = "4f6c71e2-1e90-4762-9fee-6cc4a0a9f2cf" # str | The app ID
    deployment_id = "3aa4d20e-5527-4c00-b496-601fbd22520a" # str | The deployment ID

    # example passing only required values which don't have defaults set
    try:
        # Cancel a Deployment
        api_response = api_instance.post_cancel_deployment(app_id, deployment_id)
        pprint(api_response)
    except digitalocean_client.ApiException as e:
        print("Exception when calling AppsApi->post_cancel_deployment: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**| The app ID |
 **deployment_id** | **str**| The deployment ID |

### Return type

[**AppsDeploymentResponse**](AppsDeploymentResponse.md)

### Authorization

[bearer_auth](../README.md#bearer_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A JSON the &#x60;deployment&#x60; that was just cancelled. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**401** | Unauthorized |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**404** | The resource was not found. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**429** | API Rate limit exceeded |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**500** | Server error. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**0** | Unexpected error |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_app**
> AppResponse update_app(id, apps_update_app_request)

Update an App

Update an existing app by submitting a new app specification. For documentation on app specifications (`AppSpec` objects), please refer to [the product documentation](https://www.digitalocean.com/docs/app-platform/references/app-specification-reference/).

### Example

* Bearer Authentication (bearer_auth):

```python
import time
import digitalocean_client
from digitalocean_client.api import apps_api
from digitalocean_client.model.apps_update_app_request import AppsUpdateAppRequest
from digitalocean_client.model.app_response import AppResponse
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
    api_instance = apps_api.AppsApi(api_client)
    id = "4f6c71e2-1e90-4762-9fee-6cc4a0a9f2cf" # str | The ID of the app
    apps_update_app_request = AppsUpdateAppRequest(
        spec=AppSpec(
            name="web-app-01",
            region="nyc",
            domains=[
                AppDomainSpec(
                    domain="app.example.com",
                    type="DEFAULT",
                    wildcard=True,
                    zone="example.com",
                ),
            ],
            services=[
                AppServiceSpec(None),
            ],
            static_sites=[
                AppStaticSiteSpec(None),
            ],
            jobs=[
                AppJobSpec(None),
            ],
            workers=[
                AppWorkerSpec(None),
            ],
            databases=[
                AppDatabaseSpec(
                    cluster_name="cluster_name",
                    db_name="my_db",
                    db_user="superuser",
                    engine="PG",
                    name="prod-db",
                    production=True,
                    version="12",
                ),
            ],
        ),
    ) # AppsUpdateAppRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Update an App
        api_response = api_instance.update_app(id, apps_update_app_request)
        pprint(api_response)
    except digitalocean_client.ApiException as e:
        print("Exception when calling AppsApi->update_app: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the app |
 **apps_update_app_request** | [**AppsUpdateAppRequest**](AppsUpdateAppRequest.md)|  |

### Return type

[**AppResponse**](AppResponse.md)

### Authorization

[bearer_auth](../README.md#bearer_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A JSON object of the updated &#x60;app&#x60; |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**401** | Unauthorized |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**404** | The resource was not found. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**429** | API Rate limit exceeded |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**500** | Server error. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**0** | Unexpected error |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **validate_app_spec**
> AppProposeResponse validate_app_spec(app_propose)

Propose an App Spec

To propose and validate a spec for a new or existing app, send a PUT request to the `/v2/apps/propose` endpoint. The request returns some information about the proposed app, including app cost and upgrade cost. If an existing app ID is specified, the app spec is treated as a proposed update to the existing app.

### Example

* Bearer Authentication (bearer_auth):

```python
import time
import digitalocean_client
from digitalocean_client.api import apps_api
from digitalocean_client.model.app_propose import AppPropose
from digitalocean_client.model.error import Error
from digitalocean_client.model.app_propose_response import AppProposeResponse
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
    api_instance = apps_api.AppsApi(api_client)
    app_propose = AppPropose(
        spec=AppSpec(
            name="web-app-01",
            region="nyc",
            domains=[
                AppDomainSpec(
                    domain="app.example.com",
                    type="DEFAULT",
                    wildcard=True,
                    zone="example.com",
                ),
            ],
            services=[
                AppServiceSpec(None),
            ],
            static_sites=[
                AppStaticSiteSpec(None),
            ],
            jobs=[
                AppJobSpec(None),
            ],
            workers=[
                AppWorkerSpec(None),
            ],
            databases=[
                AppDatabaseSpec(
                    cluster_name="cluster_name",
                    db_name="my_db",
                    db_user="superuser",
                    engine="PG",
                    name="prod-db",
                    production=True,
                    version="12",
                ),
            ],
        ),
        app_id="b6bdf840-2854-4f87-a36c-5f231c617c84",
    ) # AppPropose | 

    # example passing only required values which don't have defaults set
    try:
        # Propose an App Spec
        api_response = api_instance.validate_app_spec(app_propose)
        pprint(api_response)
    except digitalocean_client.ApiException as e:
        print("Exception when calling AppsApi->validate_app_spec: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_propose** | [**AppPropose**](AppPropose.md)|  |

### Return type

[**AppProposeResponse**](AppProposeResponse.md)

### Authorization

[bearer_auth](../README.md#bearer_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A JSON object. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**401** | Unauthorized |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**429** | API Rate limit exceeded |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**500** | Server error. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**0** | Unexpected error |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

