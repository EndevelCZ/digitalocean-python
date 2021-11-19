# AssociatedKubernetesResources

An object containing the IDs of resources associated with a Kubernetes cluster.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**load_balancers** | [**[AssociatedKubernetesResource]**](AssociatedKubernetesResource.md) | A list of names and IDs for associated load balancers that can be destroyed along with the cluster. | [optional] 
**volumes** | [**[AssociatedKubernetesResource]**](AssociatedKubernetesResource.md) | A list of names and IDs for associated volumes that can be destroyed along with the cluster. | [optional] 
**volume_snapshots** | [**[AssociatedKubernetesResource]**](AssociatedKubernetesResource.md) | A list of names and IDs for associated volume snapshots that can be destroyed along with the cluster. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


