# FirewallRule


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The type of resource that the firewall rule allows to access the database cluster. | 
**value** | **str** | The ID of the specific resource, the name of a tag applied to a group of resources, or the IP address that the firewall rule allows to access the database cluster. | 
**uuid** | **str** | A unique ID for the firewall rule itself. | [optional] 
**cluster_uuid** | **str** | A unique ID for the database cluster to which the rule is applied. | [optional] 
**created_at** | **datetime** | A time value given in ISO8601 combined date and time format that represents when the firewall rule was created. | [optional] [readonly] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


