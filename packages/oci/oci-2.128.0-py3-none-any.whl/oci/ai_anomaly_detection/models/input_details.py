# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20210101


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class InputDetails(object):
    """
    Detect anomaly asynchronous job details.
    """

    #: A constant which can be used with the input_type property of a InputDetails.
    #: This constant has a value of "INLINE"
    INPUT_TYPE_INLINE = "INLINE"

    #: A constant which can be used with the input_type property of a InputDetails.
    #: This constant has a value of "BASE64_ENCODED"
    INPUT_TYPE_BASE64_ENCODED = "BASE64_ENCODED"

    #: A constant which can be used with the input_type property of a InputDetails.
    #: This constant has a value of "OBJECT_LIST"
    INPUT_TYPE_OBJECT_LIST = "OBJECT_LIST"

    def __init__(self, **kwargs):
        """
        Initializes a new InputDetails object with values from keyword arguments. This class has the following subclasses and if you are using this class as input
        to a service operations then you should favor using a subclass over the base class:

        * :class:`~oci.ai_anomaly_detection.models.EmbeddedInputDetails`
        * :class:`~oci.ai_anomaly_detection.models.ObjectListInputDetails`
        * :class:`~oci.ai_anomaly_detection.models.InlineInputDetails`

        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param input_type:
            The value to assign to the input_type property of this InputDetails.
            Allowed values for this property are: "INLINE", "BASE64_ENCODED", "OBJECT_LIST"
        :type input_type: str

        """
        self.swagger_types = {
            'input_type': 'str'
        }

        self.attribute_map = {
            'input_type': 'inputType'
        }

        self._input_type = None

    @staticmethod
    def get_subtype(object_dictionary):
        """
        Given the hash representation of a subtype of this class,
        use the info in the hash to return the class of the subtype.
        """
        type = object_dictionary['inputType']

        if type == 'BASE64_ENCODED':
            return 'EmbeddedInputDetails'

        if type == 'OBJECT_LIST':
            return 'ObjectListInputDetails'

        if type == 'INLINE':
            return 'InlineInputDetails'
        else:
            return 'InputDetails'

    @property
    def input_type(self):
        """
        **[Required]** Gets the input_type of this InputDetails.
        Type of request. This parameter is automatically populated by classes generated
        by the SDK. For raw curl requests, you must provide this field.

        Allowed values for this property are: "INLINE", "BASE64_ENCODED", "OBJECT_LIST"


        :return: The input_type of this InputDetails.
        :rtype: str
        """
        return self._input_type

    @input_type.setter
    def input_type(self, input_type):
        """
        Sets the input_type of this InputDetails.
        Type of request. This parameter is automatically populated by classes generated
        by the SDK. For raw curl requests, you must provide this field.


        :param input_type: The input_type of this InputDetails.
        :type: str
        """
        allowed_values = ["INLINE", "BASE64_ENCODED", "OBJECT_LIST"]
        if not value_allowed_none_or_none_sentinel(input_type, allowed_values):
            raise ValueError(
                f"Invalid value for `input_type`, must be None or one of {allowed_values}"
            )
        self._input_type = input_type

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
