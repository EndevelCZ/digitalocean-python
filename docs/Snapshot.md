# Snapshot


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The unique identifier for the snapshot. | 
**name** | **str** | A human-readable name for the snapshot. | 
**created_at** | **datetime** | A time value given in ISO8601 combined date and time format that represents when the snapshot was created. | 
**regions** | **[str]** | An array of the regions that the snapshot is available in. The regions are represented by their identifying slug values. | 
**min_disk_size** | **int** | The minimum size in GB required for a volume or Droplet to use this snapshot. | 
**size_gigabytes** | **float** | The billable size of the snapshot in gigabytes. | 
**resource_id** | **str** | The unique identifier for the resource that the snapshot originated from. | 
**resource_type** | **str** | The type of resource that the snapshot originated from. | 
**tags** | **[str], none_type** | An array of Tags the snapshot has been tagged with. | 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


