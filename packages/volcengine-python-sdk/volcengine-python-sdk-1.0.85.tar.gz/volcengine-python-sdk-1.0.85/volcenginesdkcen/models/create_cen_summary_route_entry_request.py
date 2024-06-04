# coding: utf-8

"""
    cen

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class CreateCenSummaryRouteEntryRequest(object):
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
        'description': 'str',
        'destination_cidr_block': 'str'
    }

    attribute_map = {
        'cen_id': 'CenId',
        'description': 'Description',
        'destination_cidr_block': 'DestinationCidrBlock'
    }

    def __init__(self, cen_id=None, description=None, destination_cidr_block=None, _configuration=None):  # noqa: E501
        """CreateCenSummaryRouteEntryRequest - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._cen_id = None
        self._description = None
        self._destination_cidr_block = None
        self.discriminator = None

        self.cen_id = cen_id
        if description is not None:
            self.description = description
        self.destination_cidr_block = destination_cidr_block

    @property
    def cen_id(self):
        """Gets the cen_id of this CreateCenSummaryRouteEntryRequest.  # noqa: E501


        :return: The cen_id of this CreateCenSummaryRouteEntryRequest.  # noqa: E501
        :rtype: str
        """
        return self._cen_id

    @cen_id.setter
    def cen_id(self, cen_id):
        """Sets the cen_id of this CreateCenSummaryRouteEntryRequest.


        :param cen_id: The cen_id of this CreateCenSummaryRouteEntryRequest.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and cen_id is None:
            raise ValueError("Invalid value for `cen_id`, must not be `None`")  # noqa: E501

        self._cen_id = cen_id

    @property
    def description(self):
        """Gets the description of this CreateCenSummaryRouteEntryRequest.  # noqa: E501


        :return: The description of this CreateCenSummaryRouteEntryRequest.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this CreateCenSummaryRouteEntryRequest.


        :param description: The description of this CreateCenSummaryRouteEntryRequest.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def destination_cidr_block(self):
        """Gets the destination_cidr_block of this CreateCenSummaryRouteEntryRequest.  # noqa: E501


        :return: The destination_cidr_block of this CreateCenSummaryRouteEntryRequest.  # noqa: E501
        :rtype: str
        """
        return self._destination_cidr_block

    @destination_cidr_block.setter
    def destination_cidr_block(self, destination_cidr_block):
        """Sets the destination_cidr_block of this CreateCenSummaryRouteEntryRequest.


        :param destination_cidr_block: The destination_cidr_block of this CreateCenSummaryRouteEntryRequest.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and destination_cidr_block is None:
            raise ValueError("Invalid value for `destination_cidr_block`, must not be `None`")  # noqa: E501

        self._destination_cidr_block = destination_cidr_block

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
        if issubclass(CreateCenSummaryRouteEntryRequest, dict):
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
        if not isinstance(other, CreateCenSummaryRouteEntryRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CreateCenSummaryRouteEntryRequest):
            return True

        return self.to_dict() != other.to_dict()
