# coding: utf-8

"""
    spark

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class DescribeProjectResponse(object):
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
        'authority_type': 'str',
        'create_date': 'str',
        'description': 'str',
        'owner_id': 'str',
        'owner_name': 'str',
        'project_id': 'str',
        'project_name': 'str',
        'region_id': 'str'
    }

    attribute_map = {
        'authority_type': 'AuthorityType',
        'create_date': 'CreateDate',
        'description': 'Description',
        'owner_id': 'OwnerId',
        'owner_name': 'OwnerName',
        'project_id': 'ProjectId',
        'project_name': 'ProjectName',
        'region_id': 'RegionId'
    }

    def __init__(self, authority_type=None, create_date=None, description=None, owner_id=None, owner_name=None, project_id=None, project_name=None, region_id=None, _configuration=None):  # noqa: E501
        """DescribeProjectResponse - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._authority_type = None
        self._create_date = None
        self._description = None
        self._owner_id = None
        self._owner_name = None
        self._project_id = None
        self._project_name = None
        self._region_id = None
        self.discriminator = None

        if authority_type is not None:
            self.authority_type = authority_type
        if create_date is not None:
            self.create_date = create_date
        if description is not None:
            self.description = description
        if owner_id is not None:
            self.owner_id = owner_id
        if owner_name is not None:
            self.owner_name = owner_name
        if project_id is not None:
            self.project_id = project_id
        if project_name is not None:
            self.project_name = project_name
        if region_id is not None:
            self.region_id = region_id

    @property
    def authority_type(self):
        """Gets the authority_type of this DescribeProjectResponse.  # noqa: E501


        :return: The authority_type of this DescribeProjectResponse.  # noqa: E501
        :rtype: str
        """
        return self._authority_type

    @authority_type.setter
    def authority_type(self, authority_type):
        """Sets the authority_type of this DescribeProjectResponse.


        :param authority_type: The authority_type of this DescribeProjectResponse.  # noqa: E501
        :type: str
        """

        self._authority_type = authority_type

    @property
    def create_date(self):
        """Gets the create_date of this DescribeProjectResponse.  # noqa: E501


        :return: The create_date of this DescribeProjectResponse.  # noqa: E501
        :rtype: str
        """
        return self._create_date

    @create_date.setter
    def create_date(self, create_date):
        """Sets the create_date of this DescribeProjectResponse.


        :param create_date: The create_date of this DescribeProjectResponse.  # noqa: E501
        :type: str
        """

        self._create_date = create_date

    @property
    def description(self):
        """Gets the description of this DescribeProjectResponse.  # noqa: E501


        :return: The description of this DescribeProjectResponse.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this DescribeProjectResponse.


        :param description: The description of this DescribeProjectResponse.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def owner_id(self):
        """Gets the owner_id of this DescribeProjectResponse.  # noqa: E501


        :return: The owner_id of this DescribeProjectResponse.  # noqa: E501
        :rtype: str
        """
        return self._owner_id

    @owner_id.setter
    def owner_id(self, owner_id):
        """Sets the owner_id of this DescribeProjectResponse.


        :param owner_id: The owner_id of this DescribeProjectResponse.  # noqa: E501
        :type: str
        """

        self._owner_id = owner_id

    @property
    def owner_name(self):
        """Gets the owner_name of this DescribeProjectResponse.  # noqa: E501


        :return: The owner_name of this DescribeProjectResponse.  # noqa: E501
        :rtype: str
        """
        return self._owner_name

    @owner_name.setter
    def owner_name(self, owner_name):
        """Sets the owner_name of this DescribeProjectResponse.


        :param owner_name: The owner_name of this DescribeProjectResponse.  # noqa: E501
        :type: str
        """

        self._owner_name = owner_name

    @property
    def project_id(self):
        """Gets the project_id of this DescribeProjectResponse.  # noqa: E501


        :return: The project_id of this DescribeProjectResponse.  # noqa: E501
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this DescribeProjectResponse.


        :param project_id: The project_id of this DescribeProjectResponse.  # noqa: E501
        :type: str
        """

        self._project_id = project_id

    @property
    def project_name(self):
        """Gets the project_name of this DescribeProjectResponse.  # noqa: E501


        :return: The project_name of this DescribeProjectResponse.  # noqa: E501
        :rtype: str
        """
        return self._project_name

    @project_name.setter
    def project_name(self, project_name):
        """Sets the project_name of this DescribeProjectResponse.


        :param project_name: The project_name of this DescribeProjectResponse.  # noqa: E501
        :type: str
        """

        self._project_name = project_name

    @property
    def region_id(self):
        """Gets the region_id of this DescribeProjectResponse.  # noqa: E501


        :return: The region_id of this DescribeProjectResponse.  # noqa: E501
        :rtype: str
        """
        return self._region_id

    @region_id.setter
    def region_id(self, region_id):
        """Sets the region_id of this DescribeProjectResponse.


        :param region_id: The region_id of this DescribeProjectResponse.  # noqa: E501
        :type: str
        """

        self._region_id = region_id

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
        if issubclass(DescribeProjectResponse, dict):
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
        if not isinstance(other, DescribeProjectResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DescribeProjectResponse):
            return True

        return self.to_dict() != other.to_dict()
