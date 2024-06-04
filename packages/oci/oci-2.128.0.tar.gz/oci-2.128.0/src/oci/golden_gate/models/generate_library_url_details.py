# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20200407


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class GenerateLibraryUrlDetails(object):
    """
    The information about generating the library URL.
    """

    #: A constant which can be used with the library_type property of a GenerateLibraryUrlDetails.
    #: This constant has a value of "LOG_READER_COMPONENT"
    LIBRARY_TYPE_LOG_READER_COMPONENT = "LOG_READER_COMPONENT"

    def __init__(self, **kwargs):
        """
        Initializes a new GenerateLibraryUrlDetails object with values from keyword arguments. This class has the following subclasses and if you are using this class as input
        to a service operations then you should favor using a subclass over the base class:

        * :class:`~oci.golden_gate.models.GenerateLogReaderComponentLibraryUrlDetails`

        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param library_type:
            The value to assign to the library_type property of this GenerateLibraryUrlDetails.
            Allowed values for this property are: "LOG_READER_COMPONENT"
        :type library_type: str

        """
        self.swagger_types = {
            'library_type': 'str'
        }

        self.attribute_map = {
            'library_type': 'libraryType'
        }

        self._library_type = None

    @staticmethod
    def get_subtype(object_dictionary):
        """
        Given the hash representation of a subtype of this class,
        use the info in the hash to return the class of the subtype.
        """
        type = object_dictionary['libraryType']

        if type == 'LOG_READER_COMPONENT':
            return 'GenerateLogReaderComponentLibraryUrlDetails'
        else:
            return 'GenerateLibraryUrlDetails'

    @property
    def library_type(self):
        """
        **[Required]** Gets the library_type of this GenerateLibraryUrlDetails.
        The type of the library URL generation.

        Allowed values for this property are: "LOG_READER_COMPONENT"


        :return: The library_type of this GenerateLibraryUrlDetails.
        :rtype: str
        """
        return self._library_type

    @library_type.setter
    def library_type(self, library_type):
        """
        Sets the library_type of this GenerateLibraryUrlDetails.
        The type of the library URL generation.


        :param library_type: The library_type of this GenerateLibraryUrlDetails.
        :type: str
        """
        allowed_values = ["LOG_READER_COMPONENT"]
        if not value_allowed_none_or_none_sentinel(library_type, allowed_values):
            raise ValueError(
                f"Invalid value for `library_type`, must be None or one of {allowed_values}"
            )
        self._library_type = library_type

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
