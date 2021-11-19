# AppDatabaseSpec


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name. Must be unique across all components within the same app. | 
**cluster_name** | **str** | The name of the underlying DigitalOcean DBaaS cluster. This is required for production databases. For dev databases, if cluster_name is not set, a new cluster will be provisioned. | [optional] 
**db_name** | **str** | The name of the MySQL or PostgreSQL database to configure. | [optional] 
**db_user** | **str** | The name of the MySQL or PostgreSQL user to configure. | [optional] 
**engine** | **str** | - MYSQL: MySQL - PG: PostgreSQL - REDIS: Redis | [optional]  if omitted the server will use the default value of "UNSET"
**production** | **bool** | Whether this is a production or dev database. | [optional] 
**version** | **str** | The version of the database engine | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


