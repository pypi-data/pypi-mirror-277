# coding: utf-8

"""
    iam

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class ListProjectIdentitiesRequest(object):
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
        'identity_type': 'str',
        'limit': 'int',
        'offset': 'int',
        'project_name': 'str',
        'query': 'str'
    }

    attribute_map = {
        'identity_type': 'IdentityType',
        'limit': 'Limit',
        'offset': 'Offset',
        'project_name': 'ProjectName',
        'query': 'Query'
    }

    def __init__(self, identity_type=None, limit=None, offset=None, project_name=None, query=None, _configuration=None):  # noqa: E501
        """ListProjectIdentitiesRequest - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._identity_type = None
        self._limit = None
        self._offset = None
        self._project_name = None
        self._query = None
        self.discriminator = None

        self.identity_type = identity_type
        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset
        self.project_name = project_name
        if query is not None:
            self.query = query

    @property
    def identity_type(self):
        """Gets the identity_type of this ListProjectIdentitiesRequest.  # noqa: E501


        :return: The identity_type of this ListProjectIdentitiesRequest.  # noqa: E501
        :rtype: str
        """
        return self._identity_type

    @identity_type.setter
    def identity_type(self, identity_type):
        """Sets the identity_type of this ListProjectIdentitiesRequest.


        :param identity_type: The identity_type of this ListProjectIdentitiesRequest.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and identity_type is None:
            raise ValueError("Invalid value for `identity_type`, must not be `None`")  # noqa: E501

        self._identity_type = identity_type

    @property
    def limit(self):
        """Gets the limit of this ListProjectIdentitiesRequest.  # noqa: E501


        :return: The limit of this ListProjectIdentitiesRequest.  # noqa: E501
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListProjectIdentitiesRequest.


        :param limit: The limit of this ListProjectIdentitiesRequest.  # noqa: E501
        :type: int
        """

        self._limit = limit

    @property
    def offset(self):
        """Gets the offset of this ListProjectIdentitiesRequest.  # noqa: E501


        :return: The offset of this ListProjectIdentitiesRequest.  # noqa: E501
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListProjectIdentitiesRequest.


        :param offset: The offset of this ListProjectIdentitiesRequest.  # noqa: E501
        :type: int
        """

        self._offset = offset

    @property
    def project_name(self):
        """Gets the project_name of this ListProjectIdentitiesRequest.  # noqa: E501


        :return: The project_name of this ListProjectIdentitiesRequest.  # noqa: E501
        :rtype: str
        """
        return self._project_name

    @project_name.setter
    def project_name(self, project_name):
        """Sets the project_name of this ListProjectIdentitiesRequest.


        :param project_name: The project_name of this ListProjectIdentitiesRequest.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and project_name is None:
            raise ValueError("Invalid value for `project_name`, must not be `None`")  # noqa: E501

        self._project_name = project_name

    @property
    def query(self):
        """Gets the query of this ListProjectIdentitiesRequest.  # noqa: E501


        :return: The query of this ListProjectIdentitiesRequest.  # noqa: E501
        :rtype: str
        """
        return self._query

    @query.setter
    def query(self, query):
        """Sets the query of this ListProjectIdentitiesRequest.


        :param query: The query of this ListProjectIdentitiesRequest.  # noqa: E501
        :type: str
        """

        self._query = query

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
        if issubclass(ListProjectIdentitiesRequest, dict):
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
        if not isinstance(other, ListProjectIdentitiesRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ListProjectIdentitiesRequest):
            return True

        return self.to_dict() != other.to_dict()
