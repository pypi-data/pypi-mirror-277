# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20231130

from .message import Message
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class SystemMessage(Message):
    """
    Represents a single instance of system message.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new SystemMessage object with values from keyword arguments. The default value of the :py:attr:`~oci.generative_ai_inference.models.SystemMessage.role` attribute
        of this class is ``SYSTEM`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param role:
            The value to assign to the role property of this SystemMessage.
            Allowed values for this property are: "SYSTEM", "USER", "ASSISTANT"
        :type role: str

        :param content:
            The value to assign to the content property of this SystemMessage.
        :type content: list[oci.generative_ai_inference.models.ChatContent]

        :param name:
            The value to assign to the name property of this SystemMessage.
        :type name: str

        """
        self.swagger_types = {
            'role': 'str',
            'content': 'list[ChatContent]',
            'name': 'str'
        }

        self.attribute_map = {
            'role': 'role',
            'content': 'content',
            'name': 'name'
        }

        self._role = None
        self._content = None
        self._name = None
        self._role = 'SYSTEM'

    @property
    def name(self):
        """
        Gets the name of this SystemMessage.
        An optional name for the participant. Provides the model information to differentiate between participants of the same role.


        :return: The name of this SystemMessage.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this SystemMessage.
        An optional name for the participant. Provides the model information to differentiate between participants of the same role.


        :param name: The name of this SystemMessage.
        :type: str
        """
        self._name = name

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
