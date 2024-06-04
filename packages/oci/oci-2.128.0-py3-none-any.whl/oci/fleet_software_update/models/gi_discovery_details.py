# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20220528

from .discovery_details import DiscoveryDetails
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class GiDiscoveryDetails(DiscoveryDetails):
    """
    Details to create a 'GI' type Exadata Fleet Update Discovery.
    """

    #: A constant which can be used with the source_major_version property of a GiDiscoveryDetails.
    #: This constant has a value of "GI_18"
    SOURCE_MAJOR_VERSION_GI_18 = "GI_18"

    #: A constant which can be used with the source_major_version property of a GiDiscoveryDetails.
    #: This constant has a value of "GI_19"
    SOURCE_MAJOR_VERSION_GI_19 = "GI_19"

    def __init__(self, **kwargs):
        """
        Initializes a new GiDiscoveryDetails object with values from keyword arguments. The default value of the :py:attr:`~oci.fleet_software_update.models.GiDiscoveryDetails.type` attribute
        of this class is ``GI`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param type:
            The value to assign to the type property of this GiDiscoveryDetails.
            Allowed values for this property are: "DB", "GI", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type type: str

        :param service_type:
            The value to assign to the service_type property of this GiDiscoveryDetails.
            Allowed values for this property are: "EXACS", "EXACC", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type service_type: str

        :param source_major_version:
            The value to assign to the source_major_version property of this GiDiscoveryDetails.
            Allowed values for this property are: "GI_18", "GI_19", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type source_major_version: str

        :param criteria:
            The value to assign to the criteria property of this GiDiscoveryDetails.
        :type criteria: oci.fleet_software_update.models.GiFleetDiscoveryDetails

        """
        self.swagger_types = {
            'type': 'str',
            'service_type': 'str',
            'source_major_version': 'str',
            'criteria': 'GiFleetDiscoveryDetails'
        }

        self.attribute_map = {
            'type': 'type',
            'service_type': 'serviceType',
            'source_major_version': 'sourceMajorVersion',
            'criteria': 'criteria'
        }

        self._type = None
        self._service_type = None
        self._source_major_version = None
        self._criteria = None
        self._type = 'GI'

    @property
    def source_major_version(self):
        """
        **[Required]** Gets the source_major_version of this GiDiscoveryDetails.
        Grid Infrastructure Major Version of targets to be included in the Exadata Fleet Update Discovery results.
        Only GI targets that match the version specified in this value would be added to the Exadata Fleet Update Discovery results.

        Allowed values for this property are: "GI_18", "GI_19", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The source_major_version of this GiDiscoveryDetails.
        :rtype: str
        """
        return self._source_major_version

    @source_major_version.setter
    def source_major_version(self, source_major_version):
        """
        Sets the source_major_version of this GiDiscoveryDetails.
        Grid Infrastructure Major Version of targets to be included in the Exadata Fleet Update Discovery results.
        Only GI targets that match the version specified in this value would be added to the Exadata Fleet Update Discovery results.


        :param source_major_version: The source_major_version of this GiDiscoveryDetails.
        :type: str
        """
        allowed_values = ["GI_18", "GI_19"]
        if not value_allowed_none_or_none_sentinel(source_major_version, allowed_values):
            source_major_version = 'UNKNOWN_ENUM_VALUE'
        self._source_major_version = source_major_version

    @property
    def criteria(self):
        """
        **[Required]** Gets the criteria of this GiDiscoveryDetails.

        :return: The criteria of this GiDiscoveryDetails.
        :rtype: oci.fleet_software_update.models.GiFleetDiscoveryDetails
        """
        return self._criteria

    @criteria.setter
    def criteria(self, criteria):
        """
        Sets the criteria of this GiDiscoveryDetails.

        :param criteria: The criteria of this GiDiscoveryDetails.
        :type: oci.fleet_software_update.models.GiFleetDiscoveryDetails
        """
        self._criteria = criteria

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
