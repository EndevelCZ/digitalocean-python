# AppsDeploymentProgressStep


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**component_name** | **str** |  | [optional] 
**ended_at** | **datetime** |  | [optional] 
**message_base** | **str** | The base of a human-readable description of the step intended to be combined with the component name for presentation. For example:  &#x60;message_base&#x60; &#x3D; \&quot;Building service\&quot; &#x60;component_name&#x60; &#x3D; \&quot;api\&quot; | [optional] 
**name** | **str** |  | [optional] 
**reason** | [**AppsDeploymentProgressStepReason**](AppsDeploymentProgressStepReason.md) |  | [optional] 
**started_at** | **datetime** |  | [optional] 
**status** | [**AppsDeploymentProgressStepStatus**](AppsDeploymentProgressStepStatus.md) |  | [optional] 
**steps** | **[{str: (bool, date, datetime, dict, float, int, list, str, none_type)}]** |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


