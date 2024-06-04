# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20180401


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class SummarizeAlarmSuppressionHistoryDetails(object):
    """
    The configuration details for returning history of suppressions for the specified alarm.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new SummarizeAlarmSuppressionHistoryDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param dimensions:
            The value to assign to the dimensions property of this SummarizeAlarmSuppressionHistoryDetails.
        :type dimensions: dict(str, str)

        :param time_suppress_from_greater_than_or_equal_to:
            The value to assign to the time_suppress_from_greater_than_or_equal_to property of this SummarizeAlarmSuppressionHistoryDetails.
        :type time_suppress_from_greater_than_or_equal_to: datetime

        :param time_suppress_from_less_than:
            The value to assign to the time_suppress_from_less_than property of this SummarizeAlarmSuppressionHistoryDetails.
        :type time_suppress_from_less_than: datetime

        """
        self.swagger_types = {
            'dimensions': 'dict(str, str)',
            'time_suppress_from_greater_than_or_equal_to': 'datetime',
            'time_suppress_from_less_than': 'datetime'
        }

        self.attribute_map = {
            'dimensions': 'dimensions',
            'time_suppress_from_greater_than_or_equal_to': 'timeSuppressFromGreaterThanOrEqualTo',
            'time_suppress_from_less_than': 'timeSuppressFromLessThan'
        }

        self._dimensions = None
        self._time_suppress_from_greater_than_or_equal_to = None
        self._time_suppress_from_less_than = None

    @property
    def dimensions(self):
        """
        Gets the dimensions of this SummarizeAlarmSuppressionHistoryDetails.
        A filter to suppress only alarm state entries that include the set of specified dimension key-value pairs.
        If you specify {\"availabilityDomain\": \"phx-ad-1\"}
        and the alarm state entry corresponds to the set {\"availabilityDomain\": \"phx-ad-1\" and \"resourceId\": \"ocid1.instance.region1.phx.exampleuniqueID\"},
        then this alarm will be included for suppression.

        Example: `{\"resourceId\": \"ocid1.instance.region1.phx.exampleuniqueID\"}`


        :return: The dimensions of this SummarizeAlarmSuppressionHistoryDetails.
        :rtype: dict(str, str)
        """
        return self._dimensions

    @dimensions.setter
    def dimensions(self, dimensions):
        """
        Sets the dimensions of this SummarizeAlarmSuppressionHistoryDetails.
        A filter to suppress only alarm state entries that include the set of specified dimension key-value pairs.
        If you specify {\"availabilityDomain\": \"phx-ad-1\"}
        and the alarm state entry corresponds to the set {\"availabilityDomain\": \"phx-ad-1\" and \"resourceId\": \"ocid1.instance.region1.phx.exampleuniqueID\"},
        then this alarm will be included for suppression.

        Example: `{\"resourceId\": \"ocid1.instance.region1.phx.exampleuniqueID\"}`


        :param dimensions: The dimensions of this SummarizeAlarmSuppressionHistoryDetails.
        :type: dict(str, str)
        """
        self._dimensions = dimensions

    @property
    def time_suppress_from_greater_than_or_equal_to(self):
        """
        Gets the time_suppress_from_greater_than_or_equal_to of this SummarizeAlarmSuppressionHistoryDetails.
        A filter to return only entries with \"timeSuppressFrom\" time occurring on or after the specified time.

        The value cannot be a future time.
        Format defined by RFC3339.

        Example: `2023-02-01T01:02:29.600Z`


        :return: The time_suppress_from_greater_than_or_equal_to of this SummarizeAlarmSuppressionHistoryDetails.
        :rtype: datetime
        """
        return self._time_suppress_from_greater_than_or_equal_to

    @time_suppress_from_greater_than_or_equal_to.setter
    def time_suppress_from_greater_than_or_equal_to(self, time_suppress_from_greater_than_or_equal_to):
        """
        Sets the time_suppress_from_greater_than_or_equal_to of this SummarizeAlarmSuppressionHistoryDetails.
        A filter to return only entries with \"timeSuppressFrom\" time occurring on or after the specified time.

        The value cannot be a future time.
        Format defined by RFC3339.

        Example: `2023-02-01T01:02:29.600Z`


        :param time_suppress_from_greater_than_or_equal_to: The time_suppress_from_greater_than_or_equal_to of this SummarizeAlarmSuppressionHistoryDetails.
        :type: datetime
        """
        self._time_suppress_from_greater_than_or_equal_to = time_suppress_from_greater_than_or_equal_to

    @property
    def time_suppress_from_less_than(self):
        """
        Gets the time_suppress_from_less_than of this SummarizeAlarmSuppressionHistoryDetails.
        A filter to return only entries with \"timeSuppressFrom\" time occurring before the specified time.

        The value cannot be a future time.
        Format defined by RFC3339.

        Example: `2023-02-01T01:02:29.600Z`


        :return: The time_suppress_from_less_than of this SummarizeAlarmSuppressionHistoryDetails.
        :rtype: datetime
        """
        return self._time_suppress_from_less_than

    @time_suppress_from_less_than.setter
    def time_suppress_from_less_than(self, time_suppress_from_less_than):
        """
        Sets the time_suppress_from_less_than of this SummarizeAlarmSuppressionHistoryDetails.
        A filter to return only entries with \"timeSuppressFrom\" time occurring before the specified time.

        The value cannot be a future time.
        Format defined by RFC3339.

        Example: `2023-02-01T01:02:29.600Z`


        :param time_suppress_from_less_than: The time_suppress_from_less_than of this SummarizeAlarmSuppressionHistoryDetails.
        :type: datetime
        """
        self._time_suppress_from_less_than = time_suppress_from_less_than

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
