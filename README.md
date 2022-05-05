# Digital ocean openapi-client
# Introduction

The DigitalOcean API allows you to manage Droplets and resources within the
DigitalOcean cloud in a simple, programmatic way using conventional HTTP requests.

All of the functionality that you are familiar with in the DigitalOcean
control panel is also available through the API, allowing you to script the
complex actions that your situation requires.

The API documentation will start with a general overview about the design
and technology that has been implemented, followed by reference information
about specific endpoints.

## Requests

Any tool that is fluent in HTTP can communicate with the API simply by
requesting the correct URI. Requests should be made using the HTTPS protocol
so that traffic is encrypted. The interface responds to different methods
depending on the action required.

|Method|Usage|
|--- |--- |
|GET|For simple retrieval of information about your account, Droplets, or environment, you should use the GET method.  The information you request will be returned to you as a JSON object. The attributes defined by the JSON object can be used to form additional requests.  Any request using the GET method is read-only and will not affect any of the objects you are querying.|
|DELETE|To destroy a resource and remove it from your account and environment, the DELETE method should be used.  This will remove the specified object if it is found.  If it is not found, the operation will return a response indicating that the object was not found. This idempotency means that you do not have to check for a resource's availability prior to issuing a delete command, the final state will be the same regardless of its existence.|
|PUT|To update the information about a resource in your account, the PUT method is available. Like the DELETE Method, the PUT method is idempotent.  It sets the state of the target using the provided values, regardless of their current values. Requests using the PUT method do not need to check the current attributes of the object.|
|PATCH|Some resources support partial modification. In these cases, the PATCH method is available. Unlike PUT which generally requires a complete representation of a resource, a PATCH request is is a set of instructions on how to modify a resource updating only specific attributes.|
|POST|To create a new object, your request should specify the POST method. The POST request includes all of the attributes necessary to create a new object.  When you wish to create a new object, send a POST request to the target endpoint.|
|HEAD|Finally, to retrieve metadata information, you should use the HEAD method to get the headers.  This returns only the header of what would be returned with an associated GET request. Response headers contain some useful information about your API access and the results that are available for your request. For instance, the headers contain your current rate-limit value and the amount of time available until the limit resets. It also contains metrics about the total number of objects found, pagination information, and the total content length.|


## HTTP Statuses

Along with the HTTP methods that the API responds to, it will also return
standard HTTP statuses, including error codes.

In the event of a problem, the status will contain the error code, while the
body of the response will usually contain additional information about the
problem that was encountered.

In general, if the status returned is in the 200 range, it indicates that
the request was fulfilled successfully and that no error was encountered.

Return codes in the 400 range typically indicate that there was an issue
with the request that was sent. Among other things, this could mean that you
did not authenticate correctly, that you are requesting an action that you
do not have authorization for, that the object you are requesting does not
exist, or that your request is malformed.

If you receive a status in the 500 range, this generally indicates a
server-side problem. This means that we are having an issue on our end and
cannot fulfill your request currently.

400 and 500 level error responses will include a JSON object in their body,
including the following attributes:

|Name|Type|Description|
|--- |--- |--- |
|id|string|A short identifier corresponding to the HTTP status code returned. For example, the ID for a response returning a 404 status code would be \"not_found.\"|
|message|string|A message providing additional information about the error, including details to help resolve it when possible.|
|request_id|string|Optionally, some endpoints may include a request ID that should be provided when reporting bugs or opening support tickets to help identify the issue.|

### Example Error Response

```
    HTTP/1.1 403 Forbidden
    {
      \"id\":       \"forbidden\",
      \"message\":  \"You do not have access for the attempted action.\"
    }
```

## Responses

When a request is successful, a response body will typically be sent back in
the form of a JSON object. An exception to this is when a DELETE request is
processed, which will result in a successful HTTP 204 status and an empty
response body.

Inside of this JSON object, the resource root that was the target of the
request will be set as the key. This will be the singular form of the word
if the request operated on a single object, and the plural form of the word
if a collection was processed.

For example, if you send a GET request to `/v2/droplets/$DROPLET_ID` you
will get back an object with a key called \"`droplet`\". However, if you send
the GET request to the general collection at `/v2/droplets`, you will get
back an object with a key called \"`droplets`\".

The value of these keys will generally be a JSON object for a request on a
single object and an array of objects for a request on a collection of
objects.

### Response for a Single Object

```
    {
        \"droplet\": {
            \"name\": \"example.com\"
            . . .
        }
    }
```

### Response for an Object Collection

```
    {
        \"droplets\": [
            {
                \"name\": \"example.com\"
                . . .
            },
            {
                \"name\": \"second.com\"
                . . .
            }
        ]
    }
```

## Meta

In addition to the main resource root, the response may also contain a
`meta` object. This object contains information about the response itself.

The `meta` object contains a `total` key that is set to the total number of
objects returned by the request. This has implications on the `links` object
and pagination.

The `meta` object will only be displayed when it has a value. Currently, the
`meta` object will have a value when a request is made on a collection (like
`droplets` or `domains`).


### Sample Meta Object

```
    {
        . . .
        \"meta\": {
            \"total\": 43
        }
        . . .
    }
```

## Links & Pagination

The `links` object is returned as part of the response body when pagination
is enabled. By default, 20 objects are returned per page. If the response
contains 20 objects or fewer, no `links` object will be returned. If the
response contains more than 20 objects, the first 20 will be returned along
with the `links` object.

You can request a different pagination limit or force pagination by
appending `?per_page=` to the request with the number of items you would
like per page. For instance, to show only two results per page, you could
add `?per_page=2` to the end of your query. The maximum number of results
per page is 200.

The `links` object contains a `pages` object. The `pages` object, in turn,
contains keys indicating the relationship of additional pages. The values of
these are the URLs of the associated pages. The keys will be one of the
following:

*   **first**: The URI of the first page of results.
*   **prev**: The URI of the previous sequential page of results.
*   **next**: The URI of the next sequential page of results.
*   **last**: The URI of the last page of results.

The `pages` object will only include the links that make sense. So for the
first page of results, no `first` or `prev` links will ever be set. This
convention holds true in other situations where a link would not make sense.

### Sample Links Object

```
    {
        . . .
        \"links\": {
            \"pages\": {
                \"last\": \"https://api.digitalocean.com/v2/images?page=2\",
                \"next\": \"https://api.digitalocean.com/v2/images?page=2\"
            }
        }
        . . .
    }
```

## Rate Limit

Requests through the API are rate limited per OAuth token. Current rate limits:

*   5,000 requests per hour
*   250 requests per minute (5% of the hourly total)

Once you exceed either limit, you will be rate limited until the next cycle
starts. Space out any requests that you would otherwise issue in bursts for
the best results.

The rate limiting information is contained within the response headers of
each request. The relevant headers are:

*   **RateLimit-Limit**: The number of requests that can be made per hour.
*   **RateLimit-Remaining**: The number of requests that remain before you hit your request limit. See the information below for how the request limits expire.
*   **RateLimit-Reset**: This represents the time when the oldest request will expire. The value is given in [Unix epoch time](http://en.wikipedia.org/wiki/Unix_time). See below for more information about how request limits expire.

As long as the `RateLimit-Remaining` count is above zero, you will be able
to make additional requests.

The way that a request expires and is removed from the current limit count
is important to understand. Rather than counting all of the requests for an
hour and resetting the `RateLimit-Remaining` value at the end of the hour,
each request instead has its own timer.

This means that each request contributes toward the `RateLimit-Remaining`
count for one complete hour after the request is made. When that request's
timer runs out, it is no longer counted towards the request limit.

This has implications on the meaning of the `RateLimit-Reset` header as
well. Because the entire rate limit is not reset at one time, the value of
this header is set to the time when the _oldest_ request will expire.

Keep this in mind if you see your `RateLimit-Reset` value change, but not
move an entire hour into the future.

If the `RateLimit-Remaining` reaches zero, subsequent requests will receive
a 429 error code until the request reset has been reached. You can see the
format of the response in the examples.

**Note:** The following endpoints have special rate limit requirements that
are independent of the limits defined above.

*   Only 12 `POST` requests to the `/v2/floating_ips` endpoint to create Floating IPs can be made per 60 seconds.
*   Only 10 `GET` requests to the `/v2/account/keys` endpoint to list SSH keys can be made per 60 seconds.

### Sample Rate Limit Headers

```
    . . .
    RateLimit-Limit: 1200
    RateLimit-Remaining: 1193
    RateLimit-Reset: 1402425459
    . . .
```

### Sample Rate Exceeded Response

```
    429 Too Many Requests
    {
            id: \"too_many_requests\",
            message: \"API Rate limit exceeded.\"
    }
```

## Curl Examples

Throughout this document, some example API requests will be given using the
`curl` command. This will allow us to demonstrate the various endpoints in a
simple, textual format.

The names of account-specific references (like Droplet IDs, for instance)
will be represented by variables. For instance, a Droplet ID may be
represented by a variable called `$DROPLET_ID`. You can set the associated
variables in your environment if you wish to use the examples without
modification.

The first variable that you should set to get started is your OAuth
authorization token. The next section will go over the details of this, but
you can set an environmental variable for it now.

Generate a token by going to the [Apps & API](https://cloud.digitalocean.com/settings/applications)
section of the DigitalOcean control panel. Use an existing token if you have
saved one, or generate a new token with the \"Generate new token\" button.
Copy the generated token and use it to set and export the TOKEN variable in
your environment as the example shows.

You may also wish to set some other variables now or as you go along. For
example, you may wish to set the `DROPLET_ID` variable to one of your
Droplet IDs since this will be used frequently in the API.

If you are following along, make sure you use a Droplet ID that you control
so that your commands will execute correctly.

If you need access to the headers of a response through `curl`, you can pass
the `-i` flag to display the header information along with the body. If you
are only interested in the header, you can instead pass the `-I` flag, which
will exclude the response body entirely.

### Set and Export your OAuth Token

```
export DIGITALOCEAN_TOKEN=your_token_here
```

### Set and Export a Variable

```
export DROPLET_ID=1111111
```

## Parameters

There are two different ways to pass parameters in a request with the API.

When passing parameters to create or update an object, parameters should be
passed as a JSON object containing the appropriate attribute names and
values as key-value pairs. When you use this format, you should specify that
you are sending a JSON object in the header. This is done by setting the
`Content-Type` header to `application/json`. This ensures that your request
is interpreted correctly.

When passing parameters to filter a response on GET requests, parameters can
be passed using standard query attributes. In this case, the parameters
would be embedded into the URI itself by appending a `?` to the end of the
URI and then setting each attribute with an equal sign. Attributes can be
separated with a `&`. Tools like `curl` can create the appropriate URI when
given parameters and values; this can also be done using the `-F` flag and
then passing the key and value as an argument. The argument should take the
form of a quoted string with the attribute being set to a value with an
equal sign.

### Pass Parameters as a JSON Object

```
    curl -H \"Authorization: Bearer $DIGITALOCEAN_TOKEN\" \\
        -H \"Content-Type: application/json\" \\
        -d '{\"name\": \"example.com\", \"ip_address\": \"127.0.0.1\"}' \\
        -X POST \"https://api.digitalocean.com/v2/domains\"
```

### Pass Filter Parameters as a Query String

```
     curl -H \"Authorization: Bearer $DIGITALOCEAN_TOKEN\" \\
         -X GET \\
         \"https://api.digitalocean.com/v2/images?private=true\"
```

## Cross Origin Resource Sharing

In order to make requests to the API from other domains, the API implements
Cross Origin Resource Sharing (CORS) support.

CORS support is generally used to create AJAX requests outside of the domain
that the request originated from. This is necessary to implement projects
like control panels utilizing the API. This tells the browser that it can
send requests to an outside domain.

The procedure that the browser initiates in order to perform these actions
(other than GET requests) begins by sending a \"preflight\" request. This sets
the `Origin` header and uses the `OPTIONS` method. The server will reply
back with the methods it allows and some of the limits it imposes. The
client then sends the actual request if it falls within the allowed
constraints.

This process is usually done in the background by the browser, but you can
use curl to emulate this process using the example provided. The headers
that will be set to show the constraints are:

*   **Access-Control-Allow-Origin**: This is the domain that is sent by the client or browser as the origin of the request. It is set through an `Origin` header.
*   **Access-Control-Allow-Methods**: This specifies the allowed options for requests from that domain. This will generally be all available methods.
*   **Access-Control-Expose-Headers**: This will contain the headers that will be available to requests from the origin domain.
*   **Access-Control-Max-Age**: This is the length of time that the access is considered valid. After this expires, a new preflight should be sent.
*   **Access-Control-Allow-Credentials**: This will be set to `true`. It basically allows you to send your OAuth token for authentication.

You should not need to be concerned with the details of these headers,
because the browser will typically do all of the work for you.


This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: 2.0
- Package version: 1.0.0
- Build package: org.openapitools.codegen.languages.PythonClientCodegen

## Requirements.

Python >= 3.6

## Installation & Usage
### pip install

If the python package is hosted on a repository, you can install directly using:

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import digitalocean_client
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import digitalocean_client
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python

import time
import digitalocean_client
from pprint import pprint
from digitalocean_client.api import 1_click_applications_api
from digitalocean_client.model.error import Error
from digitalocean_client.model.inline_response200 import InlineResponse200
from digitalocean_client.model.model1_click_create import Model1ClickCreate
# Defining the host is optional and defaults to https://api.digitalocean.com
# See configuration.py for a list of all supported configuration parameters.
configuration = digitalocean_client.Configuration(
    host = "https://api.digitalocean.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: bearer_auth
configuration = digitalocean_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)


# Enter a context with an instance of the API client
with digitalocean_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = 1_click_applications_api.ClickApplicationsApi(api_client)
    model1_click_create = Model1ClickCreate(
        addon_slugs=["kube-state-metrics","loki"],
        cluster_uuid="50a994b6-c303-438f-9495-7e896cfe6b08",
    ) # Model1ClickCreate | 

    try:
        # Install Kubernetes 1-Click Applications
        api_response = api_instance.install_kubernetes(model1_click_create)
        pprint(api_response)
    except digitalocean_client.ApiException as e:
        print("Exception when calling ClickApplicationsApi->install_kubernetes: %s\n" % e)
```

## Documentation for API Endpoints

All URIs are relative to *https://api.digitalocean.com*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*ClickApplicationsApi* | [**install_kubernetes**](docs/ClickApplicationsApi.md#install_kubernetes) | **POST** /v2/1-clicks/kubernetes | Install Kubernetes 1-Click Applications
*ClickApplicationsApi* | [**list**](docs/ClickApplicationsApi.md#list) | **GET** /v2/1-clicks | List 1-Click Applications
*AccountApi* | [**get_user_information**](docs/AccountApi.md#get_user_information) | **GET** /v2/account | Get User Information
*ActionsApi* | [**get_action**](docs/ActionsApi.md#get_action) | **GET** /v2/actions/{action_id} | Retrieve an Existing Action
*ActionsApi* | [**list_all_actions**](docs/ActionsApi.md#list_all_actions) | **GET** /v2/actions | List All Actions
*AppsApi* | [**assign_alert_destinations**](docs/AppsApi.md#assign_alert_destinations) | **POST** /v2/apps/{app_id}/alerts/{alert_id}/destinations | Update destinations for alerts
*AppsApi* | [**create_app**](docs/AppsApi.md#create_app) | **POST** /v2/apps | Create a New App
*AppsApi* | [**create_deployment**](docs/AppsApi.md#create_deployment) | **POST** /v2/apps/{app_id}/deployments | Create an App Deployment
*AppsApi* | [**delete_app**](docs/AppsApi.md#delete_app) | **DELETE** /v2/apps/{id} | Delete an App
*AppsApi* | [**get_app**](docs/AppsApi.md#get_app) | **GET** /v2/apps/{id} | Retrieve an Existing App
*AppsApi* | [**get_deployment**](docs/AppsApi.md#get_deployment) | **GET** /v2/apps/{app_id}/deployments/{deployment_id} | Retrieve an App Deployment
*AppsApi* | [**get_instance_size**](docs/AppsApi.md#get_instance_size) | **GET** /v2/apps/tiers/instance_sizes/{slug} | Retrieve an Instance Size
*AppsApi* | [**get_logs**](docs/AppsApi.md#get_logs) | **GET** /v2/apps/{app_id}/deployments/{deployment_id}/components/{component_name}/logs | Retrieve Deployment Logs
*AppsApi* | [**get_logs_aggregate**](docs/AppsApi.md#get_logs_aggregate) | **GET** /v2/apps/{app_id}/deployments/{deployment_id}/logs | Retrieve Aggregate Deployment Logs
*AppsApi* | [**get_tier**](docs/AppsApi.md#get_tier) | **GET** /v2/apps/tiers/{slug} | Retrieve an App Tier
*AppsApi* | [**list_alerts**](docs/AppsApi.md#list_alerts) | **GET** /v2/apps/{app_id}/alerts | List all app alerts
*AppsApi* | [**list_apps**](docs/AppsApi.md#list_apps) | **GET** /v2/apps | List All Apps
*AppsApi* | [**list_deployments**](docs/AppsApi.md#list_deployments) | **GET** /v2/apps/{app_id}/deployments | List App Deployments
*AppsApi* | [**list_instance_sizes**](docs/AppsApi.md#list_instance_sizes) | **GET** /v2/apps/tiers/instance_sizes | List Instance Sizes
*AppsApi* | [**list_regions**](docs/AppsApi.md#list_regions) | **GET** /v2/apps/regions | List App Regions
*AppsApi* | [**list_tiers**](docs/AppsApi.md#list_tiers) | **GET** /v2/apps/tiers | List App Tiers
*AppsApi* | [**post_cancel_deployment**](docs/AppsApi.md#post_cancel_deployment) | **POST** /v2/apps/{app_id}/deployments/{deployment_id}/cancel | Cancel a Deployment
*AppsApi* | [**update_app**](docs/AppsApi.md#update_app) | **PUT** /v2/apps/{id} | Update an App
*AppsApi* | [**validate_app_spec**](docs/AppsApi.md#validate_app_spec) | **POST** /v2/apps/propose | Propose an App Spec
*BillingApi* | [**get_customer_balance**](docs/BillingApi.md#get_customer_balance) | **GET** /v2/customers/my/balance | Get Customer Balance
*BillingApi* | [**get_invoice_by_uuid**](docs/BillingApi.md#get_invoice_by_uuid) | **GET** /v2/customers/my/invoices/{invoice_uuid} | Retrieve an Invoice by UUID
*BillingApi* | [**get_invoice_csv_by_uuid**](docs/BillingApi.md#get_invoice_csv_by_uuid) | **GET** /v2/customers/my/invoices/{invoice_uuid}/csv | Retrieve an Invoice CSV by UUID
*BillingApi* | [**get_invoice_pdf_by_uuid**](docs/BillingApi.md#get_invoice_pdf_by_uuid) | **GET** /v2/customers/my/invoices/{invoice_uuid}/pdf | Retrieve an Invoice PDF by UUID
*BillingApi* | [**get_invoice_summary_by_uuid**](docs/BillingApi.md#get_invoice_summary_by_uuid) | **GET** /v2/customers/my/invoices/{invoice_uuid}/summary | Retrieve an Invoice Summary by UUID
*BillingApi* | [**list_billing_history**](docs/BillingApi.md#list_billing_history) | **GET** /v2/customers/my/billing_history | List Billing History
*BillingApi* | [**list_invoices**](docs/BillingApi.md#list_invoices) | **GET** /v2/customers/my/invoices | List All Invoices
*BlockStorageApi* | [**create_new_volume**](docs/BlockStorageApi.md#create_new_volume) | **POST** /v2/volumes | Create a New Block Storage Volume
*BlockStorageApi* | [**create_volume_snapshot**](docs/BlockStorageApi.md#create_volume_snapshot) | **POST** /v2/volumes/{volume_id}/snapshots | Create Snapshot from a Volume
*BlockStorageApi* | [**delete_volume**](docs/BlockStorageApi.md#delete_volume) | **DELETE** /v2/volumes/{volume_id} | Delete a Block Storage Volume
*BlockStorageApi* | [**delete_volume_by_name**](docs/BlockStorageApi.md#delete_volume_by_name) | **DELETE** /v2/volumes | Delete a Block Storage Volume by Name
*BlockStorageApi* | [**delete_volume_snapshot_by_id**](docs/BlockStorageApi.md#delete_volume_snapshot_by_id) | **DELETE** /v2/volumes/snapshot/{snapshot_id} | Delete a Volume Snapshot
*BlockStorageApi* | [**get_volume**](docs/BlockStorageApi.md#get_volume) | **GET** /v2/volumes/{volume_id} | Retrieve an Existing Block Storage Volume
*BlockStorageApi* | [**get_volume_snapshot_by_id**](docs/BlockStorageApi.md#get_volume_snapshot_by_id) | **GET** /v2/volumes/snapshot/{snapshot_id} | Retreive an Existing Volume Snapshot
*BlockStorageApi* | [**list_all_volumes**](docs/BlockStorageApi.md#list_all_volumes) | **GET** /v2/volumes | List All Block Storage Volumes
*BlockStorageApi* | [**list_volume_snapshots**](docs/BlockStorageApi.md#list_volume_snapshots) | **GET** /v2/volumes/{volume_id}/snapshots | List Snapshots for a Volume
*BlockStorageActionsApi* | [**get_volume_action**](docs/BlockStorageActionsApi.md#get_volume_action) | **GET** /v2/volumes/{volume_id}/actions/{action_id} | Retrieve an Existing Volume Action
*BlockStorageActionsApi* | [**list_all_volume_actions**](docs/BlockStorageActionsApi.md#list_all_volume_actions) | **GET** /v2/volumes/{volume_id}/actions | List All Actions for a Volume
*BlockStorageActionsApi* | [**post_volume_action_by_id**](docs/BlockStorageActionsApi.md#post_volume_action_by_id) | **POST** /v2/volumes/{volume_id}/actions | Initiate A Block Storage Action By Volume Id
*BlockStorageActionsApi* | [**post_volume_action_by_name**](docs/BlockStorageActionsApi.md#post_volume_action_by_name) | **POST** /v2/volumes/actions | Initiate A Block Storage Action By Volume Name
*CDNEndpointsApi* | [**create_cdn_endpoint**](docs/CDNEndpointsApi.md#create_cdn_endpoint) | **POST** /v2/cdn/endpoints | Create a New CDN Endpoint
*CDNEndpointsApi* | [**delete_cdn_endpoint**](docs/CDNEndpointsApi.md#delete_cdn_endpoint) | **DELETE** /v2/cdn/endpoints/{cdn_id} | Delete a CDN Endpoint
*CDNEndpointsApi* | [**get_cdn_endpoint**](docs/CDNEndpointsApi.md#get_cdn_endpoint) | **GET** /v2/cdn/endpoints/{cdn_id} | Retrieve an Existing CDN Endpoint
*CDNEndpointsApi* | [**list_cdn_endpoints**](docs/CDNEndpointsApi.md#list_cdn_endpoints) | **GET** /v2/cdn/endpoints | List All CDN Endpoints
*CDNEndpointsApi* | [**purge_cdn_cache**](docs/CDNEndpointsApi.md#purge_cdn_cache) | **DELETE** /v2/cdn/endpoints/{cdn_id}/cache | Purge the Cache for an Existing CDN Endpoint
*CDNEndpointsApi* | [**update_cdn_endpoint**](docs/CDNEndpointsApi.md#update_cdn_endpoint) | **PUT** /v2/cdn/endpoints/{cdn_id} | Update a CDN Endpoint
*CertificatesApi* | [**create_certificates**](docs/CertificatesApi.md#create_certificates) | **POST** /v2/certificates | Create a New Certificate
*CertificatesApi* | [**delete_certificate**](docs/CertificatesApi.md#delete_certificate) | **DELETE** /v2/certificates/{certificate_id} | Delete a Certificate
*CertificatesApi* | [**get_certificate**](docs/CertificatesApi.md#get_certificate) | **GET** /v2/certificates/{certificate_id} | Retrieve an Existing Certificate
*CertificatesApi* | [**list_certificates**](docs/CertificatesApi.md#list_certificates) | **GET** /v2/certificates | List All Certificates
*ContainerRegistryApi* | [**create_registry**](docs/ContainerRegistryApi.md#create_registry) | **POST** /v2/registry | Create Container Registry
*ContainerRegistryApi* | [**delete_registry**](docs/ContainerRegistryApi.md#delete_registry) | **DELETE** /v2/registry | Delete Container Registry
*ContainerRegistryApi* | [**delete_repository_manifest**](docs/ContainerRegistryApi.md#delete_repository_manifest) | **DELETE** /v2/registry/{registry_name}/{repository_name}/digests/{manifest_digest} | Delete Container Registry Repository Manifest
*ContainerRegistryApi* | [**delete_repository_tag**](docs/ContainerRegistryApi.md#delete_repository_tag) | **DELETE** /v2/registry/{registry_name}/{repository_name}/tags/{repository_tag} | Delete Container Registry Repository Tag
*ContainerRegistryApi* | [**get_docker_credentials**](docs/ContainerRegistryApi.md#get_docker_credentials) | **GET** /v2/registry/docker-credentials | Get Docker Credentials for Container Registry
*ContainerRegistryApi* | [**get_garbage_collection**](docs/ContainerRegistryApi.md#get_garbage_collection) | **GET** /v2/registry/{registry_name}/garbage-collection | Get Active Garbage Collection
*ContainerRegistryApi* | [**get_registry**](docs/ContainerRegistryApi.md#get_registry) | **GET** /v2/registry | Get Container Registry Information
*ContainerRegistryApi* | [**get_registry_options**](docs/ContainerRegistryApi.md#get_registry_options) | **GET** /v2/registry/options | List Available Subscription Tiers
*ContainerRegistryApi* | [**get_registry_subscription**](docs/ContainerRegistryApi.md#get_registry_subscription) | **GET** /v2/registry/subscription | Get Subscription Information
*ContainerRegistryApi* | [**list_garbage_collections**](docs/ContainerRegistryApi.md#list_garbage_collections) | **GET** /v2/registry/{registry_name}/garbage-collections | List Garbage Collections
*ContainerRegistryApi* | [**list_registry_repositories**](docs/ContainerRegistryApi.md#list_registry_repositories) | **GET** /v2/registry/{registry_name} | List All Container Registry Repositories
*ContainerRegistryApi* | [**list_repository_tags**](docs/ContainerRegistryApi.md#list_repository_tags) | **GET** /v2/registry/{registry_name}/{repository_name}/tags | List All Container Registry Repository Tags
*ContainerRegistryApi* | [**post_registry_subscription**](docs/ContainerRegistryApi.md#post_registry_subscription) | **POST** /v2/registry/subscription | Update Subscription Tier
*ContainerRegistryApi* | [**run_garbage_collection**](docs/ContainerRegistryApi.md#run_garbage_collection) | **POST** /v2/registry/{registry_name}/garbage-collection | Start Garbage Collection
*ContainerRegistryApi* | [**update_garbage_collection**](docs/ContainerRegistryApi.md#update_garbage_collection) | **PUT** /v2/registry/{registry_name}/garbage-collection/{garbage_collection_uuid} | Update Garbage Collection
*ContainerRegistryApi* | [**validate_registry_name**](docs/ContainerRegistryApi.md#validate_registry_name) | **POST** /v2/registry/validate-name | Validate a Container Registry Name
*DatabasesApi* | [**add_connection_pool**](docs/DatabasesApi.md#add_connection_pool) | **POST** /v2/databases/{database_cluster_uuid}/pools | Add a New Connection Pool (PostgreSQL)
*DatabasesApi* | [**add_database**](docs/DatabasesApi.md#add_database) | **POST** /v2/databases/{database_cluster_uuid}/dbs | Add a New Database
*DatabasesApi* | [**add_user**](docs/DatabasesApi.md#add_user) | **POST** /v2/databases/{database_cluster_uuid}/users | Add a Database User
*DatabasesApi* | [**create_database_cluster**](docs/DatabasesApi.md#create_database_cluster) | **POST** /v2/databases | Create a New Database Cluster
*DatabasesApi* | [**create_replica**](docs/DatabasesApi.md#create_replica) | **POST** /v2/databases/{database_cluster_uuid}/replicas | Create a Read-only Replica
*DatabasesApi* | [**delete_connection_pool**](docs/DatabasesApi.md#delete_connection_pool) | **DELETE** /v2/databases/{database_cluster_uuid}/pools/{pool_name} | Delete a Connection Pool (PostgreSQL)
*DatabasesApi* | [**delete_database**](docs/DatabasesApi.md#delete_database) | **DELETE** /v2/databases/{database_cluster_uuid}/dbs/{database_name} | Delete a Database
*DatabasesApi* | [**delete_online_migration**](docs/DatabasesApi.md#delete_online_migration) | **DELETE** /v2/databases/{database_cluster_uuid}/online-migration/{migration_id} | Stop an Online Migration
*DatabasesApi* | [**delete_user**](docs/DatabasesApi.md#delete_user) | **DELETE** /v2/databases/{database_cluster_uuid}/users/{username} | Remove a Database User
*DatabasesApi* | [**destroy_cluster**](docs/DatabasesApi.md#destroy_cluster) | **DELETE** /v2/databases/{database_cluster_uuid} | Destroy a Database Cluster
*DatabasesApi* | [**destroy_replica**](docs/DatabasesApi.md#destroy_replica) | **DELETE** /v2/databases/{database_cluster_uuid}/replicas/{replica_name} | Destroy a Read-only Replica
*DatabasesApi* | [**get_ca**](docs/DatabasesApi.md#get_ca) | **GET** /v2/databases/{database_cluster_uuid}/ca | Retrieve the Public Certificate
*DatabasesApi* | [**get_connection_pool**](docs/DatabasesApi.md#get_connection_pool) | **GET** /v2/databases/{database_cluster_uuid}/pools/{pool_name} | Retrieve Existing Connection Pool (PostgreSQL)
*DatabasesApi* | [**get_database**](docs/DatabasesApi.md#get_database) | **GET** /v2/databases/{database_cluster_uuid}/dbs/{database_name} | Retrieve an Existing Database
*DatabasesApi* | [**get_database_cluster**](docs/DatabasesApi.md#get_database_cluster) | **GET** /v2/databases/{database_cluster_uuid} | Retrieve an Existing Database Cluster
*DatabasesApi* | [**get_eviction_policy**](docs/DatabasesApi.md#get_eviction_policy) | **GET** /v2/databases/{database_cluster_uuid}/eviction_policy | Retrieve the Eviction Policy for a Redis Cluster
*DatabasesApi* | [**get_migration_status**](docs/DatabasesApi.md#get_migration_status) | **GET** /v2/databases/{database_cluster_uuid}/online-migration | Retrieve the Status of an Online Migration
*DatabasesApi* | [**get_replica**](docs/DatabasesApi.md#get_replica) | **GET** /v2/databases/{database_cluster_uuid}/replicas/{replica_name} | Retrieve an Existing Read-only Replica
*DatabasesApi* | [**get_sql_mode**](docs/DatabasesApi.md#get_sql_mode) | **GET** /v2/databases/{database_cluster_uuid}/sql_mode | Retrieve the SQL Modes for a MySQL Cluster
*DatabasesApi* | [**get_user**](docs/DatabasesApi.md#get_user) | **GET** /v2/databases/{database_cluster_uuid}/users/{username} | Retrieve an Existing Database User
*DatabasesApi* | [**list_connection_pools**](docs/DatabasesApi.md#list_connection_pools) | **GET** /v2/databases/{database_cluster_uuid}/pools | List Connection Pools (PostgreSQL)
*DatabasesApi* | [**list_database_backups**](docs/DatabasesApi.md#list_database_backups) | **GET** /v2/databases/{database_cluster_uuid}/backups | List Backups for a Database Cluster
*DatabasesApi* | [**list_database_clusters**](docs/DatabasesApi.md#list_database_clusters) | **GET** /v2/databases | List All Database Clusters
*DatabasesApi* | [**list_database_firewalls**](docs/DatabasesApi.md#list_database_firewalls) | **GET** /v2/databases/{database_cluster_uuid}/firewall | List Firewall Rules (Trusted Sources) for a Database Cluster
*DatabasesApi* | [**list_databases**](docs/DatabasesApi.md#list_databases) | **GET** /v2/databases/{database_cluster_uuid}/dbs | List All Databases
*DatabasesApi* | [**list_replicas**](docs/DatabasesApi.md#list_replicas) | **GET** /v2/databases/{database_cluster_uuid}/replicas | List All Read-only Replicas
*DatabasesApi* | [**list_users**](docs/DatabasesApi.md#list_users) | **GET** /v2/databases/{database_cluster_uuid}/users | List all Database Users
*DatabasesApi* | [**reset_auth**](docs/DatabasesApi.md#reset_auth) | **POST** /v2/databases/{database_cluster_uuid}/users/{username}/reset_auth | Reset a Database User&#39;s Password or Authentication Method
*DatabasesApi* | [**update_database_cluster**](docs/DatabasesApi.md#update_database_cluster) | **PUT** /v2/databases/{database_cluster_uuid}/migrate | Migrate a Database Cluster to a New Region
*DatabasesApi* | [**update_database_cluster_size**](docs/DatabasesApi.md#update_database_cluster_size) | **PUT** /v2/databases/{database_cluster_uuid}/resize | Resize a Database Cluster
*DatabasesApi* | [**update_database_firewall**](docs/DatabasesApi.md#update_database_firewall) | **PUT** /v2/databases/{database_cluster_uuid}/firewall | Update Firewall Rules (Trusted Sources) for a Database
*DatabasesApi* | [**update_eviction_policy**](docs/DatabasesApi.md#update_eviction_policy) | **PUT** /v2/databases/{database_cluster_uuid}/eviction_policy | Configure the Eviction Policy for a Redis Cluster
*DatabasesApi* | [**update_maintenance_window**](docs/DatabasesApi.md#update_maintenance_window) | **PUT** /v2/databases/{database_cluster_uuid}/maintenance | Configure a Database Cluster&#39;s Maintenance Window
*DatabasesApi* | [**update_online_migration**](docs/DatabasesApi.md#update_online_migration) | **PUT** /v2/databases/{database_cluster_uuid}/online-migration | Start an Online Migration
*DatabasesApi* | [**update_sql_mode**](docs/DatabasesApi.md#update_sql_mode) | **PUT** /v2/databases/{database_cluster_uuid}/sql_mode | Update SQL Mode for a Cluster
*DomainRecordsApi* | [**create_domain_record**](docs/DomainRecordsApi.md#create_domain_record) | **POST** /v2/domains/{domain_name}/records | Create a New Domain Record
*DomainRecordsApi* | [**delete_domain_record**](docs/DomainRecordsApi.md#delete_domain_record) | **DELETE** /v2/domains/{domain_name}/records/{domain_record_id} | Delete a Domain Record
*DomainRecordsApi* | [**get_domain_record**](docs/DomainRecordsApi.md#get_domain_record) | **GET** /v2/domains/{domain_name}/records/{domain_record_id} | Retrieve an Existing Domain Record
*DomainRecordsApi* | [**list_all_domain_records**](docs/DomainRecordsApi.md#list_all_domain_records) | **GET** /v2/domains/{domain_name}/records | List All Domain Records
*DomainRecordsApi* | [**patch_update_domain_record**](docs/DomainRecordsApi.md#patch_update_domain_record) | **PATCH** /v2/domains/{domain_name}/records/{domain_record_id} | Update a Domain Record
*DomainRecordsApi* | [**update_domain_record**](docs/DomainRecordsApi.md#update_domain_record) | **PUT** /v2/domains/{domain_name}/records/{domain_record_id} | Update a Domain Record
*DomainsApi* | [**create_domain**](docs/DomainsApi.md#create_domain) | **POST** /v2/domains | Create a New Domain
*DomainsApi* | [**delete_domain**](docs/DomainsApi.md#delete_domain) | **DELETE** /v2/domains/{domain_name} | Delete a Domain
*DomainsApi* | [**get_domain**](docs/DomainsApi.md#get_domain) | **GET** /v2/domains/{domain_name} | Retrieve an Existing Domain
*DomainsApi* | [**list_all_domains**](docs/DomainsApi.md#list_all_domains) | **GET** /v2/domains | List All Domains
*DropletActionsApi* | [**get_droplet_action**](docs/DropletActionsApi.md#get_droplet_action) | **GET** /v2/droplets/{droplet_id}/actions/{action_id} | Retrieve a Droplet Action
*DropletActionsApi* | [**list_droplet_actions**](docs/DropletActionsApi.md#list_droplet_actions) | **GET** /v2/droplets/{droplet_id}/actions | List Actions for a Droplet
*DropletActionsApi* | [**post_droplet_action**](docs/DropletActionsApi.md#post_droplet_action) | **POST** /v2/droplets/{droplet_id}/actions | Initiate a Droplet Action
*DropletActionsApi* | [**post_droplet_action_by_tag**](docs/DropletActionsApi.md#post_droplet_action_by_tag) | **POST** /v2/droplets/actions | Acting on Tagged Droplets
*DropletsApi* | [**create_droplet**](docs/DropletsApi.md#create_droplet) | **POST** /v2/droplets | Create a New Droplet
*DropletsApi* | [**destroy_droplet**](docs/DropletsApi.md#destroy_droplet) | **DELETE** /v2/droplets/{droplet_id} | Delete an Existing Droplet
*DropletsApi* | [**destroy_droplets_by_tag**](docs/DropletsApi.md#destroy_droplets_by_tag) | **DELETE** /v2/droplets | Deleting Droplets by Tag
*DropletsApi* | [**destroy_with_associated_resources_dangerous**](docs/DropletsApi.md#destroy_with_associated_resources_dangerous) | **DELETE** /v2/droplets/{droplet_id}/destroy_with_associated_resources/dangerous | Destroy a Droplet and All of its Associated Resources (Dangerous)
*DropletsApi* | [**destroy_with_associated_resources_selective**](docs/DropletsApi.md#destroy_with_associated_resources_selective) | **DELETE** /v2/droplets/{droplet_id}/destroy_with_associated_resources/selective | Selectively Destroy a Droplet and its Associated Resources
*DropletsApi* | [**get_destroy_with_associated_resources_status**](docs/DropletsApi.md#get_destroy_with_associated_resources_status) | **GET** /v2/droplets/{droplet_id}/destroy_with_associated_resources/status | Check Status of a Droplet Destroy with Associated Resources Request
*DropletsApi* | [**get_droplet**](docs/DropletsApi.md#get_droplet) | **GET** /v2/droplets/{droplet_id} | Retrieve an Existing Droplet
*DropletsApi* | [**list_all_droplet_neighbors_ids**](docs/DropletsApi.md#list_all_droplet_neighbors_ids) | **GET** /v2/reports/droplet_neighbors_ids | List All Droplet Neighbors
*DropletsApi* | [**list_all_droplets**](docs/DropletsApi.md#list_all_droplets) | **GET** /v2/droplets | List All Droplets
*DropletsApi* | [**list_droplet_associated_resources**](docs/DropletsApi.md#list_droplet_associated_resources) | **GET** /v2/droplets/{droplet_id}/destroy_with_associated_resources | List Associated Resources for a Droplet
*DropletsApi* | [**list_droplet_backups**](docs/DropletsApi.md#list_droplet_backups) | **GET** /v2/droplets/{droplet_id}/backups | List Backups for a Droplet
*DropletsApi* | [**list_droplet_firewalls**](docs/DropletsApi.md#list_droplet_firewalls) | **GET** /v2/droplets/{droplet_id}/firewalls | List all Firewalls Applied to a Droplet
*DropletsApi* | [**list_droplet_kernels**](docs/DropletsApi.md#list_droplet_kernels) | **GET** /v2/droplets/{droplet_id}/kernels | List All Available Kernels for a Droplet
*DropletsApi* | [**list_droplet_neighbors**](docs/DropletsApi.md#list_droplet_neighbors) | **GET** /v2/droplets/{droplet_id}/neighbors | List Neighbors for a Droplet
*DropletsApi* | [**list_droplet_snapshots**](docs/DropletsApi.md#list_droplet_snapshots) | **GET** /v2/droplets/{droplet_id}/snapshots | List Snapshots for a Droplet
*DropletsApi* | [**retry_destroy_with_associated_resource**](docs/DropletsApi.md#retry_destroy_with_associated_resource) | **POST** /v2/droplets/{droplet_id}/destroy_with_associated_resources/retry | Retry a Droplet Destroy with Associated Resources Request
*FirewallsApi* | [**add_firewall_droplets**](docs/FirewallsApi.md#add_firewall_droplets) | **POST** /v2/firewalls/{firewall_id}/droplets | Add Droplets to a Firewall
*FirewallsApi* | [**add_firewall_rules**](docs/FirewallsApi.md#add_firewall_rules) | **POST** /v2/firewalls/{firewall_id}/rules | Add Rules to a Firewall
*FirewallsApi* | [**add_firewall_tags**](docs/FirewallsApi.md#add_firewall_tags) | **POST** /v2/firewalls/{firewall_id}/tags | Add Tags to a Firewall
*FirewallsApi* | [**create_firewall**](docs/FirewallsApi.md#create_firewall) | **POST** /v2/firewalls | Create a New Firewall
*FirewallsApi* | [**delete_firewall**](docs/FirewallsApi.md#delete_firewall) | **DELETE** /v2/firewalls/{firewall_id} | Delete a Firewall
*FirewallsApi* | [**delete_firewall_droplets**](docs/FirewallsApi.md#delete_firewall_droplets) | **DELETE** /v2/firewalls/{firewall_id}/droplets | Remove Droplets from a Firewall
*FirewallsApi* | [**delete_firewall_rules**](docs/FirewallsApi.md#delete_firewall_rules) | **DELETE** /v2/firewalls/{firewall_id}/rules | Remove Rules from a Firewall
*FirewallsApi* | [**delete_firewall_tags**](docs/FirewallsApi.md#delete_firewall_tags) | **DELETE** /v2/firewalls/{firewall_id}/tags | Remove Tags from a Firewall
*FirewallsApi* | [**get_firewall**](docs/FirewallsApi.md#get_firewall) | **GET** /v2/firewalls/{firewall_id} | Retrieve an Existing Firewall
*FirewallsApi* | [**list_firewalls**](docs/FirewallsApi.md#list_firewalls) | **GET** /v2/firewalls | List All Firewalls
*FirewallsApi* | [**update_firewall**](docs/FirewallsApi.md#update_firewall) | **PUT** /v2/firewalls/{firewall_id} | Update a Firewall
*FloatingIPActionsApi* | [**get_floating_ip_action**](docs/FloatingIPActionsApi.md#get_floating_ip_action) | **GET** /v2/floating_ips/{floating_ip}/actions/{action_id} | Retrieve an Existing Floating IP Action
*FloatingIPActionsApi* | [**list_floating_ip_actions**](docs/FloatingIPActionsApi.md#list_floating_ip_actions) | **GET** /v2/floating_ips/{floating_ip}/actions | List All Actions for a Floating IP
*FloatingIPActionsApi* | [**post_floating_ip_action**](docs/FloatingIPActionsApi.md#post_floating_ip_action) | **POST** /v2/floating_ips/{floating_ip}/actions | Initiate a Floating IP Action
*FloatingIPsApi* | [**create_floating_ip**](docs/FloatingIPsApi.md#create_floating_ip) | **POST** /v2/floating_ips | Create a New Floating IP
*FloatingIPsApi* | [**delete_floating_ip**](docs/FloatingIPsApi.md#delete_floating_ip) | **DELETE** /v2/floating_ips/{floating_ip} | Delete a Floating IPs
*FloatingIPsApi* | [**get_floating_ip**](docs/FloatingIPsApi.md#get_floating_ip) | **GET** /v2/floating_ips/{floating_ip} | Retrieve an Existing Floating IP
*FloatingIPsApi* | [**list_floating_ips**](docs/FloatingIPsApi.md#list_floating_ips) | **GET** /v2/floating_ips | List All Floating IPs
*ImageActionsApi* | [**get_image_action**](docs/ImageActionsApi.md#get_image_action) | **GET** /v2/images/{image_id}/actions/{action_id} | Retrieve an Existing Action
*ImageActionsApi* | [**list_image_actions**](docs/ImageActionsApi.md#list_image_actions) | **GET** /v2/images/{image_id}/actions | List All Actions for an Image
*ImageActionsApi* | [**post_image_action**](docs/ImageActionsApi.md#post_image_action) | **POST** /v2/images/{image_id}/actions | Initiate an Image Action
*ImagesApi* | [**create_custom_image**](docs/ImagesApi.md#create_custom_image) | **POST** /v2/images | Create a Custom Image
*ImagesApi* | [**delete_image**](docs/ImagesApi.md#delete_image) | **DELETE** /v2/images/{image_id} | Delete an Image
*ImagesApi* | [**get_image**](docs/ImagesApi.md#get_image) | **GET** /v2/images/{image_id} | Retrieve an Existing Image
*ImagesApi* | [**get_images_list**](docs/ImagesApi.md#get_images_list) | **GET** /v2/images | List All Images
*ImagesApi* | [**update_image**](docs/ImagesApi.md#update_image) | **PUT** /v2/images/{image_id} | Update an Image
*KubernetesApi* | [**add_kubernetes_node_pool**](docs/KubernetesApi.md#add_kubernetes_node_pool) | **POST** /v2/kubernetes/clusters/{cluster_id}/node_pools | Add a Node Pool to a Kubernetes Cluster
*KubernetesApi* | [**add_registry**](docs/KubernetesApi.md#add_registry) | **POST** /v2/kubernetes/registry | Add Container Registry to Kubernetes Clusters
*KubernetesApi* | [**create_kubernetes_cluster**](docs/KubernetesApi.md#create_kubernetes_cluster) | **POST** /v2/kubernetes/clusters | Create a New Kubernetes Cluster
*KubernetesApi* | [**delete_kubernetes_cluster**](docs/KubernetesApi.md#delete_kubernetes_cluster) | **DELETE** /v2/kubernetes/clusters/{cluster_id} | Delete a Kubernetes Cluster
*KubernetesApi* | [**delete_kubernetes_node**](docs/KubernetesApi.md#delete_kubernetes_node) | **DELETE** /v2/kubernetes/clusters/{cluster_id}/node_pools/{node_pool_id}/nodes/{node_id} | Delete a Node in a Kubernetes Cluster
*KubernetesApi* | [**delete_kubernetes_node_pool**](docs/KubernetesApi.md#delete_kubernetes_node_pool) | **DELETE** /v2/kubernetes/clusters/{cluster_id}/node_pools/{node_pool_id} | Delete a Node Pool in a Kubernetes Cluster
*KubernetesApi* | [**destroy_kubernetes_associated_resources_dangerous**](docs/KubernetesApi.md#destroy_kubernetes_associated_resources_dangerous) | **DELETE** /v2/kubernetes/clusters/{cluster_id}/destroy_with_associated_resources/dangerous | Delete a Cluster and All of its Associated Resources (Dangerous)
*KubernetesApi* | [**destroy_kubernetes_associated_resources_selective**](docs/KubernetesApi.md#destroy_kubernetes_associated_resources_selective) | **DELETE** /v2/kubernetes/clusters/{cluster_id}/destroy_with_associated_resources/selective | Selectively Delete a Cluster and its Associated Resources
*KubernetesApi* | [**get_available_upgrades**](docs/KubernetesApi.md#get_available_upgrades) | **GET** /v2/kubernetes/clusters/{cluster_id}/upgrades | Retrieve Available Upgrades for an Existing Kubernetes Cluster
*KubernetesApi* | [**get_cluster_user**](docs/KubernetesApi.md#get_cluster_user) | **GET** /v2/kubernetes/clusters/{cluster_id}/user | Retrieve User Information for a Kubernetes Cluster
*KubernetesApi* | [**get_clusterlint_results**](docs/KubernetesApi.md#get_clusterlint_results) | **GET** /v2/kubernetes/clusters/{cluster_id}/clusterlint | Fetch Clusterlint Diagnostics for a Kubernetes Cluster
*KubernetesApi* | [**get_credentials**](docs/KubernetesApi.md#get_credentials) | **GET** /v2/kubernetes/clusters/{cluster_id}/credentials | Retrieve Credentials for a Kubernetes Cluster
*KubernetesApi* | [**get_kubeconfig**](docs/KubernetesApi.md#get_kubeconfig) | **GET** /v2/kubernetes/clusters/{cluster_id}/kubeconfig | Retrieve the kubeconfig for a Kubernetes Cluster
*KubernetesApi* | [**get_kubernetes_cluster**](docs/KubernetesApi.md#get_kubernetes_cluster) | **GET** /v2/kubernetes/clusters/{cluster_id} | Retrieve an Existing Kubernetes Cluster
*KubernetesApi* | [**get_node_pool**](docs/KubernetesApi.md#get_node_pool) | **GET** /v2/kubernetes/clusters/{cluster_id}/node_pools/{node_pool_id} | Retrieve a Node Pool for a Kubernetes Cluster
*KubernetesApi* | [**list_all_kubernetes_clusters**](docs/KubernetesApi.md#list_all_kubernetes_clusters) | **GET** /v2/kubernetes/clusters | List All Kubernetes Clusters
*KubernetesApi* | [**list_kubernetes_associated_resources**](docs/KubernetesApi.md#list_kubernetes_associated_resources) | **GET** /v2/kubernetes/clusters/{cluster_id}/destroy_with_associated_resources | List Associated Resources for Cluster Deletion
*KubernetesApi* | [**list_kubernetes_options**](docs/KubernetesApi.md#list_kubernetes_options) | **GET** /v2/kubernetes/options | List Available Regions, Node Sizes, and Versions of Kubernetes
*KubernetesApi* | [**list_node_pools**](docs/KubernetesApi.md#list_node_pools) | **GET** /v2/kubernetes/clusters/{cluster_id}/node_pools | List All Node Pools in a Kubernetes Clusters
*KubernetesApi* | [**recycle_kubernetes_node_pool**](docs/KubernetesApi.md#recycle_kubernetes_node_pool) | **POST** /v2/kubernetes/clusters/{cluster_id}/node_pools/{node_pool_id}/recycle | Recycle a Kubernetes Node Pool
*KubernetesApi* | [**remove_registry**](docs/KubernetesApi.md#remove_registry) | **DELETE** /v2/kubernetes/registry | Remove Container Registry from Kubernetes Clusters
*KubernetesApi* | [**run_clusterlint**](docs/KubernetesApi.md#run_clusterlint) | **POST** /v2/kubernetes/clusters/{cluster_id}/clusterlint | Run Clusterlint Checks on a Kubernetes Cluster
*KubernetesApi* | [**update_kubernetes_cluster**](docs/KubernetesApi.md#update_kubernetes_cluster) | **PUT** /v2/kubernetes/clusters/{cluster_id} | Update a Kubernetes Cluster
*KubernetesApi* | [**update_kubernetes_node_pool**](docs/KubernetesApi.md#update_kubernetes_node_pool) | **PUT** /v2/kubernetes/clusters/{cluster_id}/node_pools/{node_pool_id} | Update a Node Pool in a Kubernetes Cluster
*KubernetesApi* | [**upgrade_kubernetes_cluster**](docs/KubernetesApi.md#upgrade_kubernetes_cluster) | **POST** /v2/kubernetes/clusters/{cluster_id}/upgrade | Upgrade a Kubernetes Cluster
*LoadBalancersApi* | [**add_load_balancer_droplets**](docs/LoadBalancersApi.md#add_load_balancer_droplets) | **POST** /v2/load_balancers/{lb_id}/droplets | Add Droplets to a Load Balancer
*LoadBalancersApi* | [**add_load_balancer_forwarding_rules**](docs/LoadBalancersApi.md#add_load_balancer_forwarding_rules) | **POST** /v2/load_balancers/{lb_id}/forwarding_rules | Add Forwarding Rules to a Load Balancer
*LoadBalancersApi* | [**create_load_balancer**](docs/LoadBalancersApi.md#create_load_balancer) | **POST** /v2/load_balancers | Create a New Load Balancer
*LoadBalancersApi* | [**delete_load_balancer**](docs/LoadBalancersApi.md#delete_load_balancer) | **DELETE** /v2/load_balancers/{lb_id} | Delete a Load Balancer
*LoadBalancersApi* | [**get_load_balancer**](docs/LoadBalancersApi.md#get_load_balancer) | **GET** /v2/load_balancers/{lb_id} | Retrieve an Existing Load Balancer
*LoadBalancersApi* | [**list_all_load_balancers**](docs/LoadBalancersApi.md#list_all_load_balancers) | **GET** /v2/load_balancers | List All Load Balancers
*LoadBalancersApi* | [**remove_load_balancer_droplets**](docs/LoadBalancersApi.md#remove_load_balancer_droplets) | **DELETE** /v2/load_balancers/{lb_id}/droplets | Remove Droplets from a Load Balancer
*LoadBalancersApi* | [**remove_load_balancer_forwarding_rules**](docs/LoadBalancersApi.md#remove_load_balancer_forwarding_rules) | **DELETE** /v2/load_balancers/{lb_id}/forwarding_rules | Remove Forwarding Rules from a Load Balancer
*LoadBalancersApi* | [**update_load_balancer**](docs/LoadBalancersApi.md#update_load_balancer) | **PUT** /v2/load_balancers/{lb_id} | Update a Load Balancer
*MonitoringApi* | [**create_alert_policy**](docs/MonitoringApi.md#create_alert_policy) | **POST** /v2/monitoring/alerts | Create Alert Policy
*MonitoringApi* | [**delete_alert_policy**](docs/MonitoringApi.md#delete_alert_policy) | **DELETE** /v2/monitoring/alerts/{alert_uuid} | Delete an Alert Policy
*MonitoringApi* | [**get_alert_policy**](docs/MonitoringApi.md#get_alert_policy) | **GET** /v2/monitoring/alerts/{alert_uuid} | Retrieve an Existing Alert Policy
*MonitoringApi* | [**get_droplet_bandwidth_metrics**](docs/MonitoringApi.md#get_droplet_bandwidth_metrics) | **GET** /v2/monitoring/metrics/droplet/bandwidth | Get Droplet Bandwidth Metrics
*MonitoringApi* | [**get_droplet_cpu_metrics**](docs/MonitoringApi.md#get_droplet_cpu_metrics) | **GET** /v2/monitoring/metrics/droplet/cpu | Get Droplet CPU Metrics
*MonitoringApi* | [**get_droplet_filesystem_free_metrics**](docs/MonitoringApi.md#get_droplet_filesystem_free_metrics) | **GET** /v2/monitoring/metrics/droplet/filesystem_free | Get Droplet Filesystem Free Metrics
*MonitoringApi* | [**get_droplet_filesystem_size_metrics**](docs/MonitoringApi.md#get_droplet_filesystem_size_metrics) | **GET** /v2/monitoring/metrics/droplet/filesystem_size | Get Droplet Filesystem Size Metrics
*MonitoringApi* | [**get_droplet_load15_metrics**](docs/MonitoringApi.md#get_droplet_load15_metrics) | **GET** /v2/monitoring/metrics/droplet/load_15 | Get Droplet Load15 Metrics
*MonitoringApi* | [**get_droplet_load1_metrics**](docs/MonitoringApi.md#get_droplet_load1_metrics) | **GET** /v2/monitoring/metrics/droplet/load_1 | Get Droplet Load1 Metrics
*MonitoringApi* | [**get_droplet_load5_metrics**](docs/MonitoringApi.md#get_droplet_load5_metrics) | **GET** /v2/monitoring/metrics/droplet/load_5 | Get Droplet Load5 Metrics
*MonitoringApi* | [**get_droplet_memory_available_metrics**](docs/MonitoringApi.md#get_droplet_memory_available_metrics) | **GET** /v2/monitoring/metrics/droplet/memory_available | Get Droplet Available Memory Metrics
*MonitoringApi* | [**get_droplet_memory_cached_metrics**](docs/MonitoringApi.md#get_droplet_memory_cached_metrics) | **GET** /v2/monitoring/metrics/droplet/memory_cached | Get Droplet Cached Memory Metrics
*MonitoringApi* | [**get_droplet_memory_free_metrics**](docs/MonitoringApi.md#get_droplet_memory_free_metrics) | **GET** /v2/monitoring/metrics/droplet/memory_free | Get Droplet Free Memory Metrics
*MonitoringApi* | [**get_droplet_memory_total_metrics**](docs/MonitoringApi.md#get_droplet_memory_total_metrics) | **GET** /v2/monitoring/metrics/droplet/memory_total | Get Droplet Total Memory Metrics
*MonitoringApi* | [**list_alert_policies**](docs/MonitoringApi.md#list_alert_policies) | **GET** /v2/monitoring/alerts | List Alert Policies
*MonitoringApi* | [**update_alert_policy**](docs/MonitoringApi.md#update_alert_policy) | **PUT** /v2/monitoring/alerts/{alert_uuid} | Update an Alert Policy
*ProjectResourcesApi* | [**assign_default_project_resources**](docs/ProjectResourcesApi.md#assign_default_project_resources) | **POST** /v2/projects/default/resources | Assign Resources to Default Project
*ProjectResourcesApi* | [**assign_project_resources**](docs/ProjectResourcesApi.md#assign_project_resources) | **POST** /v2/projects/{project_id}/resources | Assign Resources to a Project
*ProjectResourcesApi* | [**list_default_project_resources**](docs/ProjectResourcesApi.md#list_default_project_resources) | **GET** /v2/projects/default/resources | List Default Project Resources
*ProjectResourcesApi* | [**list_project_resources**](docs/ProjectResourcesApi.md#list_project_resources) | **GET** /v2/projects/{project_id}/resources | List Project Resources
*ProjectsApi* | [**create_project**](docs/ProjectsApi.md#create_project) | **POST** /v2/projects | Create a Project
*ProjectsApi* | [**delete_project**](docs/ProjectsApi.md#delete_project) | **DELETE** /v2/projects/{project_id} | Delete an Existing Project
*ProjectsApi* | [**get_default_project**](docs/ProjectsApi.md#get_default_project) | **GET** /v2/projects/default | Retrieve the Default Project
*ProjectsApi* | [**get_project**](docs/ProjectsApi.md#get_project) | **GET** /v2/projects/{project_id} | Retrieve an Existing Project
*ProjectsApi* | [**list_projects**](docs/ProjectsApi.md#list_projects) | **GET** /v2/projects | List All Projects
*ProjectsApi* | [**patch_default_project**](docs/ProjectsApi.md#patch_default_project) | **PATCH** /v2/projects/default | Patch the Default Project
*ProjectsApi* | [**patch_project**](docs/ProjectsApi.md#patch_project) | **PATCH** /v2/projects/{project_id} | Patch a Project
*ProjectsApi* | [**update_default_project**](docs/ProjectsApi.md#update_default_project) | **PUT** /v2/projects/default | Update the Default Project
*ProjectsApi* | [**update_project**](docs/ProjectsApi.md#update_project) | **PUT** /v2/projects/{project_id} | Update a Project
*RegionsApi* | [**list_all_regions**](docs/RegionsApi.md#list_all_regions) | **GET** /v2/regions | List All Data Center Regions
*SSHKeysApi* | [**create_ssh_key**](docs/SSHKeysApi.md#create_ssh_key) | **POST** /v2/account/keys | Create a New SSH Key
*SSHKeysApi* | [**destroy_ssh_key**](docs/SSHKeysApi.md#destroy_ssh_key) | **DELETE** /v2/account/keys/{ssh_key_identifier} | Delete an SSH Key
*SSHKeysApi* | [**get_ssh_key**](docs/SSHKeysApi.md#get_ssh_key) | **GET** /v2/account/keys/{ssh_key_identifier} | Retrieve an Existing SSH Key
*SSHKeysApi* | [**list_all_keys**](docs/SSHKeysApi.md#list_all_keys) | **GET** /v2/account/keys | List All SSH Keys
*SSHKeysApi* | [**update_ssh_key**](docs/SSHKeysApi.md#update_ssh_key) | **PUT** /v2/account/keys/{ssh_key_identifier} | Update an SSH Key&#39;s Name
*SizesApi* | [**list_all_sizes**](docs/SizesApi.md#list_all_sizes) | **GET** /v2/sizes | List All Droplet Sizes
*SnapshotsApi* | [**delete_snapshot**](docs/SnapshotsApi.md#delete_snapshot) | **DELETE** /v2/snapshots/{snapshot_id} | Delete a Snapshot
*SnapshotsApi* | [**get_snapshot**](docs/SnapshotsApi.md#get_snapshot) | **GET** /v2/snapshots/{snapshot_id} | Retrieve an Existing Snapshot
*SnapshotsApi* | [**list_all_snapshots**](docs/SnapshotsApi.md#list_all_snapshots) | **GET** /v2/snapshots | List All Snapshots
*TagsApi* | [**create_new_tag**](docs/TagsApi.md#create_new_tag) | **POST** /v2/tags | Create a New Tag
*TagsApi* | [**delete_tag**](docs/TagsApi.md#delete_tag) | **DELETE** /v2/tags/{tag_id} | Delete a Tag
*TagsApi* | [**get_tag**](docs/TagsApi.md#get_tag) | **GET** /v2/tags/{tag_id} | Retrieve a Tag
*TagsApi* | [**list_all_tags**](docs/TagsApi.md#list_all_tags) | **GET** /v2/tags | List All Tags
*TagsApi* | [**tag_resource**](docs/TagsApi.md#tag_resource) | **POST** /v2/tags/{tag_id}/resources | Tag a Resource
*TagsApi* | [**untag_resource**](docs/TagsApi.md#untag_resource) | **DELETE** /v2/tags/{tag_id}/resources | Untag a Resource
*VPCsApi* | [**create_vpc**](docs/VPCsApi.md#create_vpc) | **POST** /v2/vpcs | Create a New VPC
*VPCsApi* | [**delete_vpc**](docs/VPCsApi.md#delete_vpc) | **DELETE** /v2/vpcs/{vpc_id} | Delete a VPC
*VPCsApi* | [**get_vpc**](docs/VPCsApi.md#get_vpc) | **GET** /v2/vpcs/{vpc_id} | Retrieve an Existing VPC
*VPCsApi* | [**list_vpc_members**](docs/VPCsApi.md#list_vpc_members) | **GET** /v2/vpcs/{vpc_id}/members | List the Member Resources of a VPC
*VPCsApi* | [**list_vpcs**](docs/VPCsApi.md#list_vpcs) | **GET** /v2/vpcs | List All VPCs
*VPCsApi* | [**patch_vpc**](docs/VPCsApi.md#patch_vpc) | **PATCH** /v2/vpcs/{vpc_id} | Partially Update a VPC
*VPCsApi* | [**update_vpc**](docs/VPCsApi.md#update_vpc) | **PUT** /v2/vpcs/{vpc_id} | Update a VPC


## Documentation For Models

 - [Account](docs/Account.md)
 - [Action](docs/Action.md)
 - [ActionLink](docs/ActionLink.md)
 - [AlertPolicy](docs/AlertPolicy.md)
 - [AlertPolicyRequest](docs/AlertPolicyRequest.md)
 - [Alerts](docs/Alerts.md)
 - [App](docs/App.md)
 - [AppAlert](docs/AppAlert.md)
 - [AppAlertPhase](docs/AppAlertPhase.md)
 - [AppAlertProgress](docs/AppAlertProgress.md)
 - [AppAlertProgressStep](docs/AppAlertProgressStep.md)
 - [AppAlertProgressStepReason](docs/AppAlertProgressStepReason.md)
 - [AppAlertProgressStepStatus](docs/AppAlertProgressStepStatus.md)
 - [AppAlertSlackWebhook](docs/AppAlertSlackWebhook.md)
 - [AppAlertSpec](docs/AppAlertSpec.md)
 - [AppAlertSpecOperator](docs/AppAlertSpecOperator.md)
 - [AppAlertSpecRule](docs/AppAlertSpecRule.md)
 - [AppAlertSpecWindow](docs/AppAlertSpecWindow.md)
 - [AppComponentBase](docs/AppComponentBase.md)
 - [AppComponentInstanceBase](docs/AppComponentInstanceBase.md)
 - [AppDatabaseSpec](docs/AppDatabaseSpec.md)
 - [AppDomainSpec](docs/AppDomainSpec.md)
 - [AppJobSpec](docs/AppJobSpec.md)
 - [AppJobSpecAllOf](docs/AppJobSpecAllOf.md)
 - [AppPropose](docs/AppPropose.md)
 - [AppProposeResponse](docs/AppProposeResponse.md)
 - [AppResponse](docs/AppResponse.md)
 - [AppRouteSpec](docs/AppRouteSpec.md)
 - [AppServiceSpec](docs/AppServiceSpec.md)
 - [AppServiceSpecAllOf](docs/AppServiceSpecAllOf.md)
 - [AppServiceSpecHealthCheck](docs/AppServiceSpecHealthCheck.md)
 - [AppSpec](docs/AppSpec.md)
 - [AppStaticSiteSpec](docs/AppStaticSiteSpec.md)
 - [AppStaticSiteSpecAllOf](docs/AppStaticSiteSpecAllOf.md)
 - [AppVariableDefinition](docs/AppVariableDefinition.md)
 - [AppWorkerSpec](docs/AppWorkerSpec.md)
 - [AppsAlertResponse](docs/AppsAlertResponse.md)
 - [AppsAssignAppAlertDestinationsRequest](docs/AppsAssignAppAlertDestinationsRequest.md)
 - [AppsCorsPolicy](docs/AppsCorsPolicy.md)
 - [AppsCreateAppRequest](docs/AppsCreateAppRequest.md)
 - [AppsCreateDeploymentRequest](docs/AppsCreateDeploymentRequest.md)
 - [AppsDeleteAppResponse](docs/AppsDeleteAppResponse.md)
 - [AppsDeployment](docs/AppsDeployment.md)
 - [AppsDeploymentJob](docs/AppsDeploymentJob.md)
 - [AppsDeploymentPhase](docs/AppsDeploymentPhase.md)
 - [AppsDeploymentProgress](docs/AppsDeploymentProgress.md)
 - [AppsDeploymentProgressStep](docs/AppsDeploymentProgressStep.md)
 - [AppsDeploymentProgressStepReason](docs/AppsDeploymentProgressStepReason.md)
 - [AppsDeploymentProgressStepStatus](docs/AppsDeploymentProgressStepStatus.md)
 - [AppsDeploymentResponse](docs/AppsDeploymentResponse.md)
 - [AppsDeploymentService](docs/AppsDeploymentService.md)
 - [AppsDeploymentStaticSite](docs/AppsDeploymentStaticSite.md)
 - [AppsDeploymentWorker](docs/AppsDeploymentWorker.md)
 - [AppsDeploymentsResponse](docs/AppsDeploymentsResponse.md)
 - [AppsDeploymentsResponseAllOf](docs/AppsDeploymentsResponseAllOf.md)
 - [AppsDomain](docs/AppsDomain.md)
 - [AppsDomainPhase](docs/AppsDomainPhase.md)
 - [AppsDomainProgress](docs/AppsDomainProgress.md)
 - [AppsGetInstanceSizeResponse](docs/AppsGetInstanceSizeResponse.md)
 - [AppsGetLogsResponse](docs/AppsGetLogsResponse.md)
 - [AppsGetTierResponse](docs/AppsGetTierResponse.md)
 - [AppsGitSourceSpec](docs/AppsGitSourceSpec.md)
 - [AppsGithubSourceSpec](docs/AppsGithubSourceSpec.md)
 - [AppsGitlabSourceSpec](docs/AppsGitlabSourceSpec.md)
 - [AppsImageSourceSpec](docs/AppsImageSourceSpec.md)
 - [AppsInstanceSize](docs/AppsInstanceSize.md)
 - [AppsListAlertsResponse](docs/AppsListAlertsResponse.md)
 - [AppsListInstanceSizesResponse](docs/AppsListInstanceSizesResponse.md)
 - [AppsListRegionsResponse](docs/AppsListRegionsResponse.md)
 - [AppsListTiersResponse](docs/AppsListTiersResponse.md)
 - [AppsRegion](docs/AppsRegion.md)
 - [AppsResponse](docs/AppsResponse.md)
 - [AppsResponseAllOf](docs/AppsResponseAllOf.md)
 - [AppsStringMatch](docs/AppsStringMatch.md)
 - [AppsTier](docs/AppsTier.md)
 - [AppsUpdateAppRequest](docs/AppsUpdateAppRequest.md)
 - [AssignToDroplet](docs/AssignToDroplet.md)
 - [AssociatedKubernetesResource](docs/AssociatedKubernetesResource.md)
 - [AssociatedKubernetesResources](docs/AssociatedKubernetesResources.md)
 - [AssociatedResource](docs/AssociatedResource.md)
 - [AssociatedResourceStatus](docs/AssociatedResourceStatus.md)
 - [AssociatedResourceStatusResources](docs/AssociatedResourceStatusResources.md)
 - [Backup](docs/Backup.md)
 - [BackwardLinks](docs/BackwardLinks.md)
 - [Balance](docs/Balance.md)
 - [BillingAddress](docs/BillingAddress.md)
 - [BillingHistory](docs/BillingHistory.md)
 - [Ca](docs/Ca.md)
 - [CdnEndpoint](docs/CdnEndpoint.md)
 - [Certificate](docs/Certificate.md)
 - [CertificateCreateBase](docs/CertificateCreateBase.md)
 - [CertificateRequestCustom](docs/CertificateRequestCustom.md)
 - [CertificateRequestCustomAllOf](docs/CertificateRequestCustomAllOf.md)
 - [CertificateRequestLetsEncrypt](docs/CertificateRequestLetsEncrypt.md)
 - [CertificateRequestLetsEncryptAllOf](docs/CertificateRequestLetsEncryptAllOf.md)
 - [Cluster](docs/Cluster.md)
 - [ClusterRegistries](docs/ClusterRegistries.md)
 - [ClusterStatus](docs/ClusterStatus.md)
 - [ClusterUpdate](docs/ClusterUpdate.md)
 - [ClusterlintRequest](docs/ClusterlintRequest.md)
 - [ClusterlintResults](docs/ClusterlintResults.md)
 - [ClusterlintResultsDiagnostics](docs/ClusterlintResultsDiagnostics.md)
 - [ClusterlintResultsObject](docs/ClusterlintResultsObject.md)
 - [ConnectionPool](docs/ConnectionPool.md)
 - [ConnectionPools](docs/ConnectionPools.md)
 - [Credentials](docs/Credentials.md)
 - [Database](docs/Database.md)
 - [DatabaseBackup](docs/DatabaseBackup.md)
 - [DatabaseCluster](docs/DatabaseCluster.md)
 - [DatabaseClusterResize](docs/DatabaseClusterResize.md)
 - [DatabaseConnection](docs/DatabaseConnection.md)
 - [DatabaseMaintenanceWindow](docs/DatabaseMaintenanceWindow.md)
 - [DatabaseReplica](docs/DatabaseReplica.md)
 - [DatabaseUser](docs/DatabaseUser.md)
 - [DestroyAssociatedKubernetesResources](docs/DestroyAssociatedKubernetesResources.md)
 - [DestroyedAssociatedResource](docs/DestroyedAssociatedResource.md)
 - [Distribution](docs/Distribution.md)
 - [DockerCredentials](docs/DockerCredentials.md)
 - [DockerCredentialsAuths](docs/DockerCredentialsAuths.md)
 - [DockerCredentialsAuthsRegistryDigitaloceanCom](docs/DockerCredentialsAuthsRegistryDigitaloceanCom.md)
 - [Domain](docs/Domain.md)
 - [DomainRecord](docs/DomainRecord.md)
 - [DomainRecordA](docs/DomainRecordA.md)
 - [DomainRecordAaaa](docs/DomainRecordAaaa.md)
 - [DomainRecordCaa](docs/DomainRecordCaa.md)
 - [DomainRecordCname](docs/DomainRecordCname.md)
 - [DomainRecordMx](docs/DomainRecordMx.md)
 - [DomainRecordNs](docs/DomainRecordNs.md)
 - [DomainRecordSoa](docs/DomainRecordSoa.md)
 - [DomainRecordSrv](docs/DomainRecordSrv.md)
 - [DomainRecordTxt](docs/DomainRecordTxt.md)
 - [Droplet](docs/Droplet.md)
 - [DropletActionChangeKernel](docs/DropletActionChangeKernel.md)
 - [DropletActionChangeKernelAllOf](docs/DropletActionChangeKernelAllOf.md)
 - [DropletActionRebuild](docs/DropletActionRebuild.md)
 - [DropletActionRebuildAllOf](docs/DropletActionRebuildAllOf.md)
 - [DropletActionRename](docs/DropletActionRename.md)
 - [DropletActionRenameAllOf](docs/DropletActionRenameAllOf.md)
 - [DropletActionResize](docs/DropletActionResize.md)
 - [DropletActionResizeAllOf](docs/DropletActionResizeAllOf.md)
 - [DropletActionRestore](docs/DropletActionRestore.md)
 - [DropletActionRestoreAllOf](docs/DropletActionRestoreAllOf.md)
 - [DropletActionSnapshot](docs/DropletActionSnapshot.md)
 - [DropletActionSnapshotAllOf](docs/DropletActionSnapshotAllOf.md)
 - [DropletActionType](docs/DropletActionType.md)
 - [DropletCreate](docs/DropletCreate.md)
 - [DropletMultiCreate](docs/DropletMultiCreate.md)
 - [DropletMultiCreateAllOf](docs/DropletMultiCreateAllOf.md)
 - [DropletNetworks](docs/DropletNetworks.md)
 - [DropletNextBackupWindow](docs/DropletNextBackupWindow.md)
 - [DropletSingleCreate](docs/DropletSingleCreate.md)
 - [DropletSingleCreateAllOf](docs/DropletSingleCreateAllOf.md)
 - [DropletSnapshot](docs/DropletSnapshot.md)
 - [DropletSnapshotAllOf](docs/DropletSnapshotAllOf.md)
 - [DropletSnapshotAllOf1](docs/DropletSnapshotAllOf1.md)
 - [Error](docs/Error.md)
 - [ErrorWithRootCauses](docs/ErrorWithRootCauses.md)
 - [EvictionPolicy](docs/EvictionPolicy.md)
 - [Firewall](docs/Firewall.md)
 - [FirewallAllOf](docs/FirewallAllOf.md)
 - [FirewallAllOfPendingChanges](docs/FirewallAllOfPendingChanges.md)
 - [FirewallRule](docs/FirewallRule.md)
 - [FirewallRuleBase](docs/FirewallRuleBase.md)
 - [FirewallRuleTarget](docs/FirewallRuleTarget.md)
 - [FirewallRules](docs/FirewallRules.md)
 - [FloatingIp](docs/FloatingIp.md)
 - [FloatingIpActionAssign](docs/FloatingIpActionAssign.md)
 - [FloatingIpActionAssignAllOf](docs/FloatingIpActionAssignAllOf.md)
 - [FloatingIpActionType](docs/FloatingIpActionType.md)
 - [FloatingIpActionUnassign](docs/FloatingIpActionUnassign.md)
 - [FloatingIpCreate](docs/FloatingIpCreate.md)
 - [ForwardLinks](docs/ForwardLinks.md)
 - [ForwardingRule](docs/ForwardingRule.md)
 - [GarbageCollection](docs/GarbageCollection.md)
 - [HealthCheck](docs/HealthCheck.md)
 - [Image](docs/Image.md)
 - [ImageActionBase](docs/ImageActionBase.md)
 - [ImageActionTransfer](docs/ImageActionTransfer.md)
 - [ImageActionTransferAllOf](docs/ImageActionTransferAllOf.md)
 - [ImageNewCustom](docs/ImageNewCustom.md)
 - [ImageNewCustomAllOf](docs/ImageNewCustomAllOf.md)
 - [ImageUpdate](docs/ImageUpdate.md)
 - [InlineObject](docs/InlineObject.md)
 - [InlineObject1](docs/InlineObject1.md)
 - [InlineObject2](docs/InlineObject2.md)
 - [InlineObject3](docs/InlineObject3.md)
 - [InlineObject4](docs/InlineObject4.md)
 - [InlineResponse200](docs/InlineResponse200.md)
 - [InlineResponse2001](docs/InlineResponse2001.md)
 - [InlineResponse20010](docs/InlineResponse20010.md)
 - [InlineResponse2002](docs/InlineResponse2002.md)
 - [InlineResponse2003](docs/InlineResponse2003.md)
 - [InlineResponse2004](docs/InlineResponse2004.md)
 - [InlineResponse2005](docs/InlineResponse2005.md)
 - [InlineResponse2006](docs/InlineResponse2006.md)
 - [InlineResponse2007](docs/InlineResponse2007.md)
 - [InlineResponse2008](docs/InlineResponse2008.md)
 - [InlineResponse2009](docs/InlineResponse2009.md)
 - [InlineResponse2009Options](docs/InlineResponse2009Options.md)
 - [InlineResponse201](docs/InlineResponse201.md)
 - [InlineResponse2011](docs/InlineResponse2011.md)
 - [InlineResponse2012](docs/InlineResponse2012.md)
 - [InlineResponse2013](docs/InlineResponse2013.md)
 - [InlineResponse2014](docs/InlineResponse2014.md)
 - [InlineResponse2015](docs/InlineResponse2015.md)
 - [InlineResponse2016](docs/InlineResponse2016.md)
 - [InlineResponse202](docs/InlineResponse202.md)
 - [InlineResponse202Links](docs/InlineResponse202Links.md)
 - [InstanceSizeCpuType](docs/InstanceSizeCpuType.md)
 - [InvoiceItem](docs/InvoiceItem.md)
 - [InvoicePreview](docs/InvoicePreview.md)
 - [InvoiceSummary](docs/InvoiceSummary.md)
 - [Kernel](docs/Kernel.md)
 - [KubernetesNodePool](docs/KubernetesNodePool.md)
 - [KubernetesNodePoolBase](docs/KubernetesNodePoolBase.md)
 - [KubernetesNodePoolSize](docs/KubernetesNodePoolSize.md)
 - [KubernetesNodePoolTaint](docs/KubernetesNodePoolTaint.md)
 - [KubernetesNodePoolUpdate](docs/KubernetesNodePoolUpdate.md)
 - [KubernetesOptions](docs/KubernetesOptions.md)
 - [KubernetesRegion](docs/KubernetesRegion.md)
 - [KubernetesSize](docs/KubernetesSize.md)
 - [KubernetesVersion](docs/KubernetesVersion.md)
 - [LinkToFirstPage](docs/LinkToFirstPage.md)
 - [LinkToLastPage](docs/LinkToLastPage.md)
 - [LinkToNextPage](docs/LinkToNextPage.md)
 - [LinkToPrevPage](docs/LinkToPrevPage.md)
 - [ListAlertPolicy](docs/ListAlertPolicy.md)
 - [LoadBalancer](docs/LoadBalancer.md)
 - [LoadBalancerAllOf](docs/LoadBalancerAllOf.md)
 - [LoadBalancerAllOf1](docs/LoadBalancerAllOf1.md)
 - [LoadBalancerAllOf2](docs/LoadBalancerAllOf2.md)
 - [LoadBalancerBase](docs/LoadBalancerBase.md)
 - [LoadBalancerCreate](docs/LoadBalancerCreate.md)
 - [MaintenancePolicy](docs/MaintenancePolicy.md)
 - [Meta](docs/Meta.md)
 - [MetaMeta](docs/MetaMeta.md)
 - [Metrics](docs/Metrics.md)
 - [MetricsData](docs/MetricsData.md)
 - [MetricsResult](docs/MetricsResult.md)
 - [Model1Click](docs/Model1Click.md)
 - [Model1ClickCreate](docs/Model1ClickCreate.md)
 - [MysqlSettings](docs/MysqlSettings.md)
 - [NeighborIds](docs/NeighborIds.md)
 - [NetworkV4](docs/NetworkV4.md)
 - [NetworkV6](docs/NetworkV6.md)
 - [NewVolumeExt4](docs/NewVolumeExt4.md)
 - [NewVolumeExt4AllOf](docs/NewVolumeExt4AllOf.md)
 - [NewVolumeXfs](docs/NewVolumeXfs.md)
 - [NewVolumeXfsAllOf](docs/NewVolumeXfsAllOf.md)
 - [Node](docs/Node.md)
 - [NodeStatus](docs/NodeStatus.md)
 - [OnlineMigration](docs/OnlineMigration.md)
 - [PageLinks](docs/PageLinks.md)
 - [Pagination](docs/Pagination.md)
 - [ProductChargeItem](docs/ProductChargeItem.md)
 - [ProductUsageCharges](docs/ProductUsageCharges.md)
 - [Project](docs/Project.md)
 - [ProjectAllOf](docs/ProjectAllOf.md)
 - [ProjectAssignment](docs/ProjectAssignment.md)
 - [ProjectBase](docs/ProjectBase.md)
 - [PurgeCache](docs/PurgeCache.md)
 - [Region](docs/Region.md)
 - [RegionSlug](docs/RegionSlug.md)
 - [RegionsArray](docs/RegionsArray.md)
 - [Registry](docs/Registry.md)
 - [RegistryCreate](docs/RegistryCreate.md)
 - [Repository](docs/Repository.md)
 - [RepositoryTag](docs/RepositoryTag.md)
 - [ReserveToRegion](docs/ReserveToRegion.md)
 - [Resource](docs/Resource.md)
 - [ResourceLinks](docs/ResourceLinks.md)
 - [SimpleCharge](docs/SimpleCharge.md)
 - [Size](docs/Size.md)
 - [SlackDetails](docs/SlackDetails.md)
 - [Snapshot](docs/Snapshot.md)
 - [SnapshotAllOf](docs/SnapshotAllOf.md)
 - [SnapshotAllOf1](docs/SnapshotAllOf1.md)
 - [SnapshotBase](docs/SnapshotBase.md)
 - [SourceDatabase](docs/SourceDatabase.md)
 - [SqlMode](docs/SqlMode.md)
 - [SshKey](docs/SshKey.md)
 - [StickySessions](docs/StickySessions.md)
 - [Subscription](docs/Subscription.md)
 - [SubscriptionTierBase](docs/SubscriptionTierBase.md)
 - [SubscriptionTierExtended](docs/SubscriptionTierExtended.md)
 - [Tag](docs/Tag.md)
 - [TagMetadata](docs/TagMetadata.md)
 - [TagResource](docs/TagResource.md)
 - [TagsArray](docs/TagsArray.md)
 - [UpdateEndpoint](docs/UpdateEndpoint.md)
 - [UpdateRegistry](docs/UpdateRegistry.md)
 - [Urn](docs/Urn.md)
 - [User](docs/User.md)
 - [UserKubernetesClusterUser](docs/UserKubernetesClusterUser.md)
 - [ValidateRegistry](docs/ValidateRegistry.md)
 - [VolumeAction](docs/VolumeAction.md)
 - [VolumeActionAllOf](docs/VolumeActionAllOf.md)
 - [VolumeActionPostAttach](docs/VolumeActionPostAttach.md)
 - [VolumeActionPostAttachAllOf](docs/VolumeActionPostAttachAllOf.md)
 - [VolumeActionPostBase](docs/VolumeActionPostBase.md)
 - [VolumeActionPostDetach](docs/VolumeActionPostDetach.md)
 - [VolumeActionPostDetachAllOf](docs/VolumeActionPostDetachAllOf.md)
 - [VolumeActionPostResize](docs/VolumeActionPostResize.md)
 - [VolumeActionPostResizeAllOf](docs/VolumeActionPostResizeAllOf.md)
 - [VolumeBase](docs/VolumeBase.md)
 - [VolumeFull](docs/VolumeFull.md)
 - [VolumeFullAllOf](docs/VolumeFullAllOf.md)
 - [VolumeSnapshotId](docs/VolumeSnapshotId.md)
 - [VolumeWriteFileSystemType](docs/VolumeWriteFileSystemType.md)
 - [Vpc](docs/Vpc.md)
 - [VpcBase](docs/VpcBase.md)
 - [VpcCreate](docs/VpcCreate.md)
 - [VpcDefault](docs/VpcDefault.md)
 - [VpcMember](docs/VpcMember.md)
 - [VpcUpdatable](docs/VpcUpdatable.md)


## Documentation For Authorization


## bearer_auth

- **Type**: Bearer authentication


## Author

api-engineering@digitalocean.com


## Notes for Large OpenAPI documents
If the OpenAPI document is large, imports in digitalocean_client.apis and digitalocean_client.models may fail with a
RecursionError indicating the maximum recursion limit has been exceeded. In that case, there are a couple of solutions:

Solution 1:
Use specific imports for apis and models like:
- `from digitalocean_client.api.default_api import DefaultApi`
- `from digitalocean_client.model.pet import Pet`

Solution 2:
Before importing the package, adjust the maximum recursion limit as shown below:
```
import sys
sys.setrecursionlimit(1500)
import digitalocean_client
from digitalocean_client.apis import *
from digitalocean_client.models import *
```

