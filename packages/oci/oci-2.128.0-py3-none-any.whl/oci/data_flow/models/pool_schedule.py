# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20200129


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class PoolSchedule(object):
    """
    Definition of when pool auto start or stop for a given day of a week.
    """

    #: A constant which can be used with the day_of_week property of a PoolSchedule.
    #: This constant has a value of "SUNDAY"
    DAY_OF_WEEK_SUNDAY = "SUNDAY"

    #: A constant which can be used with the day_of_week property of a PoolSchedule.
    #: This constant has a value of "MONDAY"
    DAY_OF_WEEK_MONDAY = "MONDAY"

    #: A constant which can be used with the day_of_week property of a PoolSchedule.
    #: This constant has a value of "TUESDAY"
    DAY_OF_WEEK_TUESDAY = "TUESDAY"

    #: A constant which can be used with the day_of_week property of a PoolSchedule.
    #: This constant has a value of "WEDNESDAY"
    DAY_OF_WEEK_WEDNESDAY = "WEDNESDAY"

    #: A constant which can be used with the day_of_week property of a PoolSchedule.
    #: This constant has a value of "THURSDAY"
    DAY_OF_WEEK_THURSDAY = "THURSDAY"

    #: A constant which can be used with the day_of_week property of a PoolSchedule.
    #: This constant has a value of "FRIDAY"
    DAY_OF_WEEK_FRIDAY = "FRIDAY"

    #: A constant which can be used with the day_of_week property of a PoolSchedule.
    #: This constant has a value of "SATURDAY"
    DAY_OF_WEEK_SATURDAY = "SATURDAY"

    def __init__(self, **kwargs):
        """
        Initializes a new PoolSchedule object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param day_of_week:
            The value to assign to the day_of_week property of this PoolSchedule.
            Allowed values for this property are: "SUNDAY", "MONDAY", "TUESDAY", "WEDNESDAY", "THURSDAY", "FRIDAY", "SATURDAY", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type day_of_week: str

        :param start_time:
            The value to assign to the start_time property of this PoolSchedule.
        :type start_time: int

        :param stop_time:
            The value to assign to the stop_time property of this PoolSchedule.
        :type stop_time: int

        """
        self.swagger_types = {
            'day_of_week': 'str',
            'start_time': 'int',
            'stop_time': 'int'
        }

        self.attribute_map = {
            'day_of_week': 'dayOfWeek',
            'start_time': 'startTime',
            'stop_time': 'stopTime'
        }

        self._day_of_week = None
        self._start_time = None
        self._stop_time = None

    @property
    def day_of_week(self):
        """
        Gets the day_of_week of this PoolSchedule.
        Day of the week SUN-SAT

        Allowed values for this property are: "SUNDAY", "MONDAY", "TUESDAY", "WEDNESDAY", "THURSDAY", "FRIDAY", "SATURDAY", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The day_of_week of this PoolSchedule.
        :rtype: str
        """
        return self._day_of_week

    @day_of_week.setter
    def day_of_week(self, day_of_week):
        """
        Sets the day_of_week of this PoolSchedule.
        Day of the week SUN-SAT


        :param day_of_week: The day_of_week of this PoolSchedule.
        :type: str
        """
        allowed_values = ["SUNDAY", "MONDAY", "TUESDAY", "WEDNESDAY", "THURSDAY", "FRIDAY", "SATURDAY"]
        if not value_allowed_none_or_none_sentinel(day_of_week, allowed_values):
            day_of_week = 'UNKNOWN_ENUM_VALUE'
        self._day_of_week = day_of_week

    @property
    def start_time(self):
        """
        Gets the start_time of this PoolSchedule.
        Hour of the day to start or stop pool.


        :return: The start_time of this PoolSchedule.
        :rtype: int
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """
        Sets the start_time of this PoolSchedule.
        Hour of the day to start or stop pool.


        :param start_time: The start_time of this PoolSchedule.
        :type: int
        """
        self._start_time = start_time

    @property
    def stop_time(self):
        """
        Gets the stop_time of this PoolSchedule.
        Hour of the day to stop the pool.


        :return: The stop_time of this PoolSchedule.
        :rtype: int
        """
        return self._stop_time

    @stop_time.setter
    def stop_time(self, stop_time):
        """
        Sets the stop_time of this PoolSchedule.
        Hour of the day to stop the pool.


        :param stop_time: The stop_time of this PoolSchedule.
        :type: int
        """
        self._stop_time = stop_time

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
