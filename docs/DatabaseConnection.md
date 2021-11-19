# DatabaseConnection


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uri** | **str** | A connection string in the format accepted by the &#x60;psql&#x60; command. This is provided as a convenience and should be able to be constructed by the other attributes. | [optional] [readonly] 
**database** | **str** | The name of the default database. | [optional] [readonly] 
**host** | **str** | The FQDN pointing to the database cluster&#39;s current primary node. | [optional] [readonly] 
**port** | **int** | The port on which the database cluster is listening. | [optional] [readonly] 
**user** | **str** | The default user for the database. | [optional] [readonly] 
**password** | **str** | The randomly generated password for the default user. | [optional] [readonly] 
**ssl** | **bool** | A boolean value indicating if the connection should be made over SSL. | [optional] [readonly] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


