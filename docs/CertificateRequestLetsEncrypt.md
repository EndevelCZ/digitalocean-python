# CertificateRequestLetsEncrypt


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | A unique human-readable name referring to a certificate. | 
**dns_names** | **[str]** | An array of fully qualified domain names (FQDNs) for which the certificate was issued. A certificate covering all subdomains can be issued using a wildcard (e.g. &#x60;*.example.com&#x60;). | 
**type** | **str** | A string representing the type of the certificate. The value will be &#x60;custom&#x60; for a user-uploaded certificate or &#x60;lets_encrypt&#x60; for one automatically generated with Let&#39;s Encrypt. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


