# ClusterlintResults


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**run_id** | **str** | Id of the clusterlint run that can be used later to fetch the diagnostics. | [optional] 
**requested_at** | **datetime** | A time value given in ISO8601 combined date and time format that represents when the schedule clusterlint run request was made. | [optional] 
**completed_at** | **datetime** | A time value given in ISO8601 combined date and time format that represents when the schedule clusterlint run request was completed. | [optional] 
**diagnostics** | [**[ClusterlintResultsDiagnostics]**](ClusterlintResultsDiagnostics.md) | An array of diagnostics reporting potential problems for the given cluster. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


