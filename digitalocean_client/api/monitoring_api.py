"""
    DigitalOcean API

    # Introduction  The DigitalOcean API allows you to manage Droplets and resources within the DigitalOcean cloud in a simple, programmatic way using conventional HTTP requests.  All of the functionality that you are familiar with in the DigitalOcean control panel is also available through the API, allowing you to script the complex actions that your situation requires.  The API documentation will start with a general overview about the design and technology that has been implemented, followed by reference information about specific endpoints.  ## Requests  Any tool that is fluent in HTTP can communicate with the API simply by requesting the correct URI. Requests should be made using the HTTPS protocol so that traffic is encrypted. The interface responds to different methods depending on the action required.  |Method|Usage| |--- |--- | |GET|For simple retrieval of information about your account, Droplets, or environment, you should use the GET method.  The information you request will be returned to you as a JSON object. The attributes defined by the JSON object can be used to form additional requests.  Any request using the GET method is read-only and will not affect any of the objects you are querying.| |DELETE|To destroy a resource and remove it from your account and environment, the DELETE method should be used.  This will remove the specified object if it is found.  If it is not found, the operation will return a response indicating that the object was not found. This idempotency means that you do not have to check for a resource's availability prior to issuing a delete command, the final state will be the same regardless of its existence.| |PUT|To update the information about a resource in your account, the PUT method is available. Like the DELETE Method, the PUT method is idempotent.  It sets the state of the target using the provided values, regardless of their current values. Requests using the PUT method do not need to check the current attributes of the object.| |PATCH|Some resources support partial modification. In these cases, the PATCH method is available. Unlike PUT which generally requires a complete representation of a resource, a PATCH request is is a set of instructions on how to modify a resource updating only specific attributes.| |POST|To create a new object, your request should specify the POST method. The POST request includes all of the attributes necessary to create a new object.  When you wish to create a new object, send a POST request to the target endpoint.| |HEAD|Finally, to retrieve metadata information, you should use the HEAD method to get the headers.  This returns only the header of what would be returned with an associated GET request. Response headers contain some useful information about your API access and the results that are available for your request. For instance, the headers contain your current rate-limit value and the amount of time available until the limit resets. It also contains metrics about the total number of objects found, pagination information, and the total content length.|   ## HTTP Statuses  Along with the HTTP methods that the API responds to, it will also return standard HTTP statuses, including error codes.  In the event of a problem, the status will contain the error code, while the body of the response will usually contain additional information about the problem that was encountered.  In general, if the status returned is in the 200 range, it indicates that the request was fulfilled successfully and that no error was encountered.  Return codes in the 400 range typically indicate that there was an issue with the request that was sent. Among other things, this could mean that you did not authenticate correctly, that you are requesting an action that you do not have authorization for, that the object you are requesting does not exist, or that your request is malformed.  If you receive a status in the 500 range, this generally indicates a server-side problem. This means that we are having an issue on our end and cannot fulfill your request currently.  400 and 500 level error responses will include a JSON object in their body, including the following attributes:  |Name|Type|Description| |--- |--- |--- | |id|string|A short identifier corresponding to the HTTP status code returned. For example, the ID for a response returning a 404 status code would be \"not_found.\"| |message|string|A message providing additional information about the error, including details to help resolve it when possible.| |request_id|string|Optionally, some endpoints may include a request ID that should be provided when reporting bugs or opening support tickets to help identify the issue.|  ### Example Error Response  ```     HTTP/1.1 403 Forbidden     {       \"id\":       \"forbidden\",       \"message\":  \"You do not have access for the attempted action.\"     } ```  ## Responses  When a request is successful, a response body will typically be sent back in the form of a JSON object. An exception to this is when a DELETE request is processed, which will result in a successful HTTP 204 status and an empty response body.  Inside of this JSON object, the resource root that was the target of the request will be set as the key. This will be the singular form of the word if the request operated on a single object, and the plural form of the word if a collection was processed.  For example, if you send a GET request to `/v2/droplets/$DROPLET_ID` you will get back an object with a key called \"`droplet`\". However, if you send the GET request to the general collection at `/v2/droplets`, you will get back an object with a key called \"`droplets`\".  The value of these keys will generally be a JSON object for a request on a single object and an array of objects for a request on a collection of objects.  ### Response for a Single Object  ```     {         \"droplet\": {             \"name\": \"example.com\"             . . .         }     } ```  ### Response for an Object Collection  ```     {         \"droplets\": [             {                 \"name\": \"example.com\"                 . . .             },             {                 \"name\": \"second.com\"                 . . .             }         ]     } ```  ## Meta  In addition to the main resource root, the response may also contain a `meta` object. This object contains information about the response itself.  The `meta` object contains a `total` key that is set to the total number of objects returned by the request. This has implications on the `links` object and pagination.  The `meta` object will only be displayed when it has a value. Currently, the `meta` object will have a value when a request is made on a collection (like `droplets` or `domains`).   ### Sample Meta Object  ```     {         . . .         \"meta\": {             \"total\": 43         }         . . .     } ```  ## Links & Pagination  The `links` object is returned as part of the response body when pagination is enabled. By default, 20 objects are returned per page. If the response contains 20 objects or fewer, no `links` object will be returned. If the response contains more than 20 objects, the first 20 will be returned along with the `links` object.  You can request a different pagination limit or force pagination by appending `?per_page=` to the request with the number of items you would like per page. For instance, to show only two results per page, you could add `?per_page=2` to the end of your query. The maximum number of results per page is 200.  The `links` object contains a `pages` object. The `pages` object, in turn, contains keys indicating the relationship of additional pages. The values of these are the URLs of the associated pages. The keys will be one of the following:  *   **first**: The URI of the first page of results. *   **prev**: The URI of the previous sequential page of results. *   **next**: The URI of the next sequential page of results. *   **last**: The URI of the last page of results.  The `pages` object will only include the links that make sense. So for the first page of results, no `first` or `prev` links will ever be set. This convention holds true in other situations where a link would not make sense.  ### Sample Links Object  ```     {         . . .         \"links\": {             \"pages\": {                 \"last\": \"https://api.digitalocean.com/v2/images?page=2\",                 \"next\": \"https://api.digitalocean.com/v2/images?page=2\"             }         }         . . .     } ```  ## Rate Limit  Requests through the API are rate limited per OAuth token. Current rate limits:  *   5,000 requests per hour *   250 requests per minute (5% of the hourly total)  Once you exceed either limit, you will be rate limited until the next cycle starts. Space out any requests that you would otherwise issue in bursts for the best results.  The rate limiting information is contained within the response headers of each request. The relevant headers are:  *   **RateLimit-Limit**: The number of requests that can be made per hour. *   **RateLimit-Remaining**: The number of requests that remain before you hit your request limit. See the information below for how the request limits expire. *   **RateLimit-Reset**: This represents the time when the oldest request will expire. The value is given in [Unix epoch time](http://en.wikipedia.org/wiki/Unix_time). See below for more information about how request limits expire.  As long as the `RateLimit-Remaining` count is above zero, you will be able to make additional requests.  The way that a request expires and is removed from the current limit count is important to understand. Rather than counting all of the requests for an hour and resetting the `RateLimit-Remaining` value at the end of the hour, each request instead has its own timer.  This means that each request contributes toward the `RateLimit-Remaining` count for one complete hour after the request is made. When that request's timer runs out, it is no longer counted towards the request limit.  This has implications on the meaning of the `RateLimit-Reset` header as well. Because the entire rate limit is not reset at one time, the value of this header is set to the time when the _oldest_ request will expire.  Keep this in mind if you see your `RateLimit-Reset` value change, but not move an entire hour into the future.  If the `RateLimit-Remaining` reaches zero, subsequent requests will receive a 429 error code until the request reset has been reached. You can see the format of the response in the examples.  **Note:** The following endpoints have special rate limit requirements that are independent of the limits defined above.  *   Only 12 `POST` requests to the `/v2/floating_ips` endpoint to create Floating IPs can be made per 60 seconds. *   Only 10 `GET` requests to the `/v2/account/keys` endpoint to list SSH keys can be made per 60 seconds.  ### Sample Rate Limit Headers  ```     . . .     RateLimit-Limit: 1200     RateLimit-Remaining: 1193     RateLimit-Reset: 1402425459     . . . ```  ### Sample Rate Exceeded Response  ```     429 Too Many Requests     {             id: \"too_many_requests\",             message: \"API Rate limit exceeded.\"     } ```  ## Curl Examples  Throughout this document, some example API requests will be given using the `curl` command. This will allow us to demonstrate the various endpoints in a simple, textual format.  The names of account-specific references (like Droplet IDs, for instance) will be represented by variables. For instance, a Droplet ID may be represented by a variable called `$DROPLET_ID`. You can set the associated variables in your environment if you wish to use the examples without modification.  The first variable that you should set to get started is your OAuth authorization token. The next section will go over the details of this, but you can set an environmental variable for it now.  Generate a token by going to the [Apps & API](https://cloud.digitalocean.com/settings/applications) section of the DigitalOcean control panel. Use an existing token if you have saved one, or generate a new token with the \"Generate new token\" button. Copy the generated token and use it to set and export the TOKEN variable in your environment as the example shows.  You may also wish to set some other variables now or as you go along. For example, you may wish to set the `DROPLET_ID` variable to one of your Droplet IDs since this will be used frequently in the API.  If you are following along, make sure you use a Droplet ID that you control so that your commands will execute correctly.  If you need access to the headers of a response through `curl`, you can pass the `-i` flag to display the header information along with the body. If you are only interested in the header, you can instead pass the `-I` flag, which will exclude the response body entirely.  ### Set and Export your OAuth Token  ``` export DIGITALOCEAN_TOKEN=your_token_here ```  ### Set and Export a Variable  ``` export DROPLET_ID=1111111 ```  ## Parameters  There are two different ways to pass parameters in a request with the API.  When passing parameters to create or update an object, parameters should be passed as a JSON object containing the appropriate attribute names and values as key-value pairs. When you use this format, you should specify that you are sending a JSON object in the header. This is done by setting the `Content-Type` header to `application/json`. This ensures that your request is interpreted correctly.  When passing parameters to filter a response on GET requests, parameters can be passed using standard query attributes. In this case, the parameters would be embedded into the URI itself by appending a `?` to the end of the URI and then setting each attribute with an equal sign. Attributes can be separated with a `&`. Tools like `curl` can create the appropriate URI when given parameters and values; this can also be done using the `-F` flag and then passing the key and value as an argument. The argument should take the form of a quoted string with the attribute being set to a value with an equal sign.  ### Pass Parameters as a JSON Object  ```     curl -H \"Authorization: Bearer $DIGITALOCEAN_TOKEN\" \\         -H \"Content-Type: application/json\" \\         -d '{\"name\": \"example.com\", \"ip_address\": \"127.0.0.1\"}' \\         -X POST \"https://api.digitalocean.com/v2/domains\" ```  ### Pass Filter Parameters as a Query String  ```      curl -H \"Authorization: Bearer $DIGITALOCEAN_TOKEN\" \\          -X GET \\          \"https://api.digitalocean.com/v2/images?private=true\" ```  ## Cross Origin Resource Sharing  In order to make requests to the API from other domains, the API implements Cross Origin Resource Sharing (CORS) support.  CORS support is generally used to create AJAX requests outside of the domain that the request originated from. This is necessary to implement projects like control panels utilizing the API. This tells the browser that it can send requests to an outside domain.  The procedure that the browser initiates in order to perform these actions (other than GET requests) begins by sending a \"preflight\" request. This sets the `Origin` header and uses the `OPTIONS` method. The server will reply back with the methods it allows and some of the limits it imposes. The client then sends the actual request if it falls within the allowed constraints.  This process is usually done in the background by the browser, but you can use curl to emulate this process using the example provided. The headers that will be set to show the constraints are:  *   **Access-Control-Allow-Origin**: This is the domain that is sent by the client or browser as the origin of the request. It is set through an `Origin` header. *   **Access-Control-Allow-Methods**: This specifies the allowed options for requests from that domain. This will generally be all available methods. *   **Access-Control-Expose-Headers**: This will contain the headers that will be available to requests from the origin domain. *   **Access-Control-Max-Age**: This is the length of time that the access is considered valid. After this expires, a new preflight should be sent. *   **Access-Control-Allow-Credentials**: This will be set to `true`. It basically allows you to send your OAuth token for authentication.  You should not need to be concerned with the details of these headers, because the browser will typically do all of the work for you.   # noqa: E501

    The version of the OpenAPI document: 2.0
    Contact: api-engineering@digitalocean.com
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from digitalocean_client.api_client import ApiClient, Endpoint as _Endpoint
from digitalocean_client.model_utils import (  # noqa: F401
    check_allowed_values,
    check_validations,
    date,
    datetime,
    file_type,
    none_type,
    validate_and_convert_types
)
from digitalocean_client.model.alert_policy import AlertPolicy
from digitalocean_client.model.alert_policy_request import AlertPolicyRequest
from digitalocean_client.model.error import Error
from digitalocean_client.model.metrics import Metrics


class MonitoringApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client
        self.create_alert_policy_endpoint = _Endpoint(
            settings={
                'response_type': (AlertPolicy,),
                'auth': [
                    'bearer_auth'
                ],
                'endpoint_path': '/v2/monitoring/alerts',
                'operation_id': 'create_alert_policy',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'alert_policy_request',
                ],
                'required': [
                    'alert_policy_request',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'alert_policy_request':
                        (AlertPolicyRequest,),
                },
                'attribute_map': {
                },
                'location_map': {
                    'alert_policy_request': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [
                    'application/json'
                ]
            },
            api_client=api_client
        )
        self.delete_alert_policy_endpoint = _Endpoint(
            settings={
                'response_type': None,
                'auth': [
                    'bearer_auth'
                ],
                'endpoint_path': '/v2/monitoring/alerts/{alert_uuid}',
                'operation_id': 'delete_alert_policy',
                'http_method': 'DELETE',
                'servers': None,
            },
            params_map={
                'all': [
                    'alert_uuid',
                ],
                'required': [
                    'alert_uuid',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'alert_uuid':
                        (str,),
                },
                'attribute_map': {
                    'alert_uuid': 'alert_uuid',
                },
                'location_map': {
                    'alert_uuid': 'path',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.get_alert_policy_endpoint = _Endpoint(
            settings={
                'response_type': (AlertPolicy,),
                'auth': [
                    'bearer_auth'
                ],
                'endpoint_path': '/v2/monitoring/alerts/{alert_uuid}',
                'operation_id': 'get_alert_policy',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'alert_uuid',
                ],
                'required': [
                    'alert_uuid',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'alert_uuid':
                        (str,),
                },
                'attribute_map': {
                    'alert_uuid': 'alert_uuid',
                },
                'location_map': {
                    'alert_uuid': 'path',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.get_droplet_bandwidth_metrics_endpoint = _Endpoint(
            settings={
                'response_type': (Metrics,),
                'auth': [
                    'bearer_auth'
                ],
                'endpoint_path': '/v2/monitoring/metrics/droplet/bandwidth',
                'operation_id': 'get_droplet_bandwidth_metrics',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'host_id',
                    'interface',
                    'direction',
                    'start',
                    'end',
                ],
                'required': [
                    'host_id',
                    'interface',
                    'direction',
                    'start',
                    'end',
                ],
                'nullable': [
                ],
                'enum': [
                    'interface',
                    'direction',
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                    ('interface',): {

                        "PRIVATE": "private",
                        "PUBLIC": "public"
                    },
                    ('direction',): {

                        "INBOUND": "inbound",
                        "OUTBOUND": "outbound"
                    },
                },
                'openapi_types': {
                    'host_id':
                        (str,),
                    'interface':
                        (str,),
                    'direction':
                        (str,),
                    'start':
                        (str,),
                    'end':
                        (str,),
                },
                'attribute_map': {
                    'host_id': 'host_id',
                    'interface': 'interface',
                    'direction': 'direction',
                    'start': 'start',
                    'end': 'end',
                },
                'location_map': {
                    'host_id': 'query',
                    'interface': 'query',
                    'direction': 'query',
                    'start': 'query',
                    'end': 'query',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.get_droplet_cpu_metrics_endpoint = _Endpoint(
            settings={
                'response_type': (Metrics,),
                'auth': [
                    'bearer_auth'
                ],
                'endpoint_path': '/v2/monitoring/metrics/droplet/cpu',
                'operation_id': 'get_droplet_cpu_metrics',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'host_id',
                    'start',
                    'end',
                ],
                'required': [
                    'host_id',
                    'start',
                    'end',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'host_id':
                        (str,),
                    'start':
                        (str,),
                    'end':
                        (str,),
                },
                'attribute_map': {
                    'host_id': 'host_id',
                    'start': 'start',
                    'end': 'end',
                },
                'location_map': {
                    'host_id': 'query',
                    'start': 'query',
                    'end': 'query',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.get_droplet_filesystem_free_metrics_endpoint = _Endpoint(
            settings={
                'response_type': (Metrics,),
                'auth': [
                    'bearer_auth'
                ],
                'endpoint_path': '/v2/monitoring/metrics/droplet/filesystem_free',
                'operation_id': 'get_droplet_filesystem_free_metrics',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'host_id',
                    'start',
                    'end',
                ],
                'required': [
                    'host_id',
                    'start',
                    'end',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'host_id':
                        (str,),
                    'start':
                        (str,),
                    'end':
                        (str,),
                },
                'attribute_map': {
                    'host_id': 'host_id',
                    'start': 'start',
                    'end': 'end',
                },
                'location_map': {
                    'host_id': 'query',
                    'start': 'query',
                    'end': 'query',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.get_droplet_filesystem_size_metrics_endpoint = _Endpoint(
            settings={
                'response_type': (Metrics,),
                'auth': [
                    'bearer_auth'
                ],
                'endpoint_path': '/v2/monitoring/metrics/droplet/filesystem_size',
                'operation_id': 'get_droplet_filesystem_size_metrics',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'host_id',
                    'start',
                    'end',
                ],
                'required': [
                    'host_id',
                    'start',
                    'end',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'host_id':
                        (str,),
                    'start':
                        (str,),
                    'end':
                        (str,),
                },
                'attribute_map': {
                    'host_id': 'host_id',
                    'start': 'start',
                    'end': 'end',
                },
                'location_map': {
                    'host_id': 'query',
                    'start': 'query',
                    'end': 'query',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.get_droplet_load15_metrics_endpoint = _Endpoint(
            settings={
                'response_type': (Metrics,),
                'auth': [
                    'bearer_auth'
                ],
                'endpoint_path': '/v2/monitoring/metrics/droplet/load_15',
                'operation_id': 'get_droplet_load15_metrics',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'host_id',
                    'start',
                    'end',
                ],
                'required': [
                    'host_id',
                    'start',
                    'end',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'host_id':
                        (str,),
                    'start':
                        (str,),
                    'end':
                        (str,),
                },
                'attribute_map': {
                    'host_id': 'host_id',
                    'start': 'start',
                    'end': 'end',
                },
                'location_map': {
                    'host_id': 'query',
                    'start': 'query',
                    'end': 'query',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.get_droplet_load1_metrics_endpoint = _Endpoint(
            settings={
                'response_type': (Metrics,),
                'auth': [
                    'bearer_auth'
                ],
                'endpoint_path': '/v2/monitoring/metrics/droplet/load_1',
                'operation_id': 'get_droplet_load1_metrics',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'host_id',
                    'start',
                    'end',
                ],
                'required': [
                    'host_id',
                    'start',
                    'end',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'host_id':
                        (str,),
                    'start':
                        (str,),
                    'end':
                        (str,),
                },
                'attribute_map': {
                    'host_id': 'host_id',
                    'start': 'start',
                    'end': 'end',
                },
                'location_map': {
                    'host_id': 'query',
                    'start': 'query',
                    'end': 'query',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.get_droplet_load5_metrics_endpoint = _Endpoint(
            settings={
                'response_type': (Metrics,),
                'auth': [
                    'bearer_auth'
                ],
                'endpoint_path': '/v2/monitoring/metrics/droplet/load_5',
                'operation_id': 'get_droplet_load5_metrics',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'host_id',
                    'start',
                    'end',
                ],
                'required': [
                    'host_id',
                    'start',
                    'end',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'host_id':
                        (str,),
                    'start':
                        (str,),
                    'end':
                        (str,),
                },
                'attribute_map': {
                    'host_id': 'host_id',
                    'start': 'start',
                    'end': 'end',
                },
                'location_map': {
                    'host_id': 'query',
                    'start': 'query',
                    'end': 'query',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.get_droplet_memory_available_metrics_endpoint = _Endpoint(
            settings={
                'response_type': (Metrics,),
                'auth': [
                    'bearer_auth'
                ],
                'endpoint_path': '/v2/monitoring/metrics/droplet/memory_available',
                'operation_id': 'get_droplet_memory_available_metrics',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'host_id',
                    'start',
                    'end',
                ],
                'required': [
                    'host_id',
                    'start',
                    'end',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'host_id':
                        (str,),
                    'start':
                        (str,),
                    'end':
                        (str,),
                },
                'attribute_map': {
                    'host_id': 'host_id',
                    'start': 'start',
                    'end': 'end',
                },
                'location_map': {
                    'host_id': 'query',
                    'start': 'query',
                    'end': 'query',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.get_droplet_memory_cached_metrics_endpoint = _Endpoint(
            settings={
                'response_type': (Metrics,),
                'auth': [
                    'bearer_auth'
                ],
                'endpoint_path': '/v2/monitoring/metrics/droplet/memory_cached',
                'operation_id': 'get_droplet_memory_cached_metrics',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'host_id',
                    'start',
                    'end',
                ],
                'required': [
                    'host_id',
                    'start',
                    'end',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'host_id':
                        (str,),
                    'start':
                        (str,),
                    'end':
                        (str,),
                },
                'attribute_map': {
                    'host_id': 'host_id',
                    'start': 'start',
                    'end': 'end',
                },
                'location_map': {
                    'host_id': 'query',
                    'start': 'query',
                    'end': 'query',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.get_droplet_memory_free_metrics_endpoint = _Endpoint(
            settings={
                'response_type': (Metrics,),
                'auth': [
                    'bearer_auth'
                ],
                'endpoint_path': '/v2/monitoring/metrics/droplet/memory_free',
                'operation_id': 'get_droplet_memory_free_metrics',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'host_id',
                    'start',
                    'end',
                ],
                'required': [
                    'host_id',
                    'start',
                    'end',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'host_id':
                        (str,),
                    'start':
                        (str,),
                    'end':
                        (str,),
                },
                'attribute_map': {
                    'host_id': 'host_id',
                    'start': 'start',
                    'end': 'end',
                },
                'location_map': {
                    'host_id': 'query',
                    'start': 'query',
                    'end': 'query',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.get_droplet_memory_total_metrics_endpoint = _Endpoint(
            settings={
                'response_type': (Metrics,),
                'auth': [
                    'bearer_auth'
                ],
                'endpoint_path': '/v2/monitoring/metrics/droplet/memory_total',
                'operation_id': 'get_droplet_memory_total_metrics',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'host_id',
                    'start',
                    'end',
                ],
                'required': [
                    'host_id',
                    'start',
                    'end',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'host_id':
                        (str,),
                    'start':
                        (str,),
                    'end':
                        (str,),
                },
                'attribute_map': {
                    'host_id': 'host_id',
                    'start': 'start',
                    'end': 'end',
                },
                'location_map': {
                    'host_id': 'query',
                    'start': 'query',
                    'end': 'query',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.list_alert_policies_endpoint = _Endpoint(
            settings={
                'response_type': (bool, date, datetime, dict, float, int, list, str, none_type,),
                'auth': [
                    'bearer_auth'
                ],
                'endpoint_path': '/v2/monitoring/alerts',
                'operation_id': 'list_alert_policies',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'per_page',
                    'page',
                ],
                'required': [],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                    'per_page',
                    'page',
                ]
            },
            root_map={
                'validations': {
                    ('per_page',): {

                        'inclusive_maximum': 200,
                        'inclusive_minimum': 1,
                    },
                    ('page',): {

                        'inclusive_minimum': 1,
                    },
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'per_page':
                        (int,),
                    'page':
                        (int,),
                },
                'attribute_map': {
                    'per_page': 'per_page',
                    'page': 'page',
                },
                'location_map': {
                    'per_page': 'query',
                    'page': 'query',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.update_alert_policy_endpoint = _Endpoint(
            settings={
                'response_type': (AlertPolicy,),
                'auth': [
                    'bearer_auth'
                ],
                'endpoint_path': '/v2/monitoring/alerts/{alert_uuid}',
                'operation_id': 'update_alert_policy',
                'http_method': 'PUT',
                'servers': None,
            },
            params_map={
                'all': [
                    'alert_uuid',
                    'alert_policy_request',
                ],
                'required': [
                    'alert_uuid',
                    'alert_policy_request',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'alert_uuid':
                        (str,),
                    'alert_policy_request':
                        (AlertPolicyRequest,),
                },
                'attribute_map': {
                    'alert_uuid': 'alert_uuid',
                },
                'location_map': {
                    'alert_uuid': 'path',
                    'alert_policy_request': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [
                    'application/json'
                ]
            },
            api_client=api_client
        )

    def create_alert_policy(
        self,
        alert_policy_request,
        **kwargs
    ):
        """Create Alert Policy  # noqa: E501

        To create a new alert, send a POST request to `/v2/monitoring/alerts`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.create_alert_policy(alert_policy_request, async_req=True)
        >>> result = thread.get()

        Args:
            alert_policy_request (AlertPolicyRequest): The 'type' field dictates what type of entity that the alert policy applies to and hence what type of entity is passed in the 'entities' array. If both the 'tags' array and 'entities' array are empty the alert policy applies to all entities of the relevant type that are owned by the user account. Otherwise the following table shows the valid entity types for each type of alert policy: <table><thead><tr><td>Type</td><td>Description</td><td>Valid Entity Type</td></tr></thead><tr><td>v1/insights/droplet/memory_utilization_percent</td><td>alert on the percent of memory utilization</td><td>droplet ID</td></tr><tr><td>v1/insights/droplet/disk_read</td><td>alert on the rate of disk read I/O in MBps</td><td>droplet ID</td></tr><tr><td>v1/insights/droplet/load_5</td><td>alert on the 5 minute load average</td><td>droplet ID</td></tr><tr><td>v1/insights/droplet/load_15</td><td>alert on the 15 minute load average</td><td>droplet ID</td></tr><tr><td>v1/insights/droplet/disk_utilization_percent</td><td>alert on the percent of disk utilization</td><td>droplet ID</td></tr><tr><td>v1/insights/droplet/cpu</td><td>alert on the percent of CPU utilization</td><td>droplet ID</td></tr><tr><td>v1/insights/droplet/disk_write</td><td>alert on the rate of disk write I/O in MBps</td><td>droplet ID</td></tr><tr><td>v1/insights/droplet/public_outbound_bandwidth</td><td>alert on the rate of public outbound bandwidth in Mbps</td><td>droplet ID</td></tr><tr><td>v1/insights/droplet/public_inbound_bandwidth</td><td>alert on the rate of public inbound bandwidth in Mbps</td><td>droplet ID</td></tr><tr><td>v1/insights/droplet/private_outbound_bandwidth</td><td>alert on the rate of private outbound bandwidth in Mbps</td><td>droplet ID</td></tr><tr><td>v1/insights/droplet/private_inbound_bandwidth</td><td>alert on the rate of private inbound bandwidth in Mbps</td><td>droplet ID</td></tr><tr><td>v1/insights/droplet/load_1</td><td>alert on the 1 minute load average</td><td>droplet ID</td></tr></table>

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            AlertPolicy
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['alert_policy_request'] = \
            alert_policy_request
        return self.create_alert_policy_endpoint.call_with_http_info(**kwargs)

    def delete_alert_policy(
        self,
        alert_uuid,
        **kwargs
    ):
        """Delete an Alert Policy  # noqa: E501

        To delete an alert policy, send a DELETE request to `/v2/monitoring/alerts/{alert_uuid}`  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.delete_alert_policy(alert_uuid, async_req=True)
        >>> result = thread.get()

        Args:
            alert_uuid (str): A unique identifier for an alert policy.

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            None
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['alert_uuid'] = \
            alert_uuid
        return self.delete_alert_policy_endpoint.call_with_http_info(**kwargs)

    def get_alert_policy(
        self,
        alert_uuid,
        **kwargs
    ):
        """Retrieve an Existing Alert Policy  # noqa: E501

        To retrieve a given alert policy, send a GET request to `/v2/monitoring/alerts/{alert_uuid}`  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_alert_policy(alert_uuid, async_req=True)
        >>> result = thread.get()

        Args:
            alert_uuid (str): A unique identifier for an alert policy.

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            AlertPolicy
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['alert_uuid'] = \
            alert_uuid
        return self.get_alert_policy_endpoint.call_with_http_info(**kwargs)

    def get_droplet_bandwidth_metrics(
        self,
        host_id,
        interface,
        direction,
        start,
        end,
        **kwargs
    ):
        """Get Droplet Bandwidth Metrics  # noqa: E501

        To retrieve bandwidth metrics for a given Droplet, send a GET request to `/v2/monitoring/metrics/droplet/bandwidth`. Use the `interface` query parameter to specify if the results should be for the `private` or `public` interface. Use the `direction` query parameter to specify if the results should be for `inbound` or `outbound` traffic.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_droplet_bandwidth_metrics(host_id, interface, direction, start, end, async_req=True)
        >>> result = thread.get()

        Args:
            host_id (str): The droplet ID.
            interface (str): The network interface.
            direction (str): The traffic direction.
            start (str): Timestamp to start metric window.
            end (str): Timestamp to end metric window.

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            Metrics
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['host_id'] = \
            host_id
        kwargs['interface'] = \
            interface
        kwargs['direction'] = \
            direction
        kwargs['start'] = \
            start
        kwargs['end'] = \
            end
        return self.get_droplet_bandwidth_metrics_endpoint.call_with_http_info(**kwargs)

    def get_droplet_cpu_metrics(
        self,
        host_id,
        start,
        end,
        **kwargs
    ):
        """Get Droplet CPU Metrics  # noqa: E501

        To retrieve CPU metrics for a given droplet, send a GET request to `/v2/monitoring/metrics/droplet/cpu`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_droplet_cpu_metrics(host_id, start, end, async_req=True)
        >>> result = thread.get()

        Args:
            host_id (str): The droplet ID.
            start (str): Timestamp to start metric window.
            end (str): Timestamp to end metric window.

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            Metrics
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['host_id'] = \
            host_id
        kwargs['start'] = \
            start
        kwargs['end'] = \
            end
        return self.get_droplet_cpu_metrics_endpoint.call_with_http_info(**kwargs)

    def get_droplet_filesystem_free_metrics(
        self,
        host_id,
        start,
        end,
        **kwargs
    ):
        """Get Droplet Filesystem Free Metrics  # noqa: E501

        To retrieve filesystem free metrics for a given droplet, send a GET request to `/v2/monitoring/metrics/droplet/filesystem_free`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_droplet_filesystem_free_metrics(host_id, start, end, async_req=True)
        >>> result = thread.get()

        Args:
            host_id (str): The droplet ID.
            start (str): Timestamp to start metric window.
            end (str): Timestamp to end metric window.

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            Metrics
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['host_id'] = \
            host_id
        kwargs['start'] = \
            start
        kwargs['end'] = \
            end
        return self.get_droplet_filesystem_free_metrics_endpoint.call_with_http_info(**kwargs)

    def get_droplet_filesystem_size_metrics(
        self,
        host_id,
        start,
        end,
        **kwargs
    ):
        """Get Droplet Filesystem Size Metrics  # noqa: E501

        To retrieve filesystem size metrics for a given droplet, send a GET request to `/v2/monitoring/metrics/droplet/filesystem_size`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_droplet_filesystem_size_metrics(host_id, start, end, async_req=True)
        >>> result = thread.get()

        Args:
            host_id (str): The droplet ID.
            start (str): Timestamp to start metric window.
            end (str): Timestamp to end metric window.

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            Metrics
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['host_id'] = \
            host_id
        kwargs['start'] = \
            start
        kwargs['end'] = \
            end
        return self.get_droplet_filesystem_size_metrics_endpoint.call_with_http_info(**kwargs)

    def get_droplet_load15_metrics(
        self,
        host_id,
        start,
        end,
        **kwargs
    ):
        """Get Droplet Load15 Metrics  # noqa: E501

        To retrieve 15 minute load average metrics for a given droplet, send a GET request to `/v2/monitoring/metrics/droplet/load_15`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_droplet_load15_metrics(host_id, start, end, async_req=True)
        >>> result = thread.get()

        Args:
            host_id (str): The droplet ID.
            start (str): Timestamp to start metric window.
            end (str): Timestamp to end metric window.

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            Metrics
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['host_id'] = \
            host_id
        kwargs['start'] = \
            start
        kwargs['end'] = \
            end
        return self.get_droplet_load15_metrics_endpoint.call_with_http_info(**kwargs)

    def get_droplet_load1_metrics(
        self,
        host_id,
        start,
        end,
        **kwargs
    ):
        """Get Droplet Load1 Metrics  # noqa: E501

        To retrieve 1 minute load average metrics for a given droplet, send a GET request to `/v2/monitoring/metrics/droplet/load_1`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_droplet_load1_metrics(host_id, start, end, async_req=True)
        >>> result = thread.get()

        Args:
            host_id (str): The droplet ID.
            start (str): Timestamp to start metric window.
            end (str): Timestamp to end metric window.

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            Metrics
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['host_id'] = \
            host_id
        kwargs['start'] = \
            start
        kwargs['end'] = \
            end
        return self.get_droplet_load1_metrics_endpoint.call_with_http_info(**kwargs)

    def get_droplet_load5_metrics(
        self,
        host_id,
        start,
        end,
        **kwargs
    ):
        """Get Droplet Load5 Metrics  # noqa: E501

        To retrieve 5 minute load average metrics for a given droplet, send a GET request to `/v2/monitoring/metrics/droplet/load_5`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_droplet_load5_metrics(host_id, start, end, async_req=True)
        >>> result = thread.get()

        Args:
            host_id (str): The droplet ID.
            start (str): Timestamp to start metric window.
            end (str): Timestamp to end metric window.

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            Metrics
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['host_id'] = \
            host_id
        kwargs['start'] = \
            start
        kwargs['end'] = \
            end
        return self.get_droplet_load5_metrics_endpoint.call_with_http_info(**kwargs)

    def get_droplet_memory_available_metrics(
        self,
        host_id,
        start,
        end,
        **kwargs
    ):
        """Get Droplet Available Memory Metrics  # noqa: E501

        To retrieve available memory metrics for a given droplet, send a GET request to `/v2/monitoring/metrics/droplet/memory_available`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_droplet_memory_available_metrics(host_id, start, end, async_req=True)
        >>> result = thread.get()

        Args:
            host_id (str): The droplet ID.
            start (str): Timestamp to start metric window.
            end (str): Timestamp to end metric window.

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            Metrics
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['host_id'] = \
            host_id
        kwargs['start'] = \
            start
        kwargs['end'] = \
            end
        return self.get_droplet_memory_available_metrics_endpoint.call_with_http_info(**kwargs)

    def get_droplet_memory_cached_metrics(
        self,
        host_id,
        start,
        end,
        **kwargs
    ):
        """Get Droplet Cached Memory Metrics  # noqa: E501

        To retrieve cached memory metrics for a given droplet, send a GET request to `/v2/monitoring/metrics/droplet/memory_cached`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_droplet_memory_cached_metrics(host_id, start, end, async_req=True)
        >>> result = thread.get()

        Args:
            host_id (str): The droplet ID.
            start (str): Timestamp to start metric window.
            end (str): Timestamp to end metric window.

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            Metrics
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['host_id'] = \
            host_id
        kwargs['start'] = \
            start
        kwargs['end'] = \
            end
        return self.get_droplet_memory_cached_metrics_endpoint.call_with_http_info(**kwargs)

    def get_droplet_memory_free_metrics(
        self,
        host_id,
        start,
        end,
        **kwargs
    ):
        """Get Droplet Free Memory Metrics  # noqa: E501

        To retrieve free memory metrics for a given droplet, send a GET request to `/v2/monitoring/metrics/droplet/memory_free`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_droplet_memory_free_metrics(host_id, start, end, async_req=True)
        >>> result = thread.get()

        Args:
            host_id (str): The droplet ID.
            start (str): Timestamp to start metric window.
            end (str): Timestamp to end metric window.

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            Metrics
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['host_id'] = \
            host_id
        kwargs['start'] = \
            start
        kwargs['end'] = \
            end
        return self.get_droplet_memory_free_metrics_endpoint.call_with_http_info(**kwargs)

    def get_droplet_memory_total_metrics(
        self,
        host_id,
        start,
        end,
        **kwargs
    ):
        """Get Droplet Total Memory Metrics  # noqa: E501

        To retrieve total memory metrics for a given droplet, send a GET request to `/v2/monitoring/metrics/droplet/memory_total`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_droplet_memory_total_metrics(host_id, start, end, async_req=True)
        >>> result = thread.get()

        Args:
            host_id (str): The droplet ID.
            start (str): Timestamp to start metric window.
            end (str): Timestamp to end metric window.

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            Metrics
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['host_id'] = \
            host_id
        kwargs['start'] = \
            start
        kwargs['end'] = \
            end
        return self.get_droplet_memory_total_metrics_endpoint.call_with_http_info(**kwargs)

    def list_alert_policies(
        self,
        **kwargs
    ):
        """List Alert Policies  # noqa: E501

        Returns all alert policies that are configured for the given account. To List all alert policies, send a GET request to `/v2/monitoring/alerts`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.list_alert_policies(async_req=True)
        >>> result = thread.get()


        Keyword Args:
            per_page (int): Number of items returned per page. [optional] if omitted the server will use the default value of 20
            page (int): Which 'page' of paginated results to return.. [optional] if omitted the server will use the default value of 1
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            bool, date, datetime, dict, float, int, list, str, none_type
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_host_index'] = kwargs.get('_host_index')
        return self.list_alert_policies_endpoint.call_with_http_info(**kwargs)

    def update_alert_policy(
        self,
        alert_uuid,
        alert_policy_request,
        **kwargs
    ):
        """Update an Alert Policy  # noqa: E501

        To update en existing policy, send a PUT request to `v2/monitoring/alerts/{alert_uuid}`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.update_alert_policy(alert_uuid, alert_policy_request, async_req=True)
        >>> result = thread.get()

        Args:
            alert_uuid (str): A unique identifier for an alert policy.
            alert_policy_request (AlertPolicyRequest): The 'type' field dictates what type of entity that the alert policy applies to and hence what type of entity is passed in the 'entities' array. If both the 'tags' array and 'entities' array are empty the alert policy applies to all entities of the relevant type that are owned by the user account. Otherwise the following table shows the valid entity types for each type of alert policy: <table><thead><tr><td>Type</td><td>Description</td><td>Valid Entity Type</td></tr></thead><tr><td>v1/insights/droplet/memory_utilization_percent</td><td>alert on the percent of memory utilization</td><td>droplet ID</td></tr><tr><td>v1/insights/droplet/disk_read</td><td>alert on the rate of disk read I/O in MBps</td><td>droplet ID</td></tr><tr><td>v1/insights/droplet/load_5</td><td>alert on the 5 minute load average</td><td>droplet ID</td></tr><tr><td>v1/insights/droplet/load_15</td><td>alert on the 15 minute load average</td><td>droplet ID</td></tr><tr><td>v1/insights/droplet/disk_utilization_percent</td><td>alert on the percent of disk utilization</td><td>droplet ID</td></tr><tr><td>v1/insights/droplet/cpu</td><td>alert on the percent of CPU utilization</td><td>droplet ID</td></tr><tr><td>v1/insights/droplet/disk_write</td><td>alert on the rate of disk write I/O in MBps</td><td>droplet ID</td></tr><tr><td>v1/insights/droplet/public_outbound_bandwidth</td><td>alert on the rate of public outbound bandwidth in Mbps</td><td>droplet ID</td></tr><tr><td>v1/insights/droplet/public_inbound_bandwidth</td><td>alert on the rate of public inbound bandwidth in Mbps</td><td>droplet ID</td></tr><tr><td>v1/insights/droplet/private_outbound_bandwidth</td><td>alert on the rate of private outbound bandwidth in Mbps</td><td>droplet ID</td></tr><tr><td>v1/insights/droplet/private_inbound_bandwidth</td><td>alert on the rate of private inbound bandwidth in Mbps</td><td>droplet ID</td></tr><tr><td>v1/insights/droplet/load_1</td><td>alert on the 1 minute load average</td><td>droplet ID</td></tr></table>

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            AlertPolicy
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['alert_uuid'] = \
            alert_uuid
        kwargs['alert_policy_request'] = \
            alert_policy_request
        return self.update_alert_policy_endpoint.call_with_http_info(**kwargs)

