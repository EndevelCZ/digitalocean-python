# Registry


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | A globally unique name for the container registry. Must be lowercase and be composed only of numbers, letters and &#x60;-&#x60;, up to a limit of 63 characters. | [optional] 
**created_at** | **datetime** | A time value given in ISO8601 combined date and time format that represents when the registry was created. | [optional] [readonly] 
**storage_usage_bytes** | **int** | The amount of storage used in the registry in bytes. | [optional] [readonly] 
**storage_usage_bytes_updated_at** | **datetime** | The time at which the storage usage was updated. Storage usage is calculated asynchronously, and may not immediately reflect pushes to the registry. | [optional] [readonly] 
**subscription** | **bool, date, datetime, dict, float, int, list, str, none_type** |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


