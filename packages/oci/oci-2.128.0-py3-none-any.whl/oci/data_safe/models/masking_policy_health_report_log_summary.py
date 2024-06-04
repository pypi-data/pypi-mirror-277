# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20181201


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class MaskingPolicyHealthReportLogSummary(object):
    """
    A log entry related to the pre-masking health check.
    """

    #: A constant which can be used with the message_type property of a MaskingPolicyHealthReportLogSummary.
    #: This constant has a value of "PASS"
    MESSAGE_TYPE_PASS = "PASS"

    #: A constant which can be used with the message_type property of a MaskingPolicyHealthReportLogSummary.
    #: This constant has a value of "WARNING"
    MESSAGE_TYPE_WARNING = "WARNING"

    #: A constant which can be used with the message_type property of a MaskingPolicyHealthReportLogSummary.
    #: This constant has a value of "ERROR"
    MESSAGE_TYPE_ERROR = "ERROR"

    def __init__(self, **kwargs):
        """
        Initializes a new MaskingPolicyHealthReportLogSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param message_type:
            The value to assign to the message_type property of this MaskingPolicyHealthReportLogSummary.
            Allowed values for this property are: "PASS", "WARNING", "ERROR", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type message_type: str

        :param timestamp:
            The value to assign to the timestamp property of this MaskingPolicyHealthReportLogSummary.
        :type timestamp: datetime

        :param message:
            The value to assign to the message property of this MaskingPolicyHealthReportLogSummary.
        :type message: str

        :param remediation:
            The value to assign to the remediation property of this MaskingPolicyHealthReportLogSummary.
        :type remediation: str

        :param description:
            The value to assign to the description property of this MaskingPolicyHealthReportLogSummary.
        :type description: str

        """
        self.swagger_types = {
            'message_type': 'str',
            'timestamp': 'datetime',
            'message': 'str',
            'remediation': 'str',
            'description': 'str'
        }

        self.attribute_map = {
            'message_type': 'messageType',
            'timestamp': 'timestamp',
            'message': 'message',
            'remediation': 'remediation',
            'description': 'description'
        }

        self._message_type = None
        self._timestamp = None
        self._message = None
        self._remediation = None
        self._description = None

    @property
    def message_type(self):
        """
        **[Required]** Gets the message_type of this MaskingPolicyHealthReportLogSummary.
        The log entry type.

        Allowed values for this property are: "PASS", "WARNING", "ERROR", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The message_type of this MaskingPolicyHealthReportLogSummary.
        :rtype: str
        """
        return self._message_type

    @message_type.setter
    def message_type(self, message_type):
        """
        Sets the message_type of this MaskingPolicyHealthReportLogSummary.
        The log entry type.


        :param message_type: The message_type of this MaskingPolicyHealthReportLogSummary.
        :type: str
        """
        allowed_values = ["PASS", "WARNING", "ERROR"]
        if not value_allowed_none_or_none_sentinel(message_type, allowed_values):
            message_type = 'UNKNOWN_ENUM_VALUE'
        self._message_type = message_type

    @property
    def timestamp(self):
        """
        **[Required]** Gets the timestamp of this MaskingPolicyHealthReportLogSummary.
        The date and time the log entry was created, in the format defined by `RFC3339`__.

        __ https://tools.ietf.org/html/rfc3339


        :return: The timestamp of this MaskingPolicyHealthReportLogSummary.
        :rtype: datetime
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """
        Sets the timestamp of this MaskingPolicyHealthReportLogSummary.
        The date and time the log entry was created, in the format defined by `RFC3339`__.

        __ https://tools.ietf.org/html/rfc3339


        :param timestamp: The timestamp of this MaskingPolicyHealthReportLogSummary.
        :type: datetime
        """
        self._timestamp = timestamp

    @property
    def message(self):
        """
        **[Required]** Gets the message of this MaskingPolicyHealthReportLogSummary.
        A human-readable log entry.


        :return: The message of this MaskingPolicyHealthReportLogSummary.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """
        Sets the message of this MaskingPolicyHealthReportLogSummary.
        A human-readable log entry.


        :param message: The message of this MaskingPolicyHealthReportLogSummary.
        :type: str
        """
        self._message = message

    @property
    def remediation(self):
        """
        Gets the remediation of this MaskingPolicyHealthReportLogSummary.
        A human-readable log entry to remedy any error or warnings in the masking policy.


        :return: The remediation of this MaskingPolicyHealthReportLogSummary.
        :rtype: str
        """
        return self._remediation

    @remediation.setter
    def remediation(self, remediation):
        """
        Sets the remediation of this MaskingPolicyHealthReportLogSummary.
        A human-readable log entry to remedy any error or warnings in the masking policy.


        :param remediation: The remediation of this MaskingPolicyHealthReportLogSummary.
        :type: str
        """
        self._remediation = remediation

    @property
    def description(self):
        """
        **[Required]** Gets the description of this MaskingPolicyHealthReportLogSummary.
        A human-readable description for the log entry.


        :return: The description of this MaskingPolicyHealthReportLogSummary.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this MaskingPolicyHealthReportLogSummary.
        A human-readable description for the log entry.


        :param description: The description of this MaskingPolicyHealthReportLogSummary.
        :type: str
        """
        self._description = description

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
