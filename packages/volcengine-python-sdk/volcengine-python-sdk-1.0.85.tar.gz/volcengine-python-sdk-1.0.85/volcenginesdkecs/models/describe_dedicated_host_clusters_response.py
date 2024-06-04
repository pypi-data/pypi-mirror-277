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


class DescribeDedicatedHostClustersResponse(object):
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
        'dedicated_host_clusters': 'list[DedicatedHostClusterForDescribeDedicatedHostClustersOutput]',
        'next_token': 'str'
    }

    attribute_map = {
        'dedicated_host_clusters': 'DedicatedHostClusters',
        'next_token': 'NextToken'
    }

    def __init__(self, dedicated_host_clusters=None, next_token=None, _configuration=None):  # noqa: E501
        """DescribeDedicatedHostClustersResponse - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._dedicated_host_clusters = None
        self._next_token = None
        self.discriminator = None

        if dedicated_host_clusters is not None:
            self.dedicated_host_clusters = dedicated_host_clusters
        if next_token is not None:
            self.next_token = next_token

    @property
    def dedicated_host_clusters(self):
        """Gets the dedicated_host_clusters of this DescribeDedicatedHostClustersResponse.  # noqa: E501


        :return: The dedicated_host_clusters of this DescribeDedicatedHostClustersResponse.  # noqa: E501
        :rtype: list[DedicatedHostClusterForDescribeDedicatedHostClustersOutput]
        """
        return self._dedicated_host_clusters

    @dedicated_host_clusters.setter
    def dedicated_host_clusters(self, dedicated_host_clusters):
        """Sets the dedicated_host_clusters of this DescribeDedicatedHostClustersResponse.


        :param dedicated_host_clusters: The dedicated_host_clusters of this DescribeDedicatedHostClustersResponse.  # noqa: E501
        :type: list[DedicatedHostClusterForDescribeDedicatedHostClustersOutput]
        """

        self._dedicated_host_clusters = dedicated_host_clusters

    @property
    def next_token(self):
        """Gets the next_token of this DescribeDedicatedHostClustersResponse.  # noqa: E501


        :return: The next_token of this DescribeDedicatedHostClustersResponse.  # noqa: E501
        :rtype: str
        """
        return self._next_token

    @next_token.setter
    def next_token(self, next_token):
        """Sets the next_token of this DescribeDedicatedHostClustersResponse.


        :param next_token: The next_token of this DescribeDedicatedHostClustersResponse.  # noqa: E501
        :type: str
        """

        self._next_token = next_token

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
        if issubclass(DescribeDedicatedHostClustersResponse, dict):
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
        if not isinstance(other, DescribeDedicatedHostClustersResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DescribeDedicatedHostClustersResponse):
            return True

        return self.to_dict() != other.to_dict()
