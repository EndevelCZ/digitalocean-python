# Image


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | A unique number that can be used to identify and reference a specific image. | [optional] [readonly] 
**name** | **str** | The display name that has been given to an image.  This is what is shown in the control panel and is generally a descriptive title for the image in question. | [optional] 
**type** | **str** | Describes the kind of image. It may be one of \&quot;snapshot\&quot;, \&quot;backup\&quot;, or \&quot;custom\&quot;. This specifies whether an image is a user-generated Droplet snapshot, automatically created Droplet backup, or a user-provided virtual machine image. | [optional] 
**distribution** | [**Distribution**](Distribution.md) |  | [optional] 
**slug** | **str, none_type** | A uniquely identifying string that is associated with each of the DigitalOcean-provided public images. These can be used to reference a public image as an alternative to the numeric id. | [optional] 
**public** | **bool** | This is a boolean value that indicates whether the image in question is public or not. An image that is public is available to all accounts. A non-public image is only accessible from your account. | [optional] 
**regions** | [**RegionsArray**](RegionsArray.md) |  | [optional] 
**created_at** | **datetime** | A time value given in ISO8601 combined date and time format that represents when the image was created. | [optional] 
**min_disk_size** | **int, none_type** | The minimum disk size in GB required for a Droplet to use this image. | [optional] 
**size_gigabytes** | **float, none_type** | The size of the image in gigabytes. | [optional] 
**description** | **str** | An optional free-form text field to describe an image. | [optional] 
**tags** | [**TagsArray**](TagsArray.md) |  | [optional] 
**status** | **str** | A status string indicating the state of a custom image. This may be &#x60;NEW&#x60;,  &#x60;available&#x60;, &#x60;pending&#x60;, &#x60;deleted&#x60;, or &#x60;retired&#x60;. | [optional] 
**error_message** | **str** | A string containing information about errors that may occur when importing  a custom image. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


