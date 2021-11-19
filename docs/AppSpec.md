# AppSpec

The desired configuration of an application.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the app. Must be unique across all apps in the same account. | 
**region** | **str** | The slug form of the geographical origin of the app. Default: &#x60;nearest available&#x60; | [optional] 
**domains** | [**[AppDomainSpec]**](AppDomainSpec.md) | A set of hostnames where the application will be available. | [optional] 
**services** | [**[AppServiceSpec]**](AppServiceSpec.md) | Workloads which expose publicy-accessible HTTP services. | [optional] 
**static_sites** | [**[AppStaticSiteSpec]**](AppStaticSiteSpec.md) | Content which can be rendered to static web assets. | [optional] 
**jobs** | [**[AppJobSpec]**](AppJobSpec.md) | Pre and post deployment workloads which do not expose publicly-accessible HTTP routes. | [optional] 
**workers** | [**[AppWorkerSpec]**](AppWorkerSpec.md) | Workloads which do not expose publicly-accessible HTTP services. | [optional] 
**databases** | [**[AppDatabaseSpec]**](AppDatabaseSpec.md) | Database instances which can provide persistence to workloads within the application. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


