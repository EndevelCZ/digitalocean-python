# openapi_client.ImagesApi

All URIs are relative to *https://api.digitalocean.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_custom_image**](ImagesApi.md#create_custom_image) | **POST** /v2/images | Create a Custom Image
[**delete_image**](ImagesApi.md#delete_image) | **DELETE** /v2/images/{image_id} | Delete an Image
[**get_image**](ImagesApi.md#get_image) | **GET** /v2/images/{image_id} | Retrieve an Existing Image
[**get_images_list**](ImagesApi.md#get_images_list) | **GET** /v2/images | List All Images
[**update_image**](ImagesApi.md#update_image) | **PUT** /v2/images/{image_id} | Update an Image


# **create_custom_image**
> bool, date, datetime, dict, float, int, list, str, none_type create_custom_image(image_new_custom)

Create a Custom Image

To create a new custom image, send a POST request to /v2/images. The body must contain a url attribute pointing to a Linux virtual machine image to be imported into DigitalOcean. The image must be in the raw, qcow2, vhdx, vdi, or vmdk format. It may be compressed using gzip or bzip2 and must be smaller than 100 GB after  being decompressed. 

### Example

* Bearer Authentication (bearer_auth):

```python
import time
import openapi_client
from openapi_client.api import images_api
from openapi_client.model.image_new_custom import ImageNewCustom
from openapi_client.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to https://api.digitalocean.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.digitalocean.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: bearer_auth
configuration = openapi_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = images_api.ImagesApi(api_client)
    image_new_custom = ImageNewCustom() # ImageNewCustom | 

    # example passing only required values which don't have defaults set
    try:
        # Create a Custom Image
        api_response = api_instance.create_custom_image(image_new_custom)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ImagesApi->create_custom_image: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **image_new_custom** | [**ImageNewCustom**](ImageNewCustom.md)|  |

### Return type

**bool, date, datetime, dict, float, int, list, str, none_type**

### Authorization

[bearer_auth](../README.md#bearer_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | The response will be a JSON object with a key set to &#x60;image&#x60;.  The value of this will be an image object containing a subset of the standard  image attributes as listed below, including the image&#39;s &#x60;id&#x60; and &#x60;status&#x60;.  After initial creation, the &#x60;status&#x60; will be &#x60;NEW&#x60;. Using the image&#39;s id, you  may query the image&#39;s status by sending a &#x60;GET&#x60; request to the  &#x60;/v2/images/$IMAGE_ID&#x60; endpoint.  When the &#x60;status&#x60; changes to &#x60;available&#x60;, the image will be ready for use. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**401** | Unauthorized |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**429** | API Rate limit exceeded |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**500** | Server error. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**0** | Unexpected error |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_image**
> delete_image(image_id)

Delete an Image

To delete a snapshot or custom image, send a `DELETE` request to `/v2/images/$IMAGE_ID`. 

### Example

* Bearer Authentication (bearer_auth):

```python
import time
import openapi_client
from openapi_client.api import images_api
from openapi_client.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to https://api.digitalocean.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.digitalocean.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: bearer_auth
configuration = openapi_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = images_api.ImagesApi(api_client)
    image_id = 62137902 # int | A unique number that can be used to identify and reference a specific image.

    # example passing only required values which don't have defaults set
    try:
        # Delete an Image
        api_instance.delete_image(image_id)
    except openapi_client.ApiException as e:
        print("Exception when calling ImagesApi->delete_image: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **image_id** | **int**| A unique number that can be used to identify and reference a specific image. |

### Return type

void (empty response body)

### Authorization

[bearer_auth](../README.md#bearer_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | The action was successful and the response body is empty. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**401** | Unauthorized |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**404** | The resource was not found. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**429** | API Rate limit exceeded |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**500** | Server error. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**0** | Unexpected error |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_image**
> InlineResponse2004 get_image(image_id)

Retrieve an Existing Image

To retrieve information about an image, send a `GET` request to `/v2/images/$IDENTIFIER`. 

### Example

* Bearer Authentication (bearer_auth):

```python
import time
import openapi_client
from openapi_client.api import images_api
from openapi_client.model.inline_response2004 import InlineResponse2004
from openapi_client.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to https://api.digitalocean.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.digitalocean.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: bearer_auth
configuration = openapi_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = images_api.ImagesApi(api_client)
    image_id = None # bool, date, datetime, dict, float, int, list, str, none_type | A unique number (id) or string (slug) used to identify and reference a specific image.  **Public** images can be identified by image `id` or `slug`.  **Private** images *must* be identified by image `id`. 

    # example passing only required values which don't have defaults set
    try:
        # Retrieve an Existing Image
        api_response = api_instance.get_image(image_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ImagesApi->get_image: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **image_id** | **bool, date, datetime, dict, float, int, list, str, none_type**| A unique number (id) or string (slug) used to identify and reference a specific image.  **Public** images can be identified by image &#x60;id&#x60; or &#x60;slug&#x60;.  **Private** images *must* be identified by image &#x60;id&#x60;.  |

### Return type

[**InlineResponse2004**](InlineResponse2004.md)

### Authorization

[bearer_auth](../README.md#bearer_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The response will be a JSON object with a key called &#x60;image&#x60;.  The value of this will be an image object containing the standard image attributes. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**401** | Unauthorized |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**404** | The resource was not found. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**429** | API Rate limit exceeded |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**500** | Server error. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**0** | Unexpected error |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_images_list**
> bool, date, datetime, dict, float, int, list, str, none_type get_images_list()

List All Images

To list all of the images available on your account, send a GET request to /v2/images.  ## Filtering Results -----  It's possible to request filtered results by including certain query parameters.  **Image Type**  Either 1-Click Application or OS Distribution images can be filtered by using the `type` query parameter.  > Important: The `type` query parameter does not directly relate to the `type` attribute.  To retrieve only ***distribution*** images, include the `type` query parameter set to distribution, `/v2/images?type=distribution`.  To retrieve only ***application*** images, include the `type` query parameter set to application, `/v2/images?type=application`.  **User Images**  To retrieve only the private images of a user, include the `private` query parameter set to true, `/v2/images?private=true`.  **Tags**  To list all images assigned to a specific tag, include the `tag_name` query parameter set to the name of the tag in your GET request. For example, `/v2/images?tag_name=$TAG_NAME`. 

### Example

* Bearer Authentication (bearer_auth):

```python
import time
import openapi_client
from openapi_client.api import images_api
from openapi_client.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to https://api.digitalocean.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.digitalocean.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: bearer_auth
configuration = openapi_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = images_api.ImagesApi(api_client)
    type = "distribution" # str | Filters results based on image type which can be either `application` or `distribution`. (optional)
    private = True # bool | Used to filter only user images. (optional)
    tag_name = "base-image" # str | Used to filter images by a specific tag. (optional)
    per_page = 2 # int | Number of items returned per page (optional) if omitted the server will use the default value of 20
    page = 1 # int | Which 'page' of paginated results to return. (optional) if omitted the server will use the default value of 1

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List All Images
        api_response = api_instance.get_images_list(type=type, private=private, tag_name=tag_name, per_page=per_page, page=page)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ImagesApi->get_images_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**| Filters results based on image type which can be either &#x60;application&#x60; or &#x60;distribution&#x60;. | [optional]
 **private** | **bool**| Used to filter only user images. | [optional]
 **tag_name** | **str**| Used to filter images by a specific tag. | [optional]
 **per_page** | **int**| Number of items returned per page | [optional] if omitted the server will use the default value of 20
 **page** | **int**| Which &#39;page&#39; of paginated results to return. | [optional] if omitted the server will use the default value of 1

### Return type

**bool, date, datetime, dict, float, int, list, str, none_type**

### Authorization

[bearer_auth](../README.md#bearer_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The response will be a JSON object with a key called &#x60;images&#x60;.  This will be set to an array of image objects, each of which will contain the standard image attributes. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**401** | Unauthorized |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**429** | API Rate limit exceeded |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**500** | Server error. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**0** | Unexpected error |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_image**
> InlineResponse2004 update_image(image_id, image_update)

Update an Image

To update an image, send a `PUT` request to `/v2/images/$IMAGE_ID`. Set the `name` attribute to the new value you would like to use. For custom images, the `description` and `distribution` attributes may also be updated. 

### Example

* Bearer Authentication (bearer_auth):

```python
import time
import openapi_client
from openapi_client.api import images_api
from openapi_client.model.inline_response2004 import InlineResponse2004
from openapi_client.model.error import Error
from openapi_client.model.image_update import ImageUpdate
from pprint import pprint
# Defining the host is optional and defaults to https://api.digitalocean.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.digitalocean.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: bearer_auth
configuration = openapi_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = images_api.ImagesApi(api_client)
    image_id = 62137902 # int | A unique number that can be used to identify and reference a specific image.
    image_update = ImageUpdate(
        name="Nifty New Snapshot",
        distribution=Distribution("Ubuntu"),
        description=" ",
    ) # ImageUpdate | 

    # example passing only required values which don't have defaults set
    try:
        # Update an Image
        api_response = api_instance.update_image(image_id, image_update)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ImagesApi->update_image: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **image_id** | **int**| A unique number that can be used to identify and reference a specific image. |
 **image_update** | [**ImageUpdate**](ImageUpdate.md)|  |

### Return type

[**InlineResponse2004**](InlineResponse2004.md)

### Authorization

[bearer_auth](../README.md#bearer_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The response will be a JSON object with a key set to &#x60;image&#x60;.  The value of this will be an image object containing the standard image attributes. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**401** | Unauthorized |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**404** | The resource was not found. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**429** | API Rate limit exceeded |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**500** | Server error. |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |
**0** | Unexpected error |  * ratelimit-limit -  <br>  * ratelimit-remaining -  <br>  * ratelimit-reset -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

