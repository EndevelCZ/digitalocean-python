# ConnectionPool


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | A unique name for the connection pool. Must be between 3 and 60 characters. | 
**mode** | **str** | The PGBouncer transaction mode for the connection pool. The allowed values are session, transaction, and statement. | 
**size** | **int** | The desired size of the PGBouncer connection pool. The maximum allowed size is determined by the size of the cluster&#39;s primary node. 25 backend server connections are allowed for every 1GB of RAM. Three are reserved for maintenance. For example, a primary node with 1 GB of RAM allows for a maximum of 22 backend server connections while one with 4 GB would allow for 97. Note that these are shared across all connection pools in a cluster. | 
**db** | **str** | The database for use with the connection pool. | 
**user** | **str** | The name of the user for use with the connection pool. | 
**connection** | **bool, date, datetime, dict, float, int, list, str, none_type** |  | [optional] 
**private_connection** | **bool, date, datetime, dict, float, int, list, str, none_type** |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


