# VolumeAction


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | This is the type of action that the object represents. For example, this could be \&quot;transfer\&quot; to represent the state of an image transfer action. | [optional] 
**resource_id** | **int, none_type** | A unique identifier for the resource that the action is associated with. | [optional] 
**id** | **int** | A unique numeric ID that can be used to identify and reference an action. | [optional] 
**status** | **str** | The current status of the action. This can be \&quot;in-progress\&quot;, \&quot;completed\&quot;, or \&quot;errored\&quot;. | [optional]  if omitted the server will use the default value of "in-progress"
**started_at** | **datetime** | A time value given in ISO8601 combined date and time format that represents when the action was initiated. | [optional] 
**completed_at** | **datetime, none_type** | A time value given in ISO8601 combined date and time format that represents when the action was completed. | [optional] 
**resource_type** | **str** | The type of resource that the action is associated with. | [optional] 
**region** | [**Region**](Region.md) |  | [optional] 
**region_slug** | **bool, date, datetime, dict, float, int, list, str, none_type** |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


