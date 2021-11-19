# AppsDeployment


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cause** | **str** |  | [optional] 
**cloned_from** | **str** |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**id** | **str** |  | [optional] 
**jobs** | [**[AppsDeploymentJob]**](AppsDeploymentJob.md) |  | [optional] 
**phase** | [**AppsDeploymentPhase**](AppsDeploymentPhase.md) |  | [optional] 
**phase_last_updated_at** | **datetime** |  | [optional] 
**progress** | [**AppsDeploymentProgress**](AppsDeploymentProgress.md) |  | [optional] 
**services** | [**[AppsDeploymentService]**](AppsDeploymentService.md) |  | [optional] 
**spec** | [**AppSpec**](AppSpec.md) |  | [optional] 
**static_sites** | [**[AppsDeploymentStaticSite]**](AppsDeploymentStaticSite.md) |  | [optional] 
**tier_slug** | **str** |  | [optional] [readonly] 
**updated_at** | **datetime** |  | [optional] 
**workers** | [**[AppsDeploymentWorker]**](AppsDeploymentWorker.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


