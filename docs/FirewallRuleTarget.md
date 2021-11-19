# FirewallRuleTarget


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**addresses** | **[str]** | An array of strings containing the IPv4 addresses, IPv6 addresses, IPv4 CIDRs, and/or IPv6 CIDRs to which the firewall will allow traffic. | [optional] 
**droplet_ids** | **[int]** | An array containing the IDs of the Droplets to which the firewall will allow traffic. | [optional] 
**load_balancer_uids** | **[str]** | An array containing the IDs of the load balancers to which the firewall will allow traffic. | [optional] 
**kubernetes_ids** | **[str]** | An array containing the IDs of the Kubernetes clusters to which the firewall will allow traffic. | [optional] 
**tags** | **bool, date, datetime, dict, float, int, list, str, none_type** |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


