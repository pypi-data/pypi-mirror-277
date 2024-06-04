# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20190531

from .level_type_details import LevelTypeDetails
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class NodeTypeLevelDetails(LevelTypeDetails):
    """
    Details of node type level used to trigger the creation of a new node backup configuration and node replacement configuration.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new NodeTypeLevelDetails object with values from keyword arguments. The default value of the :py:attr:`~oci.bds.models.NodeTypeLevelDetails.level_type` attribute
        of this class is ``NODE_TYPE_LEVEL`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param level_type:
            The value to assign to the level_type property of this NodeTypeLevelDetails.
            Allowed values for this property are: "NODE_LEVEL", "NODE_TYPE_LEVEL"
        :type level_type: str

        :param node_type:
            The value to assign to the node_type property of this NodeTypeLevelDetails.
        :type node_type: str

        """
        self.swagger_types = {
            'level_type': 'str',
            'node_type': 'str'
        }

        self.attribute_map = {
            'level_type': 'levelType',
            'node_type': 'nodeType'
        }

        self._level_type = None
        self._node_type = None
        self._level_type = 'NODE_TYPE_LEVEL'

    @property
    def node_type(self):
        """
        **[Required]** Gets the node_type of this NodeTypeLevelDetails.
        Type of the node or nodes of the node backup configuration or node replacement configuration which are going to be created.


        :return: The node_type of this NodeTypeLevelDetails.
        :rtype: str
        """
        return self._node_type

    @node_type.setter
    def node_type(self, node_type):
        """
        Sets the node_type of this NodeTypeLevelDetails.
        Type of the node or nodes of the node backup configuration or node replacement configuration which are going to be created.


        :param node_type: The node_type of this NodeTypeLevelDetails.
        :type: str
        """
        self._node_type = node_type

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
