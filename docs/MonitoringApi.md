# openapi_client.MonitoringApi

All URIs are relative to *https://api.digitalocean.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_alert_policy**](MonitoringApi.md#create_alert_policy) | **POST** /v2/monitoring/alerts | Create Alert Policy
[**delete_alert_policy**](MonitoringApi.md#delete_alert_policy) | **DELETE** /v2/monitoring/alerts/{alert_uuid} | Delete an Alert Policy
[**get_alert_policy**](MonitoringApi.md#get_alert_policy) | **GET** /v2/monitoring/alerts/{alert_uuid} | Retrieve an Existing Alert Policy
[**get_droplet_bandwidth_metrics**](MonitoringApi.md#get_droplet_bandwidth_metrics) | **GET** /v2/monitoring/metrics/droplet/bandwidth | Get Droplet Bandwidth Metrics
[**get_droplet_cpu_metrics**](MonitoringApi.md#get_droplet_cpu_metrics) | **GET** /v2/monitoring/metrics/droplet/cpu | Get Droplet CPU Metrics
[**get_droplet_filesystem_free_metrics**](MonitoringApi.md#get_droplet_filesystem_free_metrics) | **GET** /v2/monitoring/metrics/droplet/filesystem_free | Get Droplet Filesystem Free Metrics
[**get_droplet_filesystem_size_metrics**](MonitoringApi.md#get_droplet_filesystem_size_metrics) | **GET** /v2/monitoring/metrics/droplet/filesystem_size | Get Droplet Filesystem Size Metrics
[**get_droplet_load15_metrics**](MonitoringApi.md#get_droplet_load15_metrics) | **GET** /v2/monitoring/metrics/droplet/load_15 | Get Droplet Load15 Metrics
[**get_droplet_load1_metrics**](MonitoringApi.md#get_droplet_load1_metrics) | **GET** /v2/monitoring/metrics/droplet/load_1 | Get Droplet Load1 Metrics
[**get_droplet_load5_metrics**](MonitoringApi.md#get_droplet_load5_metrics) | **GET** /v2/monitoring/metrics/droplet/load_5 | Get Droplet Load5 Metrics
[**get_droplet_memory_available_metrics**](MonitoringApi.md#get_droplet_memory_available_metrics) | **GET** /v2/monitoring/metrics/droplet/memory_available | Get Droplet Available Memory Metrics
[**get_droplet_memory_cached_metrics**](MonitoringApi.md#get_droplet_memory_cached_metrics) | **GET** /v2/monitoring/metrics/droplet/memory_cached | Get Droplet Cached Memory Metrics
[**get_droplet_memory_free_metrics**](MonitoringApi.md#get_droplet_memory_free_metrics) | **GET** /v2/monitoring/metrics/droplet/memory_free | Get Droplet Free Memory Metrics
[**get_droplet_memory_total_metrics**](MonitoringApi.md#get_droplet_memory_total_metrics) | **GET** /v2/monitoring/metrics/droplet/memory_total | Get Droplet Total Memory Metrics
[**list_alert_policies**](MonitoringApi.md#list_alert_policies) | **GET** /v2/monitoring/alerts | List Alert Policies
[**update_alert_policy**](MonitoringApi.md#update_alert_policy) | **PUT** /v2/monitoring/alerts/{alert_uuid} | Update an Alert Policy


# **create_alert_policy**
> AlertPolicy create_alert_policy(alert_policy_request)

Create Alert Policy

To create a new alert, send a POST request to `/v2/monitoring/alerts`.

### Example

* Bearer Authentication (bearer_auth):

```python
import time
import openapi_client
from openapi_client.api import monitoring_api
from openapi_client.model.error import Error
from openapi_client.model.alert_policy_request import AlertPolicyRequest
from openapi_client.model.alert_policy import AlertPolicy
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
    api_instance = monitoring_api.MonitoringApi(api_client)
    alert_policy_request = AlertPolicyRequest(
        alerts=Alerts(
            email=["bob@exmaple.com"],
            slack=[
                SlackDetails(
                    channel="Production Alerts",
                    url="https://hooks.slack.com/services/T1234567/AAAAAAAA/ZZZZZZ",
                ),
            ],
        ),
        compare="GreaterThan",
        description="CPU Alert",
        enabled=True,
        entities=["192018292"],
        tags=["droplet_tag"],
        type="v1/insights/droplet/cpu",
        value=80,
        window="5m",
    ) # AlertPolicyRequest | The 'type' field dictates what type of entity that the alert policy applies to and hence what type of entity is passed in the 'entities' array. If both the 'tags' array and 'entities' array are empty the alert policy applies to all entities of the relevant type that are owned by the user account. Otherwise the following table shows the valid entity types for each type of alert policy: <table><thead><tr><td>Type</td><td>Description</td><td>Valid Entity Type</td></tr></thead><tr><td>v1/insights/droplet/memory_utilization_percent</td><td>alert on the percent of memory utilization</td><td>droplet ID</td></tr><tr><td>v1/insights/droplet/disk_read</td><td>alert on the rate of disk read I/O in MBps</td><td>droplet ID</td></tr><tr><td>v1/insights/droplet/load_5</td><td>alert on the 5 minute load average</td><td>droplet ID</td></tr><tr><td>v1/insights/droplet/load_15</td><td>alert on the 15 minute load average</td><td>droplet ID</td></tr><tr><td>v1/insights/droplet/disk_utilization_percent</td><td>alert on the percent of disk utilization</td><td>droplet ID</td></tr><tr><td>v1/insights/droplet/cpu</td><td>alert on the percent of CPU utilization</td><td>droplet ID</td></tr><tr><td>v1/insights/droplet/disk_write</td><td>alert on the rate of disk write I/O in MBps</td><td>droplet ID</td></tr><tr><td>v1/insights/droplet/public_outbound_bandwidth</td><td>alert on the rate of public outbound bandwidth in Mbps</td><td>droplet ID</td></tr><tr><td>v1/insights/droplet/public_inbound_bandwidth</td><td>alert on the rate of public inbound bandwidth in Mbps</td><td>droplet ID</td></tr><tr><td>v1/insights/droplet/private_outbound_bandwidth</td><td>alert on the rate of private outbound bandwidth in Mbps</td><td>droplet ID</td></tr><tr><td>v1/insights/droplet/private_inbound_bandwidth</td><td>alert on the rate of private inbound bandwidth in Mbps</td><td>droplet ID</td></tr><tr><td>v1/insights/droplet/load_1</td><td>alert on the 1 minute load average</td><td>droplet ID</td></tr></table>

    # example passing only required values which don't have defaults set
    try:
        # Create Alert Policy
        api_response = api_instance.create_alert_policy(alert_policy_request)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling MonitoringApi->create_alert_policy: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **alert_policy_request** | [**AlertPolicyRequest**](AlertPolicyRequest.md)| The &#39;type&#39; field dictates what type of entity that the alert policy applies to and hence what type of entity is passed in the &#39;entities&#39; array. If both the &#39;tags&#39; array and &#39;entities&#39; array are empty the alert policy applies to all entities of the relevant type that are owned by the user account. Otherwise the following table shows the valid entity types for each type of alert policy: &lt;table&gt;&lt;thead&gt;&lt;tr&gt;&lt;td&gt;Type&lt;/td&gt;&lt;td&gt;Description&lt;/td&gt;&lt;td&gt;Valid Entity Type&lt;/td&gt;&lt;/tr&gt;&lt;/thead&gt;&lt;tr&gt;&lt;td&gt;v1/insights/droplet/memory_utilization_percent&lt;/td&gt;&lt;td&gt;alert on the percent of memory utilization&lt;/td&gt;&lt;td&gt;droplet ID&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;v1/insights/droplet/disk_read&lt;/td&gt;&lt;td&gt;alert on the rate of disk read I/O in MBps&lt;/td&gt;&lt;td&gt;droplet ID&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;v1/insights/droplet/load_5&lt;/td&gt;&lt;td&gt;alert on the 5 minute load average&lt;/td&gt;&lt;td&gt;droplet ID&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;v1/insights/droplet/load_15&lt;/td&gt;&lt;td&gt;alert on the 15 minute load average&lt;/td&gt;&lt;td&gt;droplet ID&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;v1/insights/droplet/disk_utilization_percent&lt;/td&gt;&lt;td&gt;alert on the percent of disk utilization&lt;/td&gt;&lt;td&gt;droplet ID&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;v1/insights/droplet/cpu&lt;/td&gt;&lt;td&gt;alert on the percent of CPU utilization&lt;/td&gt;&lt;td&gt;droplet ID&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;v1/insights/droplet/disk_write&lt;/td&gt;&lt;td&gt;alert on the rate of disk write I/O in MBps&lt;/td&gt;&lt;td&gt;droplet ID&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;v1/insights/droplet/public_outbound_bandwidth&lt;/td&gt;&lt;td&gt;alert on the rate of public outbound bandwidth in Mbps&lt;/td&gt;&lt;td&gt;droplet ID&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;v1/insights/droplet/public_inbound_bandwidth&lt;/td&gt;&lt;td&gt;alert on the rate of public inbound bandwidth in Mbps&lt;/td&gt;&lt;td&gt;droplet ID&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;v1/insights/droplet/private_outbound_bandwidth&lt;/td&gt;&lt;td&gt;alert on the rate of private outbound bandwidth in Mbps&lt;/td&gt;&lt;td&gt;droplet ID&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;v1/insights/droplet/private_inbound_bandwidth&lt;/td&gt;&lt;td&gt;alert on the rate of private inbound bandwidth in Mbps&lt;/td&gt;&lt;td&gt;droplet ID&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;v1/insights/droplet/load_1&lt;/td&gt;&lt;td&gt;alert on the 1 minute load average&lt;/td&gt;&lt;td&gt;droplet ID&lt;/td&gt;&lt;/tr&gt;&lt;/table&gt; |

### Return type

[**AlertPolicy**](AlertPolicy.md)

### Authorization

[bearer_auth](../README.md#bearer_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | An alert policy. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**401** | Unauthorized |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**429** | API Rate limit exceeded |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**500** | Server error. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**0** | Unexpected error |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_alert_policy**
> delete_alert_policy(alert_uuid)

Delete an Alert Policy

To delete an alert policy, send a DELETE request to `/v2/monitoring/alerts/{alert_uuid}`

### Example

* Bearer Authentication (bearer_auth):

```python
import time
import openapi_client
from openapi_client.api import monitoring_api
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
    api_instance = monitoring_api.MonitoringApi(api_client)
    alert_uuid = "4de7ac8b-495b-4884-9a69-1050c6793cd6" # str | A unique identifier for an alert policy.

    # example passing only required values which don't have defaults set
    try:
        # Delete an Alert Policy
        api_instance.delete_alert_policy(alert_uuid)
    except openapi_client.ApiException as e:
        print("Exception when calling MonitoringApi->delete_alert_policy: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **alert_uuid** | **str**| A unique identifier for an alert policy. |

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

# **get_alert_policy**
> AlertPolicy get_alert_policy(alert_uuid)

Retrieve an Existing Alert Policy

To retrieve a given alert policy, send a GET request to `/v2/monitoring/alerts/{alert_uuid}`

### Example

* Bearer Authentication (bearer_auth):

```python
import time
import openapi_client
from openapi_client.api import monitoring_api
from openapi_client.model.error import Error
from openapi_client.model.alert_policy import AlertPolicy
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
    api_instance = monitoring_api.MonitoringApi(api_client)
    alert_uuid = "4de7ac8b-495b-4884-9a69-1050c6793cd6" # str | A unique identifier for an alert policy.

    # example passing only required values which don't have defaults set
    try:
        # Retrieve an Existing Alert Policy
        api_response = api_instance.get_alert_policy(alert_uuid)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling MonitoringApi->get_alert_policy: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **alert_uuid** | **str**| A unique identifier for an alert policy. |

### Return type

[**AlertPolicy**](AlertPolicy.md)

### Authorization

[bearer_auth](../README.md#bearer_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | An alert policy. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**401** | Unauthorized |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**404** | The resource was not found. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**429** | API Rate limit exceeded |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**500** | Server error. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**0** | Unexpected error |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_droplet_bandwidth_metrics**
> Metrics get_droplet_bandwidth_metrics(host_id, interface, direction, start, end)

Get Droplet Bandwidth Metrics

To retrieve bandwidth metrics for a given Droplet, send a GET request to `/v2/monitoring/metrics/droplet/bandwidth`. Use the `interface` query parameter to specify if the results should be for the `private` or `public` interface. Use the `direction` query parameter to specify if the results should be for `inbound` or `outbound` traffic.

### Example

* Bearer Authentication (bearer_auth):

```python
import time
import openapi_client
from openapi_client.api import monitoring_api
from openapi_client.model.metrics import Metrics
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
    api_instance = monitoring_api.MonitoringApi(api_client)
    host_id = "17209102" # str | The droplet ID.
    interface = "private" # str | The network interface.
    direction = "inbound" # str | The traffic direction.
    start = "1620683817" # str | Timestamp to start metric window.
    end = "1620705417" # str | Timestamp to end metric window.

    # example passing only required values which don't have defaults set
    try:
        # Get Droplet Bandwidth Metrics
        api_response = api_instance.get_droplet_bandwidth_metrics(host_id, interface, direction, start, end)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling MonitoringApi->get_droplet_bandwidth_metrics: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **host_id** | **str**| The droplet ID. |
 **interface** | **str**| The network interface. |
 **direction** | **str**| The traffic direction. |
 **start** | **str**| Timestamp to start metric window. |
 **end** | **str**| Timestamp to end metric window. |

### Return type

[**Metrics**](Metrics.md)

### Authorization

[bearer_auth](../README.md#bearer_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The response will be a JSON object with a key called &#x60;data&#x60; and &#x60;status&#x60;. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**401** | Unauthorized |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**429** | API Rate limit exceeded |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**500** | Server error. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**0** | Unexpected error |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_droplet_cpu_metrics**
> Metrics get_droplet_cpu_metrics(host_id, start, end)

Get Droplet CPU Metrics

To retrieve CPU metrics for a given droplet, send a GET request to `/v2/monitoring/metrics/droplet/cpu`.

### Example

* Bearer Authentication (bearer_auth):

```python
import time
import openapi_client
from openapi_client.api import monitoring_api
from openapi_client.model.metrics import Metrics
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
    api_instance = monitoring_api.MonitoringApi(api_client)
    host_id = "17209102" # str | The droplet ID.
    start = "1620683817" # str | Timestamp to start metric window.
    end = "1620705417" # str | Timestamp to end metric window.

    # example passing only required values which don't have defaults set
    try:
        # Get Droplet CPU Metrics
        api_response = api_instance.get_droplet_cpu_metrics(host_id, start, end)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling MonitoringApi->get_droplet_cpu_metrics: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **host_id** | **str**| The droplet ID. |
 **start** | **str**| Timestamp to start metric window. |
 **end** | **str**| Timestamp to end metric window. |

### Return type

[**Metrics**](Metrics.md)

### Authorization

[bearer_auth](../README.md#bearer_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The response will be a JSON object with a key called &#x60;data&#x60; and &#x60;status&#x60;. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**401** | Unauthorized |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**429** | API Rate limit exceeded |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**500** | Server error. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**0** | Unexpected error |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_droplet_filesystem_free_metrics**
> Metrics get_droplet_filesystem_free_metrics(host_id, start, end)

Get Droplet Filesystem Free Metrics

To retrieve filesystem free metrics for a given droplet, send a GET request to `/v2/monitoring/metrics/droplet/filesystem_free`.

### Example

* Bearer Authentication (bearer_auth):

```python
import time
import openapi_client
from openapi_client.api import monitoring_api
from openapi_client.model.metrics import Metrics
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
    api_instance = monitoring_api.MonitoringApi(api_client)
    host_id = "17209102" # str | The droplet ID.
    start = "1620683817" # str | Timestamp to start metric window.
    end = "1620705417" # str | Timestamp to end metric window.

    # example passing only required values which don't have defaults set
    try:
        # Get Droplet Filesystem Free Metrics
        api_response = api_instance.get_droplet_filesystem_free_metrics(host_id, start, end)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling MonitoringApi->get_droplet_filesystem_free_metrics: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **host_id** | **str**| The droplet ID. |
 **start** | **str**| Timestamp to start metric window. |
 **end** | **str**| Timestamp to end metric window. |

### Return type

[**Metrics**](Metrics.md)

### Authorization

[bearer_auth](../README.md#bearer_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The response will be a JSON object with a key called &#x60;data&#x60; and &#x60;status&#x60;. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**401** | Unauthorized |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**429** | API Rate limit exceeded |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**500** | Server error. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**0** | Unexpected error |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_droplet_filesystem_size_metrics**
> Metrics get_droplet_filesystem_size_metrics(host_id, start, end)

Get Droplet Filesystem Size Metrics

To retrieve filesystem size metrics for a given droplet, send a GET request to `/v2/monitoring/metrics/droplet/filesystem_size`.

### Example

* Bearer Authentication (bearer_auth):

```python
import time
import openapi_client
from openapi_client.api import monitoring_api
from openapi_client.model.metrics import Metrics
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
    api_instance = monitoring_api.MonitoringApi(api_client)
    host_id = "17209102" # str | The droplet ID.
    start = "1620683817" # str | Timestamp to start metric window.
    end = "1620705417" # str | Timestamp to end metric window.

    # example passing only required values which don't have defaults set
    try:
        # Get Droplet Filesystem Size Metrics
        api_response = api_instance.get_droplet_filesystem_size_metrics(host_id, start, end)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling MonitoringApi->get_droplet_filesystem_size_metrics: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **host_id** | **str**| The droplet ID. |
 **start** | **str**| Timestamp to start metric window. |
 **end** | **str**| Timestamp to end metric window. |

### Return type

[**Metrics**](Metrics.md)

### Authorization

[bearer_auth](../README.md#bearer_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The response will be a JSON object with a key called &#x60;data&#x60; and &#x60;status&#x60;. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**401** | Unauthorized |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**429** | API Rate limit exceeded |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**500** | Server error. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**0** | Unexpected error |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_droplet_load15_metrics**
> Metrics get_droplet_load15_metrics(host_id, start, end)

Get Droplet Load15 Metrics

To retrieve 15 minute load average metrics for a given droplet, send a GET request to `/v2/monitoring/metrics/droplet/load_15`.

### Example

* Bearer Authentication (bearer_auth):

```python
import time
import openapi_client
from openapi_client.api import monitoring_api
from openapi_client.model.metrics import Metrics
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
    api_instance = monitoring_api.MonitoringApi(api_client)
    host_id = "17209102" # str | The droplet ID.
    start = "1620683817" # str | Timestamp to start metric window.
    end = "1620705417" # str | Timestamp to end metric window.

    # example passing only required values which don't have defaults set
    try:
        # Get Droplet Load15 Metrics
        api_response = api_instance.get_droplet_load15_metrics(host_id, start, end)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling MonitoringApi->get_droplet_load15_metrics: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **host_id** | **str**| The droplet ID. |
 **start** | **str**| Timestamp to start metric window. |
 **end** | **str**| Timestamp to end metric window. |

### Return type

[**Metrics**](Metrics.md)

### Authorization

[bearer_auth](../README.md#bearer_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The response will be a JSON object with a key called &#x60;data&#x60; and &#x60;status&#x60;. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**401** | Unauthorized |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**429** | API Rate limit exceeded |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**500** | Server error. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**0** | Unexpected error |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_droplet_load1_metrics**
> Metrics get_droplet_load1_metrics(host_id, start, end)

Get Droplet Load1 Metrics

To retrieve 1 minute load average metrics for a given droplet, send a GET request to `/v2/monitoring/metrics/droplet/load_1`.

### Example

* Bearer Authentication (bearer_auth):

```python
import time
import openapi_client
from openapi_client.api import monitoring_api
from openapi_client.model.metrics import Metrics
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
    api_instance = monitoring_api.MonitoringApi(api_client)
    host_id = "17209102" # str | The droplet ID.
    start = "1620683817" # str | Timestamp to start metric window.
    end = "1620705417" # str | Timestamp to end metric window.

    # example passing only required values which don't have defaults set
    try:
        # Get Droplet Load1 Metrics
        api_response = api_instance.get_droplet_load1_metrics(host_id, start, end)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling MonitoringApi->get_droplet_load1_metrics: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **host_id** | **str**| The droplet ID. |
 **start** | **str**| Timestamp to start metric window. |
 **end** | **str**| Timestamp to end metric window. |

### Return type

[**Metrics**](Metrics.md)

### Authorization

[bearer_auth](../README.md#bearer_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The response will be a JSON object with a key called &#x60;data&#x60; and &#x60;status&#x60;. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**401** | Unauthorized |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**429** | API Rate limit exceeded |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**500** | Server error. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**0** | Unexpected error |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_droplet_load5_metrics**
> Metrics get_droplet_load5_metrics(host_id, start, end)

Get Droplet Load5 Metrics

To retrieve 5 minute load average metrics for a given droplet, send a GET request to `/v2/monitoring/metrics/droplet/load_5`.

### Example

* Bearer Authentication (bearer_auth):

```python
import time
import openapi_client
from openapi_client.api import monitoring_api
from openapi_client.model.metrics import Metrics
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
    api_instance = monitoring_api.MonitoringApi(api_client)
    host_id = "17209102" # str | The droplet ID.
    start = "1620683817" # str | Timestamp to start metric window.
    end = "1620705417" # str | Timestamp to end metric window.

    # example passing only required values which don't have defaults set
    try:
        # Get Droplet Load5 Metrics
        api_response = api_instance.get_droplet_load5_metrics(host_id, start, end)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling MonitoringApi->get_droplet_load5_metrics: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **host_id** | **str**| The droplet ID. |
 **start** | **str**| Timestamp to start metric window. |
 **end** | **str**| Timestamp to end metric window. |

### Return type

[**Metrics**](Metrics.md)

### Authorization

[bearer_auth](../README.md#bearer_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The response will be a JSON object with a key called &#x60;data&#x60; and &#x60;status&#x60;. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**401** | Unauthorized |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**429** | API Rate limit exceeded |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**500** | Server error. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**0** | Unexpected error |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_droplet_memory_available_metrics**
> Metrics get_droplet_memory_available_metrics(host_id, start, end)

Get Droplet Available Memory Metrics

To retrieve available memory metrics for a given droplet, send a GET request to `/v2/monitoring/metrics/droplet/memory_available`.

### Example

* Bearer Authentication (bearer_auth):

```python
import time
import openapi_client
from openapi_client.api import monitoring_api
from openapi_client.model.metrics import Metrics
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
    api_instance = monitoring_api.MonitoringApi(api_client)
    host_id = "17209102" # str | The droplet ID.
    start = "1620683817" # str | Timestamp to start metric window.
    end = "1620705417" # str | Timestamp to end metric window.

    # example passing only required values which don't have defaults set
    try:
        # Get Droplet Available Memory Metrics
        api_response = api_instance.get_droplet_memory_available_metrics(host_id, start, end)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling MonitoringApi->get_droplet_memory_available_metrics: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **host_id** | **str**| The droplet ID. |
 **start** | **str**| Timestamp to start metric window. |
 **end** | **str**| Timestamp to end metric window. |

### Return type

[**Metrics**](Metrics.md)

### Authorization

[bearer_auth](../README.md#bearer_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The response will be a JSON object with a key called &#x60;data&#x60; and &#x60;status&#x60;. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**401** | Unauthorized |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**429** | API Rate limit exceeded |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**500** | Server error. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**0** | Unexpected error |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_droplet_memory_cached_metrics**
> Metrics get_droplet_memory_cached_metrics(host_id, start, end)

Get Droplet Cached Memory Metrics

To retrieve cached memory metrics for a given droplet, send a GET request to `/v2/monitoring/metrics/droplet/memory_cached`.

### Example

* Bearer Authentication (bearer_auth):

```python
import time
import openapi_client
from openapi_client.api import monitoring_api
from openapi_client.model.metrics import Metrics
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
    api_instance = monitoring_api.MonitoringApi(api_client)
    host_id = "17209102" # str | The droplet ID.
    start = "1620683817" # str | Timestamp to start metric window.
    end = "1620705417" # str | Timestamp to end metric window.

    # example passing only required values which don't have defaults set
    try:
        # Get Droplet Cached Memory Metrics
        api_response = api_instance.get_droplet_memory_cached_metrics(host_id, start, end)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling MonitoringApi->get_droplet_memory_cached_metrics: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **host_id** | **str**| The droplet ID. |
 **start** | **str**| Timestamp to start metric window. |
 **end** | **str**| Timestamp to end metric window. |

### Return type

[**Metrics**](Metrics.md)

### Authorization

[bearer_auth](../README.md#bearer_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The response will be a JSON object with a key called &#x60;data&#x60; and &#x60;status&#x60;. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**401** | Unauthorized |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**429** | API Rate limit exceeded |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**500** | Server error. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**0** | Unexpected error |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_droplet_memory_free_metrics**
> Metrics get_droplet_memory_free_metrics(host_id, start, end)

Get Droplet Free Memory Metrics

To retrieve free memory metrics for a given droplet, send a GET request to `/v2/monitoring/metrics/droplet/memory_free`.

### Example

* Bearer Authentication (bearer_auth):

```python
import time
import openapi_client
from openapi_client.api import monitoring_api
from openapi_client.model.metrics import Metrics
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
    api_instance = monitoring_api.MonitoringApi(api_client)
    host_id = "17209102" # str | The droplet ID.
    start = "1620683817" # str | Timestamp to start metric window.
    end = "1620705417" # str | Timestamp to end metric window.

    # example passing only required values which don't have defaults set
    try:
        # Get Droplet Free Memory Metrics
        api_response = api_instance.get_droplet_memory_free_metrics(host_id, start, end)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling MonitoringApi->get_droplet_memory_free_metrics: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **host_id** | **str**| The droplet ID. |
 **start** | **str**| Timestamp to start metric window. |
 **end** | **str**| Timestamp to end metric window. |

### Return type

[**Metrics**](Metrics.md)

### Authorization

[bearer_auth](../README.md#bearer_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The response will be a JSON object with a key called &#x60;data&#x60; and &#x60;status&#x60;. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**401** | Unauthorized |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**429** | API Rate limit exceeded |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**500** | Server error. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**0** | Unexpected error |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_droplet_memory_total_metrics**
> Metrics get_droplet_memory_total_metrics(host_id, start, end)

Get Droplet Total Memory Metrics

To retrieve total memory metrics for a given droplet, send a GET request to `/v2/monitoring/metrics/droplet/memory_total`.

### Example

* Bearer Authentication (bearer_auth):

```python
import time
import openapi_client
from openapi_client.api import monitoring_api
from openapi_client.model.metrics import Metrics
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
    api_instance = monitoring_api.MonitoringApi(api_client)
    host_id = "17209102" # str | The droplet ID.
    start = "1620683817" # str | Timestamp to start metric window.
    end = "1620705417" # str | Timestamp to end metric window.

    # example passing only required values which don't have defaults set
    try:
        # Get Droplet Total Memory Metrics
        api_response = api_instance.get_droplet_memory_total_metrics(host_id, start, end)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling MonitoringApi->get_droplet_memory_total_metrics: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **host_id** | **str**| The droplet ID. |
 **start** | **str**| Timestamp to start metric window. |
 **end** | **str**| Timestamp to end metric window. |

### Return type

[**Metrics**](Metrics.md)

### Authorization

[bearer_auth](../README.md#bearer_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The response will be a JSON object with a key called &#x60;data&#x60; and &#x60;status&#x60;. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**401** | Unauthorized |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**429** | API Rate limit exceeded |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**500** | Server error. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**0** | Unexpected error |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_alert_policies**
> bool, date, datetime, dict, float, int, list, str, none_type list_alert_policies()

List Alert Policies

Returns all alert policies that are configured for the given account. To List all alert policies, send a GET request to `/v2/monitoring/alerts`.

### Example

* Bearer Authentication (bearer_auth):

```python
import time
import openapi_client
from openapi_client.api import monitoring_api
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
    api_instance = monitoring_api.MonitoringApi(api_client)
    per_page = 2 # int | Number of items returned per page (optional) if omitted the server will use the default value of 20
    page = 1 # int | Which 'page' of paginated results to return. (optional) if omitted the server will use the default value of 1

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List Alert Policies
        api_response = api_instance.list_alert_policies(per_page=per_page, page=page)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling MonitoringApi->list_alert_policies: %s\n" % e)
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
**200** | A list of alert policies. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**401** | Unauthorized |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**429** | API Rate limit exceeded |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**500** | Server error. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**0** | Unexpected error |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_alert_policy**
> AlertPolicy update_alert_policy(alert_uuid, alert_policy_request)

Update an Alert Policy

To update en existing policy, send a PUT request to `v2/monitoring/alerts/{alert_uuid}`.

### Example

* Bearer Authentication (bearer_auth):

```python
import time
import openapi_client
from openapi_client.api import monitoring_api
from openapi_client.model.error import Error
from openapi_client.model.alert_policy_request import AlertPolicyRequest
from openapi_client.model.alert_policy import AlertPolicy
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
    api_instance = monitoring_api.MonitoringApi(api_client)
    alert_uuid = "4de7ac8b-495b-4884-9a69-1050c6793cd6" # str | A unique identifier for an alert policy.
    alert_policy_request = AlertPolicyRequest(
        alerts=Alerts(
            email=["bob@exmaple.com"],
            slack=[
                SlackDetails(
                    channel="Production Alerts",
                    url="https://hooks.slack.com/services/T1234567/AAAAAAAA/ZZZZZZ",
                ),
            ],
        ),
        compare="GreaterThan",
        description="CPU Alert",
        enabled=True,
        entities=["192018292"],
        tags=["droplet_tag"],
        type="v1/insights/droplet/cpu",
        value=80,
        window="5m",
    ) # AlertPolicyRequest | The 'type' field dictates what type of entity that the alert policy applies to and hence what type of entity is passed in the 'entities' array. If both the 'tags' array and 'entities' array are empty the alert policy applies to all entities of the relevant type that are owned by the user account. Otherwise the following table shows the valid entity types for each type of alert policy: <table><thead><tr><td>Type</td><td>Description</td><td>Valid Entity Type</td></tr></thead><tr><td>v1/insights/droplet/memory_utilization_percent</td><td>alert on the percent of memory utilization</td><td>droplet ID</td></tr><tr><td>v1/insights/droplet/disk_read</td><td>alert on the rate of disk read I/O in MBps</td><td>droplet ID</td></tr><tr><td>v1/insights/droplet/load_5</td><td>alert on the 5 minute load average</td><td>droplet ID</td></tr><tr><td>v1/insights/droplet/load_15</td><td>alert on the 15 minute load average</td><td>droplet ID</td></tr><tr><td>v1/insights/droplet/disk_utilization_percent</td><td>alert on the percent of disk utilization</td><td>droplet ID</td></tr><tr><td>v1/insights/droplet/cpu</td><td>alert on the percent of CPU utilization</td><td>droplet ID</td></tr><tr><td>v1/insights/droplet/disk_write</td><td>alert on the rate of disk write I/O in MBps</td><td>droplet ID</td></tr><tr><td>v1/insights/droplet/public_outbound_bandwidth</td><td>alert on the rate of public outbound bandwidth in Mbps</td><td>droplet ID</td></tr><tr><td>v1/insights/droplet/public_inbound_bandwidth</td><td>alert on the rate of public inbound bandwidth in Mbps</td><td>droplet ID</td></tr><tr><td>v1/insights/droplet/private_outbound_bandwidth</td><td>alert on the rate of private outbound bandwidth in Mbps</td><td>droplet ID</td></tr><tr><td>v1/insights/droplet/private_inbound_bandwidth</td><td>alert on the rate of private inbound bandwidth in Mbps</td><td>droplet ID</td></tr><tr><td>v1/insights/droplet/load_1</td><td>alert on the 1 minute load average</td><td>droplet ID</td></tr></table>

    # example passing only required values which don't have defaults set
    try:
        # Update an Alert Policy
        api_response = api_instance.update_alert_policy(alert_uuid, alert_policy_request)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling MonitoringApi->update_alert_policy: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **alert_uuid** | **str**| A unique identifier for an alert policy. |
 **alert_policy_request** | [**AlertPolicyRequest**](AlertPolicyRequest.md)| The &#39;type&#39; field dictates what type of entity that the alert policy applies to and hence what type of entity is passed in the &#39;entities&#39; array. If both the &#39;tags&#39; array and &#39;entities&#39; array are empty the alert policy applies to all entities of the relevant type that are owned by the user account. Otherwise the following table shows the valid entity types for each type of alert policy: &lt;table&gt;&lt;thead&gt;&lt;tr&gt;&lt;td&gt;Type&lt;/td&gt;&lt;td&gt;Description&lt;/td&gt;&lt;td&gt;Valid Entity Type&lt;/td&gt;&lt;/tr&gt;&lt;/thead&gt;&lt;tr&gt;&lt;td&gt;v1/insights/droplet/memory_utilization_percent&lt;/td&gt;&lt;td&gt;alert on the percent of memory utilization&lt;/td&gt;&lt;td&gt;droplet ID&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;v1/insights/droplet/disk_read&lt;/td&gt;&lt;td&gt;alert on the rate of disk read I/O in MBps&lt;/td&gt;&lt;td&gt;droplet ID&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;v1/insights/droplet/load_5&lt;/td&gt;&lt;td&gt;alert on the 5 minute load average&lt;/td&gt;&lt;td&gt;droplet ID&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;v1/insights/droplet/load_15&lt;/td&gt;&lt;td&gt;alert on the 15 minute load average&lt;/td&gt;&lt;td&gt;droplet ID&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;v1/insights/droplet/disk_utilization_percent&lt;/td&gt;&lt;td&gt;alert on the percent of disk utilization&lt;/td&gt;&lt;td&gt;droplet ID&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;v1/insights/droplet/cpu&lt;/td&gt;&lt;td&gt;alert on the percent of CPU utilization&lt;/td&gt;&lt;td&gt;droplet ID&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;v1/insights/droplet/disk_write&lt;/td&gt;&lt;td&gt;alert on the rate of disk write I/O in MBps&lt;/td&gt;&lt;td&gt;droplet ID&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;v1/insights/droplet/public_outbound_bandwidth&lt;/td&gt;&lt;td&gt;alert on the rate of public outbound bandwidth in Mbps&lt;/td&gt;&lt;td&gt;droplet ID&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;v1/insights/droplet/public_inbound_bandwidth&lt;/td&gt;&lt;td&gt;alert on the rate of public inbound bandwidth in Mbps&lt;/td&gt;&lt;td&gt;droplet ID&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;v1/insights/droplet/private_outbound_bandwidth&lt;/td&gt;&lt;td&gt;alert on the rate of private outbound bandwidth in Mbps&lt;/td&gt;&lt;td&gt;droplet ID&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;v1/insights/droplet/private_inbound_bandwidth&lt;/td&gt;&lt;td&gt;alert on the rate of private inbound bandwidth in Mbps&lt;/td&gt;&lt;td&gt;droplet ID&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;v1/insights/droplet/load_1&lt;/td&gt;&lt;td&gt;alert on the 1 minute load average&lt;/td&gt;&lt;td&gt;droplet ID&lt;/td&gt;&lt;/tr&gt;&lt;/table&gt; |

### Return type

[**AlertPolicy**](AlertPolicy.md)

### Authorization

[bearer_auth](../README.md#bearer_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | An alert policy. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**401** | Unauthorized |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**404** | The resource was not found. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**429** | API Rate limit exceeded |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**500** | Server error. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**0** | Unexpected error |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

