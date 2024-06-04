# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20231130


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class DedicatedAiClusterCapacity(object):
    """
    The total capacity for a dedicated AI cluster.
    """

    #: A constant which can be used with the capacity_type property of a DedicatedAiClusterCapacity.
    #: This constant has a value of "HOSTING_CAPACITY"
    CAPACITY_TYPE_HOSTING_CAPACITY = "HOSTING_CAPACITY"

    def __init__(self, **kwargs):
        """
        Initializes a new DedicatedAiClusterCapacity object with values from keyword arguments. This class has the following subclasses and if you are using this class as input
        to a service operations then you should favor using a subclass over the base class:

        * :class:`~oci.generative_ai.models.DedicatedAiClusterHostingCapacity`

        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param capacity_type:
            The value to assign to the capacity_type property of this DedicatedAiClusterCapacity.
            Allowed values for this property are: "HOSTING_CAPACITY", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type capacity_type: str

        """
        self.swagger_types = {
            'capacity_type': 'str'
        }

        self.attribute_map = {
            'capacity_type': 'capacityType'
        }

        self._capacity_type = None

    @staticmethod
    def get_subtype(object_dictionary):
        """
        Given the hash representation of a subtype of this class,
        use the info in the hash to return the class of the subtype.
        """
        type = object_dictionary['capacityType']

        if type == 'HOSTING_CAPACITY':
            return 'DedicatedAiClusterHostingCapacity'
        else:
            return 'DedicatedAiClusterCapacity'

    @property
    def capacity_type(self):
        """
        **[Required]** Gets the capacity_type of this DedicatedAiClusterCapacity.
        The type of the dedicated AI cluster capacity.

        Allowed values for this property are: "HOSTING_CAPACITY", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The capacity_type of this DedicatedAiClusterCapacity.
        :rtype: str
        """
        return self._capacity_type

    @capacity_type.setter
    def capacity_type(self, capacity_type):
        """
        Sets the capacity_type of this DedicatedAiClusterCapacity.
        The type of the dedicated AI cluster capacity.


        :param capacity_type: The capacity_type of this DedicatedAiClusterCapacity.
        :type: str
        """
        allowed_values = ["HOSTING_CAPACITY"]
        if not value_allowed_none_or_none_sentinel(capacity_type, allowed_values):
            capacity_type = 'UNKNOWN_ENUM_VALUE'
        self._capacity_type = capacity_type

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
