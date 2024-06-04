# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20221001


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class MelConceptDetails(object):
    """
    The MEL concepts details for health ner.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new MelConceptDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this MelConceptDetails.
        :type id: str

        :param name:
            The value to assign to the name property of this MelConceptDetails.
        :type name: str

        :param score:
            The value to assign to the score property of this MelConceptDetails.
        :type score: float

        :param attributes:
            The value to assign to the attributes property of this MelConceptDetails.
        :type attributes: dict(str, str)

        """
        self.swagger_types = {
            'id': 'str',
            'name': 'str',
            'score': 'float',
            'attributes': 'dict(str, str)'
        }

        self.attribute_map = {
            'id': 'id',
            'name': 'name',
            'score': 'score',
            'attributes': 'attributes'
        }

        self._id = None
        self._name = None
        self._score = None
        self._attributes = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this MelConceptDetails.
        id of the relation


        :return: The id of this MelConceptDetails.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this MelConceptDetails.
        id of the relation


        :param id: The id of this MelConceptDetails.
        :type: str
        """
        self._id = id

    @property
    def name(self):
        """
        **[Required]** Gets the name of this MelConceptDetails.
        The matched concept name/description on the ontology


        :return: The name of this MelConceptDetails.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this MelConceptDetails.
        The matched concept name/description on the ontology


        :param name: The name of this MelConceptDetails.
        :type: str
        """
        self._name = name

    @property
    def score(self):
        """
        **[Required]** Gets the score of this MelConceptDetails.
        The relevant score between the concept and the input text


        :return: The score of this MelConceptDetails.
        :rtype: float
        """
        return self._score

    @score.setter
    def score(self, score):
        """
        Sets the score of this MelConceptDetails.
        The relevant score between the concept and the input text


        :param score: The score of this MelConceptDetails.
        :type: float
        """
        self._score = score

    @property
    def attributes(self):
        """
        Gets the attributes of this MelConceptDetails.
        additional attribute values specific to ontology for ex. for SNOMED semantic_type and for for ICD-10 default_charge_code etc.


        :return: The attributes of this MelConceptDetails.
        :rtype: dict(str, str)
        """
        return self._attributes

    @attributes.setter
    def attributes(self, attributes):
        """
        Sets the attributes of this MelConceptDetails.
        additional attribute values specific to ontology for ex. for SNOMED semantic_type and for for ICD-10 default_charge_code etc.


        :param attributes: The attributes of this MelConceptDetails.
        :type: dict(str, str)
        """
        self._attributes = attributes

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
