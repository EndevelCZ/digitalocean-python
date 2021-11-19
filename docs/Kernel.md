# Kernel

**Note**: All Droplets created after March 2017 use internal kernels by default. These Droplets will have this attribute set to `null`.  The current [kernel](https://www.digitalocean.com/docs/droplets/how-to/kernel/) for Droplets with externally managed kernels. This will initially be set to the kernel of the base image when the Droplet is created. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | A unique number used to identify and reference a specific kernel. | [optional] 
**name** | **str** | The display name of the kernel. This is shown in the web UI and is generally a descriptive title for the kernel in question. | [optional] 
**version** | **str** | A standard kernel version string representing the version, patch, and release information. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


