# coding: utf-8

"""
    alb

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class DescribeAllCertificatesRequest(object):
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
        'certificate_ids': 'list[str]',
        'certificate_name': 'str',
        'certificate_type': 'str',
        'page_number': 'int',
        'page_size': 'int',
        'project_name': 'str'
    }

    attribute_map = {
        'certificate_ids': 'CertificateIds',
        'certificate_name': 'CertificateName',
        'certificate_type': 'CertificateType',
        'page_number': 'PageNumber',
        'page_size': 'PageSize',
        'project_name': 'ProjectName'
    }

    def __init__(self, certificate_ids=None, certificate_name=None, certificate_type=None, page_number=None, page_size=None, project_name=None, _configuration=None):  # noqa: E501
        """DescribeAllCertificatesRequest - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._certificate_ids = None
        self._certificate_name = None
        self._certificate_type = None
        self._page_number = None
        self._page_size = None
        self._project_name = None
        self.discriminator = None

        if certificate_ids is not None:
            self.certificate_ids = certificate_ids
        if certificate_name is not None:
            self.certificate_name = certificate_name
        if certificate_type is not None:
            self.certificate_type = certificate_type
        if page_number is not None:
            self.page_number = page_number
        if page_size is not None:
            self.page_size = page_size
        if project_name is not None:
            self.project_name = project_name

    @property
    def certificate_ids(self):
        """Gets the certificate_ids of this DescribeAllCertificatesRequest.  # noqa: E501


        :return: The certificate_ids of this DescribeAllCertificatesRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._certificate_ids

    @certificate_ids.setter
    def certificate_ids(self, certificate_ids):
        """Sets the certificate_ids of this DescribeAllCertificatesRequest.


        :param certificate_ids: The certificate_ids of this DescribeAllCertificatesRequest.  # noqa: E501
        :type: list[str]
        """

        self._certificate_ids = certificate_ids

    @property
    def certificate_name(self):
        """Gets the certificate_name of this DescribeAllCertificatesRequest.  # noqa: E501


        :return: The certificate_name of this DescribeAllCertificatesRequest.  # noqa: E501
        :rtype: str
        """
        return self._certificate_name

    @certificate_name.setter
    def certificate_name(self, certificate_name):
        """Sets the certificate_name of this DescribeAllCertificatesRequest.


        :param certificate_name: The certificate_name of this DescribeAllCertificatesRequest.  # noqa: E501
        :type: str
        """

        self._certificate_name = certificate_name

    @property
    def certificate_type(self):
        """Gets the certificate_type of this DescribeAllCertificatesRequest.  # noqa: E501


        :return: The certificate_type of this DescribeAllCertificatesRequest.  # noqa: E501
        :rtype: str
        """
        return self._certificate_type

    @certificate_type.setter
    def certificate_type(self, certificate_type):
        """Sets the certificate_type of this DescribeAllCertificatesRequest.


        :param certificate_type: The certificate_type of this DescribeAllCertificatesRequest.  # noqa: E501
        :type: str
        """

        self._certificate_type = certificate_type

    @property
    def page_number(self):
        """Gets the page_number of this DescribeAllCertificatesRequest.  # noqa: E501


        :return: The page_number of this DescribeAllCertificatesRequest.  # noqa: E501
        :rtype: int
        """
        return self._page_number

    @page_number.setter
    def page_number(self, page_number):
        """Sets the page_number of this DescribeAllCertificatesRequest.


        :param page_number: The page_number of this DescribeAllCertificatesRequest.  # noqa: E501
        :type: int
        """

        self._page_number = page_number

    @property
    def page_size(self):
        """Gets the page_size of this DescribeAllCertificatesRequest.  # noqa: E501


        :return: The page_size of this DescribeAllCertificatesRequest.  # noqa: E501
        :rtype: int
        """
        return self._page_size

    @page_size.setter
    def page_size(self, page_size):
        """Sets the page_size of this DescribeAllCertificatesRequest.


        :param page_size: The page_size of this DescribeAllCertificatesRequest.  # noqa: E501
        :type: int
        """

        self._page_size = page_size

    @property
    def project_name(self):
        """Gets the project_name of this DescribeAllCertificatesRequest.  # noqa: E501


        :return: The project_name of this DescribeAllCertificatesRequest.  # noqa: E501
        :rtype: str
        """
        return self._project_name

    @project_name.setter
    def project_name(self, project_name):
        """Sets the project_name of this DescribeAllCertificatesRequest.


        :param project_name: The project_name of this DescribeAllCertificatesRequest.  # noqa: E501
        :type: str
        """

        self._project_name = project_name

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
        if issubclass(DescribeAllCertificatesRequest, dict):
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
        if not isinstance(other, DescribeAllCertificatesRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DescribeAllCertificatesRequest):
            return True

        return self.to_dict() != other.to_dict()
