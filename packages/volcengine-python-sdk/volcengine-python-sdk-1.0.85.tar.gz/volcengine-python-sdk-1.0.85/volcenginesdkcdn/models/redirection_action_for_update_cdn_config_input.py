# coding: utf-8

"""
    cdn

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class RedirectionActionForUpdateCdnConfigInput(object):
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
        'redirect_code': 'str',
        'source_path': 'str',
        'target_host': 'str',
        'target_path': 'str',
        'target_protocol': 'str',
        'target_query_components': 'TargetQueryComponentsForUpdateCdnConfigInput'
    }

    attribute_map = {
        'redirect_code': 'RedirectCode',
        'source_path': 'SourcePath',
        'target_host': 'TargetHost',
        'target_path': 'TargetPath',
        'target_protocol': 'TargetProtocol',
        'target_query_components': 'TargetQueryComponents'
    }

    def __init__(self, redirect_code=None, source_path=None, target_host=None, target_path=None, target_protocol=None, target_query_components=None, _configuration=None):  # noqa: E501
        """RedirectionActionForUpdateCdnConfigInput - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._redirect_code = None
        self._source_path = None
        self._target_host = None
        self._target_path = None
        self._target_protocol = None
        self._target_query_components = None
        self.discriminator = None

        if redirect_code is not None:
            self.redirect_code = redirect_code
        if source_path is not None:
            self.source_path = source_path
        if target_host is not None:
            self.target_host = target_host
        if target_path is not None:
            self.target_path = target_path
        if target_protocol is not None:
            self.target_protocol = target_protocol
        if target_query_components is not None:
            self.target_query_components = target_query_components

    @property
    def redirect_code(self):
        """Gets the redirect_code of this RedirectionActionForUpdateCdnConfigInput.  # noqa: E501


        :return: The redirect_code of this RedirectionActionForUpdateCdnConfigInput.  # noqa: E501
        :rtype: str
        """
        return self._redirect_code

    @redirect_code.setter
    def redirect_code(self, redirect_code):
        """Sets the redirect_code of this RedirectionActionForUpdateCdnConfigInput.


        :param redirect_code: The redirect_code of this RedirectionActionForUpdateCdnConfigInput.  # noqa: E501
        :type: str
        """

        self._redirect_code = redirect_code

    @property
    def source_path(self):
        """Gets the source_path of this RedirectionActionForUpdateCdnConfigInput.  # noqa: E501


        :return: The source_path of this RedirectionActionForUpdateCdnConfigInput.  # noqa: E501
        :rtype: str
        """
        return self._source_path

    @source_path.setter
    def source_path(self, source_path):
        """Sets the source_path of this RedirectionActionForUpdateCdnConfigInput.


        :param source_path: The source_path of this RedirectionActionForUpdateCdnConfigInput.  # noqa: E501
        :type: str
        """

        self._source_path = source_path

    @property
    def target_host(self):
        """Gets the target_host of this RedirectionActionForUpdateCdnConfigInput.  # noqa: E501


        :return: The target_host of this RedirectionActionForUpdateCdnConfigInput.  # noqa: E501
        :rtype: str
        """
        return self._target_host

    @target_host.setter
    def target_host(self, target_host):
        """Sets the target_host of this RedirectionActionForUpdateCdnConfigInput.


        :param target_host: The target_host of this RedirectionActionForUpdateCdnConfigInput.  # noqa: E501
        :type: str
        """

        self._target_host = target_host

    @property
    def target_path(self):
        """Gets the target_path of this RedirectionActionForUpdateCdnConfigInput.  # noqa: E501


        :return: The target_path of this RedirectionActionForUpdateCdnConfigInput.  # noqa: E501
        :rtype: str
        """
        return self._target_path

    @target_path.setter
    def target_path(self, target_path):
        """Sets the target_path of this RedirectionActionForUpdateCdnConfigInput.


        :param target_path: The target_path of this RedirectionActionForUpdateCdnConfigInput.  # noqa: E501
        :type: str
        """

        self._target_path = target_path

    @property
    def target_protocol(self):
        """Gets the target_protocol of this RedirectionActionForUpdateCdnConfigInput.  # noqa: E501


        :return: The target_protocol of this RedirectionActionForUpdateCdnConfigInput.  # noqa: E501
        :rtype: str
        """
        return self._target_protocol

    @target_protocol.setter
    def target_protocol(self, target_protocol):
        """Sets the target_protocol of this RedirectionActionForUpdateCdnConfigInput.


        :param target_protocol: The target_protocol of this RedirectionActionForUpdateCdnConfigInput.  # noqa: E501
        :type: str
        """

        self._target_protocol = target_protocol

    @property
    def target_query_components(self):
        """Gets the target_query_components of this RedirectionActionForUpdateCdnConfigInput.  # noqa: E501


        :return: The target_query_components of this RedirectionActionForUpdateCdnConfigInput.  # noqa: E501
        :rtype: TargetQueryComponentsForUpdateCdnConfigInput
        """
        return self._target_query_components

    @target_query_components.setter
    def target_query_components(self, target_query_components):
        """Sets the target_query_components of this RedirectionActionForUpdateCdnConfigInput.


        :param target_query_components: The target_query_components of this RedirectionActionForUpdateCdnConfigInput.  # noqa: E501
        :type: TargetQueryComponentsForUpdateCdnConfigInput
        """

        self._target_query_components = target_query_components

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
        if issubclass(RedirectionActionForUpdateCdnConfigInput, dict):
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
        if not isinstance(other, RedirectionActionForUpdateCdnConfigInput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, RedirectionActionForUpdateCdnConfigInput):
            return True

        return self.to_dict() != other.to_dict()
