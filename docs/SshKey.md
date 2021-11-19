# SshKey


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**public_key** | **str** | The entire public key string that was uploaded. Embedded into the root user&#39;s &#x60;authorized_keys&#x60; file if you include this key during Droplet creation. | 
**name** | **str** | A human-readable display name for this key, used to easily identify the SSH keys when they are displayed. | 
**id** | **int** | A unique identification number for this key. Can be used to embed a  specific SSH key into a Droplet. | [optional] [readonly] 
**fingerprint** | **str** | A unique identifier that differentiates this key from other keys using  a format that SSH recognizes. The fingerprint is created when the key is added to your account. | [optional] [readonly] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


