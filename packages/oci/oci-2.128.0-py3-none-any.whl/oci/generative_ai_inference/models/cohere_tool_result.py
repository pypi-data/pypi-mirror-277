# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20231130


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CohereToolResult(object):
    """
    The result from invoking tools recommended by the model in the previous chat turn.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CohereToolResult object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param call:
            The value to assign to the call property of this CohereToolResult.
        :type call: oci.generative_ai_inference.models.CohereToolCall

        :param outputs:
            The value to assign to the outputs property of this CohereToolResult.
        :type outputs: list[object]

        """
        self.swagger_types = {
            'call': 'CohereToolCall',
            'outputs': 'list[object]'
        }

        self.attribute_map = {
            'call': 'call',
            'outputs': 'outputs'
        }

        self._call = None
        self._outputs = None

    @property
    def call(self):
        """
        **[Required]** Gets the call of this CohereToolResult.

        :return: The call of this CohereToolResult.
        :rtype: oci.generative_ai_inference.models.CohereToolCall
        """
        return self._call

    @call.setter
    def call(self, call):
        """
        Sets the call of this CohereToolResult.

        :param call: The call of this CohereToolResult.
        :type: oci.generative_ai_inference.models.CohereToolCall
        """
        self._call = call

    @property
    def outputs(self):
        """
        **[Required]** Gets the outputs of this CohereToolResult.
        An array of objects returned by tool.


        :return: The outputs of this CohereToolResult.
        :rtype: list[object]
        """
        return self._outputs

    @outputs.setter
    def outputs(self, outputs):
        """
        Sets the outputs of this CohereToolResult.
        An array of objects returned by tool.


        :param outputs: The outputs of this CohereToolResult.
        :type: list[object]
        """
        self._outputs = outputs

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
