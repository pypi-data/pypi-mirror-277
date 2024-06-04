# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20200630


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class BulkPinMetadata(object):
    """
    Metadata about the bulk pin operation.  The bulk pin operation is atomic and binary.  If the processing of any of the attributes
    in the bulk pin request results in a processing or validation error, then none of the attributes in the request are pinned.
    """

    #: A constant which can be used with the operation_status property of a BulkPinMetadata.
    #: This constant has a value of "SUCCESS"
    OPERATION_STATUS_SUCCESS = "SUCCESS"

    #: A constant which can be used with the operation_status property of a BulkPinMetadata.
    #: This constant has a value of "EMPTY_ATTRIBUTE_LIST"
    OPERATION_STATUS_EMPTY_ATTRIBUTE_LIST = "EMPTY_ATTRIBUTE_LIST"

    #: A constant which can be used with the operation_status property of a BulkPinMetadata.
    #: This constant has a value of "INVALID_BULK_REQUEST"
    OPERATION_STATUS_INVALID_BULK_REQUEST = "INVALID_BULK_REQUEST"

    #: A constant which can be used with the operation_type property of a BulkPinMetadata.
    #: This constant has a value of "PIN"
    OPERATION_TYPE_PIN = "PIN"

    def __init__(self, **kwargs):
        """
        Initializes a new BulkPinMetadata object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param operation_status:
            The value to assign to the operation_status property of this BulkPinMetadata.
            Allowed values for this property are: "SUCCESS", "EMPTY_ATTRIBUTE_LIST", "INVALID_BULK_REQUEST", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type operation_status: str

        :param operation_type:
            The value to assign to the operation_type property of this BulkPinMetadata.
            Allowed values for this property are: "PIN", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type operation_type: str

        :param attributes_pinned:
            The value to assign to the attributes_pinned property of this BulkPinMetadata.
        :type attributes_pinned: int

        :param synthetic_attributes_pinned:
            The value to assign to the synthetic_attributes_pinned property of this BulkPinMetadata.
        :type synthetic_attributes_pinned: int

        """
        self.swagger_types = {
            'operation_status': 'str',
            'operation_type': 'str',
            'attributes_pinned': 'int',
            'synthetic_attributes_pinned': 'int'
        }

        self.attribute_map = {
            'operation_status': 'operationStatus',
            'operation_type': 'operationType',
            'attributes_pinned': 'attributesPinned',
            'synthetic_attributes_pinned': 'syntheticAttributesPinned'
        }

        self._operation_status = None
        self._operation_type = None
        self._attributes_pinned = None
        self._synthetic_attributes_pinned = None

    @property
    def operation_status(self):
        """
        **[Required]** Gets the operation_status of this BulkPinMetadata.
        Operation status of the bulk pin operation.
        SUCCESS - The bulk pin operation has succeeded and all the attributes in the bulk pin request have been pinned by this operation or pinned earlier.
        The following are error statuses for the bulk pin operation.
        EMPTY_ATTRIBUTE_LIST - The bulk pin request object was empty and did not contain any attributes to be pinned.
        INVALID_BULK_REQUEST - The bulk request contains invalid attribute(s), or attribute(s) that resulted in a validation error, or an attribute that resulted
        in a processing error.

        Allowed values for this property are: "SUCCESS", "EMPTY_ATTRIBUTE_LIST", "INVALID_BULK_REQUEST", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The operation_status of this BulkPinMetadata.
        :rtype: str
        """
        return self._operation_status

    @operation_status.setter
    def operation_status(self, operation_status):
        """
        Sets the operation_status of this BulkPinMetadata.
        Operation status of the bulk pin operation.
        SUCCESS - The bulk pin operation has succeeded and all the attributes in the bulk pin request have been pinned by this operation or pinned earlier.
        The following are error statuses for the bulk pin operation.
        EMPTY_ATTRIBUTE_LIST - The bulk pin request object was empty and did not contain any attributes to be pinned.
        INVALID_BULK_REQUEST - The bulk request contains invalid attribute(s), or attribute(s) that resulted in a validation error, or an attribute that resulted
        in a processing error.


        :param operation_status: The operation_status of this BulkPinMetadata.
        :type: str
        """
        allowed_values = ["SUCCESS", "EMPTY_ATTRIBUTE_LIST", "INVALID_BULK_REQUEST"]
        if not value_allowed_none_or_none_sentinel(operation_status, allowed_values):
            operation_status = 'UNKNOWN_ENUM_VALUE'
        self._operation_status = operation_status

    @property
    def operation_type(self):
        """
        **[Required]** Gets the operation_type of this BulkPinMetadata.
        Type of operation.

        Allowed values for this property are: "PIN", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The operation_type of this BulkPinMetadata.
        :rtype: str
        """
        return self._operation_type

    @operation_type.setter
    def operation_type(self, operation_type):
        """
        Sets the operation_type of this BulkPinMetadata.
        Type of operation.


        :param operation_type: The operation_type of this BulkPinMetadata.
        :type: str
        """
        allowed_values = ["PIN"]
        if not value_allowed_none_or_none_sentinel(operation_type, allowed_values):
            operation_type = 'UNKNOWN_ENUM_VALUE'
        self._operation_type = operation_type

    @property
    def attributes_pinned(self):
        """
        **[Required]** Gets the attributes_pinned of this BulkPinMetadata.
        Total number attributes (both string and numeric) in TRACES namespace that were pinned.


        :return: The attributes_pinned of this BulkPinMetadata.
        :rtype: int
        """
        return self._attributes_pinned

    @attributes_pinned.setter
    def attributes_pinned(self, attributes_pinned):
        """
        Sets the attributes_pinned of this BulkPinMetadata.
        Total number attributes (both string and numeric) in TRACES namespace that were pinned.


        :param attributes_pinned: The attributes_pinned of this BulkPinMetadata.
        :type: int
        """
        self._attributes_pinned = attributes_pinned

    @property
    def synthetic_attributes_pinned(self):
        """
        Gets the synthetic_attributes_pinned of this BulkPinMetadata.
        Total number attributes (both string and numeric) in SYNTHETIC namespace that were pinned.


        :return: The synthetic_attributes_pinned of this BulkPinMetadata.
        :rtype: int
        """
        return self._synthetic_attributes_pinned

    @synthetic_attributes_pinned.setter
    def synthetic_attributes_pinned(self, synthetic_attributes_pinned):
        """
        Sets the synthetic_attributes_pinned of this BulkPinMetadata.
        Total number attributes (both string and numeric) in SYNTHETIC namespace that were pinned.


        :param synthetic_attributes_pinned: The synthetic_attributes_pinned of this BulkPinMetadata.
        :type: int
        """
        self._synthetic_attributes_pinned = synthetic_attributes_pinned

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
