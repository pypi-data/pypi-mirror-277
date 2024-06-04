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


class IpFreqLimitActionForAddCdnDomainInput(object):
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
        'action': 'str',
        'freq_limit_rate': 'int',
        'status_code': 'str'
    }

    attribute_map = {
        'action': 'Action',
        'freq_limit_rate': 'FreqLimitRate',
        'status_code': 'StatusCode'
    }

    def __init__(self, action=None, freq_limit_rate=None, status_code=None, _configuration=None):  # noqa: E501
        """IpFreqLimitActionForAddCdnDomainInput - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._action = None
        self._freq_limit_rate = None
        self._status_code = None
        self.discriminator = None

        if action is not None:
            self.action = action
        if freq_limit_rate is not None:
            self.freq_limit_rate = freq_limit_rate
        if status_code is not None:
            self.status_code = status_code

    @property
    def action(self):
        """Gets the action of this IpFreqLimitActionForAddCdnDomainInput.  # noqa: E501


        :return: The action of this IpFreqLimitActionForAddCdnDomainInput.  # noqa: E501
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        """Sets the action of this IpFreqLimitActionForAddCdnDomainInput.


        :param action: The action of this IpFreqLimitActionForAddCdnDomainInput.  # noqa: E501
        :type: str
        """

        self._action = action

    @property
    def freq_limit_rate(self):
        """Gets the freq_limit_rate of this IpFreqLimitActionForAddCdnDomainInput.  # noqa: E501


        :return: The freq_limit_rate of this IpFreqLimitActionForAddCdnDomainInput.  # noqa: E501
        :rtype: int
        """
        return self._freq_limit_rate

    @freq_limit_rate.setter
    def freq_limit_rate(self, freq_limit_rate):
        """Sets the freq_limit_rate of this IpFreqLimitActionForAddCdnDomainInput.


        :param freq_limit_rate: The freq_limit_rate of this IpFreqLimitActionForAddCdnDomainInput.  # noqa: E501
        :type: int
        """

        self._freq_limit_rate = freq_limit_rate

    @property
    def status_code(self):
        """Gets the status_code of this IpFreqLimitActionForAddCdnDomainInput.  # noqa: E501


        :return: The status_code of this IpFreqLimitActionForAddCdnDomainInput.  # noqa: E501
        :rtype: str
        """
        return self._status_code

    @status_code.setter
    def status_code(self, status_code):
        """Sets the status_code of this IpFreqLimitActionForAddCdnDomainInput.


        :param status_code: The status_code of this IpFreqLimitActionForAddCdnDomainInput.  # noqa: E501
        :type: str
        """

        self._status_code = status_code

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
        if issubclass(IpFreqLimitActionForAddCdnDomainInput, dict):
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
        if not isinstance(other, IpFreqLimitActionForAddCdnDomainInput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, IpFreqLimitActionForAddCdnDomainInput):
            return True

        return self.to_dict() != other.to_dict()
