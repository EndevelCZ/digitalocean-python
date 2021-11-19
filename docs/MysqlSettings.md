# MysqlSettings


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**auth_plugin** | **str** | A string specifying the authentication method to be used for connections to the MySQL user account. The valid values are &#x60;mysql_native_password&#x60; or &#x60;caching_sha2_password&#x60;. If excluded when creating a new user, the default for the version of MySQL in use will be used. As of MySQL 8.0, the default is &#x60;caching_sha2_password&#x60;.  | 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


