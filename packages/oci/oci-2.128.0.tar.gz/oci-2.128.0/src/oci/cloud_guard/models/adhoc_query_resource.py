# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20200131


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class AdhocQueryResource(object):
    """
    Details about the adhoc resources for which query needs to be run.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new AdhocQueryResource object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param region:
            The value to assign to the region property of this AdhocQueryResource.
        :type region: str

        :param resource_ids:
            The value to assign to the resource_ids property of this AdhocQueryResource.
        :type resource_ids: list[str]

        :param resource_type:
            The value to assign to the resource_type property of this AdhocQueryResource.
        :type resource_type: str

        """
        self.swagger_types = {
            'region': 'str',
            'resource_ids': 'list[str]',
            'resource_type': 'str'
        }

        self.attribute_map = {
            'region': 'region',
            'resource_ids': 'resourceIds',
            'resource_type': 'resourceType'
        }

        self._region = None
        self._resource_ids = None
        self._resource_type = None

    @property
    def region(self):
        """
        Gets the region of this AdhocQueryResource.
        Region in which adhoc query needs to be run


        :return: The region of this AdhocQueryResource.
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        """
        Sets the region of this AdhocQueryResource.
        Region in which adhoc query needs to be run


        :param region: The region of this AdhocQueryResource.
        :type: str
        """
        self._region = region

    @property
    def resource_ids(self):
        """
        Gets the resource_ids of this AdhocQueryResource.
        List of OCIDs on which query needs to be run


        :return: The resource_ids of this AdhocQueryResource.
        :rtype: list[str]
        """
        return self._resource_ids

    @resource_ids.setter
    def resource_ids(self, resource_ids):
        """
        Sets the resource_ids of this AdhocQueryResource.
        List of OCIDs on which query needs to be run


        :param resource_ids: The resource_ids of this AdhocQueryResource.
        :type: list[str]
        """
        self._resource_ids = resource_ids

    @property
    def resource_type(self):
        """
        Gets the resource_type of this AdhocQueryResource.
        Type of resource


        :return: The resource_type of this AdhocQueryResource.
        :rtype: str
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        """
        Sets the resource_type of this AdhocQueryResource.
        Type of resource


        :param resource_type: The resource_type of this AdhocQueryResource.
        :type: str
        """
        self._resource_type = resource_type

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
