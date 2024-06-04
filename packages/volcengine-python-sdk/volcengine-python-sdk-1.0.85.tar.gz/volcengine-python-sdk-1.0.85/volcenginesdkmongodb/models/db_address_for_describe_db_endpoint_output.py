# coding: utf-8

"""
    mongodb

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class DBAddressForDescribeDBEndpointOutput(object):
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
        'address_domain': 'str',
        'address_ip': 'str',
        'address_port': 'str',
        'address_type': 'str',
        'eip_id': 'str',
        'node_id': 'str'
    }

    attribute_map = {
        'address_domain': 'AddressDomain',
        'address_ip': 'AddressIP',
        'address_port': 'AddressPort',
        'address_type': 'AddressType',
        'eip_id': 'EipId',
        'node_id': 'NodeId'
    }

    def __init__(self, address_domain=None, address_ip=None, address_port=None, address_type=None, eip_id=None, node_id=None, _configuration=None):  # noqa: E501
        """DBAddressForDescribeDBEndpointOutput - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._address_domain = None
        self._address_ip = None
        self._address_port = None
        self._address_type = None
        self._eip_id = None
        self._node_id = None
        self.discriminator = None

        if address_domain is not None:
            self.address_domain = address_domain
        if address_ip is not None:
            self.address_ip = address_ip
        if address_port is not None:
            self.address_port = address_port
        if address_type is not None:
            self.address_type = address_type
        if eip_id is not None:
            self.eip_id = eip_id
        if node_id is not None:
            self.node_id = node_id

    @property
    def address_domain(self):
        """Gets the address_domain of this DBAddressForDescribeDBEndpointOutput.  # noqa: E501


        :return: The address_domain of this DBAddressForDescribeDBEndpointOutput.  # noqa: E501
        :rtype: str
        """
        return self._address_domain

    @address_domain.setter
    def address_domain(self, address_domain):
        """Sets the address_domain of this DBAddressForDescribeDBEndpointOutput.


        :param address_domain: The address_domain of this DBAddressForDescribeDBEndpointOutput.  # noqa: E501
        :type: str
        """

        self._address_domain = address_domain

    @property
    def address_ip(self):
        """Gets the address_ip of this DBAddressForDescribeDBEndpointOutput.  # noqa: E501


        :return: The address_ip of this DBAddressForDescribeDBEndpointOutput.  # noqa: E501
        :rtype: str
        """
        return self._address_ip

    @address_ip.setter
    def address_ip(self, address_ip):
        """Sets the address_ip of this DBAddressForDescribeDBEndpointOutput.


        :param address_ip: The address_ip of this DBAddressForDescribeDBEndpointOutput.  # noqa: E501
        :type: str
        """

        self._address_ip = address_ip

    @property
    def address_port(self):
        """Gets the address_port of this DBAddressForDescribeDBEndpointOutput.  # noqa: E501


        :return: The address_port of this DBAddressForDescribeDBEndpointOutput.  # noqa: E501
        :rtype: str
        """
        return self._address_port

    @address_port.setter
    def address_port(self, address_port):
        """Sets the address_port of this DBAddressForDescribeDBEndpointOutput.


        :param address_port: The address_port of this DBAddressForDescribeDBEndpointOutput.  # noqa: E501
        :type: str
        """

        self._address_port = address_port

    @property
    def address_type(self):
        """Gets the address_type of this DBAddressForDescribeDBEndpointOutput.  # noqa: E501


        :return: The address_type of this DBAddressForDescribeDBEndpointOutput.  # noqa: E501
        :rtype: str
        """
        return self._address_type

    @address_type.setter
    def address_type(self, address_type):
        """Sets the address_type of this DBAddressForDescribeDBEndpointOutput.


        :param address_type: The address_type of this DBAddressForDescribeDBEndpointOutput.  # noqa: E501
        :type: str
        """

        self._address_type = address_type

    @property
    def eip_id(self):
        """Gets the eip_id of this DBAddressForDescribeDBEndpointOutput.  # noqa: E501


        :return: The eip_id of this DBAddressForDescribeDBEndpointOutput.  # noqa: E501
        :rtype: str
        """
        return self._eip_id

    @eip_id.setter
    def eip_id(self, eip_id):
        """Sets the eip_id of this DBAddressForDescribeDBEndpointOutput.


        :param eip_id: The eip_id of this DBAddressForDescribeDBEndpointOutput.  # noqa: E501
        :type: str
        """

        self._eip_id = eip_id

    @property
    def node_id(self):
        """Gets the node_id of this DBAddressForDescribeDBEndpointOutput.  # noqa: E501


        :return: The node_id of this DBAddressForDescribeDBEndpointOutput.  # noqa: E501
        :rtype: str
        """
        return self._node_id

    @node_id.setter
    def node_id(self, node_id):
        """Sets the node_id of this DBAddressForDescribeDBEndpointOutput.


        :param node_id: The node_id of this DBAddressForDescribeDBEndpointOutput.  # noqa: E501
        :type: str
        """

        self._node_id = node_id

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
        if issubclass(DBAddressForDescribeDBEndpointOutput, dict):
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
        if not isinstance(other, DBAddressForDescribeDBEndpointOutput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DBAddressForDescribeDBEndpointOutput):
            return True

        return self.to_dict() != other.to_dict()
