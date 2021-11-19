# KubernetesNodePoolTaint


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | An arbitrary string. The &#x60;key&#x60; and &#x60;value&#x60; fields of the &#x60;taint&#x60; object form a key-value pair. For example, if the value of the &#x60;key&#x60; field is \&quot;special\&quot; and the value of the &#x60;value&#x60; field is \&quot;gpu\&quot;, the key value pair would be &#x60;special&#x3D;gpu&#x60;. | [optional] 
**value** | **str** | An arbitrary string. The &#x60;key&#x60; and &#x60;value&#x60; fields of the &#x60;taint&#x60; object form a key-value pair. For example, if the value of the &#x60;key&#x60; field is \&quot;special\&quot; and the value of the &#x60;value&#x60; field is \&quot;gpu\&quot;, the key value pair would be &#x60;special&#x3D;gpu&#x60;. | [optional] 
**effect** | **str** | How the node reacts to pods that it won&#39;t tolerate. Available effect values are &#x60;NoSchedule&#x60;, &#x60;PreferNoSchedule&#x60;, and &#x60;NoExecute&#x60;. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


