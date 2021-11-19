# DatabaseMaintenanceWindow


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**day** | **str** | The day of the week on which to apply maintenance updates. | 
**hour** | **str** | The hour in UTC at which maintenance updates will be applied in 24 hour format. | 
**pending** | **bool** | A boolean value indicating whether any maintenance is scheduled to be performed in the next window. | [optional] [readonly] 
**description** | **[str]** | A list of strings, each containing information about a pending maintenance update. | [optional] [readonly] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


