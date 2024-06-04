# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20210224


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CertificateRule(object):
    """
    A rule that you can apply to a certificate to enforce certain conditions on the certificate's usage and management.
    """

    #: A constant which can be used with the rule_type property of a CertificateRule.
    #: This constant has a value of "CERTIFICATE_RENEWAL_RULE"
    RULE_TYPE_CERTIFICATE_RENEWAL_RULE = "CERTIFICATE_RENEWAL_RULE"

    def __init__(self, **kwargs):
        """
        Initializes a new CertificateRule object with values from keyword arguments. This class has the following subclasses and if you are using this class as input
        to a service operations then you should favor using a subclass over the base class:

        * :class:`~oci.certificates_management.models.CertificateRenewalRule`

        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param rule_type:
            The value to assign to the rule_type property of this CertificateRule.
            Allowed values for this property are: "CERTIFICATE_RENEWAL_RULE", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type rule_type: str

        """
        self.swagger_types = {
            'rule_type': 'str'
        }

        self.attribute_map = {
            'rule_type': 'ruleType'
        }

        self._rule_type = None

    @staticmethod
    def get_subtype(object_dictionary):
        """
        Given the hash representation of a subtype of this class,
        use the info in the hash to return the class of the subtype.
        """
        type = object_dictionary['ruleType']

        if type == 'CERTIFICATE_RENEWAL_RULE':
            return 'CertificateRenewalRule'
        else:
            return 'CertificateRule'

    @property
    def rule_type(self):
        """
        **[Required]** Gets the rule_type of this CertificateRule.
        The type of rule.

        Allowed values for this property are: "CERTIFICATE_RENEWAL_RULE", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The rule_type of this CertificateRule.
        :rtype: str
        """
        return self._rule_type

    @rule_type.setter
    def rule_type(self, rule_type):
        """
        Sets the rule_type of this CertificateRule.
        The type of rule.


        :param rule_type: The rule_type of this CertificateRule.
        :type: str
        """
        allowed_values = ["CERTIFICATE_RENEWAL_RULE"]
        if not value_allowed_none_or_none_sentinel(rule_type, allowed_values):
            rule_type = 'UNKNOWN_ENUM_VALUE'
        self._rule_type = rule_type

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
