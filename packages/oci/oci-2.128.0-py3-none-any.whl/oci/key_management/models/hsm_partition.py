# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: release


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class HsmPartition(object):
    """
    Dedicated KMS-HSM Partition Management
    """

    #: A constant which can be used with the lifecycle_state property of a HsmPartition.
    #: This constant has a value of "ACTIVE"
    LIFECYCLE_STATE_ACTIVE = "ACTIVE"

    #: A constant which can be used with the lifecycle_state property of a HsmPartition.
    #: This constant has a value of "INACTIVE"
    LIFECYCLE_STATE_INACTIVE = "INACTIVE"

    #: A constant which can be used with the lifecycle_state property of a HsmPartition.
    #: This constant has a value of "ACTIVATING"
    LIFECYCLE_STATE_ACTIVATING = "ACTIVATING"

    #: A constant which can be used with the lifecycle_state property of a HsmPartition.
    #: This constant has a value of "ACTIVATION_REQUIRED"
    LIFECYCLE_STATE_ACTIVATION_REQUIRED = "ACTIVATION_REQUIRED"

    def __init__(self, **kwargs):
        """
        Initializes a new HsmPartition object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this HsmPartition.
        :type id: str

        :param compartment_id:
            The value to assign to the compartment_id property of this HsmPartition.
        :type compartment_id: str

        :param port_information:
            The value to assign to the port_information property of this HsmPartition.
        :type port_information: list[oci.key_management.models.PortInformation]

        :param time_created:
            The value to assign to the time_created property of this HsmPartition.
        :type time_created: datetime

        :param time_updated:
            The value to assign to the time_updated property of this HsmPartition.
        :type time_updated: datetime

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this HsmPartition.
            Allowed values for this property are: "ACTIVE", "INACTIVE", "ACTIVATING", "ACTIVATION_REQUIRED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        """
        self.swagger_types = {
            'id': 'str',
            'compartment_id': 'str',
            'port_information': 'list[PortInformation]',
            'time_created': 'datetime',
            'time_updated': 'datetime',
            'lifecycle_state': 'str'
        }

        self.attribute_map = {
            'id': 'id',
            'compartment_id': 'compartmentId',
            'port_information': 'portInformation',
            'time_created': 'timeCreated',
            'time_updated': 'timeUpdated',
            'lifecycle_state': 'lifecycleState'
        }

        self._id = None
        self._compartment_id = None
        self._port_information = None
        self._time_created = None
        self._time_updated = None
        self._lifecycle_state = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this HsmPartition.
        The OCID of the HSM resource.


        :return: The id of this HsmPartition.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this HsmPartition.
        The OCID of the HSM resource.


        :param id: The id of this HsmPartition.
        :type: str
        """
        self._id = id

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this HsmPartition.
        The OCID of the compartment that contains a particular HSM resource.


        :return: The compartment_id of this HsmPartition.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this HsmPartition.
        The OCID of the compartment that contains a particular HSM resource.


        :param compartment_id: The compartment_id of this HsmPartition.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def port_information(self):
        """
        **[Required]** Gets the port_information of this HsmPartition.
        Details of PortNumber and PortType.


        :return: The port_information of this HsmPartition.
        :rtype: list[oci.key_management.models.PortInformation]
        """
        return self._port_information

    @port_information.setter
    def port_information(self, port_information):
        """
        Sets the port_information of this HsmPartition.
        Details of PortNumber and PortType.


        :param port_information: The port_information of this HsmPartition.
        :type: list[oci.key_management.models.PortInformation]
        """
        self._port_information = port_information

    @property
    def time_created(self):
        """
        **[Required]** Gets the time_created of this HsmPartition.
        The date and time a HSMPartition was created, expressed in `RFC 3339`__ timestamp format.

        Example: `2018-04-03T21:10:29.600Z`

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_created of this HsmPartition.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this HsmPartition.
        The date and time a HSMPartition was created, expressed in `RFC 3339`__ timestamp format.

        Example: `2018-04-03T21:10:29.600Z`

        __ https://tools.ietf.org/html/rfc3339


        :param time_created: The time_created of this HsmPartition.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def time_updated(self):
        """
        **[Required]** Gets the time_updated of this HsmPartition.
        The date and time a HSMPartition was updated, expressed in `RFC 3339`__ timestamp format.

        Example: `2018-04-03T21:10:29.600Z`

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_updated of this HsmPartition.
        :rtype: datetime
        """
        return self._time_updated

    @time_updated.setter
    def time_updated(self, time_updated):
        """
        Sets the time_updated of this HsmPartition.
        The date and time a HSMPartition was updated, expressed in `RFC 3339`__ timestamp format.

        Example: `2018-04-03T21:10:29.600Z`

        __ https://tools.ietf.org/html/rfc3339


        :param time_updated: The time_updated of this HsmPartition.
        :type: datetime
        """
        self._time_updated = time_updated

    @property
    def lifecycle_state(self):
        """
        **[Required]** Gets the lifecycle_state of this HsmPartition.
        The HSMPartition's current lifecycle state.

        Allowed values for this property are: "ACTIVE", "INACTIVE", "ACTIVATING", "ACTIVATION_REQUIRED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this HsmPartition.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this HsmPartition.
        The HSMPartition's current lifecycle state.


        :param lifecycle_state: The lifecycle_state of this HsmPartition.
        :type: str
        """
        allowed_values = ["ACTIVE", "INACTIVE", "ACTIVATING", "ACTIVATION_REQUIRED"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
