# coding: utf-8

"""
    waf

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class ListCustomBotConfigResponse(object):
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
        'count': 'int',
        'data': 'list[DataForListCustomBotConfigOutput]',
        'page': 'int',
        'page_number': 'int',
        'page_size': 'int',
        'total_count': 'int'
    }

    attribute_map = {
        'count': 'Count',
        'data': 'Data',
        'page': 'Page',
        'page_number': 'PageNumber',
        'page_size': 'PageSize',
        'total_count': 'TotalCount'
    }

    def __init__(self, count=None, data=None, page=None, page_number=None, page_size=None, total_count=None, _configuration=None):  # noqa: E501
        """ListCustomBotConfigResponse - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._count = None
        self._data = None
        self._page = None
        self._page_number = None
        self._page_size = None
        self._total_count = None
        self.discriminator = None

        if count is not None:
            self.count = count
        if data is not None:
            self.data = data
        if page is not None:
            self.page = page
        if page_number is not None:
            self.page_number = page_number
        if page_size is not None:
            self.page_size = page_size
        if total_count is not None:
            self.total_count = total_count

    @property
    def count(self):
        """Gets the count of this ListCustomBotConfigResponse.  # noqa: E501


        :return: The count of this ListCustomBotConfigResponse.  # noqa: E501
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this ListCustomBotConfigResponse.


        :param count: The count of this ListCustomBotConfigResponse.  # noqa: E501
        :type: int
        """

        self._count = count

    @property
    def data(self):
        """Gets the data of this ListCustomBotConfigResponse.  # noqa: E501


        :return: The data of this ListCustomBotConfigResponse.  # noqa: E501
        :rtype: list[DataForListCustomBotConfigOutput]
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this ListCustomBotConfigResponse.


        :param data: The data of this ListCustomBotConfigResponse.  # noqa: E501
        :type: list[DataForListCustomBotConfigOutput]
        """

        self._data = data

    @property
    def page(self):
        """Gets the page of this ListCustomBotConfigResponse.  # noqa: E501


        :return: The page of this ListCustomBotConfigResponse.  # noqa: E501
        :rtype: int
        """
        return self._page

    @page.setter
    def page(self, page):
        """Sets the page of this ListCustomBotConfigResponse.


        :param page: The page of this ListCustomBotConfigResponse.  # noqa: E501
        :type: int
        """

        self._page = page

    @property
    def page_number(self):
        """Gets the page_number of this ListCustomBotConfigResponse.  # noqa: E501


        :return: The page_number of this ListCustomBotConfigResponse.  # noqa: E501
        :rtype: int
        """
        return self._page_number

    @page_number.setter
    def page_number(self, page_number):
        """Sets the page_number of this ListCustomBotConfigResponse.


        :param page_number: The page_number of this ListCustomBotConfigResponse.  # noqa: E501
        :type: int
        """

        self._page_number = page_number

    @property
    def page_size(self):
        """Gets the page_size of this ListCustomBotConfigResponse.  # noqa: E501


        :return: The page_size of this ListCustomBotConfigResponse.  # noqa: E501
        :rtype: int
        """
        return self._page_size

    @page_size.setter
    def page_size(self, page_size):
        """Sets the page_size of this ListCustomBotConfigResponse.


        :param page_size: The page_size of this ListCustomBotConfigResponse.  # noqa: E501
        :type: int
        """

        self._page_size = page_size

    @property
    def total_count(self):
        """Gets the total_count of this ListCustomBotConfigResponse.  # noqa: E501


        :return: The total_count of this ListCustomBotConfigResponse.  # noqa: E501
        :rtype: int
        """
        return self._total_count

    @total_count.setter
    def total_count(self, total_count):
        """Sets the total_count of this ListCustomBotConfigResponse.


        :param total_count: The total_count of this ListCustomBotConfigResponse.  # noqa: E501
        :type: int
        """

        self._total_count = total_count

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
        if issubclass(ListCustomBotConfigResponse, dict):
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
        if not isinstance(other, ListCustomBotConfigResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ListCustomBotConfigResponse):
            return True

        return self.to_dict() != other.to_dict()
