# VpcCreate


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**region** | **str** | The slug identifier for the region where the VPC will be created. | [optional] 
**ip_range** | **str** | The range of IP addresses in the VPC in CIDR notation. Network ranges cannot overlap with other networks in the same account and must be in range of private addresses as defined in RFC1918. It may not be smaller than &#x60;/24&#x60; nor larger than &#x60;/16&#x60;. If no IP range is specified, a &#x60;/20&#x60; network range is generated that won&#39;t conflict with other VPC networks in your account. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


