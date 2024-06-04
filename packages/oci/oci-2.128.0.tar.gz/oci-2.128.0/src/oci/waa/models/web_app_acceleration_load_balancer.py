# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20211230

from .web_app_acceleration import WebAppAcceleration
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class WebAppAccelerationLoadBalancer(WebAppAcceleration):
    """
    WebAppAcceleration to a LoadBalancer resource.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new WebAppAccelerationLoadBalancer object with values from keyword arguments. The default value of the :py:attr:`~oci.waa.models.WebAppAccelerationLoadBalancer.backend_type` attribute
        of this class is ``LOAD_BALANCER`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this WebAppAccelerationLoadBalancer.
        :type id: str

        :param display_name:
            The value to assign to the display_name property of this WebAppAccelerationLoadBalancer.
        :type display_name: str

        :param compartment_id:
            The value to assign to the compartment_id property of this WebAppAccelerationLoadBalancer.
        :type compartment_id: str

        :param backend_type:
            The value to assign to the backend_type property of this WebAppAccelerationLoadBalancer.
            Allowed values for this property are: "LOAD_BALANCER"
        :type backend_type: str

        :param web_app_acceleration_policy_id:
            The value to assign to the web_app_acceleration_policy_id property of this WebAppAccelerationLoadBalancer.
        :type web_app_acceleration_policy_id: str

        :param time_created:
            The value to assign to the time_created property of this WebAppAccelerationLoadBalancer.
        :type time_created: datetime

        :param time_updated:
            The value to assign to the time_updated property of this WebAppAccelerationLoadBalancer.
        :type time_updated: datetime

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this WebAppAccelerationLoadBalancer.
            Allowed values for this property are: "CREATING", "UPDATING", "ACTIVE", "DELETING", "DELETED", "FAILED"
        :type lifecycle_state: str

        :param lifecycle_details:
            The value to assign to the lifecycle_details property of this WebAppAccelerationLoadBalancer.
        :type lifecycle_details: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this WebAppAccelerationLoadBalancer.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this WebAppAccelerationLoadBalancer.
        :type defined_tags: dict(str, dict(str, object))

        :param system_tags:
            The value to assign to the system_tags property of this WebAppAccelerationLoadBalancer.
        :type system_tags: dict(str, dict(str, object))

        :param load_balancer_id:
            The value to assign to the load_balancer_id property of this WebAppAccelerationLoadBalancer.
        :type load_balancer_id: str

        """
        self.swagger_types = {
            'id': 'str',
            'display_name': 'str',
            'compartment_id': 'str',
            'backend_type': 'str',
            'web_app_acceleration_policy_id': 'str',
            'time_created': 'datetime',
            'time_updated': 'datetime',
            'lifecycle_state': 'str',
            'lifecycle_details': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'system_tags': 'dict(str, dict(str, object))',
            'load_balancer_id': 'str'
        }

        self.attribute_map = {
            'id': 'id',
            'display_name': 'displayName',
            'compartment_id': 'compartmentId',
            'backend_type': 'backendType',
            'web_app_acceleration_policy_id': 'webAppAccelerationPolicyId',
            'time_created': 'timeCreated',
            'time_updated': 'timeUpdated',
            'lifecycle_state': 'lifecycleState',
            'lifecycle_details': 'lifecycleDetails',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'system_tags': 'systemTags',
            'load_balancer_id': 'loadBalancerId'
        }

        self._id = None
        self._display_name = None
        self._compartment_id = None
        self._backend_type = None
        self._web_app_acceleration_policy_id = None
        self._time_created = None
        self._time_updated = None
        self._lifecycle_state = None
        self._lifecycle_details = None
        self._freeform_tags = None
        self._defined_tags = None
        self._system_tags = None
        self._load_balancer_id = None
        self._backend_type = 'LOAD_BALANCER'

    @property
    def load_balancer_id(self):
        """
        **[Required]** Gets the load_balancer_id of this WebAppAccelerationLoadBalancer.
        LoadBalancer `OCID`__ to which the WebAppAccelerationPolicy is attached to.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The load_balancer_id of this WebAppAccelerationLoadBalancer.
        :rtype: str
        """
        return self._load_balancer_id

    @load_balancer_id.setter
    def load_balancer_id(self, load_balancer_id):
        """
        Sets the load_balancer_id of this WebAppAccelerationLoadBalancer.
        LoadBalancer `OCID`__ to which the WebAppAccelerationPolicy is attached to.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param load_balancer_id: The load_balancer_id of this WebAppAccelerationLoadBalancer.
        :type: str
        """
        self._load_balancer_id = load_balancer_id

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
