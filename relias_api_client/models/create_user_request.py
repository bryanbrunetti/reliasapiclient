# coding: utf-8

"""
    Relias API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: v1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from relias_api_client.configuration import Configuration


class CreateUserRequest(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'org_id': 'int',
        'first_name': 'str',
        'last_name': 'str',
        'user_name': 'str',
        'email': 'str',
        'password': 'str',
        'user_roles': 'list[str]',
        'job_titles': 'list[str]',
        'departments': 'list[str]',
        'location': 'str',
        'hierarchy_id': 'int',
        'require_password_change': 'bool',
        'learner_id': 'str',
        'guid': 'str'
    }

    attribute_map = {
        'org_id': 'orgId',
        'first_name': 'firstName',
        'last_name': 'lastName',
        'user_name': 'userName',
        'email': 'email',
        'password': 'password',
        'user_roles': 'userRoles',
        'job_titles': 'jobTitles',
        'departments': 'departments',
        'location': 'location',
        'hierarchy_id': 'hierarchyId',
        'require_password_change': 'requirePasswordChange',
        'learner_id': 'learnerId',
        'guid': 'guid'
    }

    def __init__(self, org_id=None, first_name=None, last_name=None, user_name=None, email=None, password=None, user_roles=None, job_titles=None, departments=None, location=None, hierarchy_id=None, require_password_change=None, learner_id=None, guid=None, _configuration=None):  # noqa: E501
        """CreateUserRequest - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._org_id = None
        self._first_name = None
        self._last_name = None
        self._user_name = None
        self._email = None
        self._password = None
        self._user_roles = None
        self._job_titles = None
        self._departments = None
        self._location = None
        self._hierarchy_id = None
        self._require_password_change = None
        self._learner_id = None
        self._guid = None
        self.discriminator = None

        if org_id is not None:
            self.org_id = org_id
        if first_name is not None:
            self.first_name = first_name
        if last_name is not None:
            self.last_name = last_name
        if user_name is not None:
            self.user_name = user_name
        if email is not None:
            self.email = email
        if password is not None:
            self.password = password
        if user_roles is not None:
            self.user_roles = user_roles
        if job_titles is not None:
            self.job_titles = job_titles
        if departments is not None:
            self.departments = departments
        if location is not None:
            self.location = location
        if hierarchy_id is not None:
            self.hierarchy_id = hierarchy_id
        if require_password_change is not None:
            self.require_password_change = require_password_change
        if learner_id is not None:
            self.learner_id = learner_id
        if guid is not None:
            self.guid = guid

    @property
    def org_id(self):
        """Gets the org_id of this CreateUserRequest.  # noqa: E501


        :return: The org_id of this CreateUserRequest.  # noqa: E501
        :rtype: int
        """
        return self._org_id

    @org_id.setter
    def org_id(self, org_id):
        """Sets the org_id of this CreateUserRequest.


        :param org_id: The org_id of this CreateUserRequest.  # noqa: E501
        :type: int
        """

        self._org_id = org_id

    @property
    def first_name(self):
        """Gets the first_name of this CreateUserRequest.  # noqa: E501


        :return: The first_name of this CreateUserRequest.  # noqa: E501
        :rtype: str
        """
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        """Sets the first_name of this CreateUserRequest.


        :param first_name: The first_name of this CreateUserRequest.  # noqa: E501
        :type: str
        """

        self._first_name = first_name

    @property
    def last_name(self):
        """Gets the last_name of this CreateUserRequest.  # noqa: E501


        :return: The last_name of this CreateUserRequest.  # noqa: E501
        :rtype: str
        """
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        """Sets the last_name of this CreateUserRequest.


        :param last_name: The last_name of this CreateUserRequest.  # noqa: E501
        :type: str
        """

        self._last_name = last_name

    @property
    def user_name(self):
        """Gets the user_name of this CreateUserRequest.  # noqa: E501


        :return: The user_name of this CreateUserRequest.  # noqa: E501
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        """Sets the user_name of this CreateUserRequest.


        :param user_name: The user_name of this CreateUserRequest.  # noqa: E501
        :type: str
        """

        self._user_name = user_name

    @property
    def email(self):
        """Gets the email of this CreateUserRequest.  # noqa: E501


        :return: The email of this CreateUserRequest.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this CreateUserRequest.


        :param email: The email of this CreateUserRequest.  # noqa: E501
        :type: str
        """

        self._email = email

    @property
    def password(self):
        """Gets the password of this CreateUserRequest.  # noqa: E501


        :return: The password of this CreateUserRequest.  # noqa: E501
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """Sets the password of this CreateUserRequest.


        :param password: The password of this CreateUserRequest.  # noqa: E501
        :type: str
        """

        self._password = password

    @property
    def user_roles(self):
        """Gets the user_roles of this CreateUserRequest.  # noqa: E501


        :return: The user_roles of this CreateUserRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._user_roles

    @user_roles.setter
    def user_roles(self, user_roles):
        """Sets the user_roles of this CreateUserRequest.


        :param user_roles: The user_roles of this CreateUserRequest.  # noqa: E501
        :type: list[str]
        """

        self._user_roles = user_roles

    @property
    def job_titles(self):
        """Gets the job_titles of this CreateUserRequest.  # noqa: E501


        :return: The job_titles of this CreateUserRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._job_titles

    @job_titles.setter
    def job_titles(self, job_titles):
        """Sets the job_titles of this CreateUserRequest.


        :param job_titles: The job_titles of this CreateUserRequest.  # noqa: E501
        :type: list[str]
        """

        self._job_titles = job_titles

    @property
    def departments(self):
        """Gets the departments of this CreateUserRequest.  # noqa: E501


        :return: The departments of this CreateUserRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._departments

    @departments.setter
    def departments(self, departments):
        """Sets the departments of this CreateUserRequest.


        :param departments: The departments of this CreateUserRequest.  # noqa: E501
        :type: list[str]
        """

        self._departments = departments

    @property
    def location(self):
        """Gets the location of this CreateUserRequest.  # noqa: E501


        :return: The location of this CreateUserRequest.  # noqa: E501
        :rtype: str
        """
        return self._location

    @location.setter
    def location(self, location):
        """Sets the location of this CreateUserRequest.


        :param location: The location of this CreateUserRequest.  # noqa: E501
        :type: str
        """

        self._location = location

    @property
    def hierarchy_id(self):
        """Gets the hierarchy_id of this CreateUserRequest.  # noqa: E501


        :return: The hierarchy_id of this CreateUserRequest.  # noqa: E501
        :rtype: int
        """
        return self._hierarchy_id

    @hierarchy_id.setter
    def hierarchy_id(self, hierarchy_id):
        """Sets the hierarchy_id of this CreateUserRequest.


        :param hierarchy_id: The hierarchy_id of this CreateUserRequest.  # noqa: E501
        :type: int
        """

        self._hierarchy_id = hierarchy_id

    @property
    def require_password_change(self):
        """Gets the require_password_change of this CreateUserRequest.  # noqa: E501


        :return: The require_password_change of this CreateUserRequest.  # noqa: E501
        :rtype: bool
        """
        return self._require_password_change

    @require_password_change.setter
    def require_password_change(self, require_password_change):
        """Sets the require_password_change of this CreateUserRequest.


        :param require_password_change: The require_password_change of this CreateUserRequest.  # noqa: E501
        :type: bool
        """

        self._require_password_change = require_password_change

    @property
    def learner_id(self):
        """Gets the learner_id of this CreateUserRequest.  # noqa: E501


        :return: The learner_id of this CreateUserRequest.  # noqa: E501
        :rtype: str
        """
        return self._learner_id

    @learner_id.setter
    def learner_id(self, learner_id):
        """Sets the learner_id of this CreateUserRequest.


        :param learner_id: The learner_id of this CreateUserRequest.  # noqa: E501
        :type: str
        """

        self._learner_id = learner_id

    @property
    def guid(self):
        """Gets the guid of this CreateUserRequest.  # noqa: E501


        :return: The guid of this CreateUserRequest.  # noqa: E501
        :rtype: str
        """
        return self._guid

    @guid.setter
    def guid(self, guid):
        """Sets the guid of this CreateUserRequest.


        :param guid: The guid of this CreateUserRequest.  # noqa: E501
        :type: str
        """

        self._guid = guid

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(CreateUserRequest, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, CreateUserRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CreateUserRequest):
            return True

        return self.to_dict() != other.to_dict()
