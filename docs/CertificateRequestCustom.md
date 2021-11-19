# CertificateRequestCustom


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | A unique human-readable name referring to a certificate. | 
**private_key** | **str** | The contents of a PEM-formatted private-key corresponding to the SSL certificate. | 
**leaf_certificate** | **str** | The contents of a PEM-formatted public SSL certificate. | 
**type** | **str** | A string representing the type of the certificate. The value will be &#x60;custom&#x60; for a user-uploaded certificate or &#x60;lets_encrypt&#x60; for one automatically generated with Let&#39;s Encrypt. | [optional] 
**certificate_chain** | **str** | The full PEM-formatted trust chain between the certificate authority&#39;s certificate and your domain&#39;s SSL certificate. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


