# coding: utf-8

"""
    alb

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class DescribeListenerHealthResponse(object):
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
        'listeners': 'list[ListenerForDescribeListenerHealthOutput]',
        'request_id': 'str',
        'total_count': 'int'
    }

    attribute_map = {
        'listeners': 'Listeners',
        'request_id': 'RequestId',
        'total_count': 'TotalCount'
    }

    def __init__(self, listeners=None, request_id=None, total_count=None, _configuration=None):  # noqa: E501
        """DescribeListenerHealthResponse - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._listeners = None
        self._request_id = None
        self._total_count = None
        self.discriminator = None

        if listeners is not None:
            self.listeners = listeners
        if request_id is not None:
            self.request_id = request_id
        if total_count is not None:
            self.total_count = total_count

    @property
    def listeners(self):
        """Gets the listeners of this DescribeListenerHealthResponse.  # noqa: E501


        :return: The listeners of this DescribeListenerHealthResponse.  # noqa: E501
        :rtype: list[ListenerForDescribeListenerHealthOutput]
        """
        return self._listeners

    @listeners.setter
    def listeners(self, listeners):
        """Sets the listeners of this DescribeListenerHealthResponse.


        :param listeners: The listeners of this DescribeListenerHealthResponse.  # noqa: E501
        :type: list[ListenerForDescribeListenerHealthOutput]
        """

        self._listeners = listeners

    @property
    def request_id(self):
        """Gets the request_id of this DescribeListenerHealthResponse.  # noqa: E501


        :return: The request_id of this DescribeListenerHealthResponse.  # noqa: E501
        :rtype: str
        """
        return self._request_id

    @request_id.setter
    def request_id(self, request_id):
        """Sets the request_id of this DescribeListenerHealthResponse.


        :param request_id: The request_id of this DescribeListenerHealthResponse.  # noqa: E501
        :type: str
        """

        self._request_id = request_id

    @property
    def total_count(self):
        """Gets the total_count of this DescribeListenerHealthResponse.  # noqa: E501


        :return: The total_count of this DescribeListenerHealthResponse.  # noqa: E501
        :rtype: int
        """
        return self._total_count

    @total_count.setter
    def total_count(self, total_count):
        """Sets the total_count of this DescribeListenerHealthResponse.


        :param total_count: The total_count of this DescribeListenerHealthResponse.  # noqa: E501
        :type: int
        """

        self._total_count = total_count

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
        if issubclass(DescribeListenerHealthResponse, dict):
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
        if not isinstance(other, DescribeListenerHealthResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DescribeListenerHealthResponse):
            return True

        return self.to_dict() != other.to_dict()
