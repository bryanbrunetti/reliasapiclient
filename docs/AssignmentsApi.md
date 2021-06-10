# relias_api_client.AssignmentsApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_assignments_for_user**](AssignmentsApi.md#create_assignments_for_user) | **POST** /v1/users/{username}/assignments | Assigns multiple assessments to one user
[**get_user_assignments**](AssignmentsApi.md#get_user_assignments) | **GET** /v1/users/{username}/assignments | Retrieves a paginated list of assignments for the provided username
[**get_users_behavioral_assignment**](AssignmentsApi.md#get_users_behavioral_assignment) | **GET** /v1/users/{username}/behavioral-assignments/{assignmentId} | Retrieves behavioral assignment results for a provided username and assignment ID
[**get_users_behavioral_assignment_result_pdf**](AssignmentsApi.md#get_users_behavioral_assignment_result_pdf) | **GET** /v1/users/{username}/behavioral-assignments/{assignmentId}/results | Retrieves a behavioral assignment results pdf for a provided username and assignment ID
[**get_users_clinical_assignment**](AssignmentsApi.md#get_users_clinical_assignment) | **GET** /v1/users/{username}/clinical-assignments/{assignmentId} | Retrieves clinical assignment results for a provided username and assignment ID
[**get_users_clinical_assignment_result_pdf**](AssignmentsApi.md#get_users_clinical_assignment_result_pdf) | **GET** /v1/users/{username}/clinical-assignments/{assignmentId}/results | Retrieves a clinical assignment results pdf for a provided username and assignment ID
[**get_users_self_assignment**](AssignmentsApi.md#get_users_self_assignment) | **GET** /v1/users/{username}/self-assignments/{assignmentId} | Retrieves self assignment results for a provided username and assignment ID
[**get_users_self_assignment_result_pdf**](AssignmentsApi.md#get_users_self_assignment_result_pdf) | **GET** /v1/users/{username}/self-assignments/{assignmentId}/results | Retrieves a self assignment results pdf for a provided username and assignment ID
[**get_users_situational_assignment**](AssignmentsApi.md#get_users_situational_assignment) | **GET** /v1/users/{username}/situational-assignments/{assignmentId} | Retrieves a situational assignment results for a provided username and assignment ID
[**get_users_situational_assignment_result_pdf**](AssignmentsApi.md#get_users_situational_assignment_result_pdf) | **GET** /v1/users/{username}/situational-assignments/{assignmentId}/results | Retrieves a situational assignment results pdf for a provided username and assignment ID


# **create_assignments_for_user**
> list[CreateAssignmentResponse] create_assignments_for_user(username, assignment_request, org_id=org_id)

Assigns multiple assessments to one user

When providing username, be sure to URL encode the value if it contains any special characters. <br />  Notes:                Create Assignment Request:  <ul><li>AssessmentIds is a required list of Assessment IDs to create assignments. The Organization should have access to all of them.</li><li>Expiration is required for the assignments. The time will be set to 23:59 UTC of the date provided.</li><li>Availability is the date and time in UTC the assignments will be available to the user. This is optional and will default to the current date.</li><li>Locked, if true, indicates that the user cannot take the assignment until it is manually unlocked. This is optional; however, Availability should not be provided when Locked is true.</li></ul>                Create Assignment Response:  <ul><li>AssignmentId is the ID for the Assignment.</li><li>UserId is the ID of the User in the Assignment.</li><li>Expiration is the expiration date for the Assignment.</li><li>AssessmentId is the ID of the assigned Assessment.</li></ul>

### Example
```python
from __future__ import print_function
import time
import relias_api_client
from relias_api_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = relias_api_client.AssignmentsApi()
username = 'username_example' # str | the username of the user to assign the Assessment
assignment_request = relias_api_client.CreateAssignmentRequest() # CreateAssignmentRequest | The assignment information
org_id = 56 # int | Organization ID of the user (defaults to current organization ID) (optional)

try:
    # Assigns multiple assessments to one user
    api_response = api_instance.create_assignments_for_user(username, assignment_request, org_id=org_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssignmentsApi->create_assignments_for_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| the username of the user to assign the Assessment | 
 **assignment_request** | [**CreateAssignmentRequest**](CreateAssignmentRequest.md)| The assignment information | 
 **org_id** | **int**| Organization ID of the user (defaults to current organization ID) | [optional] 

### Return type

[**list[CreateAssignmentResponse]**](CreateAssignmentResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_assignments**
> PaginatedListOfAssignmentModel get_user_assignments(username, page_number=page_number, page_size=page_size, org_id=org_id)

Retrieves a paginated list of assignments for the provided username

When providing username, be sure to URL encode the value if it contains any special characters.

### Example
```python
from __future__ import print_function
import time
import relias_api_client
from relias_api_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = relias_api_client.AssignmentsApi()
username = 'username_example' # str | the username of the user whose assignments are wanted
page_number = 56 # int |  (optional)
page_size = 56 # int |  (optional)
org_id = 56 # int | organization ID of the user (defaults to current organization ID) (optional)

try:
    # Retrieves a paginated list of assignments for the provided username
    api_response = api_instance.get_user_assignments(username, page_number=page_number, page_size=page_size, org_id=org_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssignmentsApi->get_user_assignments: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| the username of the user whose assignments are wanted | 
 **page_number** | **int**|  | [optional] 
 **page_size** | **int**|  | [optional] 
 **org_id** | **int**| organization ID of the user (defaults to current organization ID) | [optional] 

### Return type

[**PaginatedListOfAssignmentModel**](PaginatedListOfAssignmentModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_users_behavioral_assignment**
> BehavioralResult get_users_behavioral_assignment(username, assignment_id, job_category=job_category, org_id=org_id)

Retrieves behavioral assignment results for a provided username and assignment ID

When providing username, be sure to URL encode the value if it contains any special characters.

### Example
```python
from __future__ import print_function
import time
import relias_api_client
from relias_api_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = relias_api_client.AssignmentsApi()
username = 'username_example' # str | the username of the user whose assignment is wanted
assignment_id = 56 # int | the ID of the assignment
job_category = 'job_category_example' # str | the title of the job category used to measure job fit. * Not applicable to the \"Attitude Only\" behavioral assessment.                Possible values are:  <ul><li>Allied Health</li><li>Clinical Educator</li><li>Executive</li><li>Manager / Supervisor</li><li>Non-Clinical Non-Patient-Facing</li><li>Non-Clinical Patient-Facing</li><li>Nursing Assistant</li><li>Registered Nurse</li><li>Registered Nurse - ER</li><li>Registered Nurse - ICU</li><li>Registered Nurse - Labor &amp; Delivery</li><li>Registered Nurse - Medical Surgical</li><li>Registered Nurse - NICU</li></ul> (optional)
org_id = 56 # int | organization ID of the user (defaults to current organization ID) (optional)

try:
    # Retrieves behavioral assignment results for a provided username and assignment ID
    api_response = api_instance.get_users_behavioral_assignment(username, assignment_id, job_category=job_category, org_id=org_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssignmentsApi->get_users_behavioral_assignment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| the username of the user whose assignment is wanted | 
 **assignment_id** | **int**| the ID of the assignment | 
 **job_category** | **str**| the title of the job category used to measure job fit. * Not applicable to the \&quot;Attitude Only\&quot; behavioral assessment.                Possible values are:  &lt;ul&gt;&lt;li&gt;Allied Health&lt;/li&gt;&lt;li&gt;Clinical Educator&lt;/li&gt;&lt;li&gt;Executive&lt;/li&gt;&lt;li&gt;Manager / Supervisor&lt;/li&gt;&lt;li&gt;Non-Clinical Non-Patient-Facing&lt;/li&gt;&lt;li&gt;Non-Clinical Patient-Facing&lt;/li&gt;&lt;li&gt;Nursing Assistant&lt;/li&gt;&lt;li&gt;Registered Nurse&lt;/li&gt;&lt;li&gt;Registered Nurse - ER&lt;/li&gt;&lt;li&gt;Registered Nurse - ICU&lt;/li&gt;&lt;li&gt;Registered Nurse - Labor &amp;amp; Delivery&lt;/li&gt;&lt;li&gt;Registered Nurse - Medical Surgical&lt;/li&gt;&lt;li&gt;Registered Nurse - NICU&lt;/li&gt;&lt;/ul&gt; | [optional] 
 **org_id** | **int**| organization ID of the user (defaults to current organization ID) | [optional] 

### Return type

[**BehavioralResult**](BehavioralResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_users_behavioral_assignment_result_pdf**
> FileStreamResult get_users_behavioral_assignment_result_pdf(username, assignment_id, job_category=job_category, org_id=org_id)

Retrieves a behavioral assignment results pdf for a provided username and assignment ID

When providing username, be sure to URL encode the value if it contains any special characters.

### Example
```python
from __future__ import print_function
import time
import relias_api_client
from relias_api_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = relias_api_client.AssignmentsApi()
username = 'username_example' # str | the username of the user whose assignment is wanted
assignment_id = 56 # int | the ID of the assignment
job_category = 'job_category_example' # str | the title of the job category used to measure job fit. * Not applicable to the \"Attitude Only\" behavioral assessment.                Possible values are:  <ul><li>Allied Health</li><li>Clinical Educator</li><li>Executive</li><li>Manager / Supervisor</li><li>Non-Clinical Non-Patient-Facing</li><li>Non-Clinical Patient-Facing</li><li>Nursing Assistant</li><li>Registered Nurse</li><li>Registered Nurse - ER</li><li>Registered Nurse - ICU</li><li>Registered Nurse - Labor &amp; Delivery</li><li>Registered Nurse - Medical Surgical</li><li>Registered Nurse - NICU</li></ul> (optional)
org_id = 56 # int | organization ID of the user (defaults to current organization ID) (optional)

try:
    # Retrieves a behavioral assignment results pdf for a provided username and assignment ID
    api_response = api_instance.get_users_behavioral_assignment_result_pdf(username, assignment_id, job_category=job_category, org_id=org_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssignmentsApi->get_users_behavioral_assignment_result_pdf: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| the username of the user whose assignment is wanted | 
 **assignment_id** | **int**| the ID of the assignment | 
 **job_category** | **str**| the title of the job category used to measure job fit. * Not applicable to the \&quot;Attitude Only\&quot; behavioral assessment.                Possible values are:  &lt;ul&gt;&lt;li&gt;Allied Health&lt;/li&gt;&lt;li&gt;Clinical Educator&lt;/li&gt;&lt;li&gt;Executive&lt;/li&gt;&lt;li&gt;Manager / Supervisor&lt;/li&gt;&lt;li&gt;Non-Clinical Non-Patient-Facing&lt;/li&gt;&lt;li&gt;Non-Clinical Patient-Facing&lt;/li&gt;&lt;li&gt;Nursing Assistant&lt;/li&gt;&lt;li&gt;Registered Nurse&lt;/li&gt;&lt;li&gt;Registered Nurse - ER&lt;/li&gt;&lt;li&gt;Registered Nurse - ICU&lt;/li&gt;&lt;li&gt;Registered Nurse - Labor &amp;amp; Delivery&lt;/li&gt;&lt;li&gt;Registered Nurse - Medical Surgical&lt;/li&gt;&lt;li&gt;Registered Nurse - NICU&lt;/li&gt;&lt;/ul&gt; | [optional] 
 **org_id** | **int**| organization ID of the user (defaults to current organization ID) | [optional] 

### Return type

[**FileStreamResult**](FileStreamResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/pdf, application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_users_clinical_assignment**
> ClinicalResult get_users_clinical_assignment(username, assignment_id, org_id=org_id)

Retrieves clinical assignment results for a provided username and assignment ID

When providing username, be sure to URL encode the value if it contains any special characters.

### Example
```python
from __future__ import print_function
import time
import relias_api_client
from relias_api_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = relias_api_client.AssignmentsApi()
username = 'username_example' # str | the username of the user whose assignment is wanted
assignment_id = 56 # int | the ID of the assignment
org_id = 56 # int | organization ID of the user (defaults to current organization ID) (optional)

try:
    # Retrieves clinical assignment results for a provided username and assignment ID
    api_response = api_instance.get_users_clinical_assignment(username, assignment_id, org_id=org_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssignmentsApi->get_users_clinical_assignment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| the username of the user whose assignment is wanted | 
 **assignment_id** | **int**| the ID of the assignment | 
 **org_id** | **int**| organization ID of the user (defaults to current organization ID) | [optional] 

### Return type

[**ClinicalResult**](ClinicalResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_users_clinical_assignment_result_pdf**
> FileStreamResult get_users_clinical_assignment_result_pdf(username, assignment_id, org_id=org_id)

Retrieves a clinical assignment results pdf for a provided username and assignment ID

When providing username, be sure to URL encode the value if it contains any special characters.  <br />   A results PDF is generated automatically when an assignment is completed. If this endpoint is called before the PDF has finished generating, a new one will be generated at that time. If using this endpoint in combination with an Assignment Completed webhook, note that calling this endpoint immediately after receiving that notification will likely require a new PDF to generate, resulting in a slower than usual response time.

### Example
```python
from __future__ import print_function
import time
import relias_api_client
from relias_api_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = relias_api_client.AssignmentsApi()
username = 'username_example' # str | the username of the user whose assignment is wanted
assignment_id = 56 # int | the ID of the assignment
org_id = 56 # int | organization ID of the user (defaults to current organization ID) (optional)

try:
    # Retrieves a clinical assignment results pdf for a provided username and assignment ID
    api_response = api_instance.get_users_clinical_assignment_result_pdf(username, assignment_id, org_id=org_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssignmentsApi->get_users_clinical_assignment_result_pdf: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| the username of the user whose assignment is wanted | 
 **assignment_id** | **int**| the ID of the assignment | 
 **org_id** | **int**| organization ID of the user (defaults to current organization ID) | [optional] 

### Return type

[**FileStreamResult**](FileStreamResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/pdf, application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_users_self_assignment**
> SelfResult get_users_self_assignment(username, assignment_id, org_id=org_id)

Retrieves self assignment results for a provided username and assignment ID

When providing username, be sure to URL encode the value if it contains any special characters.

### Example
```python
from __future__ import print_function
import time
import relias_api_client
from relias_api_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = relias_api_client.AssignmentsApi()
username = 'username_example' # str | the username of the user whose assignment is wanted
assignment_id = 56 # int | the ID of the assignment
org_id = 56 # int | organization ID of the user (defaults to current organization ID) (optional)

try:
    # Retrieves self assignment results for a provided username and assignment ID
    api_response = api_instance.get_users_self_assignment(username, assignment_id, org_id=org_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssignmentsApi->get_users_self_assignment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| the username of the user whose assignment is wanted | 
 **assignment_id** | **int**| the ID of the assignment | 
 **org_id** | **int**| organization ID of the user (defaults to current organization ID) | [optional] 

### Return type

[**SelfResult**](SelfResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_users_self_assignment_result_pdf**
> FileStreamResult get_users_self_assignment_result_pdf(username, assignment_id, org_id=org_id)

Retrieves a self assignment results pdf for a provided username and assignment ID

When providing username, be sure to URL encode the value if it contains any special characters.

### Example
```python
from __future__ import print_function
import time
import relias_api_client
from relias_api_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = relias_api_client.AssignmentsApi()
username = 'username_example' # str | the username of the user whose assignment is wanted
assignment_id = 56 # int | the ID of the assignment
org_id = 56 # int | organization ID of the user (defaults to current organization ID) (optional)

try:
    # Retrieves a self assignment results pdf for a provided username and assignment ID
    api_response = api_instance.get_users_self_assignment_result_pdf(username, assignment_id, org_id=org_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssignmentsApi->get_users_self_assignment_result_pdf: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| the username of the user whose assignment is wanted | 
 **assignment_id** | **int**| the ID of the assignment | 
 **org_id** | **int**| organization ID of the user (defaults to current organization ID) | [optional] 

### Return type

[**FileStreamResult**](FileStreamResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/pdf, application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_users_situational_assignment**
> SituationalResult get_users_situational_assignment(username, assignment_id, org_id=org_id)

Retrieves a situational assignment results for a provided username and assignment ID

When providing username, be sure to URL encode the value if it contains any special characters.

### Example
```python
from __future__ import print_function
import time
import relias_api_client
from relias_api_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = relias_api_client.AssignmentsApi()
username = 'username_example' # str | the username of the user whose assignment is wanted
assignment_id = 56 # int | the ID of the assignment
org_id = 56 # int | organization ID of the user (defaults to current organization ID) (optional)

try:
    # Retrieves a situational assignment results for a provided username and assignment ID
    api_response = api_instance.get_users_situational_assignment(username, assignment_id, org_id=org_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssignmentsApi->get_users_situational_assignment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| the username of the user whose assignment is wanted | 
 **assignment_id** | **int**| the ID of the assignment | 
 **org_id** | **int**| organization ID of the user (defaults to current organization ID) | [optional] 

### Return type

[**SituationalResult**](SituationalResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_users_situational_assignment_result_pdf**
> FileStreamResult get_users_situational_assignment_result_pdf(username, assignment_id, org_id=org_id)

Retrieves a situational assignment results pdf for a provided username and assignment ID

When providing username, be sure to URL encode the value if it contains any special characters.

### Example
```python
from __future__ import print_function
import time
import relias_api_client
from relias_api_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = relias_api_client.AssignmentsApi()
username = 'username_example' # str | the username of the user whose assignment is wanted
assignment_id = 56 # int | the ID of the assignment
org_id = 56 # int | organization ID of the user (defaults to current organization ID) (optional)

try:
    # Retrieves a situational assignment results pdf for a provided username and assignment ID
    api_response = api_instance.get_users_situational_assignment_result_pdf(username, assignment_id, org_id=org_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssignmentsApi->get_users_situational_assignment_result_pdf: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| the username of the user whose assignment is wanted | 
 **assignment_id** | **int**| the ID of the assignment | 
 **org_id** | **int**| organization ID of the user (defaults to current organization ID) | [optional] 

### Return type

[**FileStreamResult**](FileStreamResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/pdf, application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

