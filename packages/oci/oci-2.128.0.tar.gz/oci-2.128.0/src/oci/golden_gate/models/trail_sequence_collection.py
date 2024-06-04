# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20200407


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class TrailSequenceCollection(object):
    """
    A list of TrailSequences.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new TrailSequenceCollection object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param time_last_fetched:
            The value to assign to the time_last_fetched property of this TrailSequenceCollection.
        :type time_last_fetched: datetime

        :param items:
            The value to assign to the items property of this TrailSequenceCollection.
        :type items: list[oci.golden_gate.models.TrailSequenceSummary]

        """
        self.swagger_types = {
            'time_last_fetched': 'datetime',
            'items': 'list[TrailSequenceSummary]'
        }

        self.attribute_map = {
            'time_last_fetched': 'timeLastFetched',
            'items': 'items'
        }

        self._time_last_fetched = None
        self._items = None

    @property
    def time_last_fetched(self):
        """
        **[Required]** Gets the time_last_fetched of this TrailSequenceCollection.
        The time the data was last fetched from the deployment. The format is defined by
        `RFC3339`__, such as `2016-08-25T21:10:29.600Z`.

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_last_fetched of this TrailSequenceCollection.
        :rtype: datetime
        """
        return self._time_last_fetched

    @time_last_fetched.setter
    def time_last_fetched(self, time_last_fetched):
        """
        Sets the time_last_fetched of this TrailSequenceCollection.
        The time the data was last fetched from the deployment. The format is defined by
        `RFC3339`__, such as `2016-08-25T21:10:29.600Z`.

        __ https://tools.ietf.org/html/rfc3339


        :param time_last_fetched: The time_last_fetched of this TrailSequenceCollection.
        :type: datetime
        """
        self._time_last_fetched = time_last_fetched

    @property
    def items(self):
        """
        **[Required]** Gets the items of this TrailSequenceCollection.
        An array of TrailSequences.


        :return: The items of this TrailSequenceCollection.
        :rtype: list[oci.golden_gate.models.TrailSequenceSummary]
        """
        return self._items

    @items.setter
    def items(self, items):
        """
        Sets the items of this TrailSequenceCollection.
        An array of TrailSequences.


        :param items: The items of this TrailSequenceCollection.
        :type: list[oci.golden_gate.models.TrailSequenceSummary]
        """
        self._items = items

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
