# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20220528

from .fsu_action import FsuAction
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ApplyAction(FsuAction):
    """
    Apply Exadata Fleet Update Action details.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ApplyAction object with values from keyword arguments. The default value of the :py:attr:`~oci.fleet_software_update.models.ApplyAction.type` attribute
        of this class is ``APPLY`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this ApplyAction.
        :type id: str

        :param display_name:
            The value to assign to the display_name property of this ApplyAction.
        :type display_name: str

        :param compartment_id:
            The value to assign to the compartment_id property of this ApplyAction.
        :type compartment_id: str

        :param type:
            The value to assign to the type property of this ApplyAction.
            Allowed values for this property are: "STAGE", "PRECHECK", "APPLY", "ROLLBACK_AND_REMOVE_TARGET", "CLEANUP"
        :type type: str

        :param time_created:
            The value to assign to the time_created property of this ApplyAction.
        :type time_created: datetime

        :param time_started:
            The value to assign to the time_started property of this ApplyAction.
        :type time_started: datetime

        :param time_finished:
            The value to assign to the time_finished property of this ApplyAction.
        :type time_finished: datetime

        :param time_updated:
            The value to assign to the time_updated property of this ApplyAction.
        :type time_updated: datetime

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this ApplyAction.
            Allowed values for this property are: "ACCEPTED", "IN_PROGRESS", "WAITING", "UPDATING", "FAILED", "NEEDS_ATTENTION", "SUCCEEDED", "CANCELING", "CANCELED", "UNKNOWN", "DELETING", "DELETED"
        :type lifecycle_state: str

        :param lifecycle_details:
            The value to assign to the lifecycle_details property of this ApplyAction.
        :type lifecycle_details: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this ApplyAction.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this ApplyAction.
        :type defined_tags: dict(str, dict(str, object))

        :param system_tags:
            The value to assign to the system_tags property of this ApplyAction.
        :type system_tags: dict(str, dict(str, object))

        :param fsu_cycle_id:
            The value to assign to the fsu_cycle_id property of this ApplyAction.
        :type fsu_cycle_id: str

        :param related_fsu_action_id:
            The value to assign to the related_fsu_action_id property of this ApplyAction.
        :type related_fsu_action_id: str

        :param schedule_details:
            The value to assign to the schedule_details property of this ApplyAction.
        :type schedule_details: oci.fleet_software_update.models.ScheduleDetails

        :param progress:
            The value to assign to the progress property of this ApplyAction.
        :type progress: oci.fleet_software_update.models.FsuActionProgressDetails

        """
        self.swagger_types = {
            'id': 'str',
            'display_name': 'str',
            'compartment_id': 'str',
            'type': 'str',
            'time_created': 'datetime',
            'time_started': 'datetime',
            'time_finished': 'datetime',
            'time_updated': 'datetime',
            'lifecycle_state': 'str',
            'lifecycle_details': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'system_tags': 'dict(str, dict(str, object))',
            'fsu_cycle_id': 'str',
            'related_fsu_action_id': 'str',
            'schedule_details': 'ScheduleDetails',
            'progress': 'FsuActionProgressDetails'
        }

        self.attribute_map = {
            'id': 'id',
            'display_name': 'displayName',
            'compartment_id': 'compartmentId',
            'type': 'type',
            'time_created': 'timeCreated',
            'time_started': 'timeStarted',
            'time_finished': 'timeFinished',
            'time_updated': 'timeUpdated',
            'lifecycle_state': 'lifecycleState',
            'lifecycle_details': 'lifecycleDetails',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'system_tags': 'systemTags',
            'fsu_cycle_id': 'fsuCycleId',
            'related_fsu_action_id': 'relatedFsuActionId',
            'schedule_details': 'scheduleDetails',
            'progress': 'progress'
        }

        self._id = None
        self._display_name = None
        self._compartment_id = None
        self._type = None
        self._time_created = None
        self._time_started = None
        self._time_finished = None
        self._time_updated = None
        self._lifecycle_state = None
        self._lifecycle_details = None
        self._freeform_tags = None
        self._defined_tags = None
        self._system_tags = None
        self._fsu_cycle_id = None
        self._related_fsu_action_id = None
        self._schedule_details = None
        self._progress = None
        self._type = 'APPLY'

    @property
    def fsu_cycle_id(self):
        """
        **[Required]** Gets the fsu_cycle_id of this ApplyAction.
        OCID identifier for the Exadata Fleet Update Cycle the Action will be part of.


        :return: The fsu_cycle_id of this ApplyAction.
        :rtype: str
        """
        return self._fsu_cycle_id

    @fsu_cycle_id.setter
    def fsu_cycle_id(self, fsu_cycle_id):
        """
        Sets the fsu_cycle_id of this ApplyAction.
        OCID identifier for the Exadata Fleet Update Cycle the Action will be part of.


        :param fsu_cycle_id: The fsu_cycle_id of this ApplyAction.
        :type: str
        """
        self._fsu_cycle_id = fsu_cycle_id

    @property
    def related_fsu_action_id(self):
        """
        Gets the related_fsu_action_id of this ApplyAction.
        OCID identifier for the Exadata Fleet Update Action.


        :return: The related_fsu_action_id of this ApplyAction.
        :rtype: str
        """
        return self._related_fsu_action_id

    @related_fsu_action_id.setter
    def related_fsu_action_id(self, related_fsu_action_id):
        """
        Sets the related_fsu_action_id of this ApplyAction.
        OCID identifier for the Exadata Fleet Update Action.


        :param related_fsu_action_id: The related_fsu_action_id of this ApplyAction.
        :type: str
        """
        self._related_fsu_action_id = related_fsu_action_id

    @property
    def schedule_details(self):
        """
        Gets the schedule_details of this ApplyAction.

        :return: The schedule_details of this ApplyAction.
        :rtype: oci.fleet_software_update.models.ScheduleDetails
        """
        return self._schedule_details

    @schedule_details.setter
    def schedule_details(self, schedule_details):
        """
        Sets the schedule_details of this ApplyAction.

        :param schedule_details: The schedule_details of this ApplyAction.
        :type: oci.fleet_software_update.models.ScheduleDetails
        """
        self._schedule_details = schedule_details

    @property
    def progress(self):
        """
        Gets the progress of this ApplyAction.

        :return: The progress of this ApplyAction.
        :rtype: oci.fleet_software_update.models.FsuActionProgressDetails
        """
        return self._progress

    @progress.setter
    def progress(self, progress):
        """
        Sets the progress of this ApplyAction.

        :param progress: The progress of this ApplyAction.
        :type: oci.fleet_software_update.models.FsuActionProgressDetails
        """
        self._progress = progress

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
