# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20160918

from .routing_action import RoutingAction
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class NoRouteRoutingAction(RoutingAction):
    """
    Defines the routing actions taken on traffic when no route is found.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new NoRouteRoutingAction object with values from keyword arguments. The default value of the :py:attr:`~oci.vn_monitoring.models.NoRouteRoutingAction.action` attribute
        of this class is ``NO_ROUTE`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param action:
            The value to assign to the action property of this NoRouteRoutingAction.
            Allowed values for this property are: "FORWARDED", "NO_ROUTE", "INDETERMINATE"
        :type action: str

        :param action_type:
            The value to assign to the action_type property of this NoRouteRoutingAction.
            Allowed values for this property are: "EXPLICIT", "IMPLICIT", "NOT_SUPPORTED"
        :type action_type: str

        :param no_route_routing_action_details:
            The value to assign to the no_route_routing_action_details property of this NoRouteRoutingAction.
        :type no_route_routing_action_details: oci.vn_monitoring.models.NoRouteRoutingActionDetails

        """
        self.swagger_types = {
            'action': 'str',
            'action_type': 'str',
            'no_route_routing_action_details': 'NoRouteRoutingActionDetails'
        }

        self.attribute_map = {
            'action': 'action',
            'action_type': 'actionType',
            'no_route_routing_action_details': 'noRouteRoutingActionDetails'
        }

        self._action = None
        self._action_type = None
        self._no_route_routing_action_details = None
        self._action = 'NO_ROUTE'

    @property
    def no_route_routing_action_details(self):
        """
        Gets the no_route_routing_action_details of this NoRouteRoutingAction.

        :return: The no_route_routing_action_details of this NoRouteRoutingAction.
        :rtype: oci.vn_monitoring.models.NoRouteRoutingActionDetails
        """
        return self._no_route_routing_action_details

    @no_route_routing_action_details.setter
    def no_route_routing_action_details(self, no_route_routing_action_details):
        """
        Sets the no_route_routing_action_details of this NoRouteRoutingAction.

        :param no_route_routing_action_details: The no_route_routing_action_details of this NoRouteRoutingAction.
        :type: oci.vn_monitoring.models.NoRouteRoutingActionDetails
        """
        self._no_route_routing_action_details = no_route_routing_action_details

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
