# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20200430

from .base_type import BaseType
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class MaterializedCompositeType(BaseType):
    """
    A `MaterializedCompositeType` represents a type that is composed of a list of sub-types, for example an `Address` type.   The sub-types can be simple `DataType` or other `CompositeType` objects. Typically, a `CompositeType` may represent an arbitrarily deep hierarchy of types.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new MaterializedCompositeType object with values from keyword arguments. The default value of the :py:attr:`~oci.data_integration.models.MaterializedCompositeType.model_type` attribute
        of this class is ``MATERIALIZED_COMPOSITE_TYPE`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param model_type:
            The value to assign to the model_type property of this MaterializedCompositeType.
            Allowed values for this property are: "DYNAMIC_TYPE", "STRUCTURED_TYPE", "DATA_TYPE", "JAVA_TYPE", "CONFIGURED_TYPE", "COMPOSITE_TYPE", "DERIVED_TYPE", "ARRAY_TYPE", "MAP_TYPE", "MATERIALIZED_COMPOSITE_TYPE"
        :type model_type: str

        :param key:
            The value to assign to the key property of this MaterializedCompositeType.
        :type key: str

        :param model_version:
            The value to assign to the model_version property of this MaterializedCompositeType.
        :type model_version: str

        :param parent_ref:
            The value to assign to the parent_ref property of this MaterializedCompositeType.
        :type parent_ref: oci.data_integration.models.ParentReference

        :param name:
            The value to assign to the name property of this MaterializedCompositeType.
        :type name: str

        :param object_status:
            The value to assign to the object_status property of this MaterializedCompositeType.
        :type object_status: int

        :param description:
            The value to assign to the description property of this MaterializedCompositeType.
        :type description: str

        :param elements:
            The value to assign to the elements property of this MaterializedCompositeType.
        :type elements: list[str]

        :param path_names:
            The value to assign to the path_names property of this MaterializedCompositeType.
        :type path_names: list[str]

        :param config_definition:
            The value to assign to the config_definition property of this MaterializedCompositeType.
        :type config_definition: oci.data_integration.models.ConfigDefinition

        """
        self.swagger_types = {
            'model_type': 'str',
            'key': 'str',
            'model_version': 'str',
            'parent_ref': 'ParentReference',
            'name': 'str',
            'object_status': 'int',
            'description': 'str',
            'elements': 'list[str]',
            'path_names': 'list[str]',
            'config_definition': 'ConfigDefinition'
        }

        self.attribute_map = {
            'model_type': 'modelType',
            'key': 'key',
            'model_version': 'modelVersion',
            'parent_ref': 'parentRef',
            'name': 'name',
            'object_status': 'objectStatus',
            'description': 'description',
            'elements': 'elements',
            'path_names': 'pathNames',
            'config_definition': 'configDefinition'
        }

        self._model_type = None
        self._key = None
        self._model_version = None
        self._parent_ref = None
        self._name = None
        self._object_status = None
        self._description = None
        self._elements = None
        self._path_names = None
        self._config_definition = None
        self._model_type = 'MATERIALIZED_COMPOSITE_TYPE'

    @property
    def elements(self):
        """
        Gets the elements of this MaterializedCompositeType.
        An array of elements.


        :return: The elements of this MaterializedCompositeType.
        :rtype: list[str]
        """
        return self._elements

    @elements.setter
    def elements(self, elements):
        """
        Sets the elements of this MaterializedCompositeType.
        An array of elements.


        :param elements: The elements of this MaterializedCompositeType.
        :type: list[str]
        """
        self._elements = elements

    @property
    def path_names(self):
        """
        Gets the path_names of this MaterializedCompositeType.
        An array of path names corresponding to the elements.  The path names are used when referring to the field in an expression.


        :return: The path_names of this MaterializedCompositeType.
        :rtype: list[str]
        """
        return self._path_names

    @path_names.setter
    def path_names(self, path_names):
        """
        Sets the path_names of this MaterializedCompositeType.
        An array of path names corresponding to the elements.  The path names are used when referring to the field in an expression.


        :param path_names: The path_names of this MaterializedCompositeType.
        :type: list[str]
        """
        self._path_names = path_names

    @property
    def config_definition(self):
        """
        Gets the config_definition of this MaterializedCompositeType.

        :return: The config_definition of this MaterializedCompositeType.
        :rtype: oci.data_integration.models.ConfigDefinition
        """
        return self._config_definition

    @config_definition.setter
    def config_definition(self, config_definition):
        """
        Sets the config_definition of this MaterializedCompositeType.

        :param config_definition: The config_definition of this MaterializedCompositeType.
        :type: oci.data_integration.models.ConfigDefinition
        """
        self._config_definition = config_definition

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
