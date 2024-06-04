# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20181201


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class Finding(object):
    """
    The particular finding reported by the security assessment.
    """

    #: A constant which can be used with the severity property of a Finding.
    #: This constant has a value of "HIGH"
    SEVERITY_HIGH = "HIGH"

    #: A constant which can be used with the severity property of a Finding.
    #: This constant has a value of "MEDIUM"
    SEVERITY_MEDIUM = "MEDIUM"

    #: A constant which can be used with the severity property of a Finding.
    #: This constant has a value of "LOW"
    SEVERITY_LOW = "LOW"

    #: A constant which can be used with the severity property of a Finding.
    #: This constant has a value of "EVALUATE"
    SEVERITY_EVALUATE = "EVALUATE"

    #: A constant which can be used with the severity property of a Finding.
    #: This constant has a value of "ADVISORY"
    SEVERITY_ADVISORY = "ADVISORY"

    #: A constant which can be used with the severity property of a Finding.
    #: This constant has a value of "PASS"
    SEVERITY_PASS = "PASS"

    #: A constant which can be used with the severity property of a Finding.
    #: This constant has a value of "DEFERRED"
    SEVERITY_DEFERRED = "DEFERRED"

    #: A constant which can be used with the lifecycle_state property of a Finding.
    #: This constant has a value of "ACTIVE"
    LIFECYCLE_STATE_ACTIVE = "ACTIVE"

    #: A constant which can be used with the lifecycle_state property of a Finding.
    #: This constant has a value of "UPDATING"
    LIFECYCLE_STATE_UPDATING = "UPDATING"

    #: A constant which can be used with the lifecycle_state property of a Finding.
    #: This constant has a value of "NEEDS_ATTENTION"
    LIFECYCLE_STATE_NEEDS_ATTENTION = "NEEDS_ATTENTION"

    #: A constant which can be used with the lifecycle_state property of a Finding.
    #: This constant has a value of "FAILED"
    LIFECYCLE_STATE_FAILED = "FAILED"

    def __init__(self, **kwargs):
        """
        Initializes a new Finding object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param key:
            The value to assign to the key property of this Finding.
        :type key: str

        :param severity:
            The value to assign to the severity property of this Finding.
            Allowed values for this property are: "HIGH", "MEDIUM", "LOW", "EVALUATE", "ADVISORY", "PASS", "DEFERRED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type severity: str

        :param assessment_id:
            The value to assign to the assessment_id property of this Finding.
        :type assessment_id: str

        :param target_id:
            The value to assign to the target_id property of this Finding.
        :type target_id: str

        :param title:
            The value to assign to the title property of this Finding.
        :type title: str

        :param remarks:
            The value to assign to the remarks property of this Finding.
        :type remarks: str

        :param details:
            The value to assign to the details property of this Finding.
        :type details: object

        :param summary:
            The value to assign to the summary property of this Finding.
        :type summary: str

        :param references:
            The value to assign to the references property of this Finding.
        :type references: oci.data_safe.models.References

        :param oracle_defined_severity:
            The value to assign to the oracle_defined_severity property of this Finding.
        :type oracle_defined_severity: str

        :param is_risk_modified:
            The value to assign to the is_risk_modified property of this Finding.
        :type is_risk_modified: bool

        :param has_target_db_risk_level_changed:
            The value to assign to the has_target_db_risk_level_changed property of this Finding.
        :type has_target_db_risk_level_changed: bool

        :param justification:
            The value to assign to the justification property of this Finding.
        :type justification: str

        :param time_valid_until:
            The value to assign to the time_valid_until property of this Finding.
        :type time_valid_until: datetime

        :param time_updated:
            The value to assign to the time_updated property of this Finding.
        :type time_updated: datetime

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this Finding.
            Allowed values for this property are: "ACTIVE", "UPDATING", "NEEDS_ATTENTION", "FAILED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param lifecycle_details:
            The value to assign to the lifecycle_details property of this Finding.
        :type lifecycle_details: str

        """
        self.swagger_types = {
            'key': 'str',
            'severity': 'str',
            'assessment_id': 'str',
            'target_id': 'str',
            'title': 'str',
            'remarks': 'str',
            'details': 'object',
            'summary': 'str',
            'references': 'References',
            'oracle_defined_severity': 'str',
            'is_risk_modified': 'bool',
            'has_target_db_risk_level_changed': 'bool',
            'justification': 'str',
            'time_valid_until': 'datetime',
            'time_updated': 'datetime',
            'lifecycle_state': 'str',
            'lifecycle_details': 'str'
        }

        self.attribute_map = {
            'key': 'key',
            'severity': 'severity',
            'assessment_id': 'assessmentId',
            'target_id': 'targetId',
            'title': 'title',
            'remarks': 'remarks',
            'details': 'details',
            'summary': 'summary',
            'references': 'references',
            'oracle_defined_severity': 'oracleDefinedSeverity',
            'is_risk_modified': 'isRiskModified',
            'has_target_db_risk_level_changed': 'hasTargetDbRiskLevelChanged',
            'justification': 'justification',
            'time_valid_until': 'timeValidUntil',
            'time_updated': 'timeUpdated',
            'lifecycle_state': 'lifecycleState',
            'lifecycle_details': 'lifecycleDetails'
        }

        self._key = None
        self._severity = None
        self._assessment_id = None
        self._target_id = None
        self._title = None
        self._remarks = None
        self._details = None
        self._summary = None
        self._references = None
        self._oracle_defined_severity = None
        self._is_risk_modified = None
        self._has_target_db_risk_level_changed = None
        self._justification = None
        self._time_valid_until = None
        self._time_updated = None
        self._lifecycle_state = None
        self._lifecycle_details = None

    @property
    def key(self):
        """
        Gets the key of this Finding.
        A unique identifier for the finding. This is common for the finding across targets.


        :return: The key of this Finding.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """
        Sets the key of this Finding.
        A unique identifier for the finding. This is common for the finding across targets.


        :param key: The key of this Finding.
        :type: str
        """
        self._key = key

    @property
    def severity(self):
        """
        Gets the severity of this Finding.
        The severity of the finding.

        Allowed values for this property are: "HIGH", "MEDIUM", "LOW", "EVALUATE", "ADVISORY", "PASS", "DEFERRED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The severity of this Finding.
        :rtype: str
        """
        return self._severity

    @severity.setter
    def severity(self, severity):
        """
        Sets the severity of this Finding.
        The severity of the finding.


        :param severity: The severity of this Finding.
        :type: str
        """
        allowed_values = ["HIGH", "MEDIUM", "LOW", "EVALUATE", "ADVISORY", "PASS", "DEFERRED"]
        if not value_allowed_none_or_none_sentinel(severity, allowed_values):
            severity = 'UNKNOWN_ENUM_VALUE'
        self._severity = severity

    @property
    def assessment_id(self):
        """
        Gets the assessment_id of this Finding.
        The OCID of the assessment that generated this finding.


        :return: The assessment_id of this Finding.
        :rtype: str
        """
        return self._assessment_id

    @assessment_id.setter
    def assessment_id(self, assessment_id):
        """
        Sets the assessment_id of this Finding.
        The OCID of the assessment that generated this finding.


        :param assessment_id: The assessment_id of this Finding.
        :type: str
        """
        self._assessment_id = assessment_id

    @property
    def target_id(self):
        """
        Gets the target_id of this Finding.
        The OCID of the target database.


        :return: The target_id of this Finding.
        :rtype: str
        """
        return self._target_id

    @target_id.setter
    def target_id(self, target_id):
        """
        Sets the target_id of this Finding.
        The OCID of the target database.


        :param target_id: The target_id of this Finding.
        :type: str
        """
        self._target_id = target_id

    @property
    def title(self):
        """
        Gets the title of this Finding.
        The short title for the finding.


        :return: The title of this Finding.
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """
        Sets the title of this Finding.
        The short title for the finding.


        :param title: The title of this Finding.
        :type: str
        """
        self._title = title

    @property
    def remarks(self):
        """
        Gets the remarks of this Finding.
        The explanation of the issue in this finding. It explains the reason for the rule and, if a risk is reported, it may also explain the recommended actions for remediation.


        :return: The remarks of this Finding.
        :rtype: str
        """
        return self._remarks

    @remarks.setter
    def remarks(self, remarks):
        """
        Sets the remarks of this Finding.
        The explanation of the issue in this finding. It explains the reason for the rule and, if a risk is reported, it may also explain the recommended actions for remediation.


        :param remarks: The remarks of this Finding.
        :type: str
        """
        self._remarks = remarks

    @property
    def details(self):
        """
        Gets the details of this Finding.
        The details of the finding. Provides detailed information to explain the finding summary, typically results from the assessed database, followed by any recommendations for changes.


        :return: The details of this Finding.
        :rtype: object
        """
        return self._details

    @details.setter
    def details(self, details):
        """
        Sets the details of this Finding.
        The details of the finding. Provides detailed information to explain the finding summary, typically results from the assessed database, followed by any recommendations for changes.


        :param details: The details of this Finding.
        :type: object
        """
        self._details = details

    @property
    def summary(self):
        """
        Gets the summary of this Finding.
        The brief summary of the finding. When the finding is informational, the summary typically reports only the number of data elements that were examined.


        :return: The summary of this Finding.
        :rtype: str
        """
        return self._summary

    @summary.setter
    def summary(self, summary):
        """
        Sets the summary of this Finding.
        The brief summary of the finding. When the finding is informational, the summary typically reports only the number of data elements that were examined.


        :param summary: The summary of this Finding.
        :type: str
        """
        self._summary = summary

    @property
    def references(self):
        """
        Gets the references of this Finding.
        Provides information on whether the finding is related to a CIS Oracle Database Benchmark recommendation, STIG rule, or related to a GDPR Article/Recital.


        :return: The references of this Finding.
        :rtype: oci.data_safe.models.References
        """
        return self._references

    @references.setter
    def references(self, references):
        """
        Sets the references of this Finding.
        Provides information on whether the finding is related to a CIS Oracle Database Benchmark recommendation, STIG rule, or related to a GDPR Article/Recital.


        :param references: The references of this Finding.
        :type: oci.data_safe.models.References
        """
        self._references = references

    @property
    def oracle_defined_severity(self):
        """
        Gets the oracle_defined_severity of this Finding.
        The severity of the finding as determined by security assessment. This cannot be modified by user.


        :return: The oracle_defined_severity of this Finding.
        :rtype: str
        """
        return self._oracle_defined_severity

    @oracle_defined_severity.setter
    def oracle_defined_severity(self, oracle_defined_severity):
        """
        Sets the oracle_defined_severity of this Finding.
        The severity of the finding as determined by security assessment. This cannot be modified by user.


        :param oracle_defined_severity: The oracle_defined_severity of this Finding.
        :type: str
        """
        self._oracle_defined_severity = oracle_defined_severity

    @property
    def is_risk_modified(self):
        """
        Gets the is_risk_modified of this Finding.
        Determines if this risk level was modified by user.


        :return: The is_risk_modified of this Finding.
        :rtype: bool
        """
        return self._is_risk_modified

    @is_risk_modified.setter
    def is_risk_modified(self, is_risk_modified):
        """
        Sets the is_risk_modified of this Finding.
        Determines if this risk level was modified by user.


        :param is_risk_modified: The is_risk_modified of this Finding.
        :type: bool
        """
        self._is_risk_modified = is_risk_modified

    @property
    def has_target_db_risk_level_changed(self):
        """
        Gets the has_target_db_risk_level_changed of this Finding.
        Determines if this risk level has changed on the target database since the last time 'severity' was modified by user.


        :return: The has_target_db_risk_level_changed of this Finding.
        :rtype: bool
        """
        return self._has_target_db_risk_level_changed

    @has_target_db_risk_level_changed.setter
    def has_target_db_risk_level_changed(self, has_target_db_risk_level_changed):
        """
        Sets the has_target_db_risk_level_changed of this Finding.
        Determines if this risk level has changed on the target database since the last time 'severity' was modified by user.


        :param has_target_db_risk_level_changed: The has_target_db_risk_level_changed of this Finding.
        :type: bool
        """
        self._has_target_db_risk_level_changed = has_target_db_risk_level_changed

    @property
    def justification(self):
        """
        Gets the justification of this Finding.
        User provided reason for accepting or modifying this finding if they choose to do so.


        :return: The justification of this Finding.
        :rtype: str
        """
        return self._justification

    @justification.setter
    def justification(self, justification):
        """
        Sets the justification of this Finding.
        User provided reason for accepting or modifying this finding if they choose to do so.


        :param justification: The justification of this Finding.
        :type: str
        """
        self._justification = justification

    @property
    def time_valid_until(self):
        """
        Gets the time_valid_until of this Finding.
        The time until which the change in severity(deferred/modified) of this finding is valid.


        :return: The time_valid_until of this Finding.
        :rtype: datetime
        """
        return self._time_valid_until

    @time_valid_until.setter
    def time_valid_until(self, time_valid_until):
        """
        Sets the time_valid_until of this Finding.
        The time until which the change in severity(deferred/modified) of this finding is valid.


        :param time_valid_until: The time_valid_until of this Finding.
        :type: datetime
        """
        self._time_valid_until = time_valid_until

    @property
    def time_updated(self):
        """
        Gets the time_updated of this Finding.
        The date and time the risk level of finding was last updated, in the format defined by `RFC3339`__.

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_updated of this Finding.
        :rtype: datetime
        """
        return self._time_updated

    @time_updated.setter
    def time_updated(self, time_updated):
        """
        Sets the time_updated of this Finding.
        The date and time the risk level of finding was last updated, in the format defined by `RFC3339`__.

        __ https://tools.ietf.org/html/rfc3339


        :param time_updated: The time_updated of this Finding.
        :type: datetime
        """
        self._time_updated = time_updated

    @property
    def lifecycle_state(self):
        """
        Gets the lifecycle_state of this Finding.
        The current state of the finding.

        Allowed values for this property are: "ACTIVE", "UPDATING", "NEEDS_ATTENTION", "FAILED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this Finding.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this Finding.
        The current state of the finding.


        :param lifecycle_state: The lifecycle_state of this Finding.
        :type: str
        """
        allowed_values = ["ACTIVE", "UPDATING", "NEEDS_ATTENTION", "FAILED"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def lifecycle_details(self):
        """
        Gets the lifecycle_details of this Finding.
        Details about the current state of the finding.


        :return: The lifecycle_details of this Finding.
        :rtype: str
        """
        return self._lifecycle_details

    @lifecycle_details.setter
    def lifecycle_details(self, lifecycle_details):
        """
        Sets the lifecycle_details of this Finding.
        Details about the current state of the finding.


        :param lifecycle_details: The lifecycle_details of this Finding.
        :type: str
        """
        self._lifecycle_details = lifecycle_details

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
