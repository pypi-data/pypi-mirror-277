# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20200630


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class TagMetadata(object):
    """
    Definition of the tag metadata.
    """

    #: A constant which can be used with the tag_type property of a TagMetadata.
    #: This constant has a value of "STRING"
    TAG_TYPE_STRING = "STRING"

    #: A constant which can be used with the tag_type property of a TagMetadata.
    #: This constant has a value of "NUMERIC"
    TAG_TYPE_NUMERIC = "NUMERIC"

    #: A constant which can be used with the tag_unit property of a TagMetadata.
    #: This constant has a value of "EPOCH_TIME_MS"
    TAG_UNIT_EPOCH_TIME_MS = "EPOCH_TIME_MS"

    #: A constant which can be used with the tag_unit property of a TagMetadata.
    #: This constant has a value of "BYTES"
    TAG_UNIT_BYTES = "BYTES"

    #: A constant which can be used with the tag_unit property of a TagMetadata.
    #: This constant has a value of "COUNT"
    TAG_UNIT_COUNT = "COUNT"

    #: A constant which can be used with the tag_unit property of a TagMetadata.
    #: This constant has a value of "DURATION_MS"
    TAG_UNIT_DURATION_MS = "DURATION_MS"

    #: A constant which can be used with the tag_unit property of a TagMetadata.
    #: This constant has a value of "TRACE_STATUS"
    TAG_UNIT_TRACE_STATUS = "TRACE_STATUS"

    #: A constant which can be used with the tag_unit property of a TagMetadata.
    #: This constant has a value of "PERCENTAGE"
    TAG_UNIT_PERCENTAGE = "PERCENTAGE"

    #: A constant which can be used with the tag_unit property of a TagMetadata.
    #: This constant has a value of "NONE"
    TAG_UNIT_NONE = "NONE"

    def __init__(self, **kwargs):
        """
        Initializes a new TagMetadata object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param tag_type:
            The value to assign to the tag_type property of this TagMetadata.
            Allowed values for this property are: "STRING", "NUMERIC", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type tag_type: str

        :param tag_unit:
            The value to assign to the tag_unit property of this TagMetadata.
            Allowed values for this property are: "EPOCH_TIME_MS", "BYTES", "COUNT", "DURATION_MS", "TRACE_STATUS", "PERCENTAGE", "NONE", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type tag_unit: str

        """
        self.swagger_types = {
            'tag_type': 'str',
            'tag_unit': 'str'
        }

        self.attribute_map = {
            'tag_type': 'tagType',
            'tag_unit': 'tagUnit'
        }

        self._tag_type = None
        self._tag_unit = None

    @property
    def tag_type(self):
        """
        Gets the tag_type of this TagMetadata.
        Type associated with the tag key.

        Allowed values for this property are: "STRING", "NUMERIC", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The tag_type of this TagMetadata.
        :rtype: str
        """
        return self._tag_type

    @tag_type.setter
    def tag_type(self, tag_type):
        """
        Sets the tag_type of this TagMetadata.
        Type associated with the tag key.


        :param tag_type: The tag_type of this TagMetadata.
        :type: str
        """
        allowed_values = ["STRING", "NUMERIC"]
        if not value_allowed_none_or_none_sentinel(tag_type, allowed_values):
            tag_type = 'UNKNOWN_ENUM_VALUE'
        self._tag_type = tag_type

    @property
    def tag_unit(self):
        """
        Gets the tag_unit of this TagMetadata.
        Unit associated with the tag key.

        Allowed values for this property are: "EPOCH_TIME_MS", "BYTES", "COUNT", "DURATION_MS", "TRACE_STATUS", "PERCENTAGE", "NONE", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The tag_unit of this TagMetadata.
        :rtype: str
        """
        return self._tag_unit

    @tag_unit.setter
    def tag_unit(self, tag_unit):
        """
        Sets the tag_unit of this TagMetadata.
        Unit associated with the tag key.


        :param tag_unit: The tag_unit of this TagMetadata.
        :type: str
        """
        allowed_values = ["EPOCH_TIME_MS", "BYTES", "COUNT", "DURATION_MS", "TRACE_STATUS", "PERCENTAGE", "NONE"]
        if not value_allowed_none_or_none_sentinel(tag_unit, allowed_values):
            tag_unit = 'UNKNOWN_ENUM_VALUE'
        self._tag_unit = tag_unit

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
