# InvoiceSummary


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**invoice_uuid** | **str** | UUID of the invoice | [optional] 
**billing_period** | **str** | Billing period of usage for which the invoice is issued, in &#x60;YYYY-MM&#x60;  format. | [optional] 
**amount** | **str** | Total amount of the invoice, in USD.  This will reflect month-to-date usage in the invoice preview. | [optional] 
**user_name** | **str** | Name of the DigitalOcean customer being invoiced. | [optional] 
**user_billing_address** | **bool, date, datetime, dict, float, int, list, str, none_type** |  | [optional] 
**user_company** | **str** | Company of the DigitalOcean customer being invoiced, if set. | [optional] 
**user_email** | **str** | Email of the DigitalOcean customer being invoiced. | [optional] 
**product_charges** | **bool, date, datetime, dict, float, int, list, str, none_type** |  | [optional] 
**overages** | **bool, date, datetime, dict, float, int, list, str, none_type** |  | [optional] 
**taxes** | **bool, date, datetime, dict, float, int, list, str, none_type** |  | [optional] 
**credits_and_adjustments** | **bool, date, datetime, dict, float, int, list, str, none_type** |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


