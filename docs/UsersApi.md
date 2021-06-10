# relias_api_client.UsersApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_user**](UsersApi.md#create_user) | **POST** /v1/users | Creates a user with the supplied information
[**get_user**](UsersApi.md#get_user) | **GET** /v1/users/{username} | Retrieves a user based on the username provided
[**update_user**](UsersApi.md#update_user) | **PATCH** /v1/users/{username} | Update a user using JSON patch documents.


# **create_user**
> CreateUserResponse create_user(user_information)

Creates a user with the supplied information

Notes:  <ul><li>Org ID is required and should be the ID of your organization.</li><li>First Name is required and must not exceed 50 characters.</li><li>Last Name is required and must not exceed 50 characters.</li><li>Username is required, must be unique within your organization and not exceed 255 characters.</li><li>Email is required when supplying User Roles other than learner and must not exceed 150 characters.</li><li>Password is required and must be at minimum 4 characters long.</li><li>Job Titles, Departments, Location and Hierarchy ID are optional.</li><li>Learner ID, optional, must be unique within your organization and not exceed 50 characters.</li><li>GUID, optional, must be unique within your organization and not exceed 50 characters.</li><li>User Roles are optional but may be supplied to provide additional roles beyond learner.<br />          Options Include:          <ul><li>Administrator</li><li>Report Supervisor</li><li>Enrollment Supervisor</li><li>User Supervisor</li><li>Instructor</li><li>Skills Checklist Observer</li><li>Skills Checklist Data Entry</li></ul></li></ul>

### Example
```python
from __future__ import print_function
import time
import relias_api_client
from relias_api_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = relias_api_client.UsersApi()
user_information = relias_api_client.CreateUserRequest() # CreateUserRequest | the information of the user

try:
    # Creates a user with the supplied information
    api_response = api_instance.create_user(user_information)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->create_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_information** | [**CreateUserRequest**](CreateUserRequest.md)| the information of the user | 

### Return type

[**CreateUserResponse**](CreateUserResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user**
> GetUserModel get_user(username, org_id=org_id)

Retrieves a user based on the username provided

When providing username, be sure to URL encode the value if it contains any special characters.

### Example
```python
from __future__ import print_function
import time
import relias_api_client
from relias_api_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = relias_api_client.UsersApi()
username = 'username_example' # str | the username of the user
org_id = 56 # int | organization ID of the user (defaults to current organization ID) (optional)

try:
    # Retrieves a user based on the username provided
    api_response = api_instance.get_user(username, org_id=org_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->get_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| the username of the user | 
 **org_id** | **int**| organization ID of the user (defaults to current organization ID) | [optional] 

### Return type

[**GetUserModel**](GetUserModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_user**
> update_user(username, request, org_id=org_id)

Update a user using JSON patch documents.

When providing username, be sure to URL encode the value if it contains any special characters.  Provide a set of one or more JSON patch documents describing the changes to apply to the applicant.  See http://jsonpatch.com/ and below for examples.  <br />  Fields that can be updated include:  <ul><li>First name          <pre>{\"op\": \"replace\", \"path\": \"/FirstName\", \"value\": \"new name\"}</pre></li><br /><li>Last name          <pre>{\"op\": \"replace\", \"path\": \"/LastName\", \"value\": \"new name\"}</pre></li><br /><li>Username          <pre>{\"op\": \"replace\", \"path\": \"/UserName\", \"value\": \"new_username\"}</pre></li><br /><li>Email          <pre>{\"op\": \"replace\", \"path\": \"/Email\", \"value\": \"new@email.com\"}</pre></li><br /><li>Password          <pre>{\"op\": \"replace\", \"path\": \"/Password\", \"value\": \"new_password\"}</pre></li><br /><li>Job titles          <pre>{\"op\": \"replace\", \"path\": \"/JobTitles\", \"value\": [\"Job title 1\", \"Job title 2\"]}</pre></li><br /><li>Departments          <pre>{\"op\": \"replace\", \"path\": \"/Departments\", \"value\": [\"Department 1\", \"Department 2\"]}</pre></li><br /><li>Location          <pre>{\"op\": \"replace\", \"path\": \"/Location\", \"value\": \"new location\"}</pre></li><br /><li>Hierarchy ID          <pre>{\"op\": \"replace\", \"path\": \"/HierarchyId\", \"value\": 1}</pre></li><br /><li>Learner ID          <pre>{\"op\": \"replace\", \"path\": \"/LearnerId\", \"value\": \"new learner ID\"}</pre></li><br /><li>GUID          <pre>{\"op\": \"replace\", \"path\": \"/Guid\", \"value\": \"new GUID\"}</pre></li><br /><li>User roles          <pre>{\"op\": \"replace\", \"path\": \"/UserRoles\", \"value\": [\"Administrator\", \"Enrollment Supervisor\"]}</pre>          Options:          <ul><li>Administrator</li><li>Report Supervisor</li><li>Enrollment Supervisor</li><li>User Supervisor</li><li>Instructor</li><li>Skills Checklist Observer</li><li>Skills Checklist Data Entry</li></ul></li><br /><li>User status          <pre>{\"op\": \"replace\", \"path\": \"/UserStatus\", \"value\": \"Inactive\"}</pre>          Options:          <ul><li>Active</li><li>Inactive</li><li>OnLeave</li></ul></li><br /><li>Require password change          <pre>{\"op\": \"replace\", \"path\": \"/RequirePasswordChange\", \"value\": true}</pre>          Options:          <ul><li>True</li><li>False</li></ul></li></ul><p>  Note that the <b>path</b> parameter is case sensitive.  <br /><br />  Example: Changing a user's first name, last name, departments and user roles  </p><pre>  [      {\"op\": \"replace\", \"path\": \"/FirstName\", \"value\": \"new first name\"},      {\"op\": \"replace\", \"path\": \"/LastName\", \"value\": \"new last name\"},      {\"op\": \"replace\", \"path\": \"/Departments\", \"value\": [\"department1\", \"department2\"]},      {\"op\": \"replace\", \"path\": \"/UserRoles\", \"value\": [\"Instructor\", \"Skills Checklist Data Entry\"]}  ]  </pre>

### Example
```python
from __future__ import print_function
import time
import relias_api_client
from relias_api_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = relias_api_client.UsersApi()
username = 'username_example' # str | The username of the user to update.
request = [relias_api_client.Operation()] # list[Operation] | An array of JSON patch documents.
org_id = 56 # int | Organization ID of the user (defaults to current organization ID) (optional)

try:
    # Update a user using JSON patch documents.
    api_instance.update_user(username, request, org_id=org_id)
except ApiException as e:
    print("Exception when calling UsersApi->update_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| The username of the user to update. | 
 **request** | [**list[Operation]**](Operation.md)| An array of JSON patch documents. | 
 **org_id** | **int**| Organization ID of the user (defaults to current organization ID) | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

