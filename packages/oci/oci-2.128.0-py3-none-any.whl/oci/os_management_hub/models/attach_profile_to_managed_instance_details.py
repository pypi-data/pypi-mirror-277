# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20220901


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class AttachProfileToManagedInstanceDetails(object):
    """
    Provides the information used to set a profile for a managed instance.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new AttachProfileToManagedInstanceDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param profile_id:
            The value to assign to the profile_id property of this AttachProfileToManagedInstanceDetails.
        :type profile_id: str

        """
        self.swagger_types = {
            'profile_id': 'str'
        }

        self.attribute_map = {
            'profile_id': 'profileId'
        }

        self._profile_id = None

    @property
    def profile_id(self):
        """
        **[Required]** Gets the profile_id of this AttachProfileToManagedInstanceDetails.
        The profile `OCID`__ to attach to the managed instance.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The profile_id of this AttachProfileToManagedInstanceDetails.
        :rtype: str
        """
        return self._profile_id

    @profile_id.setter
    def profile_id(self, profile_id):
        """
        Sets the profile_id of this AttachProfileToManagedInstanceDetails.
        The profile `OCID`__ to attach to the managed instance.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param profile_id: The profile_id of this AttachProfileToManagedInstanceDetails.
        :type: str
        """
        self._profile_id = profile_id

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
