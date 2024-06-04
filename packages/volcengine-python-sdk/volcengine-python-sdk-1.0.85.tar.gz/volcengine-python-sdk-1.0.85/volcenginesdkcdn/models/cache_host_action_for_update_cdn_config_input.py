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


class CacheHostActionForUpdateCdnConfigInput(object):
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
        'cache_host': 'str'
    }

    attribute_map = {
        'cache_host': 'CacheHost'
    }

    def __init__(self, cache_host=None, _configuration=None):  # noqa: E501
        """CacheHostActionForUpdateCdnConfigInput - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._cache_host = None
        self.discriminator = None

        if cache_host is not None:
            self.cache_host = cache_host

    @property
    def cache_host(self):
        """Gets the cache_host of this CacheHostActionForUpdateCdnConfigInput.  # noqa: E501


        :return: The cache_host of this CacheHostActionForUpdateCdnConfigInput.  # noqa: E501
        :rtype: str
        """
        return self._cache_host

    @cache_host.setter
    def cache_host(self, cache_host):
        """Sets the cache_host of this CacheHostActionForUpdateCdnConfigInput.


        :param cache_host: The cache_host of this CacheHostActionForUpdateCdnConfigInput.  # noqa: E501
        :type: str
        """

        self._cache_host = cache_host

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
        if issubclass(CacheHostActionForUpdateCdnConfigInput, dict):
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
        if not isinstance(other, CacheHostActionForUpdateCdnConfigInput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CacheHostActionForUpdateCdnConfigInput):
            return True

        return self.to_dict() != other.to_dict()
