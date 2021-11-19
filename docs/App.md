# App

An application's configuration and status.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**spec** | [**AppSpec**](AppSpec.md) |  | 
**active_deployment** | [**AppsDeployment**](AppsDeployment.md) |  | [optional] 
**created_at** | **datetime** |  | [optional] [readonly] 
**default_ingress** | **str** |  | [optional] [readonly] 
**domains** | [**[AppsDomain]**](AppsDomain.md) |  | [optional] [readonly] 
**id** | **str** |  | [optional] [readonly] 
**in_progress_deployment** | [**AppsDeployment**](AppsDeployment.md) |  | [optional] 
**last_deployment_created_at** | **datetime** |  | [optional] [readonly] 
**live_domain** | **str** |  | [optional] [readonly] 
**live_url** | **str** |  | [optional] [readonly] 
**live_url_base** | **str** |  | [optional] [readonly] 
**owner_uuid** | **str** |  | [optional] [readonly] 
**region** | [**AppsRegion**](AppsRegion.md) |  | [optional] 
**tier_slug** | **str** |  | [optional] [readonly] 
**updated_at** | **datetime** |  | [optional] [readonly] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


