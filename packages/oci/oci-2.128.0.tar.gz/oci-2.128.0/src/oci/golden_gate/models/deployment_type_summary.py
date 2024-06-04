# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20200407


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class DeploymentTypeSummary(object):
    """
    The meta-data specific on particular deployment type represented by deploymentType field.
    """

    #: A constant which can be used with the category property of a DeploymentTypeSummary.
    #: This constant has a value of "DATA_REPLICATION"
    CATEGORY_DATA_REPLICATION = "DATA_REPLICATION"

    #: A constant which can be used with the category property of a DeploymentTypeSummary.
    #: This constant has a value of "STREAM_ANALYTICS"
    CATEGORY_STREAM_ANALYTICS = "STREAM_ANALYTICS"

    #: A constant which can be used with the category property of a DeploymentTypeSummary.
    #: This constant has a value of "DATA_TRANSFORMS"
    CATEGORY_DATA_TRANSFORMS = "DATA_TRANSFORMS"

    #: A constant which can be used with the deployment_type property of a DeploymentTypeSummary.
    #: This constant has a value of "OGG"
    DEPLOYMENT_TYPE_OGG = "OGG"

    #: A constant which can be used with the deployment_type property of a DeploymentTypeSummary.
    #: This constant has a value of "DATABASE_ORACLE"
    DEPLOYMENT_TYPE_DATABASE_ORACLE = "DATABASE_ORACLE"

    #: A constant which can be used with the deployment_type property of a DeploymentTypeSummary.
    #: This constant has a value of "BIGDATA"
    DEPLOYMENT_TYPE_BIGDATA = "BIGDATA"

    #: A constant which can be used with the deployment_type property of a DeploymentTypeSummary.
    #: This constant has a value of "DATABASE_MICROSOFT_SQLSERVER"
    DEPLOYMENT_TYPE_DATABASE_MICROSOFT_SQLSERVER = "DATABASE_MICROSOFT_SQLSERVER"

    #: A constant which can be used with the deployment_type property of a DeploymentTypeSummary.
    #: This constant has a value of "DATABASE_MYSQL"
    DEPLOYMENT_TYPE_DATABASE_MYSQL = "DATABASE_MYSQL"

    #: A constant which can be used with the deployment_type property of a DeploymentTypeSummary.
    #: This constant has a value of "DATABASE_POSTGRESQL"
    DEPLOYMENT_TYPE_DATABASE_POSTGRESQL = "DATABASE_POSTGRESQL"

    #: A constant which can be used with the deployment_type property of a DeploymentTypeSummary.
    #: This constant has a value of "DATABASE_DB2ZOS"
    DEPLOYMENT_TYPE_DATABASE_DB2_ZOS = "DATABASE_DB2ZOS"

    #: A constant which can be used with the deployment_type property of a DeploymentTypeSummary.
    #: This constant has a value of "GGSA"
    DEPLOYMENT_TYPE_GGSA = "GGSA"

    #: A constant which can be used with the deployment_type property of a DeploymentTypeSummary.
    #: This constant has a value of "DATA_TRANSFORMS"
    DEPLOYMENT_TYPE_DATA_TRANSFORMS = "DATA_TRANSFORMS"

    #: A constant which can be used with the connection_types property of a DeploymentTypeSummary.
    #: This constant has a value of "GOLDENGATE"
    CONNECTION_TYPES_GOLDENGATE = "GOLDENGATE"

    #: A constant which can be used with the connection_types property of a DeploymentTypeSummary.
    #: This constant has a value of "KAFKA"
    CONNECTION_TYPES_KAFKA = "KAFKA"

    #: A constant which can be used with the connection_types property of a DeploymentTypeSummary.
    #: This constant has a value of "KAFKA_SCHEMA_REGISTRY"
    CONNECTION_TYPES_KAFKA_SCHEMA_REGISTRY = "KAFKA_SCHEMA_REGISTRY"

    #: A constant which can be used with the connection_types property of a DeploymentTypeSummary.
    #: This constant has a value of "MYSQL"
    CONNECTION_TYPES_MYSQL = "MYSQL"

    #: A constant which can be used with the connection_types property of a DeploymentTypeSummary.
    #: This constant has a value of "JAVA_MESSAGE_SERVICE"
    CONNECTION_TYPES_JAVA_MESSAGE_SERVICE = "JAVA_MESSAGE_SERVICE"

    #: A constant which can be used with the connection_types property of a DeploymentTypeSummary.
    #: This constant has a value of "MICROSOFT_SQLSERVER"
    CONNECTION_TYPES_MICROSOFT_SQLSERVER = "MICROSOFT_SQLSERVER"

    #: A constant which can be used with the connection_types property of a DeploymentTypeSummary.
    #: This constant has a value of "OCI_OBJECT_STORAGE"
    CONNECTION_TYPES_OCI_OBJECT_STORAGE = "OCI_OBJECT_STORAGE"

    #: A constant which can be used with the connection_types property of a DeploymentTypeSummary.
    #: This constant has a value of "ORACLE"
    CONNECTION_TYPES_ORACLE = "ORACLE"

    #: A constant which can be used with the connection_types property of a DeploymentTypeSummary.
    #: This constant has a value of "AZURE_DATA_LAKE_STORAGE"
    CONNECTION_TYPES_AZURE_DATA_LAKE_STORAGE = "AZURE_DATA_LAKE_STORAGE"

    #: A constant which can be used with the connection_types property of a DeploymentTypeSummary.
    #: This constant has a value of "POSTGRESQL"
    CONNECTION_TYPES_POSTGRESQL = "POSTGRESQL"

    #: A constant which can be used with the connection_types property of a DeploymentTypeSummary.
    #: This constant has a value of "AZURE_SYNAPSE_ANALYTICS"
    CONNECTION_TYPES_AZURE_SYNAPSE_ANALYTICS = "AZURE_SYNAPSE_ANALYTICS"

    #: A constant which can be used with the connection_types property of a DeploymentTypeSummary.
    #: This constant has a value of "SNOWFLAKE"
    CONNECTION_TYPES_SNOWFLAKE = "SNOWFLAKE"

    #: A constant which can be used with the connection_types property of a DeploymentTypeSummary.
    #: This constant has a value of "AMAZON_S3"
    CONNECTION_TYPES_AMAZON_S3 = "AMAZON_S3"

    #: A constant which can be used with the connection_types property of a DeploymentTypeSummary.
    #: This constant has a value of "HDFS"
    CONNECTION_TYPES_HDFS = "HDFS"

    #: A constant which can be used with the connection_types property of a DeploymentTypeSummary.
    #: This constant has a value of "ORACLE_NOSQL"
    CONNECTION_TYPES_ORACLE_NOSQL = "ORACLE_NOSQL"

    #: A constant which can be used with the connection_types property of a DeploymentTypeSummary.
    #: This constant has a value of "MONGODB"
    CONNECTION_TYPES_MONGODB = "MONGODB"

    #: A constant which can be used with the connection_types property of a DeploymentTypeSummary.
    #: This constant has a value of "AMAZON_KINESIS"
    CONNECTION_TYPES_AMAZON_KINESIS = "AMAZON_KINESIS"

    #: A constant which can be used with the connection_types property of a DeploymentTypeSummary.
    #: This constant has a value of "AMAZON_REDSHIFT"
    CONNECTION_TYPES_AMAZON_REDSHIFT = "AMAZON_REDSHIFT"

    #: A constant which can be used with the connection_types property of a DeploymentTypeSummary.
    #: This constant has a value of "DB2"
    CONNECTION_TYPES_DB2 = "DB2"

    #: A constant which can be used with the connection_types property of a DeploymentTypeSummary.
    #: This constant has a value of "REDIS"
    CONNECTION_TYPES_REDIS = "REDIS"

    #: A constant which can be used with the connection_types property of a DeploymentTypeSummary.
    #: This constant has a value of "ELASTICSEARCH"
    CONNECTION_TYPES_ELASTICSEARCH = "ELASTICSEARCH"

    #: A constant which can be used with the connection_types property of a DeploymentTypeSummary.
    #: This constant has a value of "GENERIC"
    CONNECTION_TYPES_GENERIC = "GENERIC"

    #: A constant which can be used with the connection_types property of a DeploymentTypeSummary.
    #: This constant has a value of "GOOGLE_CLOUD_STORAGE"
    CONNECTION_TYPES_GOOGLE_CLOUD_STORAGE = "GOOGLE_CLOUD_STORAGE"

    #: A constant which can be used with the connection_types property of a DeploymentTypeSummary.
    #: This constant has a value of "GOOGLE_BIGQUERY"
    CONNECTION_TYPES_GOOGLE_BIGQUERY = "GOOGLE_BIGQUERY"

    def __init__(self, **kwargs):
        """
        Initializes a new DeploymentTypeSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param category:
            The value to assign to the category property of this DeploymentTypeSummary.
            Allowed values for this property are: "DATA_REPLICATION", "STREAM_ANALYTICS", "DATA_TRANSFORMS", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type category: str

        :param display_name:
            The value to assign to the display_name property of this DeploymentTypeSummary.
        :type display_name: str

        :param deployment_type:
            The value to assign to the deployment_type property of this DeploymentTypeSummary.
            Allowed values for this property are: "OGG", "DATABASE_ORACLE", "BIGDATA", "DATABASE_MICROSOFT_SQLSERVER", "DATABASE_MYSQL", "DATABASE_POSTGRESQL", "DATABASE_DB2ZOS", "GGSA", "DATA_TRANSFORMS", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type deployment_type: str

        :param connection_types:
            The value to assign to the connection_types property of this DeploymentTypeSummary.
            Allowed values for items in this list are: "GOLDENGATE", "KAFKA", "KAFKA_SCHEMA_REGISTRY", "MYSQL", "JAVA_MESSAGE_SERVICE", "MICROSOFT_SQLSERVER", "OCI_OBJECT_STORAGE", "ORACLE", "AZURE_DATA_LAKE_STORAGE", "POSTGRESQL", "AZURE_SYNAPSE_ANALYTICS", "SNOWFLAKE", "AMAZON_S3", "HDFS", "ORACLE_NOSQL", "MONGODB", "AMAZON_KINESIS", "AMAZON_REDSHIFT", "DB2", "REDIS", "ELASTICSEARCH", "GENERIC", "GOOGLE_CLOUD_STORAGE", "GOOGLE_BIGQUERY", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type connection_types: list[str]

        :param source_technologies:
            The value to assign to the source_technologies property of this DeploymentTypeSummary.
        :type source_technologies: list[str]

        :param target_technologies:
            The value to assign to the target_technologies property of this DeploymentTypeSummary.
        :type target_technologies: list[str]

        :param ogg_version:
            The value to assign to the ogg_version property of this DeploymentTypeSummary.
        :type ogg_version: str

        :param supported_technologies_url:
            The value to assign to the supported_technologies_url property of this DeploymentTypeSummary.
        :type supported_technologies_url: str

        :param default_username:
            The value to assign to the default_username property of this DeploymentTypeSummary.
        :type default_username: str

        """
        self.swagger_types = {
            'category': 'str',
            'display_name': 'str',
            'deployment_type': 'str',
            'connection_types': 'list[str]',
            'source_technologies': 'list[str]',
            'target_technologies': 'list[str]',
            'ogg_version': 'str',
            'supported_technologies_url': 'str',
            'default_username': 'str'
        }

        self.attribute_map = {
            'category': 'category',
            'display_name': 'displayName',
            'deployment_type': 'deploymentType',
            'connection_types': 'connectionTypes',
            'source_technologies': 'sourceTechnologies',
            'target_technologies': 'targetTechnologies',
            'ogg_version': 'oggVersion',
            'supported_technologies_url': 'supportedTechnologiesUrl',
            'default_username': 'defaultUsername'
        }

        self._category = None
        self._display_name = None
        self._deployment_type = None
        self._connection_types = None
        self._source_technologies = None
        self._target_technologies = None
        self._ogg_version = None
        self._supported_technologies_url = None
        self._default_username = None

    @property
    def category(self):
        """
        **[Required]** Gets the category of this DeploymentTypeSummary.
        The deployment category defines the broad separation of the deployment type into three categories.
        Currently the separation is 'DATA_REPLICATION', 'STREAM_ANALYTICS' and 'DATA_TRANSFORMS'.

        Allowed values for this property are: "DATA_REPLICATION", "STREAM_ANALYTICS", "DATA_TRANSFORMS", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The category of this DeploymentTypeSummary.
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category):
        """
        Sets the category of this DeploymentTypeSummary.
        The deployment category defines the broad separation of the deployment type into three categories.
        Currently the separation is 'DATA_REPLICATION', 'STREAM_ANALYTICS' and 'DATA_TRANSFORMS'.


        :param category: The category of this DeploymentTypeSummary.
        :type: str
        """
        allowed_values = ["DATA_REPLICATION", "STREAM_ANALYTICS", "DATA_TRANSFORMS"]
        if not value_allowed_none_or_none_sentinel(category, allowed_values):
            category = 'UNKNOWN_ENUM_VALUE'
        self._category = category

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this DeploymentTypeSummary.
        An object's Display Name.


        :return: The display_name of this DeploymentTypeSummary.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this DeploymentTypeSummary.
        An object's Display Name.


        :param display_name: The display_name of this DeploymentTypeSummary.
        :type: str
        """
        self._display_name = display_name

    @property
    def deployment_type(self):
        """
        **[Required]** Gets the deployment_type of this DeploymentTypeSummary.
        The type of deployment, which can be any one of the Allowed values.
        NOTE: Use of the value 'OGG' is maintained for backward compatibility purposes.
            Its use is discouraged in favor of 'DATABASE_ORACLE'.

        Allowed values for this property are: "OGG", "DATABASE_ORACLE", "BIGDATA", "DATABASE_MICROSOFT_SQLSERVER", "DATABASE_MYSQL", "DATABASE_POSTGRESQL", "DATABASE_DB2ZOS", "GGSA", "DATA_TRANSFORMS", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The deployment_type of this DeploymentTypeSummary.
        :rtype: str
        """
        return self._deployment_type

    @deployment_type.setter
    def deployment_type(self, deployment_type):
        """
        Sets the deployment_type of this DeploymentTypeSummary.
        The type of deployment, which can be any one of the Allowed values.
        NOTE: Use of the value 'OGG' is maintained for backward compatibility purposes.
            Its use is discouraged in favor of 'DATABASE_ORACLE'.


        :param deployment_type: The deployment_type of this DeploymentTypeSummary.
        :type: str
        """
        allowed_values = ["OGG", "DATABASE_ORACLE", "BIGDATA", "DATABASE_MICROSOFT_SQLSERVER", "DATABASE_MYSQL", "DATABASE_POSTGRESQL", "DATABASE_DB2ZOS", "GGSA", "DATA_TRANSFORMS"]
        if not value_allowed_none_or_none_sentinel(deployment_type, allowed_values):
            deployment_type = 'UNKNOWN_ENUM_VALUE'
        self._deployment_type = deployment_type

    @property
    def connection_types(self):
        """
        Gets the connection_types of this DeploymentTypeSummary.
        An array of connectionTypes.

        Allowed values for items in this list are: "GOLDENGATE", "KAFKA", "KAFKA_SCHEMA_REGISTRY", "MYSQL", "JAVA_MESSAGE_SERVICE", "MICROSOFT_SQLSERVER", "OCI_OBJECT_STORAGE", "ORACLE", "AZURE_DATA_LAKE_STORAGE", "POSTGRESQL", "AZURE_SYNAPSE_ANALYTICS", "SNOWFLAKE", "AMAZON_S3", "HDFS", "ORACLE_NOSQL", "MONGODB", "AMAZON_KINESIS", "AMAZON_REDSHIFT", "DB2", "REDIS", "ELASTICSEARCH", "GENERIC", "GOOGLE_CLOUD_STORAGE", "GOOGLE_BIGQUERY", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The connection_types of this DeploymentTypeSummary.
        :rtype: list[str]
        """
        return self._connection_types

    @connection_types.setter
    def connection_types(self, connection_types):
        """
        Sets the connection_types of this DeploymentTypeSummary.
        An array of connectionTypes.


        :param connection_types: The connection_types of this DeploymentTypeSummary.
        :type: list[str]
        """
        allowed_values = ["GOLDENGATE", "KAFKA", "KAFKA_SCHEMA_REGISTRY", "MYSQL", "JAVA_MESSAGE_SERVICE", "MICROSOFT_SQLSERVER", "OCI_OBJECT_STORAGE", "ORACLE", "AZURE_DATA_LAKE_STORAGE", "POSTGRESQL", "AZURE_SYNAPSE_ANALYTICS", "SNOWFLAKE", "AMAZON_S3", "HDFS", "ORACLE_NOSQL", "MONGODB", "AMAZON_KINESIS", "AMAZON_REDSHIFT", "DB2", "REDIS", "ELASTICSEARCH", "GENERIC", "GOOGLE_CLOUD_STORAGE", "GOOGLE_BIGQUERY"]
        if connection_types:
            connection_types[:] = ['UNKNOWN_ENUM_VALUE' if not value_allowed_none_or_none_sentinel(x, allowed_values) else x for x in connection_types]
        self._connection_types = connection_types

    @property
    def source_technologies(self):
        """
        Gets the source_technologies of this DeploymentTypeSummary.
        List of the supported technologies generally.  The value is a freeform text string generally consisting
        of a description of the technology and optionally the speific version(s) support.  For example,
        [ \"Oracle Database 19c\", \"Oracle Exadata\", \"OCI Streaming\" ]


        :return: The source_technologies of this DeploymentTypeSummary.
        :rtype: list[str]
        """
        return self._source_technologies

    @source_technologies.setter
    def source_technologies(self, source_technologies):
        """
        Sets the source_technologies of this DeploymentTypeSummary.
        List of the supported technologies generally.  The value is a freeform text string generally consisting
        of a description of the technology and optionally the speific version(s) support.  For example,
        [ \"Oracle Database 19c\", \"Oracle Exadata\", \"OCI Streaming\" ]


        :param source_technologies: The source_technologies of this DeploymentTypeSummary.
        :type: list[str]
        """
        self._source_technologies = source_technologies

    @property
    def target_technologies(self):
        """
        Gets the target_technologies of this DeploymentTypeSummary.
        List of the supported technologies generally.  The value is a freeform text string generally consisting
        of a description of the technology and optionally the speific version(s) support.  For example,
        [ \"Oracle Database 19c\", \"Oracle Exadata\", \"OCI Streaming\" ]


        :return: The target_technologies of this DeploymentTypeSummary.
        :rtype: list[str]
        """
        return self._target_technologies

    @target_technologies.setter
    def target_technologies(self, target_technologies):
        """
        Sets the target_technologies of this DeploymentTypeSummary.
        List of the supported technologies generally.  The value is a freeform text string generally consisting
        of a description of the technology and optionally the speific version(s) support.  For example,
        [ \"Oracle Database 19c\", \"Oracle Exadata\", \"OCI Streaming\" ]


        :param target_technologies: The target_technologies of this DeploymentTypeSummary.
        :type: list[str]
        """
        self._target_technologies = target_technologies

    @property
    def ogg_version(self):
        """
        Gets the ogg_version of this DeploymentTypeSummary.
        Version of OGG


        :return: The ogg_version of this DeploymentTypeSummary.
        :rtype: str
        """
        return self._ogg_version

    @ogg_version.setter
    def ogg_version(self, ogg_version):
        """
        Sets the ogg_version of this DeploymentTypeSummary.
        Version of OGG


        :param ogg_version: The ogg_version of this DeploymentTypeSummary.
        :type: str
        """
        self._ogg_version = ogg_version

    @property
    def supported_technologies_url(self):
        """
        Gets the supported_technologies_url of this DeploymentTypeSummary.
        The URL to the webpage listing the supported technologies.


        :return: The supported_technologies_url of this DeploymentTypeSummary.
        :rtype: str
        """
        return self._supported_technologies_url

    @supported_technologies_url.setter
    def supported_technologies_url(self, supported_technologies_url):
        """
        Sets the supported_technologies_url of this DeploymentTypeSummary.
        The URL to the webpage listing the supported technologies.


        :param supported_technologies_url: The supported_technologies_url of this DeploymentTypeSummary.
        :type: str
        """
        self._supported_technologies_url = supported_technologies_url

    @property
    def default_username(self):
        """
        Gets the default_username of this DeploymentTypeSummary.
        The default admin username used by deployment.


        :return: The default_username of this DeploymentTypeSummary.
        :rtype: str
        """
        return self._default_username

    @default_username.setter
    def default_username(self, default_username):
        """
        Sets the default_username of this DeploymentTypeSummary.
        The default admin username used by deployment.


        :param default_username: The default_username of this DeploymentTypeSummary.
        :type: str
        """
        self._default_username = default_username

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
