# FirewallRuleBase


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**protocol** | **str** | The type of traffic to be allowed. This may be one of &#x60;tcp&#x60;, &#x60;udp&#x60;, or &#x60;icmp&#x60;. | 
**ports** | **str** | The ports on which traffic will be allowed specified as a string containing a single port, a range (e.g. \&quot;8000-9000\&quot;), or \&quot;0\&quot; when all ports are open for a protocol. For ICMP rules this parameter will always return \&quot;0\&quot;. | 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


