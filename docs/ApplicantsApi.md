# relias_api_client.ApplicantsApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**convert_to_learner**](ApplicantsApi.md#convert_to_learner) | **POST** /v1/applicants/{username}/convert | Converts an applicant based on the username provided to a learner with the new username supplied
[**create_applicant**](ApplicantsApi.md#create_applicant) | **POST** /v1/applicants | Creates an applicant with the supplied information
[**get_applicant**](ApplicantsApi.md#get_applicant) | **GET** /v1/applicants/{username} | Retrieves an applicant based on the username provided
[**update_applicant**](ApplicantsApi.md#update_applicant) | **PATCH** /v1/applicants/{username} | Update an applicant using JSON patch documents.


# **convert_to_learner**
> convert_to_learner(username, request, org_id=org_id)

Converts an applicant based on the username provided to a learner with the new username supplied

When providing username, be sure to URL encode the value if it contains any special characters.

### Example
```python
from __future__ import print_function
import time
import relias_api_client
from relias_api_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = relias_api_client.ApplicantsApi()
username = 'username_example' # str | The username of the applicant to convert to a learner.
request = relias_api_client.ConvertToLearnerRequest() # ConvertToLearnerRequest | The applicant's new username.
org_id = 56 # int | organization ID of the applicant (defaults to current organization ID) (optional)

try:
    # Converts an applicant based on the username provided to a learner with the new username supplied
    api_instance.convert_to_learner(username, request, org_id=org_id)
except ApiException as e:
    print("Exception when calling ApplicantsApi->convert_to_learner: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| The username of the applicant to convert to a learner. | 
 **request** | [**ConvertToLearnerRequest**](ConvertToLearnerRequest.md)| The applicant&#39;s new username. | 
 **org_id** | **int**| organization ID of the applicant (defaults to current organization ID) | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_applicant**
> CreateApplicantResponse create_applicant(applicant_information)

Creates an applicant with the supplied information

Notes:  <ul><li>Org ID is required and should be the ID of your organization.</li><li>First name is required and must not exceed 50 characters.</li><li>Last name is required and must not exceed 50 characters.</li><li>Email is required and will become the username.</li><li>Email must be unique within your organization and not exceed 150 characters.</li><li>Temporary password will be emailed to applicant.</li><li>Job Titles are optional.</li><li>Tracking ID, optional, must be unique within your organization and not exceed 50 characters.          Used to link to an applicant in an external system.      </li><li>GUID, optional, must be unique within your organization and not exceed 50 characters.</li></ul>

### Example
```python
from __future__ import print_function
import time
import relias_api_client
from relias_api_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = relias_api_client.ApplicantsApi()
applicant_information = relias_api_client.CreateApplicantRequest() # CreateApplicantRequest | the information of the applicant

try:
    # Creates an applicant with the supplied information
    api_response = api_instance.create_applicant(applicant_information)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicantsApi->create_applicant: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **applicant_information** | [**CreateApplicantRequest**](CreateApplicantRequest.md)| the information of the applicant | 

### Return type

[**CreateApplicantResponse**](CreateApplicantResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_applicant**
> GetApplicantModel get_applicant(username, org_id=org_id)

Retrieves an applicant based on the username provided

When providing username, be sure to URL encode the value if it contains any special characters.

### Example
```python
from __future__ import print_function
import time
import relias_api_client
from relias_api_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = relias_api_client.ApplicantsApi()
username = 'username_example' # str | the username of the applicant
org_id = 56 # int | organization ID of the applicant (defaults to current organization ID) (optional)

try:
    # Retrieves an applicant based on the username provided
    api_response = api_instance.get_applicant(username, org_id=org_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicantsApi->get_applicant: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| the username of the applicant | 
 **org_id** | **int**| organization ID of the applicant (defaults to current organization ID) | [optional] 

### Return type

[**GetApplicantModel**](GetApplicantModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_applicant**
> update_applicant(username, request, org_id=org_id)

Update an applicant using JSON patch documents.

When providing username, be sure to URL encode the value if it contains any special characters.  Provide a set of one or more JSON patch documents describing the changes to apply to the applicant.  See http://jsonpatch.com/ and below for examples.  <br />  Fields that can be updated include:  <ul><li>First name          <pre>{\"op\": \"replace\", \"path\": \"/FirstName\", \"value\": \"new name\"}</pre></li><br /><li>Last name          <pre>{\"op\": \"replace\", \"path\": \"/LastName\", \"value\": \"new name\"}</pre></li><br /><li>Email (will also change the applicant's login)          <pre>{\"op\": \"replace\", \"path\": \"/Email\", \"value\": \"new@email.com\"}</pre></li><br /><li>Job titles          <pre>{\"op\": \"replace\", \"path\": \"/JobTitles\", \"value\": [\"Job title 1\", \"Job title 2\"]}</pre></li><br /><li>Tracking ID          <pre>{\"op\": \"replace\", \"path\": \"/TrackingId\", \"value\": \"new tracking ID\"}</pre></li><br /><li>GUID          <pre>{\"op\": \"replace\", \"path\": \"/Guid\", \"value\": \"new GUID\"}</pre></li><br /><li>User status          <pre>{\"op\": \"replace\", \"path\": \"/UserStatus\", \"value\": \"Inactive\"}</pre>          Options:          <ul><li>Active</li><li>Inactive</li></ul></li></ul><p>  Note that the <b>path</b> parameter is case sensitive.  <br /><br />  Example: Changing an applicant's first name, last name and user status  </p><pre>  [      {\"op\": \"replace\", \"path\": \"/FirstName\", \"value\": \"new first name\"},      {\"op\": \"replace\", \"path\": \"/LastName\", \"value\": \"new last name\"},      {\"op\": \"replace\", \"path\": \"/UserStatus\", \"value\": \"Inactive\"}  ]  </pre>

### Example
```python
from __future__ import print_function
import time
import relias_api_client
from relias_api_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = relias_api_client.ApplicantsApi()
username = 'username_example' # str | The username of the applicant to update.
request = [relias_api_client.Operation()] # list[Operation] | An array of JSON patch documents.
org_id = 56 # int | organization ID of the applicant (defaults to current organization ID) (optional)

try:
    # Update an applicant using JSON patch documents.
    api_instance.update_applicant(username, request, org_id=org_id)
except ApiException as e:
    print("Exception when calling ApplicantsApi->update_applicant: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| The username of the applicant to update. | 
 **request** | [**list[Operation]**](Operation.md)| An array of JSON patch documents. | 
 **org_id** | **int**| organization ID of the applicant (defaults to current organization ID) | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

