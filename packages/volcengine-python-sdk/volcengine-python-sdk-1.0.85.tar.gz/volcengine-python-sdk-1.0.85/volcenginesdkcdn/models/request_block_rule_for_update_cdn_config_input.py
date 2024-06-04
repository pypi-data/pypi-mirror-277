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


class RequestBlockRuleForUpdateCdnConfigInput(object):
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
        'block_rule': 'list[BlockRuleForUpdateCdnConfigInput]',
        'switch': 'bool'
    }

    attribute_map = {
        'block_rule': 'BlockRule',
        'switch': 'Switch'
    }

    def __init__(self, block_rule=None, switch=None, _configuration=None):  # noqa: E501
        """RequestBlockRuleForUpdateCdnConfigInput - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._block_rule = None
        self._switch = None
        self.discriminator = None

        if block_rule is not None:
            self.block_rule = block_rule
        if switch is not None:
            self.switch = switch

    @property
    def block_rule(self):
        """Gets the block_rule of this RequestBlockRuleForUpdateCdnConfigInput.  # noqa: E501


        :return: The block_rule of this RequestBlockRuleForUpdateCdnConfigInput.  # noqa: E501
        :rtype: list[BlockRuleForUpdateCdnConfigInput]
        """
        return self._block_rule

    @block_rule.setter
    def block_rule(self, block_rule):
        """Sets the block_rule of this RequestBlockRuleForUpdateCdnConfigInput.


        :param block_rule: The block_rule of this RequestBlockRuleForUpdateCdnConfigInput.  # noqa: E501
        :type: list[BlockRuleForUpdateCdnConfigInput]
        """

        self._block_rule = block_rule

    @property
    def switch(self):
        """Gets the switch of this RequestBlockRuleForUpdateCdnConfigInput.  # noqa: E501


        :return: The switch of this RequestBlockRuleForUpdateCdnConfigInput.  # noqa: E501
        :rtype: bool
        """
        return self._switch

    @switch.setter
    def switch(self, switch):
        """Sets the switch of this RequestBlockRuleForUpdateCdnConfigInput.


        :param switch: The switch of this RequestBlockRuleForUpdateCdnConfigInput.  # noqa: E501
        :type: bool
        """

        self._switch = switch

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
        if issubclass(RequestBlockRuleForUpdateCdnConfigInput, dict):
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
        if not isinstance(other, RequestBlockRuleForUpdateCdnConfigInput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, RequestBlockRuleForUpdateCdnConfigInput):
            return True

        return self.to_dict() != other.to_dict()
