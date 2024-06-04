# coding: utf-8

"""
    volc_observe

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class DataForListContactsOutput(object):
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
        'email': 'str',
        'id': 'str',
        'name': 'str',
        'phone': 'str'
    }

    attribute_map = {
        'email': 'Email',
        'id': 'Id',
        'name': 'Name',
        'phone': 'Phone'
    }

    def __init__(self, email=None, id=None, name=None, phone=None, _configuration=None):  # noqa: E501
        """DataForListContactsOutput - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._email = None
        self._id = None
        self._name = None
        self._phone = None
        self.discriminator = None

        if email is not None:
            self.email = email
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if phone is not None:
            self.phone = phone

    @property
    def email(self):
        """Gets the email of this DataForListContactsOutput.  # noqa: E501


        :return: The email of this DataForListContactsOutput.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this DataForListContactsOutput.


        :param email: The email of this DataForListContactsOutput.  # noqa: E501
        :type: str
        """

        self._email = email

    @property
    def id(self):
        """Gets the id of this DataForListContactsOutput.  # noqa: E501


        :return: The id of this DataForListContactsOutput.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this DataForListContactsOutput.


        :param id: The id of this DataForListContactsOutput.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this DataForListContactsOutput.  # noqa: E501


        :return: The name of this DataForListContactsOutput.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this DataForListContactsOutput.


        :param name: The name of this DataForListContactsOutput.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def phone(self):
        """Gets the phone of this DataForListContactsOutput.  # noqa: E501


        :return: The phone of this DataForListContactsOutput.  # noqa: E501
        :rtype: str
        """
        return self._phone

    @phone.setter
    def phone(self, phone):
        """Sets the phone of this DataForListContactsOutput.


        :param phone: The phone of this DataForListContactsOutput.  # noqa: E501
        :type: str
        """

        self._phone = phone

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
        if issubclass(DataForListContactsOutput, dict):
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
        if not isinstance(other, DataForListContactsOutput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DataForListContactsOutput):
            return True

        return self.to_dict() != other.to_dict()
