# Credentials


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**server** | **str** | The URL used to access the cluster API server. | [optional] 
**certificate_authority_data** | **str** | A base64 encoding of bytes representing the certificate authority data for accessing the cluster. | [optional] 
**client_certificate_data** | **str, none_type** | A base64 encoding of bytes representing the x509 client certificate data for access the cluster. This is only returned for clusters without support for token-based authentication.  Newly created Kubernetes clusters do not return credentials using certificate-based authentication. For additional information, [see here](https://www.digitalocean.com/docs/kubernetes/how-to/connect-to-cluster/#authenticate).  | [optional] 
**client_key_data** | **str, none_type** | A base64 encoding of bytes representing the x509 client key data for access the cluster. This is only returned for clusters without support for token-based authentication.  Newly created Kubernetes clusters do not return credentials using certificate-based authentication. For additional information, [see here](https://www.digitalocean.com/docs/kubernetes/how-to/connect-to-cluster/#authenticate).  | [optional] 
**token** | **str** | An access token used to authenticate with the cluster. This is only returned for clusters with support for token-based authentication. | [optional] 
**expires_at** | **datetime** | A time value given in ISO8601 combined date and time format that represents when the access token expires. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


