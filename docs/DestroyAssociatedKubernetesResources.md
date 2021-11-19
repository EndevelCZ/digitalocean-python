# DestroyAssociatedKubernetesResources

An object containing the IDs of resources to be destroyed along with their associated with a Kubernetes cluster.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**load_balancers** | **[str]** | A list of IDs for associated load balancers to destroy along with the cluster. | [optional] 
**volumes** | **[str]** | A list of IDs for associated volumes to destroy along with the cluster. | [optional] 
**volume_snapshots** | **[str]** | A list of IDs for associated volume snapshots to destroy along with the cluster. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


