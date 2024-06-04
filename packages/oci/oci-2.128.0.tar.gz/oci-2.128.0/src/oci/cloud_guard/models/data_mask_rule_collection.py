# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20200131


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class DataMaskRuleCollection(object):
    """
    Collection of data mask rules.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new DataMaskRuleCollection object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param items:
            The value to assign to the items property of this DataMaskRuleCollection.
        :type items: list[oci.cloud_guard.models.DataMaskRuleSummary]

        :param locks:
            The value to assign to the locks property of this DataMaskRuleCollection.
        :type locks: list[oci.cloud_guard.models.ResourceLock]

        """
        self.swagger_types = {
            'items': 'list[DataMaskRuleSummary]',
            'locks': 'list[ResourceLock]'
        }

        self.attribute_map = {
            'items': 'items',
            'locks': 'locks'
        }

        self._items = None
        self._locks = None

    @property
    def items(self):
        """
        **[Required]** Gets the items of this DataMaskRuleCollection.
        List of DataMaskRuleSummary resources


        :return: The items of this DataMaskRuleCollection.
        :rtype: list[oci.cloud_guard.models.DataMaskRuleSummary]
        """
        return self._items

    @items.setter
    def items(self, items):
        """
        Sets the items of this DataMaskRuleCollection.
        List of DataMaskRuleSummary resources


        :param items: The items of this DataMaskRuleCollection.
        :type: list[oci.cloud_guard.models.DataMaskRuleSummary]
        """
        self._items = items

    @property
    def locks(self):
        """
        Gets the locks of this DataMaskRuleCollection.
        Locks associated with this resource.


        :return: The locks of this DataMaskRuleCollection.
        :rtype: list[oci.cloud_guard.models.ResourceLock]
        """
        return self._locks

    @locks.setter
    def locks(self, locks):
        """
        Sets the locks of this DataMaskRuleCollection.
        Locks associated with this resource.


        :param locks: The locks of this DataMaskRuleCollection.
        :type: list[oci.cloud_guard.models.ResourceLock]
        """
        self._locks = locks

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
