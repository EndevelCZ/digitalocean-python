# ClusterUpdate


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | A human-readable name for a Kubernetes cluster. | 
**tags** | **[str]** | An array of tags applied to the Kubernetes cluster. All clusters are automatically tagged &#x60;k8s&#x60; and &#x60;k8s:$K8S_CLUSTER_ID&#x60;. | [optional] 
**maintenance_policy** | [**MaintenancePolicy**](MaintenancePolicy.md) |  | [optional] 
**auto_upgrade** | **bool** | A boolean value indicating whether the cluster will be automatically upgraded to new patch releases during its maintenance window. | [optional]  if omitted the server will use the default value of False
**surge_upgrade** | **bool** | A boolean value indicating whether surge upgrade is enabled/disabled for the cluster. Surge upgrade makes cluster upgrades fast and reliable by bringing up new nodes before destroying the outdated nodes. | [optional]  if omitted the server will use the default value of False
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


