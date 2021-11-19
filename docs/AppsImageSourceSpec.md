# AppsImageSourceSpec


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**registry** | **str** | The registry name. Must be left empty for the &#x60;DOCR&#x60; registry type. | [optional] 
**registry_type** | **str** | - DOCKER_HUB: The DockerHub container registry type. - DOCR: The DigitalOcean container registry type. | [optional] 
**repository** | **str** | The repository name. | [optional] 
**tag** | **str** | The repository tag. Defaults to &#x60;latest&#x60; if not provided. | [optional]  if omitted the server will use the default value of "latest"
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


