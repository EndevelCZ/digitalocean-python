# DatabaseReplica


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name to give the read-only replicating | 
**region** | **str** | A slug identifier for the region where the read-only replica will be located. If excluded, the replica will be placed in the same region as the cluster. | [optional] 
**size** | **str** | A slug identifier representing the size of the node for the read-only replica. The size of the replica must be at least as large as the node size for the database cluster from which it is replicating. | [optional] 
**status** | **str** | A string representing the current status of the database cluster. | [optional] [readonly] 
**tags** | **[str]** | A flat array of tag names as strings to apply to the read-only replica after it is created. Tag names can either be existing or new tags. | [optional] 
**created_at** | **datetime** | A time value given in ISO8601 combined date and time format that represents when the database cluster was created. | [optional] [readonly] 
**private_network_uuid** | **str** | A string specifying the UUID of the VPC to which the read-only replica will be assigned. If excluded, the replica will be assigned to your account&#39;s default VPC for the region. | [optional] 
**connection** | **bool, date, datetime, dict, float, int, list, str, none_type** |  | [optional] 
**private_connection** | **bool, date, datetime, dict, float, int, list, str, none_type** |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


