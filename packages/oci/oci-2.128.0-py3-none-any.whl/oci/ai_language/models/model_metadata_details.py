# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20221001


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ModelMetadataDetails(object):
    """
    training model details
    For this release only one model is allowed to be input here.
    One of the three modelType, ModelId, endpointId should be given other wise error will be thrown from API
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ModelMetadataDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param model_type:
            The value to assign to the model_type property of this ModelMetadataDetails.
        :type model_type: str

        :param model_id:
            The value to assign to the model_id property of this ModelMetadataDetails.
        :type model_id: str

        :param endpoint_id:
            The value to assign to the endpoint_id property of this ModelMetadataDetails.
        :type endpoint_id: str

        :param language_code:
            The value to assign to the language_code property of this ModelMetadataDetails.
        :type language_code: str

        :param configuration:
            The value to assign to the configuration property of this ModelMetadataDetails.
        :type configuration: dict(str, ConfigurationDetails)

        """
        self.swagger_types = {
            'model_type': 'str',
            'model_id': 'str',
            'endpoint_id': 'str',
            'language_code': 'str',
            'configuration': 'dict(str, ConfigurationDetails)'
        }

        self.attribute_map = {
            'model_type': 'modelType',
            'model_id': 'modelId',
            'endpoint_id': 'endpointId',
            'language_code': 'languageCode',
            'configuration': 'configuration'
        }

        self._model_type = None
        self._model_id = None
        self._endpoint_id = None
        self._language_code = None
        self._configuration = None

    @property
    def model_type(self):
        """
        Gets the model_type of this ModelMetadataDetails.
        model type to used for inference allowed values are
        - LANGUAGE_SENTIMENT_ANALYSIS
        - LANGUAGE_DETECTION
        - TEXT_CLASSIFICATION
        - NAMED_ENTITY_RECOGNITION
        - KEY_PHRASE_EXTRACTION
        - LANGUAGE_PII_ENTITIES
        - LANGUAGE_TRANSLATION


        :return: The model_type of this ModelMetadataDetails.
        :rtype: str
        """
        return self._model_type

    @model_type.setter
    def model_type(self, model_type):
        """
        Sets the model_type of this ModelMetadataDetails.
        model type to used for inference allowed values are
        - LANGUAGE_SENTIMENT_ANALYSIS
        - LANGUAGE_DETECTION
        - TEXT_CLASSIFICATION
        - NAMED_ENTITY_RECOGNITION
        - KEY_PHRASE_EXTRACTION
        - LANGUAGE_PII_ENTITIES
        - LANGUAGE_TRANSLATION


        :param model_type: The model_type of this ModelMetadataDetails.
        :type: str
        """
        self._model_type = model_type

    @property
    def model_id(self):
        """
        Gets the model_id of this ModelMetadataDetails.
        Unique identifier model OCID that should be used for inference


        :return: The model_id of this ModelMetadataDetails.
        :rtype: str
        """
        return self._model_id

    @model_id.setter
    def model_id(self, model_id):
        """
        Sets the model_id of this ModelMetadataDetails.
        Unique identifier model OCID that should be used for inference


        :param model_id: The model_id of this ModelMetadataDetails.
        :type: str
        """
        self._model_id = model_id

    @property
    def endpoint_id(self):
        """
        Gets the endpoint_id of this ModelMetadataDetails.
        Unique identifier endpoint OCID that should be used for inference


        :return: The endpoint_id of this ModelMetadataDetails.
        :rtype: str
        """
        return self._endpoint_id

    @endpoint_id.setter
    def endpoint_id(self, endpoint_id):
        """
        Sets the endpoint_id of this ModelMetadataDetails.
        Unique identifier endpoint OCID that should be used for inference


        :param endpoint_id: The endpoint_id of this ModelMetadataDetails.
        :type: str
        """
        self._endpoint_id = endpoint_id

    @property
    def language_code(self):
        """
        Gets the language_code of this ModelMetadataDetails.
        Language code supported
        - auto : Automatically detect language
        - ar : Arabic
        - pt-BR : Brazilian Portuguese
        - cs : Czech
        - da : Danish
        - nl : Dutch
        - en : English
        - fi : Finnish
        - fr : French
        - fr-CA : Canadian French
        - de : German
        - it : Italian
        - ja : Japanese
        - ko : Korean
        - no : Norwegian
        - pl : Polish
        - ro : Romanian
        - zh-CN : Simplified Chinese
        - es : Spanish
        - sv : Swedish
        - zh-TW : Traditional Chinese
        - tr : Turkish
        - el : Greek
        - he : Hebrew


        :return: The language_code of this ModelMetadataDetails.
        :rtype: str
        """
        return self._language_code

    @language_code.setter
    def language_code(self, language_code):
        """
        Sets the language_code of this ModelMetadataDetails.
        Language code supported
        - auto : Automatically detect language
        - ar : Arabic
        - pt-BR : Brazilian Portuguese
        - cs : Czech
        - da : Danish
        - nl : Dutch
        - en : English
        - fi : Finnish
        - fr : French
        - fr-CA : Canadian French
        - de : German
        - it : Italian
        - ja : Japanese
        - ko : Korean
        - no : Norwegian
        - pl : Polish
        - ro : Romanian
        - zh-CN : Simplified Chinese
        - es : Spanish
        - sv : Swedish
        - zh-TW : Traditional Chinese
        - tr : Turkish
        - el : Greek
        - he : Hebrew


        :param language_code: The language_code of this ModelMetadataDetails.
        :type: str
        """
        self._language_code = language_code

    @property
    def configuration(self):
        """
        Gets the configuration of this ModelMetadataDetails.
        model configuration details
        For PII :  < ENTITY_TYPE , ConfigurationDetails>
        ex.\"ORACLE\":{ \"mode\" : \"MASK\",\"maskingCharacter\" : \"&\",\"leaveCharactersUnmasked\": 3,\"isUnmaskedFromEnd\" : true  }
        For language translation : { \"targetLanguageCodes\" : ConfigurationDetails}


        :return: The configuration of this ModelMetadataDetails.
        :rtype: dict(str, ConfigurationDetails)
        """
        return self._configuration

    @configuration.setter
    def configuration(self, configuration):
        """
        Sets the configuration of this ModelMetadataDetails.
        model configuration details
        For PII :  < ENTITY_TYPE , ConfigurationDetails>
        ex.\"ORACLE\":{ \"mode\" : \"MASK\",\"maskingCharacter\" : \"&\",\"leaveCharactersUnmasked\": 3,\"isUnmaskedFromEnd\" : true  }
        For language translation : { \"targetLanguageCodes\" : ConfigurationDetails}


        :param configuration: The configuration of this ModelMetadataDetails.
        :type: dict(str, ConfigurationDetails)
        """
        self._configuration = configuration

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
