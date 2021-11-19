# AppServiceSpecHealthCheck


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**failure_threshold** | **int** | The number of failed health checks before considered unhealthy. | [optional] 
**http_path** | **str** | The route path used for the HTTP health check ping. If not set, the HTTP health check will be disabled and a TCP health check used instead. | [optional] 
**initial_delay_seconds** | **int** | The number of seconds to wait before beginning health checks. | [optional] 
**period_seconds** | **int** | The number of seconds to wait between health checks. | [optional] 
**success_threshold** | **int** | The number of successful health checks before considered healthy. | [optional] 
**timeout_seconds** | **int** | The number of seconds after which the check times out. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


