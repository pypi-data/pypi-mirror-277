# coding: utf-8

"""
    directconnect

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class DescribeDirectConnectGatewaysRequest(object):
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
        'cen_id': 'str',
        'direct_connect_gateway_ids': 'list[str]',
        'direct_connect_gateway_name': 'str',
        'page_number': 'int',
        'page_size': 'int',
        'tag_filters': 'list[TagFilterForDescribeDirectConnectGatewaysInput]'
    }

    attribute_map = {
        'cen_id': 'CenId',
        'direct_connect_gateway_ids': 'DirectConnectGatewayIds',
        'direct_connect_gateway_name': 'DirectConnectGatewayName',
        'page_number': 'PageNumber',
        'page_size': 'PageSize',
        'tag_filters': 'TagFilters'
    }

    def __init__(self, cen_id=None, direct_connect_gateway_ids=None, direct_connect_gateway_name=None, page_number=None, page_size=None, tag_filters=None, _configuration=None):  # noqa: E501
        """DescribeDirectConnectGatewaysRequest - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._cen_id = None
        self._direct_connect_gateway_ids = None
        self._direct_connect_gateway_name = None
        self._page_number = None
        self._page_size = None
        self._tag_filters = None
        self.discriminator = None

        if cen_id is not None:
            self.cen_id = cen_id
        if direct_connect_gateway_ids is not None:
            self.direct_connect_gateway_ids = direct_connect_gateway_ids
        if direct_connect_gateway_name is not None:
            self.direct_connect_gateway_name = direct_connect_gateway_name
        if page_number is not None:
            self.page_number = page_number
        if page_size is not None:
            self.page_size = page_size
        if tag_filters is not None:
            self.tag_filters = tag_filters

    @property
    def cen_id(self):
        """Gets the cen_id of this DescribeDirectConnectGatewaysRequest.  # noqa: E501


        :return: The cen_id of this DescribeDirectConnectGatewaysRequest.  # noqa: E501
        :rtype: str
        """
        return self._cen_id

    @cen_id.setter
    def cen_id(self, cen_id):
        """Sets the cen_id of this DescribeDirectConnectGatewaysRequest.


        :param cen_id: The cen_id of this DescribeDirectConnectGatewaysRequest.  # noqa: E501
        :type: str
        """

        self._cen_id = cen_id

    @property
    def direct_connect_gateway_ids(self):
        """Gets the direct_connect_gateway_ids of this DescribeDirectConnectGatewaysRequest.  # noqa: E501


        :return: The direct_connect_gateway_ids of this DescribeDirectConnectGatewaysRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._direct_connect_gateway_ids

    @direct_connect_gateway_ids.setter
    def direct_connect_gateway_ids(self, direct_connect_gateway_ids):
        """Sets the direct_connect_gateway_ids of this DescribeDirectConnectGatewaysRequest.


        :param direct_connect_gateway_ids: The direct_connect_gateway_ids of this DescribeDirectConnectGatewaysRequest.  # noqa: E501
        :type: list[str]
        """

        self._direct_connect_gateway_ids = direct_connect_gateway_ids

    @property
    def direct_connect_gateway_name(self):
        """Gets the direct_connect_gateway_name of this DescribeDirectConnectGatewaysRequest.  # noqa: E501


        :return: The direct_connect_gateway_name of this DescribeDirectConnectGatewaysRequest.  # noqa: E501
        :rtype: str
        """
        return self._direct_connect_gateway_name

    @direct_connect_gateway_name.setter
    def direct_connect_gateway_name(self, direct_connect_gateway_name):
        """Sets the direct_connect_gateway_name of this DescribeDirectConnectGatewaysRequest.


        :param direct_connect_gateway_name: The direct_connect_gateway_name of this DescribeDirectConnectGatewaysRequest.  # noqa: E501
        :type: str
        """

        self._direct_connect_gateway_name = direct_connect_gateway_name

    @property
    def page_number(self):
        """Gets the page_number of this DescribeDirectConnectGatewaysRequest.  # noqa: E501


        :return: The page_number of this DescribeDirectConnectGatewaysRequest.  # noqa: E501
        :rtype: int
        """
        return self._page_number

    @page_number.setter
    def page_number(self, page_number):
        """Sets the page_number of this DescribeDirectConnectGatewaysRequest.


        :param page_number: The page_number of this DescribeDirectConnectGatewaysRequest.  # noqa: E501
        :type: int
        """

        self._page_number = page_number

    @property
    def page_size(self):
        """Gets the page_size of this DescribeDirectConnectGatewaysRequest.  # noqa: E501


        :return: The page_size of this DescribeDirectConnectGatewaysRequest.  # noqa: E501
        :rtype: int
        """
        return self._page_size

    @page_size.setter
    def page_size(self, page_size):
        """Sets the page_size of this DescribeDirectConnectGatewaysRequest.


        :param page_size: The page_size of this DescribeDirectConnectGatewaysRequest.  # noqa: E501
        :type: int
        """

        self._page_size = page_size

    @property
    def tag_filters(self):
        """Gets the tag_filters of this DescribeDirectConnectGatewaysRequest.  # noqa: E501


        :return: The tag_filters of this DescribeDirectConnectGatewaysRequest.  # noqa: E501
        :rtype: list[TagFilterForDescribeDirectConnectGatewaysInput]
        """
        return self._tag_filters

    @tag_filters.setter
    def tag_filters(self, tag_filters):
        """Sets the tag_filters of this DescribeDirectConnectGatewaysRequest.


        :param tag_filters: The tag_filters of this DescribeDirectConnectGatewaysRequest.  # noqa: E501
        :type: list[TagFilterForDescribeDirectConnectGatewaysInput]
        """

        self._tag_filters = tag_filters

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
        if issubclass(DescribeDirectConnectGatewaysRequest, dict):
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
        if not isinstance(other, DescribeDirectConnectGatewaysRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DescribeDirectConnectGatewaysRequest):
            return True

        return self.to_dict() != other.to_dict()
