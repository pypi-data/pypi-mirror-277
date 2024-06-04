# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20220901


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdatableAutonomousSettings(object):
    """
    Updatable settings for the Autonomous Linux service.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new UpdatableAutonomousSettings object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param is_data_collection_authorized:
            The value to assign to the is_data_collection_authorized property of this UpdatableAutonomousSettings.
        :type is_data_collection_authorized: bool

        """
        self.swagger_types = {
            'is_data_collection_authorized': 'bool'
        }

        self.attribute_map = {
            'is_data_collection_authorized': 'isDataCollectionAuthorized'
        }

        self._is_data_collection_authorized = None

    @property
    def is_data_collection_authorized(self):
        """
        Gets the is_data_collection_authorized of this UpdatableAutonomousSettings.
        Indicates whether Autonomous Linux will collect crash files.


        :return: The is_data_collection_authorized of this UpdatableAutonomousSettings.
        :rtype: bool
        """
        return self._is_data_collection_authorized

    @is_data_collection_authorized.setter
    def is_data_collection_authorized(self, is_data_collection_authorized):
        """
        Sets the is_data_collection_authorized of this UpdatableAutonomousSettings.
        Indicates whether Autonomous Linux will collect crash files.


        :param is_data_collection_authorized: The is_data_collection_authorized of this UpdatableAutonomousSettings.
        :type: bool
        """
        self._is_data_collection_authorized = is_data_collection_authorized

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
