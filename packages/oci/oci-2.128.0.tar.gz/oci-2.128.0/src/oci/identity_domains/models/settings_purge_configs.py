# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: v1


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class SettingsPurgeConfigs(object):
    """
    Purge Configs for different Resource Types
    """

    def __init__(self, **kwargs):
        """
        Initializes a new SettingsPurgeConfigs object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param resource_name:
            The value to assign to the resource_name property of this SettingsPurgeConfigs.
        :type resource_name: str

        :param retention_period:
            The value to assign to the retention_period property of this SettingsPurgeConfigs.
        :type retention_period: int

        """
        self.swagger_types = {
            'resource_name': 'str',
            'retention_period': 'int'
        }

        self.attribute_map = {
            'resource_name': 'resourceName',
            'retention_period': 'retentionPeriod'
        }

        self._resource_name = None
        self._retention_period = None

    @property
    def resource_name(self):
        """
        **[Required]** Gets the resource_name of this SettingsPurgeConfigs.
        Resource Name

        **Deprecated Since: 19.1.6**

        **SCIM++ Properties:**
         - multiValued: false
         - mutability: readWrite
         - required: true
         - returned: default
         - type: string


        :return: The resource_name of this SettingsPurgeConfigs.
        :rtype: str
        """
        return self._resource_name

    @resource_name.setter
    def resource_name(self, resource_name):
        """
        Sets the resource_name of this SettingsPurgeConfigs.
        Resource Name

        **Deprecated Since: 19.1.6**

        **SCIM++ Properties:**
         - multiValued: false
         - mutability: readWrite
         - required: true
         - returned: default
         - type: string


        :param resource_name: The resource_name of this SettingsPurgeConfigs.
        :type: str
        """
        self._resource_name = resource_name

    @property
    def retention_period(self):
        """
        **[Required]** Gets the retention_period of this SettingsPurgeConfigs.
        Retention Period

        **Deprecated Since: 19.1.6**

        **SCIM++ Properties:**
         - multiValued: false
         - mutability: readWrite
         - required: true
         - returned: default
         - type: integer


        :return: The retention_period of this SettingsPurgeConfigs.
        :rtype: int
        """
        return self._retention_period

    @retention_period.setter
    def retention_period(self, retention_period):
        """
        Sets the retention_period of this SettingsPurgeConfigs.
        Retention Period

        **Deprecated Since: 19.1.6**

        **SCIM++ Properties:**
         - multiValued: false
         - mutability: readWrite
         - required: true
         - returned: default
         - type: integer


        :param retention_period: The retention_period of this SettingsPurgeConfigs.
        :type: int
        """
        self._retention_period = retention_period

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
