# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20200630


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateWorkerDetails(object):
    """
    Details of the request body used to update an On-premise VP worker.
    """

    #: A constant which can be used with the status property of a UpdateWorkerDetails.
    #: This constant has a value of "ENABLED"
    STATUS_ENABLED = "ENABLED"

    #: A constant which can be used with the status property of a UpdateWorkerDetails.
    #: This constant has a value of "DISABLED"
    STATUS_DISABLED = "DISABLED"

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateWorkerDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param configuration_details:
            The value to assign to the configuration_details property of this UpdateWorkerDetails.
        :type configuration_details: object

        :param status:
            The value to assign to the status property of this UpdateWorkerDetails.
            Allowed values for this property are: "ENABLED", "DISABLED"
        :type status: str

        :param priority:
            The value to assign to the priority property of this UpdateWorkerDetails.
        :type priority: int

        :param freeform_tags:
            The value to assign to the freeform_tags property of this UpdateWorkerDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this UpdateWorkerDetails.
        :type defined_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'configuration_details': 'object',
            'status': 'str',
            'priority': 'int',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'configuration_details': 'configurationDetails',
            'status': 'status',
            'priority': 'priority',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags'
        }

        self._configuration_details = None
        self._status = None
        self._priority = None
        self._freeform_tags = None
        self._defined_tags = None

    @property
    def configuration_details(self):
        """
        Gets the configuration_details of this UpdateWorkerDetails.
        Configuration details of the On-premise VP worker.


        :return: The configuration_details of this UpdateWorkerDetails.
        :rtype: object
        """
        return self._configuration_details

    @configuration_details.setter
    def configuration_details(self, configuration_details):
        """
        Sets the configuration_details of this UpdateWorkerDetails.
        Configuration details of the On-premise VP worker.


        :param configuration_details: The configuration_details of this UpdateWorkerDetails.
        :type: object
        """
        self._configuration_details = configuration_details

    @property
    def status(self):
        """
        Gets the status of this UpdateWorkerDetails.
        Enables or disables the On-premise VP worker.

        Allowed values for this property are: "ENABLED", "DISABLED"


        :return: The status of this UpdateWorkerDetails.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this UpdateWorkerDetails.
        Enables or disables the On-premise VP worker.


        :param status: The status of this UpdateWorkerDetails.
        :type: str
        """
        allowed_values = ["ENABLED", "DISABLED"]
        if not value_allowed_none_or_none_sentinel(status, allowed_values):
            raise ValueError(
                f"Invalid value for `status`, must be None or one of {allowed_values}"
            )
        self._status = status

    @property
    def priority(self):
        """
        Gets the priority of this UpdateWorkerDetails.
        Priority of the On-premise VP worker to schedule monitors.


        :return: The priority of this UpdateWorkerDetails.
        :rtype: int
        """
        return self._priority

    @priority.setter
    def priority(self, priority):
        """
        Sets the priority of this UpdateWorkerDetails.
        Priority of the On-premise VP worker to schedule monitors.


        :param priority: The priority of this UpdateWorkerDetails.
        :type: int
        """
        self._priority = priority

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this UpdateWorkerDetails.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :return: The freeform_tags of this UpdateWorkerDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this UpdateWorkerDetails.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :param freeform_tags: The freeform_tags of this UpdateWorkerDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this UpdateWorkerDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :return: The defined_tags of this UpdateWorkerDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this UpdateWorkerDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :param defined_tags: The defined_tags of this UpdateWorkerDetails.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
