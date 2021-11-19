# HealthCheck

An object specifying health check settings for the load balancer.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**protocol** | **str** | The protocol used for health checks sent to the backend Droplets. The possible values are &#x60;http&#x60;, &#x60;https&#x60;, or &#x60;tcp&#x60;. | [optional]  if omitted the server will use the default value of "http"
**port** | **int** | An integer representing the port on the backend Droplets on which the health check will attempt a connection. | [optional]  if omitted the server will use the default value of 80
**path** | **str** | The path on the backend Droplets to which the load balancer instance will send a request. | [optional]  if omitted the server will use the default value of "/"
**check_interval_seconds** | **int** | The number of seconds between between two consecutive health checks. | [optional]  if omitted the server will use the default value of 10
**response_timeout_seconds** | **int** | The number of seconds the load balancer instance will wait for a response until marking a health check as failed. | [optional]  if omitted the server will use the default value of 5
**unhealthy_threshold** | **int** | The number of times a health check must fail for a backend Droplet to be marked \&quot;unhealthy\&quot; and be removed from the pool. | [optional]  if omitted the server will use the default value of 5
**healthy_threshold** | **int** | The number of times a health check must pass for a backend Droplet to be marked \&quot;healthy\&quot; and be re-added to the pool. | [optional]  if omitted the server will use the default value of 3
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


