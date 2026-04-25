# ReservationResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**book_id** | **int** |  | 
**user_name** | **str** |  | 
**reservation_date** | **datetime** |  | 
**expires_at** | **datetime** |  | 

## Example

```python
from openapi_client.models.reservation_response import ReservationResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ReservationResponse from a JSON string
reservation_response_instance = ReservationResponse.from_json(json)
# print the JSON string representation of the object
print(ReservationResponse.to_json())

# convert the object into a dict
reservation_response_dict = reservation_response_instance.to_dict()
# create an instance of ReservationResponse from a dict
reservation_response_from_dict = ReservationResponse.from_dict(reservation_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


