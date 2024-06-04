# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20220901


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ModuleStreamSummary(object):
    """
    Provides the summary information for a module stream contained within a software source.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ModuleStreamSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param name:
            The value to assign to the name property of this ModuleStreamSummary.
        :type name: str

        :param module_name:
            The value to assign to the module_name property of this ModuleStreamSummary.
        :type module_name: str

        :param profiles:
            The value to assign to the profiles property of this ModuleStreamSummary.
        :type profiles: list[str]

        :param is_latest:
            The value to assign to the is_latest property of this ModuleStreamSummary.
        :type is_latest: bool

        :param software_source_id:
            The value to assign to the software_source_id property of this ModuleStreamSummary.
        :type software_source_id: str

        """
        self.swagger_types = {
            'name': 'str',
            'module_name': 'str',
            'profiles': 'list[str]',
            'is_latest': 'bool',
            'software_source_id': 'str'
        }

        self.attribute_map = {
            'name': 'name',
            'module_name': 'moduleName',
            'profiles': 'profiles',
            'is_latest': 'isLatest',
            'software_source_id': 'softwareSourceId'
        }

        self._name = None
        self._module_name = None
        self._profiles = None
        self._is_latest = None
        self._software_source_id = None

    @property
    def name(self):
        """
        **[Required]** Gets the name of this ModuleStreamSummary.
        The name of the stream.


        :return: The name of this ModuleStreamSummary.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this ModuleStreamSummary.
        The name of the stream.


        :param name: The name of this ModuleStreamSummary.
        :type: str
        """
        self._name = name

    @property
    def module_name(self):
        """
        **[Required]** Gets the module_name of this ModuleStreamSummary.
        The name of the module that contains the stream.


        :return: The module_name of this ModuleStreamSummary.
        :rtype: str
        """
        return self._module_name

    @module_name.setter
    def module_name(self, module_name):
        """
        Sets the module_name of this ModuleStreamSummary.
        The name of the module that contains the stream.


        :param module_name: The module_name of this ModuleStreamSummary.
        :type: str
        """
        self._module_name = module_name

    @property
    def profiles(self):
        """
        **[Required]** Gets the profiles of this ModuleStreamSummary.
        List of profiles in the stream.


        :return: The profiles of this ModuleStreamSummary.
        :rtype: list[str]
        """
        return self._profiles

    @profiles.setter
    def profiles(self, profiles):
        """
        Sets the profiles of this ModuleStreamSummary.
        List of profiles in the stream.


        :param profiles: The profiles of this ModuleStreamSummary.
        :type: list[str]
        """
        self._profiles = profiles

    @property
    def is_latest(self):
        """
        Gets the is_latest of this ModuleStreamSummary.
        Indicates whether this module stream is the latest.


        :return: The is_latest of this ModuleStreamSummary.
        :rtype: bool
        """
        return self._is_latest

    @is_latest.setter
    def is_latest(self, is_latest):
        """
        Sets the is_latest of this ModuleStreamSummary.
        Indicates whether this module stream is the latest.


        :param is_latest: The is_latest of this ModuleStreamSummary.
        :type: bool
        """
        self._is_latest = is_latest

    @property
    def software_source_id(self):
        """
        Gets the software_source_id of this ModuleStreamSummary.
        The `OCID`__ of the software source that contains the the module stream.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The software_source_id of this ModuleStreamSummary.
        :rtype: str
        """
        return self._software_source_id

    @software_source_id.setter
    def software_source_id(self, software_source_id):
        """
        Sets the software_source_id of this ModuleStreamSummary.
        The `OCID`__ of the software source that contains the the module stream.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param software_source_id: The software_source_id of this ModuleStreamSummary.
        :type: str
        """
        self._software_source_id = software_source_id

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
