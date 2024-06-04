# coding: utf-8

"""
    cr

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class FilterForListRegistriesInput(object):
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
        'names': 'list[str]',
        'statuses': 'list[StatusForListRegistriesInput]',
        'types': 'list[str]'
    }

    attribute_map = {
        'names': 'Names',
        'statuses': 'Statuses',
        'types': 'Types'
    }

    def __init__(self, names=None, statuses=None, types=None, _configuration=None):  # noqa: E501
        """FilterForListRegistriesInput - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._names = None
        self._statuses = None
        self._types = None
        self.discriminator = None

        if names is not None:
            self.names = names
        if statuses is not None:
            self.statuses = statuses
        if types is not None:
            self.types = types

    @property
    def names(self):
        """Gets the names of this FilterForListRegistriesInput.  # noqa: E501


        :return: The names of this FilterForListRegistriesInput.  # noqa: E501
        :rtype: list[str]
        """
        return self._names

    @names.setter
    def names(self, names):
        """Sets the names of this FilterForListRegistriesInput.


        :param names: The names of this FilterForListRegistriesInput.  # noqa: E501
        :type: list[str]
        """

        self._names = names

    @property
    def statuses(self):
        """Gets the statuses of this FilterForListRegistriesInput.  # noqa: E501


        :return: The statuses of this FilterForListRegistriesInput.  # noqa: E501
        :rtype: list[StatusForListRegistriesInput]
        """
        return self._statuses

    @statuses.setter
    def statuses(self, statuses):
        """Sets the statuses of this FilterForListRegistriesInput.


        :param statuses: The statuses of this FilterForListRegistriesInput.  # noqa: E501
        :type: list[StatusForListRegistriesInput]
        """

        self._statuses = statuses

    @property
    def types(self):
        """Gets the types of this FilterForListRegistriesInput.  # noqa: E501


        :return: The types of this FilterForListRegistriesInput.  # noqa: E501
        :rtype: list[str]
        """
        return self._types

    @types.setter
    def types(self, types):
        """Sets the types of this FilterForListRegistriesInput.


        :param types: The types of this FilterForListRegistriesInput.  # noqa: E501
        :type: list[str]
        """

        self._types = types

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
        if issubclass(FilterForListRegistriesInput, dict):
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
        if not isinstance(other, FilterForListRegistriesInput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, FilterForListRegistriesInput):
            return True

        return self.to_dict() != other.to_dict()
