# Size


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**slug** | **str** | A human-readable string that is used to uniquely identify each size. | 
**memory** | **int** | The amount of RAM allocated to Droplets created of this size. The value is represented in megabytes. | 
**vcpus** | **int** | The integer of number CPUs allocated to Droplets of this size. | 
**disk** | **int** | The amount of disk space set aside for Droplets of this size. The value is represented in gigabytes. | 
**transfer** | **float** | The amount of transfer bandwidth that is available for Droplets created in this size. This only counts traffic on the public interface. The value is given in terabytes. | 
**price_monthly** | **float** | This attribute describes the monthly cost of this Droplet size if the Droplet is kept for an entire month. The value is measured in US dollars. | 
**price_hourly** | **float** | This describes the price of the Droplet size as measured hourly. The value is measured in US dollars. | 
**regions** | **[str]** | An array containing the region slugs where this size is available for Droplet creates. | 
**description** | **str** | A string describing the class of Droplets created from this size. For example: Basic, General Purpose, CPU-Optimized, Memory-Optimized, or Storage-Optimized. | 
**available** | **bool** | This is a boolean value that represents whether new Droplets can be created with this size. | defaults to True
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


