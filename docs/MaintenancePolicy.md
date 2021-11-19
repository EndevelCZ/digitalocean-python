# MaintenancePolicy

An object specifying the maintenance window policy for the Kubernetes cluster.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start_time** | **str** | The start time in UTC of the maintenance window policy in 24-hour clock format / HH:MM notation (e.g., &#x60;15:00&#x60;). | [optional] 
**duration** | **str** | The duration of the maintenance window policy in human-readable format. | [optional] [readonly] 
**day** | **str** | The day of the maintenance window policy. May be one of &#x60;monday&#x60; through &#x60;sunday&#x60;, or &#x60;any&#x60; to indicate an arbitrary week day. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


