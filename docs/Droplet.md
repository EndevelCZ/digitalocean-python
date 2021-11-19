# Droplet


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | A unique identifier for each Droplet instance. This is automatically generated upon Droplet creation. | 
**name** | **str** | The human-readable name set for the Droplet instance. | 
**memory** | **int** | Memory of the Droplet in megabytes. | 
**vcpus** | **int** | The number of virtual CPUs. | 
**disk** | **int** | The size of the Droplet&#39;s disk in gigabytes. | 
**locked** | **bool** | A boolean value indicating whether the Droplet has been locked, preventing actions by users. | 
**status** | **str** | A status string indicating the state of the Droplet instance. This may be \&quot;new\&quot;, \&quot;active\&quot;, \&quot;off\&quot;, or \&quot;archive\&quot;. | 
**kernel** | [**Kernel**](Kernel.md) |  | 
**created_at** | **datetime** | A time value given in ISO8601 combined date and time format that represents when the Droplet was created. | 
**features** | **[str]** | An array of features enabled on this Droplet. | 
**backup_ids** | **[int]** | An array of backup IDs of any backups that have been taken of the Droplet instance.  Droplet backups are enabled at the time of the instance creation. | 
**next_backup_window** | [**DropletNextBackupWindow**](DropletNextBackupWindow.md) |  | 
**snapshot_ids** | **[int]** | An array of snapshot IDs of any snapshots created from the Droplet instance. | 
**image** | [**Image**](Image.md) |  | 
**volume_ids** | **[str]** | A flat array including the unique identifier for each Block Storage volume attached to the Droplet. | 
**size** | [**Size**](Size.md) |  | 
**size_slug** | **str** | The unique slug identifier for the size of this Droplet. | 
**networks** | [**DropletNetworks**](DropletNetworks.md) |  | 
**region** | [**Region**](Region.md) |  | 
**tags** | **[str]** | An array of Tags the Droplet has been tagged with. | 
**vpc_uuid** | **str** | A string specifying the UUID of the VPC to which the Droplet is assigned. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


