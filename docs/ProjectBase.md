# ProjectBase


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The unique universal identifier of this project. | [optional] [readonly] 
**owner_uuid** | **str** | The unique universal identifier of the project owner. | [optional] [readonly] 
**owner_id** | **int** | The integer id of the project owner. | [optional] [readonly] 
**name** | **str** | The human-readable name for the project. The maximum length is 175 characters and the name must be unique. | [optional] 
**description** | **str** | The description of the project. The maximum length is 255 characters. | [optional] 
**purpose** | **str** | The purpose of the project. The maximum length is 255 characters. It can have one of the following values:  - Just trying out DigitalOcean - Class project / Educational purposes - Website or blog - Web Application - Service or API - Mobile Application - Machine learning / AI / Data processing - IoT - Operational / Developer tooling  If another value for purpose is specified, for example, \&quot;your custom purpose\&quot;, your purpose will be stored as &#x60;Other: your custom purpose&#x60;.  | [optional] 
**environment** | **str** | The environment of the project&#39;s resources. | [optional] 
**created_at** | **datetime** | A time value given in ISO8601 combined date and time format that represents when the project was created. | [optional] [readonly] 
**updated_at** | **datetime** | A time value given in ISO8601 combined date and time format that represents when the project was updated. | [optional] [readonly] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


