# coding: utf-8

"""
    vke

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class ResourceTagForListTagsForResourcesOutput(object):
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
        'resource_id': 'str',
        'resource_type': 'str',
        'tag_key': 'str',
        'tag_value': 'str',
        'type': 'str'
    }

    attribute_map = {
        'resource_id': 'ResourceId',
        'resource_type': 'ResourceType',
        'tag_key': 'TagKey',
        'tag_value': 'TagValue',
        'type': 'Type'
    }

    def __init__(self, resource_id=None, resource_type=None, tag_key=None, tag_value=None, type=None, _configuration=None):  # noqa: E501
        """ResourceTagForListTagsForResourcesOutput - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._resource_id = None
        self._resource_type = None
        self._tag_key = None
        self._tag_value = None
        self._type = None
        self.discriminator = None

        if resource_id is not None:
            self.resource_id = resource_id
        if resource_type is not None:
            self.resource_type = resource_type
        if tag_key is not None:
            self.tag_key = tag_key
        if tag_value is not None:
            self.tag_value = tag_value
        if type is not None:
            self.type = type

    @property
    def resource_id(self):
        """Gets the resource_id of this ResourceTagForListTagsForResourcesOutput.  # noqa: E501


        :return: The resource_id of this ResourceTagForListTagsForResourcesOutput.  # noqa: E501
        :rtype: str
        """
        return self._resource_id

    @resource_id.setter
    def resource_id(self, resource_id):
        """Sets the resource_id of this ResourceTagForListTagsForResourcesOutput.


        :param resource_id: The resource_id of this ResourceTagForListTagsForResourcesOutput.  # noqa: E501
        :type: str
        """

        self._resource_id = resource_id

    @property
    def resource_type(self):
        """Gets the resource_type of this ResourceTagForListTagsForResourcesOutput.  # noqa: E501


        :return: The resource_type of this ResourceTagForListTagsForResourcesOutput.  # noqa: E501
        :rtype: str
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        """Sets the resource_type of this ResourceTagForListTagsForResourcesOutput.


        :param resource_type: The resource_type of this ResourceTagForListTagsForResourcesOutput.  # noqa: E501
        :type: str
        """

        self._resource_type = resource_type

    @property
    def tag_key(self):
        """Gets the tag_key of this ResourceTagForListTagsForResourcesOutput.  # noqa: E501


        :return: The tag_key of this ResourceTagForListTagsForResourcesOutput.  # noqa: E501
        :rtype: str
        """
        return self._tag_key

    @tag_key.setter
    def tag_key(self, tag_key):
        """Sets the tag_key of this ResourceTagForListTagsForResourcesOutput.


        :param tag_key: The tag_key of this ResourceTagForListTagsForResourcesOutput.  # noqa: E501
        :type: str
        """

        self._tag_key = tag_key

    @property
    def tag_value(self):
        """Gets the tag_value of this ResourceTagForListTagsForResourcesOutput.  # noqa: E501


        :return: The tag_value of this ResourceTagForListTagsForResourcesOutput.  # noqa: E501
        :rtype: str
        """
        return self._tag_value

    @tag_value.setter
    def tag_value(self, tag_value):
        """Sets the tag_value of this ResourceTagForListTagsForResourcesOutput.


        :param tag_value: The tag_value of this ResourceTagForListTagsForResourcesOutput.  # noqa: E501
        :type: str
        """

        self._tag_value = tag_value

    @property
    def type(self):
        """Gets the type of this ResourceTagForListTagsForResourcesOutput.  # noqa: E501


        :return: The type of this ResourceTagForListTagsForResourcesOutput.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ResourceTagForListTagsForResourcesOutput.


        :param type: The type of this ResourceTagForListTagsForResourcesOutput.  # noqa: E501
        :type: str
        """

        self._type = type

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
        if issubclass(ResourceTagForListTagsForResourcesOutput, dict):
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
        if not isinstance(other, ResourceTagForListTagsForResourcesOutput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ResourceTagForListTagsForResourcesOutput):
            return True

        return self.to_dict() != other.to_dict()
