# coding: utf-8

"""
    vpn

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class DescribeVpnGatewayRoutesRequest(object):
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
        'destination_cidr_block': 'str',
        'next_hop_id': 'str',
        'page_number': 'int',
        'page_size': 'int',
        'vpn_gateway_id': 'str',
        'vpn_gateway_route_ids': 'list[str]'
    }

    attribute_map = {
        'destination_cidr_block': 'DestinationCidrBlock',
        'next_hop_id': 'NextHopId',
        'page_number': 'PageNumber',
        'page_size': 'PageSize',
        'vpn_gateway_id': 'VpnGatewayId',
        'vpn_gateway_route_ids': 'VpnGatewayRouteIds'
    }

    def __init__(self, destination_cidr_block=None, next_hop_id=None, page_number=None, page_size=None, vpn_gateway_id=None, vpn_gateway_route_ids=None, _configuration=None):  # noqa: E501
        """DescribeVpnGatewayRoutesRequest - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._destination_cidr_block = None
        self._next_hop_id = None
        self._page_number = None
        self._page_size = None
        self._vpn_gateway_id = None
        self._vpn_gateway_route_ids = None
        self.discriminator = None

        if destination_cidr_block is not None:
            self.destination_cidr_block = destination_cidr_block
        if next_hop_id is not None:
            self.next_hop_id = next_hop_id
        if page_number is not None:
            self.page_number = page_number
        if page_size is not None:
            self.page_size = page_size
        if vpn_gateway_id is not None:
            self.vpn_gateway_id = vpn_gateway_id
        if vpn_gateway_route_ids is not None:
            self.vpn_gateway_route_ids = vpn_gateway_route_ids

    @property
    def destination_cidr_block(self):
        """Gets the destination_cidr_block of this DescribeVpnGatewayRoutesRequest.  # noqa: E501


        :return: The destination_cidr_block of this DescribeVpnGatewayRoutesRequest.  # noqa: E501
        :rtype: str
        """
        return self._destination_cidr_block

    @destination_cidr_block.setter
    def destination_cidr_block(self, destination_cidr_block):
        """Sets the destination_cidr_block of this DescribeVpnGatewayRoutesRequest.


        :param destination_cidr_block: The destination_cidr_block of this DescribeVpnGatewayRoutesRequest.  # noqa: E501
        :type: str
        """

        self._destination_cidr_block = destination_cidr_block

    @property
    def next_hop_id(self):
        """Gets the next_hop_id of this DescribeVpnGatewayRoutesRequest.  # noqa: E501


        :return: The next_hop_id of this DescribeVpnGatewayRoutesRequest.  # noqa: E501
        :rtype: str
        """
        return self._next_hop_id

    @next_hop_id.setter
    def next_hop_id(self, next_hop_id):
        """Sets the next_hop_id of this DescribeVpnGatewayRoutesRequest.


        :param next_hop_id: The next_hop_id of this DescribeVpnGatewayRoutesRequest.  # noqa: E501
        :type: str
        """

        self._next_hop_id = next_hop_id

    @property
    def page_number(self):
        """Gets the page_number of this DescribeVpnGatewayRoutesRequest.  # noqa: E501


        :return: The page_number of this DescribeVpnGatewayRoutesRequest.  # noqa: E501
        :rtype: int
        """
        return self._page_number

    @page_number.setter
    def page_number(self, page_number):
        """Sets the page_number of this DescribeVpnGatewayRoutesRequest.


        :param page_number: The page_number of this DescribeVpnGatewayRoutesRequest.  # noqa: E501
        :type: int
        """

        self._page_number = page_number

    @property
    def page_size(self):
        """Gets the page_size of this DescribeVpnGatewayRoutesRequest.  # noqa: E501


        :return: The page_size of this DescribeVpnGatewayRoutesRequest.  # noqa: E501
        :rtype: int
        """
        return self._page_size

    @page_size.setter
    def page_size(self, page_size):
        """Sets the page_size of this DescribeVpnGatewayRoutesRequest.


        :param page_size: The page_size of this DescribeVpnGatewayRoutesRequest.  # noqa: E501
        :type: int
        """

        self._page_size = page_size

    @property
    def vpn_gateway_id(self):
        """Gets the vpn_gateway_id of this DescribeVpnGatewayRoutesRequest.  # noqa: E501


        :return: The vpn_gateway_id of this DescribeVpnGatewayRoutesRequest.  # noqa: E501
        :rtype: str
        """
        return self._vpn_gateway_id

    @vpn_gateway_id.setter
    def vpn_gateway_id(self, vpn_gateway_id):
        """Sets the vpn_gateway_id of this DescribeVpnGatewayRoutesRequest.


        :param vpn_gateway_id: The vpn_gateway_id of this DescribeVpnGatewayRoutesRequest.  # noqa: E501
        :type: str
        """

        self._vpn_gateway_id = vpn_gateway_id

    @property
    def vpn_gateway_route_ids(self):
        """Gets the vpn_gateway_route_ids of this DescribeVpnGatewayRoutesRequest.  # noqa: E501


        :return: The vpn_gateway_route_ids of this DescribeVpnGatewayRoutesRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._vpn_gateway_route_ids

    @vpn_gateway_route_ids.setter
    def vpn_gateway_route_ids(self, vpn_gateway_route_ids):
        """Sets the vpn_gateway_route_ids of this DescribeVpnGatewayRoutesRequest.


        :param vpn_gateway_route_ids: The vpn_gateway_route_ids of this DescribeVpnGatewayRoutesRequest.  # noqa: E501
        :type: list[str]
        """

        self._vpn_gateway_route_ids = vpn_gateway_route_ids

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
        if issubclass(DescribeVpnGatewayRoutesRequest, dict):
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
        if not isinstance(other, DescribeVpnGatewayRoutesRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DescribeVpnGatewayRoutesRequest):
            return True

        return self.to_dict() != other.to_dict()
