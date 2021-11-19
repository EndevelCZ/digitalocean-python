# AssociatedResourceStatus

An objects containing information about a resources scheduled for deletion.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**droplet** | [**DestroyedAssociatedResource**](DestroyedAssociatedResource.md) |  | [optional] 
**resources** | [**AssociatedResourceStatusResources**](AssociatedResourceStatusResources.md) |  | [optional] 
**completed_at** | **datetime** | A time value given in ISO8601 combined date and time format indicating when the requested action was completed. | [optional] 
**failures** | **int** | A count of the associated resources that failed to be destroyed, if any. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


