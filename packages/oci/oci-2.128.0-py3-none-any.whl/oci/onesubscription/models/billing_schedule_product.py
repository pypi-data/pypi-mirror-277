# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20190111


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class BillingScheduleProduct(object):
    """
    Product description
    """

    def __init__(self, **kwargs):
        """
        Initializes a new BillingScheduleProduct object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param part_number:
            The value to assign to the part_number property of this BillingScheduleProduct.
        :type part_number: str

        :param name:
            The value to assign to the name property of this BillingScheduleProduct.
        :type name: str

        """
        self.swagger_types = {
            'part_number': 'str',
            'name': 'str'
        }

        self.attribute_map = {
            'part_number': 'partNumber',
            'name': 'name'
        }

        self._part_number = None
        self._name = None

    @property
    def part_number(self):
        """
        **[Required]** Gets the part_number of this BillingScheduleProduct.
        Indicates the associated AR Invoice Number


        :return: The part_number of this BillingScheduleProduct.
        :rtype: str
        """
        return self._part_number

    @part_number.setter
    def part_number(self, part_number):
        """
        Sets the part_number of this BillingScheduleProduct.
        Indicates the associated AR Invoice Number


        :param part_number: The part_number of this BillingScheduleProduct.
        :type: str
        """
        self._part_number = part_number

    @property
    def name(self):
        """
        **[Required]** Gets the name of this BillingScheduleProduct.
        Product name


        :return: The name of this BillingScheduleProduct.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this BillingScheduleProduct.
        Product name


        :param name: The name of this BillingScheduleProduct.
        :type: str
        """
        self._name = name

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
