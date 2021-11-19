# DomainRecordMx


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The type of the DNS record. For example: A, CNAME, TXT, ... | 
**data** | **str** | Variable data depending on record type. For example, the \&quot;data\&quot; value for an A record would be the IPv4 address to which the domain will be mapped. For a CAA record, it would contain the domain name of the CA being granted permission to issue certificates. | 
**priority** | **int, none_type** | The priority for SRV and MX records. | 
**id** | **int** | A unique identifier for each domain record. | [optional] [readonly] 
**name** | **str** | The host name, alias, or service being defined by the record. | [optional] 
**port** | **int, none_type** | The port for SRV records. | [optional] 
**ttl** | **int** | This value is the time to live for the record, in seconds. This defines the time frame that clients can cache queried information before a refresh should be requested. | [optional] 
**weight** | **int, none_type** | The weight for SRV records. | [optional] 
**flags** | **int, none_type** | An unsigned integer between 0-255 used for CAA records. | [optional] 
**tag** | **str, none_type** | The parameter tag for CAA records. Valid values are \&quot;issue\&quot;, \&quot;issuewild\&quot;, or \&quot;iodef\&quot; | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


