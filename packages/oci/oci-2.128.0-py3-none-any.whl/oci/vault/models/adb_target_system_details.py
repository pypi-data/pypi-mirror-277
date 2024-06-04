# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20180608

from .target_system_details import TargetSystemDetails
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class AdbTargetSystemDetails(TargetSystemDetails):
    """
    Target System type and id for an autonomous database target system
    """

    def __init__(self, **kwargs):
        """
        Initializes a new AdbTargetSystemDetails object with values from keyword arguments. The default value of the :py:attr:`~oci.vault.models.AdbTargetSystemDetails.target_system_type` attribute
        of this class is ``ADB`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param target_system_type:
            The value to assign to the target_system_type property of this AdbTargetSystemDetails.
            Allowed values for this property are: "ADB", "FUNCTION"
        :type target_system_type: str

        :param adb_id:
            The value to assign to the adb_id property of this AdbTargetSystemDetails.
        :type adb_id: str

        """
        self.swagger_types = {
            'target_system_type': 'str',
            'adb_id': 'str'
        }

        self.attribute_map = {
            'target_system_type': 'targetSystemType',
            'adb_id': 'adbId'
        }

        self._target_system_type = None
        self._adb_id = None
        self._target_system_type = 'ADB'

    @property
    def adb_id(self):
        """
        **[Required]** Gets the adb_id of this AdbTargetSystemDetails.
        The unique identifier (OCID) for the autonomous database that Vault Secret connects to.


        :return: The adb_id of this AdbTargetSystemDetails.
        :rtype: str
        """
        return self._adb_id

    @adb_id.setter
    def adb_id(self, adb_id):
        """
        Sets the adb_id of this AdbTargetSystemDetails.
        The unique identifier (OCID) for the autonomous database that Vault Secret connects to.


        :param adb_id: The adb_id of this AdbTargetSystemDetails.
        :type: str
        """
        self._adb_id = adb_id

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
