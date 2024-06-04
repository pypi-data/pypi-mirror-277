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


class DescribeOriginStatusCodeRankingRequest(object):
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
        'domain': 'str',
        'end_time': 'int',
        'interval': 'str',
        'item': 'str',
        'metric': 'str',
        'project': 'str',
        'start_time': 'int'
    }

    attribute_map = {
        'domain': 'Domain',
        'end_time': 'EndTime',
        'interval': 'Interval',
        'item': 'Item',
        'metric': 'Metric',
        'project': 'Project',
        'start_time': 'StartTime'
    }

    def __init__(self, domain=None, end_time=None, interval=None, item=None, metric=None, project=None, start_time=None, _configuration=None):  # noqa: E501
        """DescribeOriginStatusCodeRankingRequest - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._domain = None
        self._end_time = None
        self._interval = None
        self._item = None
        self._metric = None
        self._project = None
        self._start_time = None
        self.discriminator = None

        if domain is not None:
            self.domain = domain
        self.end_time = end_time
        if interval is not None:
            self.interval = interval
        self.item = item
        self.metric = metric
        if project is not None:
            self.project = project
        self.start_time = start_time

    @property
    def domain(self):
        """Gets the domain of this DescribeOriginStatusCodeRankingRequest.  # noqa: E501


        :return: The domain of this DescribeOriginStatusCodeRankingRequest.  # noqa: E501
        :rtype: str
        """
        return self._domain

    @domain.setter
    def domain(self, domain):
        """Sets the domain of this DescribeOriginStatusCodeRankingRequest.


        :param domain: The domain of this DescribeOriginStatusCodeRankingRequest.  # noqa: E501
        :type: str
        """

        self._domain = domain

    @property
    def end_time(self):
        """Gets the end_time of this DescribeOriginStatusCodeRankingRequest.  # noqa: E501


        :return: The end_time of this DescribeOriginStatusCodeRankingRequest.  # noqa: E501
        :rtype: int
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this DescribeOriginStatusCodeRankingRequest.


        :param end_time: The end_time of this DescribeOriginStatusCodeRankingRequest.  # noqa: E501
        :type: int
        """
        if self._configuration.client_side_validation and end_time is None:
            raise ValueError("Invalid value for `end_time`, must not be `None`")  # noqa: E501

        self._end_time = end_time

    @property
    def interval(self):
        """Gets the interval of this DescribeOriginStatusCodeRankingRequest.  # noqa: E501


        :return: The interval of this DescribeOriginStatusCodeRankingRequest.  # noqa: E501
        :rtype: str
        """
        return self._interval

    @interval.setter
    def interval(self, interval):
        """Sets the interval of this DescribeOriginStatusCodeRankingRequest.


        :param interval: The interval of this DescribeOriginStatusCodeRankingRequest.  # noqa: E501
        :type: str
        """

        self._interval = interval

    @property
    def item(self):
        """Gets the item of this DescribeOriginStatusCodeRankingRequest.  # noqa: E501


        :return: The item of this DescribeOriginStatusCodeRankingRequest.  # noqa: E501
        :rtype: str
        """
        return self._item

    @item.setter
    def item(self, item):
        """Sets the item of this DescribeOriginStatusCodeRankingRequest.


        :param item: The item of this DescribeOriginStatusCodeRankingRequest.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and item is None:
            raise ValueError("Invalid value for `item`, must not be `None`")  # noqa: E501

        self._item = item

    @property
    def metric(self):
        """Gets the metric of this DescribeOriginStatusCodeRankingRequest.  # noqa: E501


        :return: The metric of this DescribeOriginStatusCodeRankingRequest.  # noqa: E501
        :rtype: str
        """
        return self._metric

    @metric.setter
    def metric(self, metric):
        """Sets the metric of this DescribeOriginStatusCodeRankingRequest.


        :param metric: The metric of this DescribeOriginStatusCodeRankingRequest.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and metric is None:
            raise ValueError("Invalid value for `metric`, must not be `None`")  # noqa: E501

        self._metric = metric

    @property
    def project(self):
        """Gets the project of this DescribeOriginStatusCodeRankingRequest.  # noqa: E501


        :return: The project of this DescribeOriginStatusCodeRankingRequest.  # noqa: E501
        :rtype: str
        """
        return self._project

    @project.setter
    def project(self, project):
        """Sets the project of this DescribeOriginStatusCodeRankingRequest.


        :param project: The project of this DescribeOriginStatusCodeRankingRequest.  # noqa: E501
        :type: str
        """

        self._project = project

    @property
    def start_time(self):
        """Gets the start_time of this DescribeOriginStatusCodeRankingRequest.  # noqa: E501


        :return: The start_time of this DescribeOriginStatusCodeRankingRequest.  # noqa: E501
        :rtype: int
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this DescribeOriginStatusCodeRankingRequest.


        :param start_time: The start_time of this DescribeOriginStatusCodeRankingRequest.  # noqa: E501
        :type: int
        """
        if self._configuration.client_side_validation and start_time is None:
            raise ValueError("Invalid value for `start_time`, must not be `None`")  # noqa: E501

        self._start_time = start_time

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
        if issubclass(DescribeOriginStatusCodeRankingRequest, dict):
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
        if not isinstance(other, DescribeOriginStatusCodeRankingRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DescribeOriginStatusCodeRankingRequest):
            return True

        return self.to_dict() != other.to_dict()
