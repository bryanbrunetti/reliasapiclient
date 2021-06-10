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


class FileStreamResult(object):
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
        'file_stream': 'Stream',
        'content_type': 'str',
        'file_download_name': 'str',
        'last_modified': 'datetime',
        'entity_tag': 'EntityTagHeaderValue',
        'enable_range_processing': 'bool'
    }

    attribute_map = {
        'file_stream': 'fileStream',
        'content_type': 'contentType',
        'file_download_name': 'fileDownloadName',
        'last_modified': 'lastModified',
        'entity_tag': 'entityTag',
        'enable_range_processing': 'enableRangeProcessing'
    }

    def __init__(self, file_stream=None, content_type=None, file_download_name=None, last_modified=None, entity_tag=None, enable_range_processing=None, _configuration=None):  # noqa: E501
        """FileStreamResult - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._file_stream = None
        self._content_type = None
        self._file_download_name = None
        self._last_modified = None
        self._entity_tag = None
        self._enable_range_processing = None
        self.discriminator = None

        if file_stream is not None:
            self.file_stream = file_stream
        if content_type is not None:
            self.content_type = content_type
        if file_download_name is not None:
            self.file_download_name = file_download_name
        if last_modified is not None:
            self.last_modified = last_modified
        if entity_tag is not None:
            self.entity_tag = entity_tag
        if enable_range_processing is not None:
            self.enable_range_processing = enable_range_processing

    @property
    def file_stream(self):
        """Gets the file_stream of this FileStreamResult.  # noqa: E501


        :return: The file_stream of this FileStreamResult.  # noqa: E501
        :rtype: Stream
        """
        return self._file_stream

    @file_stream.setter
    def file_stream(self, file_stream):
        """Sets the file_stream of this FileStreamResult.


        :param file_stream: The file_stream of this FileStreamResult.  # noqa: E501
        :type: Stream
        """

        self._file_stream = file_stream

    @property
    def content_type(self):
        """Gets the content_type of this FileStreamResult.  # noqa: E501


        :return: The content_type of this FileStreamResult.  # noqa: E501
        :rtype: str
        """
        return self._content_type

    @content_type.setter
    def content_type(self, content_type):
        """Sets the content_type of this FileStreamResult.


        :param content_type: The content_type of this FileStreamResult.  # noqa: E501
        :type: str
        """

        self._content_type = content_type

    @property
    def file_download_name(self):
        """Gets the file_download_name of this FileStreamResult.  # noqa: E501


        :return: The file_download_name of this FileStreamResult.  # noqa: E501
        :rtype: str
        """
        return self._file_download_name

    @file_download_name.setter
    def file_download_name(self, file_download_name):
        """Sets the file_download_name of this FileStreamResult.


        :param file_download_name: The file_download_name of this FileStreamResult.  # noqa: E501
        :type: str
        """

        self._file_download_name = file_download_name

    @property
    def last_modified(self):
        """Gets the last_modified of this FileStreamResult.  # noqa: E501


        :return: The last_modified of this FileStreamResult.  # noqa: E501
        :rtype: datetime
        """
        return self._last_modified

    @last_modified.setter
    def last_modified(self, last_modified):
        """Sets the last_modified of this FileStreamResult.


        :param last_modified: The last_modified of this FileStreamResult.  # noqa: E501
        :type: datetime
        """

        self._last_modified = last_modified

    @property
    def entity_tag(self):
        """Gets the entity_tag of this FileStreamResult.  # noqa: E501


        :return: The entity_tag of this FileStreamResult.  # noqa: E501
        :rtype: EntityTagHeaderValue
        """
        return self._entity_tag

    @entity_tag.setter
    def entity_tag(self, entity_tag):
        """Sets the entity_tag of this FileStreamResult.


        :param entity_tag: The entity_tag of this FileStreamResult.  # noqa: E501
        :type: EntityTagHeaderValue
        """

        self._entity_tag = entity_tag

    @property
    def enable_range_processing(self):
        """Gets the enable_range_processing of this FileStreamResult.  # noqa: E501


        :return: The enable_range_processing of this FileStreamResult.  # noqa: E501
        :rtype: bool
        """
        return self._enable_range_processing

    @enable_range_processing.setter
    def enable_range_processing(self, enable_range_processing):
        """Sets the enable_range_processing of this FileStreamResult.


        :param enable_range_processing: The enable_range_processing of this FileStreamResult.  # noqa: E501
        :type: bool
        """

        self._enable_range_processing = enable_range_processing

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
        if issubclass(FileStreamResult, dict):
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
        if not isinstance(other, FileStreamResult):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, FileStreamResult):
            return True

        return self.to_dict() != other.to_dict()
