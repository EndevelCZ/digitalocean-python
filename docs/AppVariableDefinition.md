# AppVariableDefinition


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | The variable name | 
**scope** | **str** | - RUN_TIME: Made available only at run-time - BUILD_TIME: Made available only at build-time - RUN_AND_BUILD_TIME: Made available at both build and run-time | [optional]  if omitted the server will use the default value of "RUN_AND_BUILD_TIME"
**type** | **str** | - GENERAL: A plain-text environment variable - SECRET: A secret encrypted environment variable | [optional]  if omitted the server will use the default value of "GENERAL"
**value** | **str** | The value. If the type is &#x60;SECRET&#x60;, the value will be encrypted on first submission. On following submissions, the encrypted value should be used. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


