# openapi_client.ReservationsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cancel_reservation_reservations_reservation_id_delete**](ReservationsApi.md#cancel_reservation_reservations_reservation_id_delete) | **DELETE** /reservations/{reservation_id} | Cancel Reservation
[**get_reservations_reservations_get**](ReservationsApi.md#get_reservations_reservations_get) | **GET** /reservations/ | Get Reservations


# **cancel_reservation_reservations_reservation_id_delete**
> object cancel_reservation_reservations_reservation_id_delete(reservation_id)

Cancel Reservation

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
    api_instance = openapi_client.ReservationsApi(api_client)
    reservation_id = 56 # int | 

    try:
        # Cancel Reservation
        api_response = api_instance.cancel_reservation_reservations_reservation_id_delete(reservation_id)
        print("The response of ReservationsApi->cancel_reservation_reservations_reservation_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReservationsApi->cancel_reservation_reservations_reservation_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **reservation_id** | **int**|  | 

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
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_reservations_reservations_get**
> List[ReservationResponse] get_reservations_reservations_get()

Get Reservations

### Example


```python
import openapi_client
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
    api_instance = openapi_client.ReservationsApi(api_client)

    try:
        # Get Reservations
        api_response = api_instance.get_reservations_reservations_get()
        print("The response of ReservationsApi->get_reservations_reservations_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReservationsApi->get_reservations_reservations_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[ReservationResponse]**](ReservationResponse.md)

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

