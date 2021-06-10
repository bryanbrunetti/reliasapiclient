# relias_api_client.AuthenticationApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**authenticate**](AuthenticationApi.md#authenticate) | **POST** /v1/authenticate | Get an authentication token.


# **authenticate**
> AuthenticateResponse authenticate(credentials)

Get an authentication token.

### Example
```python
from __future__ import print_function
import time
import relias_api_client
from relias_api_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = relias_api_client.AuthenticationApi()
credentials = relias_api_client.AuthenticateRequest() # AuthenticateRequest | 

try:
    # Get an authentication token.
    api_response = api_instance.authenticate(credentials)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthenticationApi->authenticate: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **credentials** | [**AuthenticateRequest**](AuthenticateRequest.md)|  | 

### Return type

[**AuthenticateResponse**](AuthenticateResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

