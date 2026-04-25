# openapi_client.BooksApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_book_books_post**](BooksApi.md#create_book_books_post) | **POST** /books/ | Create Book
[**get_book_books_book_id_get**](BooksApi.md#get_book_books_book_id_get) | **GET** /books/{book_id} | Get Book
[**get_books_books_get**](BooksApi.md#get_books_books_get) | **GET** /books/ | Get Books
[**get_stats_books_stats_get**](BooksApi.md#get_stats_books_stats_get) | **GET** /books/stats | Get Stats
[**reserve_book_books_book_id_reserve_post**](BooksApi.md#reserve_book_books_book_id_reserve_post) | **POST** /books/{book_id}/reserve | Reserve Book


# **create_book_books_post**
> BookResponse create_book_books_post(book_create)

Create Book

### Example


```python
import openapi_client
from openapi_client.models.book_create import BookCreate
from openapi_client.models.book_response import BookResponse
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.BooksApi(api_client)
    book_create = openapi_client.BookCreate() # BookCreate | 

    try:
        # Create Book
        api_response = api_instance.create_book_books_post(book_create)
        print("The response of BooksApi->create_book_books_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BooksApi->create_book_books_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **book_create** | [**BookCreate**](BookCreate.md)|  | 

### Return type

[**BookResponse**](BookResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_book_books_book_id_get**
> BookResponse get_book_books_book_id_get(book_id)

Get Book

### Example


```python
import openapi_client
from openapi_client.models.book_response import BookResponse
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.BooksApi(api_client)
    book_id = 56 # int | 

    try:
        # Get Book
        api_response = api_instance.get_book_books_book_id_get(book_id)
        print("The response of BooksApi->get_book_books_book_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BooksApi->get_book_books_book_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **book_id** | **int**|  | 

### Return type

[**BookResponse**](BookResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_books_books_get**
> List[BookResponse] get_books_books_get()

Get Books

### Example


```python
import openapi_client
from openapi_client.models.book_response import BookResponse
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.BooksApi(api_client)

    try:
        # Get Books
        api_response = api_instance.get_books_books_get()
        print("The response of BooksApi->get_books_books_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BooksApi->get_books_books_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[BookResponse]**](BookResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_stats_books_stats_get**
> object get_stats_books_stats_get()

Get Stats

### Example


```python
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.BooksApi(api_client)

    try:
        # Get Stats
        api_response = api_instance.get_stats_books_stats_get()
        print("The response of BooksApi->get_stats_books_stats_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BooksApi->get_stats_books_stats_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reserve_book_books_book_id_reserve_post**
> ReservationResponse reserve_book_books_book_id_reserve_post(book_id, reservation_create)

Reserve Book

### Example


```python
import openapi_client
from openapi_client.models.reservation_create import ReservationCreate
from openapi_client.models.reservation_response import ReservationResponse
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.BooksApi(api_client)
    book_id = 56 # int | 
    reservation_create = openapi_client.ReservationCreate() # ReservationCreate | 

    try:
        # Reserve Book
        api_response = api_instance.reserve_book_books_book_id_reserve_post(book_id, reservation_create)
        print("The response of BooksApi->reserve_book_books_book_id_reserve_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BooksApi->reserve_book_books_book_id_reserve_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **book_id** | **int**|  | 
 **reservation_create** | [**ReservationCreate**](ReservationCreate.md)|  | 

### Return type

[**ReservationResponse**](ReservationResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

