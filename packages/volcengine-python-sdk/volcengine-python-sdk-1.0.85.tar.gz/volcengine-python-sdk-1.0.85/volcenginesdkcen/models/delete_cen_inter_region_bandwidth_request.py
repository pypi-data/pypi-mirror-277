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


class DeleteCenInterRegionBandwidthRequest(object):
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
        'inter_region_bandwidth_id': 'str'
    }

    attribute_map = {
        'inter_region_bandwidth_id': 'InterRegionBandwidthId'
    }

    def __init__(self, inter_region_bandwidth_id=None, _configuration=None):  # noqa: E501
        """DeleteCenInterRegionBandwidthRequest - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._inter_region_bandwidth_id = None
        self.discriminator = None

        self.inter_region_bandwidth_id = inter_region_bandwidth_id

    @property
    def inter_region_bandwidth_id(self):
        """Gets the inter_region_bandwidth_id of this DeleteCenInterRegionBandwidthRequest.  # noqa: E501


        :return: The inter_region_bandwidth_id of this DeleteCenInterRegionBandwidthRequest.  # noqa: E501
        :rtype: str
        """
        return self._inter_region_bandwidth_id

    @inter_region_bandwidth_id.setter
    def inter_region_bandwidth_id(self, inter_region_bandwidth_id):
        """Sets the inter_region_bandwidth_id of this DeleteCenInterRegionBandwidthRequest.


        :param inter_region_bandwidth_id: The inter_region_bandwidth_id of this DeleteCenInterRegionBandwidthRequest.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and inter_region_bandwidth_id is None:
            raise ValueError("Invalid value for `inter_region_bandwidth_id`, must not be `None`")  # noqa: E501

        self._inter_region_bandwidth_id = inter_region_bandwidth_id

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
        if issubclass(DeleteCenInterRegionBandwidthRequest, dict):
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
        if not isinstance(other, DeleteCenInterRegionBandwidthRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DeleteCenInterRegionBandwidthRequest):
            return True

        return self.to_dict() != other.to_dict()
