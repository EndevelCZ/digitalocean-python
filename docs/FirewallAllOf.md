# FirewallAllOf


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | A unique ID that can be used to identify and reference a firewall. | [optional] [readonly] 
**status** | **str** | A status string indicating the current state of the firewall. This can be \&quot;waiting\&quot;, \&quot;succeeded\&quot;, or \&quot;failed\&quot;. | [optional] [readonly] 
**created_at** | **datetime** | A time value given in ISO8601 combined date and time format that represents when the firewall was created. | [optional] [readonly] 
**pending_changes** | [**[FirewallAllOfPendingChanges]**](FirewallAllOfPendingChanges.md) | An array of objects each containing the fields \&quot;droplet_id\&quot;, \&quot;removing\&quot;, and \&quot;status\&quot;. It is provided to detail exactly which Droplets are having their security policies updated. When empty, all changes have been successfully applied. | [optional] [readonly] 
**name** | **str** | A human-readable name for a firewall. The name must begin with an alphanumeric character. Subsequent characters must either be alphanumeric characters, a period (.), or a dash (-). | [optional] 
**droplet_ids** | **[int], none_type** | An array containing the IDs of the Droplets assigned to the firewall. | [optional] 
**tags** | **bool, date, datetime, dict, float, int, list, str, none_type** |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


