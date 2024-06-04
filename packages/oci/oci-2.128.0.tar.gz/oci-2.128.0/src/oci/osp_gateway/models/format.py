# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20191001


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class Format(object):
    """
    Format information
    """

    def __init__(self, **kwargs):
        """
        Initializes a new Format object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param value:
            The value to assign to the value property of this Format.
        :type value: str

        :param example:
            The value to assign to the example property of this Format.
        :type example: str

        """
        self.swagger_types = {
            'value': 'str',
            'example': 'str'
        }

        self.attribute_map = {
            'value': 'value',
            'example': 'example'
        }

        self._value = None
        self._example = None

    @property
    def value(self):
        """
        **[Required]** Gets the value of this Format.
        Regex format specification


        :return: The value of this Format.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """
        Sets the value of this Format.
        Regex format specification


        :param value: The value of this Format.
        :type: str
        """
        self._value = value

    @property
    def example(self):
        """
        Gets the example of this Format.
        Example of the desired format that matches the regex


        :return: The example of this Format.
        :rtype: str
        """
        return self._example

    @example.setter
    def example(self, example):
        """
        Sets the example of this Format.
        Example of the desired format that matches the regex


        :param example: The example of this Format.
        :type: str
        """
        self._example = example

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
