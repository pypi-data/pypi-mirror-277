# coding: utf-8

"""
    billing

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class ListSplitBillDetailRequest(object):
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
        'bill_category': 'list[str]',
        'bill_period': 'str',
        'billing_mode': 'list[str]',
        'expense_date': 'str',
        'group_period': 'int',
        'ignore_zero': 'int',
        'instance_no': 'str',
        'limit': 'int',
        'need_record_num': 'int',
        'offset': 'int',
        'product': 'list[str]',
        'split_item_id': 'str'
    }

    attribute_map = {
        'bill_category': 'BillCategory',
        'bill_period': 'BillPeriod',
        'billing_mode': 'BillingMode',
        'expense_date': 'ExpenseDate',
        'group_period': 'GroupPeriod',
        'ignore_zero': 'IgnoreZero',
        'instance_no': 'InstanceNo',
        'limit': 'Limit',
        'need_record_num': 'NeedRecordNum',
        'offset': 'Offset',
        'product': 'Product',
        'split_item_id': 'SplitItemID'
    }

    def __init__(self, bill_category=None, bill_period=None, billing_mode=None, expense_date=None, group_period=None, ignore_zero=None, instance_no=None, limit=None, need_record_num=None, offset=None, product=None, split_item_id=None, _configuration=None):  # noqa: E501
        """ListSplitBillDetailRequest - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._bill_category = None
        self._bill_period = None
        self._billing_mode = None
        self._expense_date = None
        self._group_period = None
        self._ignore_zero = None
        self._instance_no = None
        self._limit = None
        self._need_record_num = None
        self._offset = None
        self._product = None
        self._split_item_id = None
        self.discriminator = None

        if bill_category is not None:
            self.bill_category = bill_category
        self.bill_period = bill_period
        if billing_mode is not None:
            self.billing_mode = billing_mode
        if expense_date is not None:
            self.expense_date = expense_date
        if group_period is not None:
            self.group_period = group_period
        if ignore_zero is not None:
            self.ignore_zero = ignore_zero
        if instance_no is not None:
            self.instance_no = instance_no
        self.limit = limit
        if need_record_num is not None:
            self.need_record_num = need_record_num
        if offset is not None:
            self.offset = offset
        if product is not None:
            self.product = product
        if split_item_id is not None:
            self.split_item_id = split_item_id

    @property
    def bill_category(self):
        """Gets the bill_category of this ListSplitBillDetailRequest.  # noqa: E501


        :return: The bill_category of this ListSplitBillDetailRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._bill_category

    @bill_category.setter
    def bill_category(self, bill_category):
        """Sets the bill_category of this ListSplitBillDetailRequest.


        :param bill_category: The bill_category of this ListSplitBillDetailRequest.  # noqa: E501
        :type: list[str]
        """

        self._bill_category = bill_category

    @property
    def bill_period(self):
        """Gets the bill_period of this ListSplitBillDetailRequest.  # noqa: E501


        :return: The bill_period of this ListSplitBillDetailRequest.  # noqa: E501
        :rtype: str
        """
        return self._bill_period

    @bill_period.setter
    def bill_period(self, bill_period):
        """Sets the bill_period of this ListSplitBillDetailRequest.


        :param bill_period: The bill_period of this ListSplitBillDetailRequest.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and bill_period is None:
            raise ValueError("Invalid value for `bill_period`, must not be `None`")  # noqa: E501

        self._bill_period = bill_period

    @property
    def billing_mode(self):
        """Gets the billing_mode of this ListSplitBillDetailRequest.  # noqa: E501


        :return: The billing_mode of this ListSplitBillDetailRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._billing_mode

    @billing_mode.setter
    def billing_mode(self, billing_mode):
        """Sets the billing_mode of this ListSplitBillDetailRequest.


        :param billing_mode: The billing_mode of this ListSplitBillDetailRequest.  # noqa: E501
        :type: list[str]
        """

        self._billing_mode = billing_mode

    @property
    def expense_date(self):
        """Gets the expense_date of this ListSplitBillDetailRequest.  # noqa: E501


        :return: The expense_date of this ListSplitBillDetailRequest.  # noqa: E501
        :rtype: str
        """
        return self._expense_date

    @expense_date.setter
    def expense_date(self, expense_date):
        """Sets the expense_date of this ListSplitBillDetailRequest.


        :param expense_date: The expense_date of this ListSplitBillDetailRequest.  # noqa: E501
        :type: str
        """

        self._expense_date = expense_date

    @property
    def group_period(self):
        """Gets the group_period of this ListSplitBillDetailRequest.  # noqa: E501


        :return: The group_period of this ListSplitBillDetailRequest.  # noqa: E501
        :rtype: int
        """
        return self._group_period

    @group_period.setter
    def group_period(self, group_period):
        """Sets the group_period of this ListSplitBillDetailRequest.


        :param group_period: The group_period of this ListSplitBillDetailRequest.  # noqa: E501
        :type: int
        """

        self._group_period = group_period

    @property
    def ignore_zero(self):
        """Gets the ignore_zero of this ListSplitBillDetailRequest.  # noqa: E501


        :return: The ignore_zero of this ListSplitBillDetailRequest.  # noqa: E501
        :rtype: int
        """
        return self._ignore_zero

    @ignore_zero.setter
    def ignore_zero(self, ignore_zero):
        """Sets the ignore_zero of this ListSplitBillDetailRequest.


        :param ignore_zero: The ignore_zero of this ListSplitBillDetailRequest.  # noqa: E501
        :type: int
        """

        self._ignore_zero = ignore_zero

    @property
    def instance_no(self):
        """Gets the instance_no of this ListSplitBillDetailRequest.  # noqa: E501


        :return: The instance_no of this ListSplitBillDetailRequest.  # noqa: E501
        :rtype: str
        """
        return self._instance_no

    @instance_no.setter
    def instance_no(self, instance_no):
        """Sets the instance_no of this ListSplitBillDetailRequest.


        :param instance_no: The instance_no of this ListSplitBillDetailRequest.  # noqa: E501
        :type: str
        """

        self._instance_no = instance_no

    @property
    def limit(self):
        """Gets the limit of this ListSplitBillDetailRequest.  # noqa: E501


        :return: The limit of this ListSplitBillDetailRequest.  # noqa: E501
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListSplitBillDetailRequest.


        :param limit: The limit of this ListSplitBillDetailRequest.  # noqa: E501
        :type: int
        """
        if self._configuration.client_side_validation and limit is None:
            raise ValueError("Invalid value for `limit`, must not be `None`")  # noqa: E501

        self._limit = limit

    @property
    def need_record_num(self):
        """Gets the need_record_num of this ListSplitBillDetailRequest.  # noqa: E501


        :return: The need_record_num of this ListSplitBillDetailRequest.  # noqa: E501
        :rtype: int
        """
        return self._need_record_num

    @need_record_num.setter
    def need_record_num(self, need_record_num):
        """Sets the need_record_num of this ListSplitBillDetailRequest.


        :param need_record_num: The need_record_num of this ListSplitBillDetailRequest.  # noqa: E501
        :type: int
        """

        self._need_record_num = need_record_num

    @property
    def offset(self):
        """Gets the offset of this ListSplitBillDetailRequest.  # noqa: E501


        :return: The offset of this ListSplitBillDetailRequest.  # noqa: E501
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListSplitBillDetailRequest.


        :param offset: The offset of this ListSplitBillDetailRequest.  # noqa: E501
        :type: int
        """

        self._offset = offset

    @property
    def product(self):
        """Gets the product of this ListSplitBillDetailRequest.  # noqa: E501


        :return: The product of this ListSplitBillDetailRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._product

    @product.setter
    def product(self, product):
        """Sets the product of this ListSplitBillDetailRequest.


        :param product: The product of this ListSplitBillDetailRequest.  # noqa: E501
        :type: list[str]
        """

        self._product = product

    @property
    def split_item_id(self):
        """Gets the split_item_id of this ListSplitBillDetailRequest.  # noqa: E501


        :return: The split_item_id of this ListSplitBillDetailRequest.  # noqa: E501
        :rtype: str
        """
        return self._split_item_id

    @split_item_id.setter
    def split_item_id(self, split_item_id):
        """Sets the split_item_id of this ListSplitBillDetailRequest.


        :param split_item_id: The split_item_id of this ListSplitBillDetailRequest.  # noqa: E501
        :type: str
        """

        self._split_item_id = split_item_id

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
        if issubclass(ListSplitBillDetailRequest, dict):
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
        if not isinstance(other, ListSplitBillDetailRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ListSplitBillDetailRequest):
            return True

        return self.to_dict() != other.to_dict()
