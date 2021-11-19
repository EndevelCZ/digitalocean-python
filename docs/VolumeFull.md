# VolumeFull


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The unique identifier for the block storage volume. | [optional] [readonly] 
**droplet_ids** | **[int], none_type** | An array containing the IDs of the Droplets the volume is attached to. Note that at this time, a volume can only be attached to a single Droplet. | [optional] [readonly] 
**name** | **str** | A human-readable name for the block storage volume. Must be lowercase and be composed only of numbers, letters and \&quot;-\&quot;, up to a limit of 64 characters. The name must begin with a letter. | [optional] 
**description** | **str** | An optional free-form text field to describe a block storage volume. | [optional] 
**size_gigabytes** | **int** | The size of the block storage volume in GiB (1024^3). | [optional] 
**created_at** | **str** | A time value given in ISO8601 combined date and time format that represents when the block storage volume was created. | [optional] [readonly] 
**tags** | [**TagsArray**](TagsArray.md) |  | [optional] 
**region** | **bool, date, datetime, dict, float, int, list, str, none_type** |  | [optional] [readonly] 
**filesystem_type** | **str** | The type of filesystem currently in-use on the volume. | [optional] 
**filesystem_label** | **str** | The label currently applied to the filesystem. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


