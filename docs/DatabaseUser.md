# DatabaseUser


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of a database user. | 
**role** | **str** | A string representing the database user&#39;s role. The value will be either \&quot;primary\&quot; or \&quot;normal\&quot;.  | [optional] [readonly] 
**password** | **str** | A randomly generated password for the database user. | [optional] [readonly] 
**mysql_settings** | [**MysqlSettings**](MysqlSettings.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


