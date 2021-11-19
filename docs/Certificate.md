# Certificate


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | A unique ID that can be used to identify and reference a certificate. | [optional] [readonly] 
**name** | **str** | A unique human-readable name referring to a certificate. | [optional] 
**not_after** | **datetime** | A time value given in ISO8601 combined date and time format that represents the certificate&#39;s expiration date. | [optional] [readonly] 
**sha1_fingerprint** | **str** | A unique identifier generated from the SHA-1 fingerprint of the certificate. | [optional] [readonly] 
**created_at** | **datetime** | A time value given in ISO8601 combined date and time format that represents when the certificate was created. | [optional] [readonly] 
**dns_names** | **[str]** | An array of fully qualified domain names (FQDNs) for which the certificate was issued. | [optional] 
**state** | **str** | A string representing the current state of the certificate. It may be &#x60;pending&#x60;, &#x60;verified&#x60;, or &#x60;error&#x60;. | [optional] [readonly] 
**type** | **str** | A string representing the type of the certificate. The value will be &#x60;custom&#x60; for a user-uploaded certificate or &#x60;lets_encrypt&#x60; for one automatically generated with Let&#39;s Encrypt. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


