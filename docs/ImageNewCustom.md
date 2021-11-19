# ImageNewCustom


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The display name that has been given to an image.  This is what is shown in the control panel and is generally a descriptive title for the image in question. | 
**url** | **str** | A URL from which the custom Linux virtual machine image may be retrieved.  The image it points to must be in the raw, qcow2, vhdx, vdi, or vmdk format.  It may be compressed using gzip or bzip2 and must be smaller than 100 GB after being decompressed. | 
**region** | [**RegionSlug**](RegionSlug.md) |  | 
**distribution** | [**Distribution**](Distribution.md) |  | [optional] 
**description** | **str** | An optional free-form text field to describe an image. | [optional] 
**tags** | [**TagsArray**](TagsArray.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


