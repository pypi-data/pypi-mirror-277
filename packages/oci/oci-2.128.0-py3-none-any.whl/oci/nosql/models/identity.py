# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20190828


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class Identity(object):
    """
    The identity properties of a table, if any.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new Identity object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param column_name:
            The value to assign to the column_name property of this Identity.
        :type column_name: str

        :param is_always:
            The value to assign to the is_always property of this Identity.
        :type is_always: bool

        :param is_null:
            The value to assign to the is_null property of this Identity.
        :type is_null: bool

        """
        self.swagger_types = {
            'column_name': 'str',
            'is_always': 'bool',
            'is_null': 'bool'
        }

        self.attribute_map = {
            'column_name': 'columnName',
            'is_always': 'isAlways',
            'is_null': 'isNull'
        }

        self._column_name = None
        self._is_always = None
        self._is_null = None

    @property
    def column_name(self):
        """
        Gets the column_name of this Identity.
        The name of the identity column.


        :return: The column_name of this Identity.
        :rtype: str
        """
        return self._column_name

    @column_name.setter
    def column_name(self, column_name):
        """
        Sets the column_name of this Identity.
        The name of the identity column.


        :param column_name: The column_name of this Identity.
        :type: str
        """
        self._column_name = column_name

    @property
    def is_always(self):
        """
        Gets the is_always of this Identity.
        True if the identity value is GENERATED ALWAYS.


        :return: The is_always of this Identity.
        :rtype: bool
        """
        return self._is_always

    @is_always.setter
    def is_always(self, is_always):
        """
        Sets the is_always of this Identity.
        True if the identity value is GENERATED ALWAYS.


        :param is_always: The is_always of this Identity.
        :type: bool
        """
        self._is_always = is_always

    @property
    def is_null(self):
        """
        Gets the is_null of this Identity.
        True if the identity value is GENERATED BY DEFAULT ON NULL.


        :return: The is_null of this Identity.
        :rtype: bool
        """
        return self._is_null

    @is_null.setter
    def is_null(self, is_null):
        """
        Sets the is_null of this Identity.
        True if the identity value is GENERATED BY DEFAULT ON NULL.


        :param is_null: The is_null of this Identity.
        :type: bool
        """
        self._is_null = is_null

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
