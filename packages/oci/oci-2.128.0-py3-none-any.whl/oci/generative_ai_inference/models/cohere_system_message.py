# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20231130

from .cohere_message import CohereMessage
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CohereSystemMessage(CohereMessage):
    """
    A message that represents a single chat dialog as SYSTEM role.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CohereSystemMessage object with values from keyword arguments. The default value of the :py:attr:`~oci.generative_ai_inference.models.CohereSystemMessage.role` attribute
        of this class is ``SYSTEM`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param role:
            The value to assign to the role property of this CohereSystemMessage.
            Allowed values for this property are: "CHATBOT", "USER", "SYSTEM", "TOOL"
        :type role: str

        :param message:
            The value to assign to the message property of this CohereSystemMessage.
        :type message: str

        """
        self.swagger_types = {
            'role': 'str',
            'message': 'str'
        }

        self.attribute_map = {
            'role': 'role',
            'message': 'message'
        }

        self._role = None
        self._message = None
        self._role = 'SYSTEM'

    @property
    def message(self):
        """
        **[Required]** Gets the message of this CohereSystemMessage.
        Contents of the chat message.


        :return: The message of this CohereSystemMessage.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """
        Sets the message of this CohereSystemMessage.
        Contents of the chat message.


        :param message: The message of this CohereSystemMessage.
        :type: str
        """
        self._message = message

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
