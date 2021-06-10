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


class CreateApplicantRequest(object):
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
        'first_name': 'str',
        'last_name': 'str',
        'org_id': 'int',
        'email': 'str',
        'job_titles': 'list[str]',
        'tracking_id': 'str',
        'guid': 'str'
    }

    attribute_map = {
        'first_name': 'firstName',
        'last_name': 'lastName',
        'org_id': 'orgId',
        'email': 'email',
        'job_titles': 'jobTitles',
        'tracking_id': 'trackingId',
        'guid': 'guid'
    }

    def __init__(self, first_name=None, last_name=None, org_id=None, email=None, job_titles=None, tracking_id=None, guid=None, _configuration=None):  # noqa: E501
        """CreateApplicantRequest - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._first_name = None
        self._last_name = None
        self._org_id = None
        self._email = None
        self._job_titles = None
        self._tracking_id = None
        self._guid = None
        self.discriminator = None

        if first_name is not None:
            self.first_name = first_name
        if last_name is not None:
            self.last_name = last_name
        if org_id is not None:
            self.org_id = org_id
        if email is not None:
            self.email = email
        if job_titles is not None:
            self.job_titles = job_titles
        if tracking_id is not None:
            self.tracking_id = tracking_id
        if guid is not None:
            self.guid = guid

    @property
    def first_name(self):
        """Gets the first_name of this CreateApplicantRequest.  # noqa: E501


        :return: The first_name of this CreateApplicantRequest.  # noqa: E501
        :rtype: str
        """
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        """Sets the first_name of this CreateApplicantRequest.


        :param first_name: The first_name of this CreateApplicantRequest.  # noqa: E501
        :type: str
        """

        self._first_name = first_name

    @property
    def last_name(self):
        """Gets the last_name of this CreateApplicantRequest.  # noqa: E501


        :return: The last_name of this CreateApplicantRequest.  # noqa: E501
        :rtype: str
        """
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        """Sets the last_name of this CreateApplicantRequest.


        :param last_name: The last_name of this CreateApplicantRequest.  # noqa: E501
        :type: str
        """

        self._last_name = last_name

    @property
    def org_id(self):
        """Gets the org_id of this CreateApplicantRequest.  # noqa: E501


        :return: The org_id of this CreateApplicantRequest.  # noqa: E501
        :rtype: int
        """
        return self._org_id

    @org_id.setter
    def org_id(self, org_id):
        """Sets the org_id of this CreateApplicantRequest.


        :param org_id: The org_id of this CreateApplicantRequest.  # noqa: E501
        :type: int
        """

        self._org_id = org_id

    @property
    def email(self):
        """Gets the email of this CreateApplicantRequest.  # noqa: E501


        :return: The email of this CreateApplicantRequest.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this CreateApplicantRequest.


        :param email: The email of this CreateApplicantRequest.  # noqa: E501
        :type: str
        """

        self._email = email

    @property
    def job_titles(self):
        """Gets the job_titles of this CreateApplicantRequest.  # noqa: E501


        :return: The job_titles of this CreateApplicantRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._job_titles

    @job_titles.setter
    def job_titles(self, job_titles):
        """Sets the job_titles of this CreateApplicantRequest.


        :param job_titles: The job_titles of this CreateApplicantRequest.  # noqa: E501
        :type: list[str]
        """

        self._job_titles = job_titles

    @property
    def tracking_id(self):
        """Gets the tracking_id of this CreateApplicantRequest.  # noqa: E501


        :return: The tracking_id of this CreateApplicantRequest.  # noqa: E501
        :rtype: str
        """
        return self._tracking_id

    @tracking_id.setter
    def tracking_id(self, tracking_id):
        """Sets the tracking_id of this CreateApplicantRequest.


        :param tracking_id: The tracking_id of this CreateApplicantRequest.  # noqa: E501
        :type: str
        """

        self._tracking_id = tracking_id

    @property
    def guid(self):
        """Gets the guid of this CreateApplicantRequest.  # noqa: E501


        :return: The guid of this CreateApplicantRequest.  # noqa: E501
        :rtype: str
        """
        return self._guid

    @guid.setter
    def guid(self, guid):
        """Sets the guid of this CreateApplicantRequest.


        :param guid: The guid of this CreateApplicantRequest.  # noqa: E501
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
        if issubclass(CreateApplicantRequest, dict):
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
        if not isinstance(other, CreateApplicantRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CreateApplicantRequest):
            return True

        return self.to_dict() != other.to_dict()