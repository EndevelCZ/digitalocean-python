# DatabaseCluster


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | A unique, human-readable name referring to a database cluster. | 
**engine** | **str** | A slug representing the database engine used for the cluster. The possible values are: \&quot;pg\&quot; for PostgreSQL, \&quot;mysql\&quot; for MySQL, \&quot;redis\&quot; for Redis, and \&quot;mongodb\&quot; for MongoDB. | 
**num_nodes** | **int** | The number of nodes in the database cluster. | 
**size** | **str** | The slug identifier representing the size of the nodes in the database cluster. | 
**region** | **str** | The slug identifier for the region where the database cluster is located. | 
**id** | **str** | A unique ID that can be used to identify and reference a database cluster. | [optional] [readonly] 
**version** | **str** | A string representing the version of the database engine in use for the cluster. | [optional] 
**status** | **str** | A string representing the current status of the database cluster. | [optional] [readonly] 
**created_at** | **datetime** | A time value given in ISO8601 combined date and time format that represents when the database cluster was created. | [optional] [readonly] 
**private_network_uuid** | **str** | A string specifying the UUID of the VPC to which the database cluster will be assigned. If excluded, the cluster when creating a new database cluster, it will be assigned to your account&#39;s default VPC for the region. | [optional] 
**tags** | **[str], none_type** | An array of tags that have been applied to the database cluster. | [optional] 
**db_names** | **[str], none_type** | An array of strings containing the names of databases created in the database cluster. | [optional] [readonly] 
**connection** | **bool, date, datetime, dict, float, int, list, str, none_type** |  | [optional] 
**private_connection** | **bool, date, datetime, dict, float, int, list, str, none_type** |  | [optional] 
**users** | [**[DatabaseUser], none_type**](DatabaseUser.md) |  | [optional] [readonly] 
**maintenance_window** | **bool, date, datetime, dict, float, int, list, str, none_type** |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


