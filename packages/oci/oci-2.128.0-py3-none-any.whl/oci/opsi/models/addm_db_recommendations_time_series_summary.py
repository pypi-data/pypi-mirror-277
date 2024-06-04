# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20200630


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class AddmDbRecommendationsTimeSeriesSummary(object):
    """
    ADDM recommendation
    """

    def __init__(self, **kwargs):
        """
        Initializes a new AddmDbRecommendationsTimeSeriesSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this AddmDbRecommendationsTimeSeriesSummary.
        :type id: str

        :param task_id:
            The value to assign to the task_id property of this AddmDbRecommendationsTimeSeriesSummary.
        :type task_id: int

        :param task_name:
            The value to assign to the task_name property of this AddmDbRecommendationsTimeSeriesSummary.
        :type task_name: str

        :param timestamp:
            The value to assign to the timestamp property of this AddmDbRecommendationsTimeSeriesSummary.
        :type timestamp: datetime

        :param time_analysis_started:
            The value to assign to the time_analysis_started property of this AddmDbRecommendationsTimeSeriesSummary.
        :type time_analysis_started: datetime

        :param time_analysis_ended:
            The value to assign to the time_analysis_ended property of this AddmDbRecommendationsTimeSeriesSummary.
        :type time_analysis_ended: datetime

        :param type:
            The value to assign to the type property of this AddmDbRecommendationsTimeSeriesSummary.
        :type type: str

        :param analysis_db_time_in_secs:
            The value to assign to the analysis_db_time_in_secs property of this AddmDbRecommendationsTimeSeriesSummary.
        :type analysis_db_time_in_secs: float

        :param analysis_avg_active_sessions:
            The value to assign to the analysis_avg_active_sessions property of this AddmDbRecommendationsTimeSeriesSummary.
        :type analysis_avg_active_sessions: float

        :param max_benefit_percent:
            The value to assign to the max_benefit_percent property of this AddmDbRecommendationsTimeSeriesSummary.
        :type max_benefit_percent: float

        :param max_benefit_db_time_in_secs:
            The value to assign to the max_benefit_db_time_in_secs property of this AddmDbRecommendationsTimeSeriesSummary.
        :type max_benefit_db_time_in_secs: float

        :param max_benefit_avg_active_sessions:
            The value to assign to the max_benefit_avg_active_sessions property of this AddmDbRecommendationsTimeSeriesSummary.
        :type max_benefit_avg_active_sessions: float

        :param related_object:
            The value to assign to the related_object property of this AddmDbRecommendationsTimeSeriesSummary.
        :type related_object: oci.opsi.models.RelatedObjectTypeDetails

        """
        self.swagger_types = {
            'id': 'str',
            'task_id': 'int',
            'task_name': 'str',
            'timestamp': 'datetime',
            'time_analysis_started': 'datetime',
            'time_analysis_ended': 'datetime',
            'type': 'str',
            'analysis_db_time_in_secs': 'float',
            'analysis_avg_active_sessions': 'float',
            'max_benefit_percent': 'float',
            'max_benefit_db_time_in_secs': 'float',
            'max_benefit_avg_active_sessions': 'float',
            'related_object': 'RelatedObjectTypeDetails'
        }

        self.attribute_map = {
            'id': 'id',
            'task_id': 'taskId',
            'task_name': 'taskName',
            'timestamp': 'timestamp',
            'time_analysis_started': 'timeAnalysisStarted',
            'time_analysis_ended': 'timeAnalysisEnded',
            'type': 'type',
            'analysis_db_time_in_secs': 'analysisDbTimeInSecs',
            'analysis_avg_active_sessions': 'analysisAvgActiveSessions',
            'max_benefit_percent': 'maxBenefitPercent',
            'max_benefit_db_time_in_secs': 'maxBenefitDbTimeInSecs',
            'max_benefit_avg_active_sessions': 'maxBenefitAvgActiveSessions',
            'related_object': 'relatedObject'
        }

        self._id = None
        self._task_id = None
        self._task_name = None
        self._timestamp = None
        self._time_analysis_started = None
        self._time_analysis_ended = None
        self._type = None
        self._analysis_db_time_in_secs = None
        self._analysis_avg_active_sessions = None
        self._max_benefit_percent = None
        self._max_benefit_db_time_in_secs = None
        self._max_benefit_avg_active_sessions = None
        self._related_object = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this AddmDbRecommendationsTimeSeriesSummary.
        The `OCID`__ of the Database insight.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The id of this AddmDbRecommendationsTimeSeriesSummary.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this AddmDbRecommendationsTimeSeriesSummary.
        The `OCID`__ of the Database insight.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param id: The id of this AddmDbRecommendationsTimeSeriesSummary.
        :type: str
        """
        self._id = id

    @property
    def task_id(self):
        """
        **[Required]** Gets the task_id of this AddmDbRecommendationsTimeSeriesSummary.
        Unique ADDM task id


        :return: The task_id of this AddmDbRecommendationsTimeSeriesSummary.
        :rtype: int
        """
        return self._task_id

    @task_id.setter
    def task_id(self, task_id):
        """
        Sets the task_id of this AddmDbRecommendationsTimeSeriesSummary.
        Unique ADDM task id


        :param task_id: The task_id of this AddmDbRecommendationsTimeSeriesSummary.
        :type: int
        """
        self._task_id = task_id

    @property
    def task_name(self):
        """
        **[Required]** Gets the task_name of this AddmDbRecommendationsTimeSeriesSummary.
        ADDM task name


        :return: The task_name of this AddmDbRecommendationsTimeSeriesSummary.
        :rtype: str
        """
        return self._task_name

    @task_name.setter
    def task_name(self, task_name):
        """
        Sets the task_name of this AddmDbRecommendationsTimeSeriesSummary.
        ADDM task name


        :param task_name: The task_name of this AddmDbRecommendationsTimeSeriesSummary.
        :type: str
        """
        self._task_name = task_name

    @property
    def timestamp(self):
        """
        **[Required]** Gets the timestamp of this AddmDbRecommendationsTimeSeriesSummary.
        Timestamp when recommendation was generated


        :return: The timestamp of this AddmDbRecommendationsTimeSeriesSummary.
        :rtype: datetime
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """
        Sets the timestamp of this AddmDbRecommendationsTimeSeriesSummary.
        Timestamp when recommendation was generated


        :param timestamp: The timestamp of this AddmDbRecommendationsTimeSeriesSummary.
        :type: datetime
        """
        self._timestamp = timestamp

    @property
    def time_analysis_started(self):
        """
        Gets the time_analysis_started of this AddmDbRecommendationsTimeSeriesSummary.
        Start Timestamp of snapshot


        :return: The time_analysis_started of this AddmDbRecommendationsTimeSeriesSummary.
        :rtype: datetime
        """
        return self._time_analysis_started

    @time_analysis_started.setter
    def time_analysis_started(self, time_analysis_started):
        """
        Sets the time_analysis_started of this AddmDbRecommendationsTimeSeriesSummary.
        Start Timestamp of snapshot


        :param time_analysis_started: The time_analysis_started of this AddmDbRecommendationsTimeSeriesSummary.
        :type: datetime
        """
        self._time_analysis_started = time_analysis_started

    @property
    def time_analysis_ended(self):
        """
        Gets the time_analysis_ended of this AddmDbRecommendationsTimeSeriesSummary.
        End Timestamp of snapshot


        :return: The time_analysis_ended of this AddmDbRecommendationsTimeSeriesSummary.
        :rtype: datetime
        """
        return self._time_analysis_ended

    @time_analysis_ended.setter
    def time_analysis_ended(self, time_analysis_ended):
        """
        Sets the time_analysis_ended of this AddmDbRecommendationsTimeSeriesSummary.
        End Timestamp of snapshot


        :param time_analysis_ended: The time_analysis_ended of this AddmDbRecommendationsTimeSeriesSummary.
        :type: datetime
        """
        self._time_analysis_ended = time_analysis_ended

    @property
    def type(self):
        """
        Gets the type of this AddmDbRecommendationsTimeSeriesSummary.
        Type of recommendation


        :return: The type of this AddmDbRecommendationsTimeSeriesSummary.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this AddmDbRecommendationsTimeSeriesSummary.
        Type of recommendation


        :param type: The type of this AddmDbRecommendationsTimeSeriesSummary.
        :type: str
        """
        self._type = type

    @property
    def analysis_db_time_in_secs(self):
        """
        Gets the analysis_db_time_in_secs of this AddmDbRecommendationsTimeSeriesSummary.
        DB time in seconds for the snapshot


        :return: The analysis_db_time_in_secs of this AddmDbRecommendationsTimeSeriesSummary.
        :rtype: float
        """
        return self._analysis_db_time_in_secs

    @analysis_db_time_in_secs.setter
    def analysis_db_time_in_secs(self, analysis_db_time_in_secs):
        """
        Sets the analysis_db_time_in_secs of this AddmDbRecommendationsTimeSeriesSummary.
        DB time in seconds for the snapshot


        :param analysis_db_time_in_secs: The analysis_db_time_in_secs of this AddmDbRecommendationsTimeSeriesSummary.
        :type: float
        """
        self._analysis_db_time_in_secs = analysis_db_time_in_secs

    @property
    def analysis_avg_active_sessions(self):
        """
        Gets the analysis_avg_active_sessions of this AddmDbRecommendationsTimeSeriesSummary.
        DB avg active sessions for the snapshot


        :return: The analysis_avg_active_sessions of this AddmDbRecommendationsTimeSeriesSummary.
        :rtype: float
        """
        return self._analysis_avg_active_sessions

    @analysis_avg_active_sessions.setter
    def analysis_avg_active_sessions(self, analysis_avg_active_sessions):
        """
        Sets the analysis_avg_active_sessions of this AddmDbRecommendationsTimeSeriesSummary.
        DB avg active sessions for the snapshot


        :param analysis_avg_active_sessions: The analysis_avg_active_sessions of this AddmDbRecommendationsTimeSeriesSummary.
        :type: float
        """
        self._analysis_avg_active_sessions = analysis_avg_active_sessions

    @property
    def max_benefit_percent(self):
        """
        Gets the max_benefit_percent of this AddmDbRecommendationsTimeSeriesSummary.
        Maximum estimated benefit in terms of percentage of total activity


        :return: The max_benefit_percent of this AddmDbRecommendationsTimeSeriesSummary.
        :rtype: float
        """
        return self._max_benefit_percent

    @max_benefit_percent.setter
    def max_benefit_percent(self, max_benefit_percent):
        """
        Sets the max_benefit_percent of this AddmDbRecommendationsTimeSeriesSummary.
        Maximum estimated benefit in terms of percentage of total activity


        :param max_benefit_percent: The max_benefit_percent of this AddmDbRecommendationsTimeSeriesSummary.
        :type: float
        """
        self._max_benefit_percent = max_benefit_percent

    @property
    def max_benefit_db_time_in_secs(self):
        """
        Gets the max_benefit_db_time_in_secs of this AddmDbRecommendationsTimeSeriesSummary.
        Maximum estimated benefit in terms of seconds


        :return: The max_benefit_db_time_in_secs of this AddmDbRecommendationsTimeSeriesSummary.
        :rtype: float
        """
        return self._max_benefit_db_time_in_secs

    @max_benefit_db_time_in_secs.setter
    def max_benefit_db_time_in_secs(self, max_benefit_db_time_in_secs):
        """
        Sets the max_benefit_db_time_in_secs of this AddmDbRecommendationsTimeSeriesSummary.
        Maximum estimated benefit in terms of seconds


        :param max_benefit_db_time_in_secs: The max_benefit_db_time_in_secs of this AddmDbRecommendationsTimeSeriesSummary.
        :type: float
        """
        self._max_benefit_db_time_in_secs = max_benefit_db_time_in_secs

    @property
    def max_benefit_avg_active_sessions(self):
        """
        Gets the max_benefit_avg_active_sessions of this AddmDbRecommendationsTimeSeriesSummary.
        Maximum estimated benefit in terms of average active sessions


        :return: The max_benefit_avg_active_sessions of this AddmDbRecommendationsTimeSeriesSummary.
        :rtype: float
        """
        return self._max_benefit_avg_active_sessions

    @max_benefit_avg_active_sessions.setter
    def max_benefit_avg_active_sessions(self, max_benefit_avg_active_sessions):
        """
        Sets the max_benefit_avg_active_sessions of this AddmDbRecommendationsTimeSeriesSummary.
        Maximum estimated benefit in terms of average active sessions


        :param max_benefit_avg_active_sessions: The max_benefit_avg_active_sessions of this AddmDbRecommendationsTimeSeriesSummary.
        :type: float
        """
        self._max_benefit_avg_active_sessions = max_benefit_avg_active_sessions

    @property
    def related_object(self):
        """
        Gets the related_object of this AddmDbRecommendationsTimeSeriesSummary.

        :return: The related_object of this AddmDbRecommendationsTimeSeriesSummary.
        :rtype: oci.opsi.models.RelatedObjectTypeDetails
        """
        return self._related_object

    @related_object.setter
    def related_object(self, related_object):
        """
        Sets the related_object of this AddmDbRecommendationsTimeSeriesSummary.

        :param related_object: The related_object of this AddmDbRecommendationsTimeSeriesSummary.
        :type: oci.opsi.models.RelatedObjectTypeDetails
        """
        self._related_object = related_object

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
