# AppJobSpecAllOf


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kind** | **str** | - UNSPECIFIED: Default job type, will auto-complete to POST_DEPLOY kind. - PRE_DEPLOY: Indicates a job that runs before an app deployment. - POST_DEPLOY: Indicates a job that runs after an app deployment. - FAILED_DEPLOY: Indicates a job that runs after a component fails to deploy. | [optional]  if omitted the server will use the default value of "UNSPECIFIED"
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


