# VpcDefault


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**default** | **bool** | A boolean value indicating whether or not the VPC is the default network for the region. All applicable resources are placed into the default VPC network unless otherwise specified during their creation. The &#x60;default&#x60; field cannot be unset from &#x60;true&#x60;. If you want to set a new default VPC network, update the &#x60;default&#x60; field of another VPC network in the same region. The previous network&#39;s &#x60;default&#x60; field will be set to &#x60;false&#x60; when a new default VPC has been defined. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


