# NewVolumeExt4


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | A human-readable name for the block storage volume. Must be lowercase and be composed only of numbers, letters and \&quot;-\&quot;, up to a limit of 64 characters. The name must begin with a letter. | 
**size_gigabytes** | **int** | The size of the block storage volume in GiB (1024^3). | 
**region** | [**RegionSlug**](RegionSlug.md) |  | 
**filesystem_type** | **str** | The name of the filesystem type to be used on the volume. When provided, the volume will automatically be formatted to the specified filesystem type. Currently, the available options are &#x60;ext4&#x60; and &#x60;xfs&#x60;. Pre-formatted volumes are automatically mounted when attached to Ubuntu, Debian, Fedora, Fedora Atomic, and CentOS Droplets created on or after April 26, 2018. Attaching pre-formatted volumes to other Droplets is not recommended. | 
**id** | **str** | The unique identifier for the block storage volume. | [optional] [readonly] 
**droplet_ids** | **[int], none_type** | An array containing the IDs of the Droplets the volume is attached to. Note that at this time, a volume can only be attached to a single Droplet. | [optional] [readonly] 
**description** | **str** | An optional free-form text field to describe a block storage volume. | [optional] 
**created_at** | **str** | A time value given in ISO8601 combined date and time format that represents when the block storage volume was created. | [optional] [readonly] 
**tags** | [**TagsArray**](TagsArray.md) |  | [optional] 
**snapshot_id** | **str** | The unique identifier for the volume snapshot from which to create the volume. | [optional] 
**filesystem_label** | **bool, date, datetime, dict, float, int, list, str, none_type** |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


