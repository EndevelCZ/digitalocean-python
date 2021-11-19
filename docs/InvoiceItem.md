# InvoiceItem


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**product** | **str** | Name of the product being billed in the invoice item. | [optional] 
**resource_uuid** | **str** | UUID of the resource billing in the invoice item if available. | [optional] 
**resource_id** | **str** | ID of the resource billing in the invoice item if available. | [optional] 
**group_description** | **str** | Description of the invoice item when it is a grouped set of usage, such  as DOKS or databases. | [optional] 
**description** | **str** | Description of the invoice item. | [optional] 
**amount** | **str** | Billed amount of this invoice item. Billed in USD. | [optional] 
**duration** | **str** | Duration of time this invoice item was used and subsequently billed. | [optional] 
**duration_unit** | **str** | Unit of time for duration. | [optional] 
**start_time** | **str** | Time the invoice item began to be billed for usage. | [optional] 
**end_time** | **str** | Time the invoice item stoped being billed for usage. | [optional] 
**project_name** | **str** | Name of the DigitalOcean Project this resource belongs to. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


