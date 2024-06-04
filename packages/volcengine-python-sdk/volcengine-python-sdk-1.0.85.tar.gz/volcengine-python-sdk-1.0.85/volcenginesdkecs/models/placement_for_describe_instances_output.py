# coding: utf-8

"""
    ecs

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class PlacementForDescribeInstancesOutput(object):
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
        'affinity': 'str',
        'dedicated_host_cluster_id': 'str',
        'dedicated_host_id': 'str',
        'tenancy': 'str'
    }

    attribute_map = {
        'affinity': 'Affinity',
        'dedicated_host_cluster_id': 'DedicatedHostClusterId',
        'dedicated_host_id': 'DedicatedHostId',
        'tenancy': 'Tenancy'
    }

    def __init__(self, affinity=None, dedicated_host_cluster_id=None, dedicated_host_id=None, tenancy=None, _configuration=None):  # noqa: E501
        """PlacementForDescribeInstancesOutput - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._affinity = None
        self._dedicated_host_cluster_id = None
        self._dedicated_host_id = None
        self._tenancy = None
        self.discriminator = None

        if affinity is not None:
            self.affinity = affinity
        if dedicated_host_cluster_id is not None:
            self.dedicated_host_cluster_id = dedicated_host_cluster_id
        if dedicated_host_id is not None:
            self.dedicated_host_id = dedicated_host_id
        if tenancy is not None:
            self.tenancy = tenancy

    @property
    def affinity(self):
        """Gets the affinity of this PlacementForDescribeInstancesOutput.  # noqa: E501


        :return: The affinity of this PlacementForDescribeInstancesOutput.  # noqa: E501
        :rtype: str
        """
        return self._affinity

    @affinity.setter
    def affinity(self, affinity):
        """Sets the affinity of this PlacementForDescribeInstancesOutput.


        :param affinity: The affinity of this PlacementForDescribeInstancesOutput.  # noqa: E501
        :type: str
        """

        self._affinity = affinity

    @property
    def dedicated_host_cluster_id(self):
        """Gets the dedicated_host_cluster_id of this PlacementForDescribeInstancesOutput.  # noqa: E501


        :return: The dedicated_host_cluster_id of this PlacementForDescribeInstancesOutput.  # noqa: E501
        :rtype: str
        """
        return self._dedicated_host_cluster_id

    @dedicated_host_cluster_id.setter
    def dedicated_host_cluster_id(self, dedicated_host_cluster_id):
        """Sets the dedicated_host_cluster_id of this PlacementForDescribeInstancesOutput.


        :param dedicated_host_cluster_id: The dedicated_host_cluster_id of this PlacementForDescribeInstancesOutput.  # noqa: E501
        :type: str
        """

        self._dedicated_host_cluster_id = dedicated_host_cluster_id

    @property
    def dedicated_host_id(self):
        """Gets the dedicated_host_id of this PlacementForDescribeInstancesOutput.  # noqa: E501


        :return: The dedicated_host_id of this PlacementForDescribeInstancesOutput.  # noqa: E501
        :rtype: str
        """
        return self._dedicated_host_id

    @dedicated_host_id.setter
    def dedicated_host_id(self, dedicated_host_id):
        """Sets the dedicated_host_id of this PlacementForDescribeInstancesOutput.


        :param dedicated_host_id: The dedicated_host_id of this PlacementForDescribeInstancesOutput.  # noqa: E501
        :type: str
        """

        self._dedicated_host_id = dedicated_host_id

    @property
    def tenancy(self):
        """Gets the tenancy of this PlacementForDescribeInstancesOutput.  # noqa: E501


        :return: The tenancy of this PlacementForDescribeInstancesOutput.  # noqa: E501
        :rtype: str
        """
        return self._tenancy

    @tenancy.setter
    def tenancy(self, tenancy):
        """Sets the tenancy of this PlacementForDescribeInstancesOutput.


        :param tenancy: The tenancy of this PlacementForDescribeInstancesOutput.  # noqa: E501
        :type: str
        """

        self._tenancy = tenancy

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
        if issubclass(PlacementForDescribeInstancesOutput, dict):
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
        if not isinstance(other, PlacementForDescribeInstancesOutput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PlacementForDescribeInstancesOutput):
            return True

        return self.to_dict() != other.to_dict()
