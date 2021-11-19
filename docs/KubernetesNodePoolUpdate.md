# KubernetesNodePoolUpdate


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | A human-readable name for the node pool. | 
**count** | **int** | The number of Droplet instances in the node pool. | 
**id** | **str** | A unique ID that can be used to identify and reference a specific node pool. | [optional] [readonly] 
**tags** | **[str]** | An array containing the tags applied to the node pool. All node pools are automatically tagged &#x60;k8s&#x60;, &#x60;k8s-worker&#x60;, and &#x60;k8s:$K8S_CLUSTER_ID&#x60;. | [optional] 
**labels** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}, none_type** | An object containing a set of Kubernetes labels. The keys and are values are both user-defined. | [optional] 
**taints** | [**[KubernetesNodePoolTaint]**](KubernetesNodePoolTaint.md) | An array of taints to apply to all nodes in a pool. Taints will automatically be applied to all existing nodes and any subsequent nodes added to the pool. When a taint is removed, it is removed from all nodes in the pool. | [optional] 
**auto_scale** | **bool** | A boolean value indicating whether auto-scaling is enabled for this node pool. | [optional] 
**min_nodes** | **int** | The minimum number of nodes that this node pool can be auto-scaled to. The value will be &#x60;0&#x60; if &#x60;auto_scale&#x60; is set to &#x60;false&#x60;. | [optional] 
**max_nodes** | **int** | The maximum number of nodes that this node pool can be auto-scaled to. The value will be &#x60;0&#x60; if &#x60;auto_scale&#x60; is set to &#x60;false&#x60;. | [optional] 
**nodes** | [**[Node]**](Node.md) | An object specifying the details of a specific worker node in a node pool. | [optional] [readonly] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


