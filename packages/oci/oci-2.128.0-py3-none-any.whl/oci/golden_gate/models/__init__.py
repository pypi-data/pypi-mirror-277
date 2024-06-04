# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20200407

from __future__ import absolute_import

from .add_resource_lock_details import AddResourceLockDetails
from .amazon_kinesis_connection import AmazonKinesisConnection
from .amazon_kinesis_connection_summary import AmazonKinesisConnectionSummary
from .amazon_redshift_connection import AmazonRedshiftConnection
from .amazon_redshift_connection_summary import AmazonRedshiftConnectionSummary
from .amazon_s3_connection import AmazonS3Connection
from .amazon_s3_connection_summary import AmazonS3ConnectionSummary
from .azure_data_lake_storage_connection import AzureDataLakeStorageConnection
from .azure_data_lake_storage_connection_summary import AzureDataLakeStorageConnectionSummary
from .azure_synapse_connection import AzureSynapseConnection
from .azure_synapse_connection_summary import AzureSynapseConnectionSummary
from .cancel_deployment_backup_details import CancelDeploymentBackupDetails
from .cancel_deployment_upgrade_details import CancelDeploymentUpgradeDetails
from .cancel_snooze_deployment_upgrade_details import CancelSnoozeDeploymentUpgradeDetails
from .certificate import Certificate
from .certificate_collection import CertificateCollection
from .certificate_summary import CertificateSummary
from .change_connection_compartment_details import ChangeConnectionCompartmentDetails
from .change_database_registration_compartment_details import ChangeDatabaseRegistrationCompartmentDetails
from .change_deployment_backup_compartment_details import ChangeDeploymentBackupCompartmentDetails
from .change_deployment_compartment_details import ChangeDeploymentCompartmentDetails
from .collect_deployment_diagnostic_details import CollectDeploymentDiagnosticDetails
from .connection import Connection
from .connection_assignment import ConnectionAssignment
from .connection_assignment_collection import ConnectionAssignmentCollection
from .connection_assignment_summary import ConnectionAssignmentSummary
from .connection_collection import ConnectionCollection
from .connection_summary import ConnectionSummary
from .copy_deployment_backup_details import CopyDeploymentBackupDetails
from .create_amazon_kinesis_connection_details import CreateAmazonKinesisConnectionDetails
from .create_amazon_redshift_connection_details import CreateAmazonRedshiftConnectionDetails
from .create_amazon_s3_connection_details import CreateAmazonS3ConnectionDetails
from .create_azure_data_lake_storage_connection_details import CreateAzureDataLakeStorageConnectionDetails
from .create_azure_synapse_connection_details import CreateAzureSynapseConnectionDetails
from .create_certificate_details import CreateCertificateDetails
from .create_connection_assignment_details import CreateConnectionAssignmentDetails
from .create_connection_details import CreateConnectionDetails
from .create_database_registration_details import CreateDatabaseRegistrationDetails
from .create_db2_connection_details import CreateDb2ConnectionDetails
from .create_deployment_backup_details import CreateDeploymentBackupDetails
from .create_deployment_details import CreateDeploymentDetails
from .create_elasticsearch_connection_details import CreateElasticsearchConnectionDetails
from .create_generic_connection_details import CreateGenericConnectionDetails
from .create_golden_gate_connection_details import CreateGoldenGateConnectionDetails
from .create_google_big_query_connection_details import CreateGoogleBigQueryConnectionDetails
from .create_google_cloud_storage_connection_details import CreateGoogleCloudStorageConnectionDetails
from .create_hdfs_connection_details import CreateHdfsConnectionDetails
from .create_java_message_service_connection_details import CreateJavaMessageServiceConnectionDetails
from .create_kafka_connection_details import CreateKafkaConnectionDetails
from .create_kafka_schema_registry_connection_details import CreateKafkaSchemaRegistryConnectionDetails
from .create_maintenance_configuration_details import CreateMaintenanceConfigurationDetails
from .create_maintenance_window_details import CreateMaintenanceWindowDetails
from .create_microsoft_sqlserver_connection_details import CreateMicrosoftSqlserverConnectionDetails
from .create_mongo_db_connection_details import CreateMongoDbConnectionDetails
from .create_mysql_connection_details import CreateMysqlConnectionDetails
from .create_oci_object_storage_connection_details import CreateOciObjectStorageConnectionDetails
from .create_ogg_deployment_details import CreateOggDeploymentDetails
from .create_oracle_connection_details import CreateOracleConnectionDetails
from .create_oracle_nosql_connection_details import CreateOracleNosqlConnectionDetails
from .create_postgresql_connection_details import CreatePostgresqlConnectionDetails
from .create_redis_connection_details import CreateRedisConnectionDetails
from .create_snowflake_connection_details import CreateSnowflakeConnectionDetails
from .database_registration import DatabaseRegistration
from .database_registration_collection import DatabaseRegistrationCollection
from .database_registration_summary import DatabaseRegistrationSummary
from .db2_connection import Db2Connection
from .db2_connection_summary import Db2ConnectionSummary
from .default_cancel_deployment_backup_details import DefaultCancelDeploymentBackupDetails
from .default_cancel_deployment_upgrade_details import DefaultCancelDeploymentUpgradeDetails
from .default_cancel_snooze_deployment_upgrade_details import DefaultCancelSnoozeDeploymentUpgradeDetails
from .default_deployment_wallet_exists_details import DefaultDeploymentWalletExistsDetails
from .default_restore_deployment_details import DefaultRestoreDeploymentDetails
from .default_rollback_deployment_upgrade_details import DefaultRollbackDeploymentUpgradeDetails
from .default_snooze_deployment_upgrade_details import DefaultSnoozeDeploymentUpgradeDetails
from .default_start_deployment_details import DefaultStartDeploymentDetails
from .default_stop_deployment_details import DefaultStopDeploymentDetails
from .default_test_connection_assignment_details import DefaultTestConnectionAssignmentDetails
from .default_upgrade_deployment_upgrade_details import DefaultUpgradeDeploymentUpgradeDetails
from .deployment import Deployment
from .deployment_backup import DeploymentBackup
from .deployment_backup_collection import DeploymentBackupCollection
from .deployment_backup_summary import DeploymentBackupSummary
from .deployment_collection import DeploymentCollection
from .deployment_diagnostic_data import DeploymentDiagnosticData
from .deployment_message_collection import DeploymentMessageCollection
from .deployment_summary import DeploymentSummary
from .deployment_type_collection import DeploymentTypeCollection
from .deployment_type_summary import DeploymentTypeSummary
from .deployment_upgrade import DeploymentUpgrade
from .deployment_upgrade_collection import DeploymentUpgradeCollection
from .deployment_upgrade_summary import DeploymentUpgradeSummary
from .deployment_version_collection import DeploymentVersionCollection
from .deployment_version_summary import DeploymentVersionSummary
from .deployment_wallet_exists_details import DeploymentWalletExistsDetails
from .deployment_wallet_exists_response_details import DeploymentWalletExistsResponseDetails
from .deployment_wallets_operation_collection import DeploymentWalletsOperationCollection
from .deployment_wallets_operation_summary import DeploymentWalletsOperationSummary
from .elasticsearch_connection import ElasticsearchConnection
from .elasticsearch_connection_summary import ElasticsearchConnectionSummary
from .export_deployment_wallet_details import ExportDeploymentWalletDetails
from .generate_library_url_details import GenerateLibraryUrlDetails
from .generate_log_reader_component_library_url_details import GenerateLogReaderComponentLibraryUrlDetails
from .generic_connection import GenericConnection
from .generic_connection_summary import GenericConnectionSummary
from .golden_gate_connection import GoldenGateConnection
from .golden_gate_connection_summary import GoldenGateConnectionSummary
from .google_big_query_connection import GoogleBigQueryConnection
from .google_big_query_connection_summary import GoogleBigQueryConnectionSummary
from .google_cloud_storage_connection import GoogleCloudStorageConnection
from .google_cloud_storage_connection_summary import GoogleCloudStorageConnectionSummary
from .hdfs_connection import HdfsConnection
from .hdfs_connection_summary import HdfsConnectionSummary
from .import_deployment_wallet_details import ImportDeploymentWalletDetails
from .ingress_ip_details import IngressIpDetails
from .java_message_service_connection import JavaMessageServiceConnection
from .java_message_service_connection_summary import JavaMessageServiceConnectionSummary
from .kafka_bootstrap_server import KafkaBootstrapServer
from .kafka_connection import KafkaConnection
from .kafka_connection_summary import KafkaConnectionSummary
from .kafka_schema_registry_connection import KafkaSchemaRegistryConnection
from .kafka_schema_registry_connection_summary import KafkaSchemaRegistryConnectionSummary
from .library_url import LibraryUrl
from .maintenance_configuration import MaintenanceConfiguration
from .maintenance_window import MaintenanceWindow
from .message_summary import MessageSummary
from .microsoft_sqlserver_connection import MicrosoftSqlserverConnection
from .microsoft_sqlserver_connection_summary import MicrosoftSqlserverConnectionSummary
from .mongo_db_connection import MongoDbConnection
from .mongo_db_connection_summary import MongoDbConnectionSummary
from .mysql_connection import MysqlConnection
from .mysql_connection_summary import MysqlConnectionSummary
from .name_value_pair import NameValuePair
from .oci_object_storage_connection import OciObjectStorageConnection
from .oci_object_storage_connection_summary import OciObjectStorageConnectionSummary
from .ogg_deployment import OggDeployment
from .oracle_connection import OracleConnection
from .oracle_connection_summary import OracleConnectionSummary
from .oracle_nosql_connection import OracleNosqlConnection
from .oracle_nosql_connection_summary import OracleNosqlConnectionSummary
from .postgresql_connection import PostgresqlConnection
from .postgresql_connection_summary import PostgresqlConnectionSummary
from .redis_connection import RedisConnection
from .redis_connection_summary import RedisConnectionSummary
from .remove_resource_lock_details import RemoveResourceLockDetails
from .reschedule_deployment_upgrade_details import RescheduleDeploymentUpgradeDetails
from .reschedule_deployment_upgrade_to_date_details import RescheduleDeploymentUpgradeToDateDetails
from .resource_lock import ResourceLock
from .restore_deployment_details import RestoreDeploymentDetails
from .rollback_deployment_upgrade_details import RollbackDeploymentUpgradeDetails
from .snooze_deployment_upgrade_details import SnoozeDeploymentUpgradeDetails
from .snowflake_connection import SnowflakeConnection
from .snowflake_connection_summary import SnowflakeConnectionSummary
from .start_deployment_details import StartDeploymentDetails
from .stop_deployment_details import StopDeploymentDetails
from .test_connection_assignment_details import TestConnectionAssignmentDetails
from .test_connection_assignment_error import TestConnectionAssignmentError
from .test_connection_assignment_result import TestConnectionAssignmentResult
from .trail_file_collection import TrailFileCollection
from .trail_file_summary import TrailFileSummary
from .trail_sequence_collection import TrailSequenceCollection
from .trail_sequence_summary import TrailSequenceSummary
from .update_amazon_kinesis_connection_details import UpdateAmazonKinesisConnectionDetails
from .update_amazon_redshift_connection_details import UpdateAmazonRedshiftConnectionDetails
from .update_amazon_s3_connection_details import UpdateAmazonS3ConnectionDetails
from .update_azure_data_lake_storage_connection_details import UpdateAzureDataLakeStorageConnectionDetails
from .update_azure_synapse_connection_details import UpdateAzureSynapseConnectionDetails
from .update_connection_details import UpdateConnectionDetails
from .update_database_registration_details import UpdateDatabaseRegistrationDetails
from .update_db2_connection_details import UpdateDb2ConnectionDetails
from .update_deployment_backup_details import UpdateDeploymentBackupDetails
from .update_deployment_details import UpdateDeploymentDetails
from .update_elasticsearch_connection_details import UpdateElasticsearchConnectionDetails
from .update_generic_connection_details import UpdateGenericConnectionDetails
from .update_golden_gate_connection_details import UpdateGoldenGateConnectionDetails
from .update_google_big_query_connection_details import UpdateGoogleBigQueryConnectionDetails
from .update_google_cloud_storage_connection_details import UpdateGoogleCloudStorageConnectionDetails
from .update_hdfs_connection_details import UpdateHdfsConnectionDetails
from .update_java_message_service_connection_details import UpdateJavaMessageServiceConnectionDetails
from .update_kafka_connection_details import UpdateKafkaConnectionDetails
from .update_kafka_schema_registry_connection_details import UpdateKafkaSchemaRegistryConnectionDetails
from .update_maintenance_configuration_details import UpdateMaintenanceConfigurationDetails
from .update_maintenance_window_details import UpdateMaintenanceWindowDetails
from .update_microsoft_sqlserver_connection_details import UpdateMicrosoftSqlserverConnectionDetails
from .update_mongo_db_connection_details import UpdateMongoDbConnectionDetails
from .update_mysql_connection_details import UpdateMysqlConnectionDetails
from .update_oci_object_storage_connection_details import UpdateOciObjectStorageConnectionDetails
from .update_ogg_deployment_details import UpdateOggDeploymentDetails
from .update_oracle_connection_details import UpdateOracleConnectionDetails
from .update_oracle_nosql_connection_details import UpdateOracleNosqlConnectionDetails
from .update_postgresql_connection_details import UpdatePostgresqlConnectionDetails
from .update_redis_connection_details import UpdateRedisConnectionDetails
from .update_snowflake_connection_details import UpdateSnowflakeConnectionDetails
from .upgrade_deployment_current_release_details import UpgradeDeploymentCurrentReleaseDetails
from .upgrade_deployment_details import UpgradeDeploymentDetails
from .upgrade_deployment_specific_release_details import UpgradeDeploymentSpecificReleaseDetails
from .upgrade_deployment_upgrade_details import UpgradeDeploymentUpgradeDetails
from .work_request import WorkRequest
from .work_request_error import WorkRequestError
from .work_request_log_entry import WorkRequestLogEntry
from .work_request_resource import WorkRequestResource

# Maps type names to classes for golden_gate services.
golden_gate_type_mapping = {
    "AddResourceLockDetails": AddResourceLockDetails,
    "AmazonKinesisConnection": AmazonKinesisConnection,
    "AmazonKinesisConnectionSummary": AmazonKinesisConnectionSummary,
    "AmazonRedshiftConnection": AmazonRedshiftConnection,
    "AmazonRedshiftConnectionSummary": AmazonRedshiftConnectionSummary,
    "AmazonS3Connection": AmazonS3Connection,
    "AmazonS3ConnectionSummary": AmazonS3ConnectionSummary,
    "AzureDataLakeStorageConnection": AzureDataLakeStorageConnection,
    "AzureDataLakeStorageConnectionSummary": AzureDataLakeStorageConnectionSummary,
    "AzureSynapseConnection": AzureSynapseConnection,
    "AzureSynapseConnectionSummary": AzureSynapseConnectionSummary,
    "CancelDeploymentBackupDetails": CancelDeploymentBackupDetails,
    "CancelDeploymentUpgradeDetails": CancelDeploymentUpgradeDetails,
    "CancelSnoozeDeploymentUpgradeDetails": CancelSnoozeDeploymentUpgradeDetails,
    "Certificate": Certificate,
    "CertificateCollection": CertificateCollection,
    "CertificateSummary": CertificateSummary,
    "ChangeConnectionCompartmentDetails": ChangeConnectionCompartmentDetails,
    "ChangeDatabaseRegistrationCompartmentDetails": ChangeDatabaseRegistrationCompartmentDetails,
    "ChangeDeploymentBackupCompartmentDetails": ChangeDeploymentBackupCompartmentDetails,
    "ChangeDeploymentCompartmentDetails": ChangeDeploymentCompartmentDetails,
    "CollectDeploymentDiagnosticDetails": CollectDeploymentDiagnosticDetails,
    "Connection": Connection,
    "ConnectionAssignment": ConnectionAssignment,
    "ConnectionAssignmentCollection": ConnectionAssignmentCollection,
    "ConnectionAssignmentSummary": ConnectionAssignmentSummary,
    "ConnectionCollection": ConnectionCollection,
    "ConnectionSummary": ConnectionSummary,
    "CopyDeploymentBackupDetails": CopyDeploymentBackupDetails,
    "CreateAmazonKinesisConnectionDetails": CreateAmazonKinesisConnectionDetails,
    "CreateAmazonRedshiftConnectionDetails": CreateAmazonRedshiftConnectionDetails,
    "CreateAmazonS3ConnectionDetails": CreateAmazonS3ConnectionDetails,
    "CreateAzureDataLakeStorageConnectionDetails": CreateAzureDataLakeStorageConnectionDetails,
    "CreateAzureSynapseConnectionDetails": CreateAzureSynapseConnectionDetails,
    "CreateCertificateDetails": CreateCertificateDetails,
    "CreateConnectionAssignmentDetails": CreateConnectionAssignmentDetails,
    "CreateConnectionDetails": CreateConnectionDetails,
    "CreateDatabaseRegistrationDetails": CreateDatabaseRegistrationDetails,
    "CreateDb2ConnectionDetails": CreateDb2ConnectionDetails,
    "CreateDeploymentBackupDetails": CreateDeploymentBackupDetails,
    "CreateDeploymentDetails": CreateDeploymentDetails,
    "CreateElasticsearchConnectionDetails": CreateElasticsearchConnectionDetails,
    "CreateGenericConnectionDetails": CreateGenericConnectionDetails,
    "CreateGoldenGateConnectionDetails": CreateGoldenGateConnectionDetails,
    "CreateGoogleBigQueryConnectionDetails": CreateGoogleBigQueryConnectionDetails,
    "CreateGoogleCloudStorageConnectionDetails": CreateGoogleCloudStorageConnectionDetails,
    "CreateHdfsConnectionDetails": CreateHdfsConnectionDetails,
    "CreateJavaMessageServiceConnectionDetails": CreateJavaMessageServiceConnectionDetails,
    "CreateKafkaConnectionDetails": CreateKafkaConnectionDetails,
    "CreateKafkaSchemaRegistryConnectionDetails": CreateKafkaSchemaRegistryConnectionDetails,
    "CreateMaintenanceConfigurationDetails": CreateMaintenanceConfigurationDetails,
    "CreateMaintenanceWindowDetails": CreateMaintenanceWindowDetails,
    "CreateMicrosoftSqlserverConnectionDetails": CreateMicrosoftSqlserverConnectionDetails,
    "CreateMongoDbConnectionDetails": CreateMongoDbConnectionDetails,
    "CreateMysqlConnectionDetails": CreateMysqlConnectionDetails,
    "CreateOciObjectStorageConnectionDetails": CreateOciObjectStorageConnectionDetails,
    "CreateOggDeploymentDetails": CreateOggDeploymentDetails,
    "CreateOracleConnectionDetails": CreateOracleConnectionDetails,
    "CreateOracleNosqlConnectionDetails": CreateOracleNosqlConnectionDetails,
    "CreatePostgresqlConnectionDetails": CreatePostgresqlConnectionDetails,
    "CreateRedisConnectionDetails": CreateRedisConnectionDetails,
    "CreateSnowflakeConnectionDetails": CreateSnowflakeConnectionDetails,
    "DatabaseRegistration": DatabaseRegistration,
    "DatabaseRegistrationCollection": DatabaseRegistrationCollection,
    "DatabaseRegistrationSummary": DatabaseRegistrationSummary,
    "Db2Connection": Db2Connection,
    "Db2ConnectionSummary": Db2ConnectionSummary,
    "DefaultCancelDeploymentBackupDetails": DefaultCancelDeploymentBackupDetails,
    "DefaultCancelDeploymentUpgradeDetails": DefaultCancelDeploymentUpgradeDetails,
    "DefaultCancelSnoozeDeploymentUpgradeDetails": DefaultCancelSnoozeDeploymentUpgradeDetails,
    "DefaultDeploymentWalletExistsDetails": DefaultDeploymentWalletExistsDetails,
    "DefaultRestoreDeploymentDetails": DefaultRestoreDeploymentDetails,
    "DefaultRollbackDeploymentUpgradeDetails": DefaultRollbackDeploymentUpgradeDetails,
    "DefaultSnoozeDeploymentUpgradeDetails": DefaultSnoozeDeploymentUpgradeDetails,
    "DefaultStartDeploymentDetails": DefaultStartDeploymentDetails,
    "DefaultStopDeploymentDetails": DefaultStopDeploymentDetails,
    "DefaultTestConnectionAssignmentDetails": DefaultTestConnectionAssignmentDetails,
    "DefaultUpgradeDeploymentUpgradeDetails": DefaultUpgradeDeploymentUpgradeDetails,
    "Deployment": Deployment,
    "DeploymentBackup": DeploymentBackup,
    "DeploymentBackupCollection": DeploymentBackupCollection,
    "DeploymentBackupSummary": DeploymentBackupSummary,
    "DeploymentCollection": DeploymentCollection,
    "DeploymentDiagnosticData": DeploymentDiagnosticData,
    "DeploymentMessageCollection": DeploymentMessageCollection,
    "DeploymentSummary": DeploymentSummary,
    "DeploymentTypeCollection": DeploymentTypeCollection,
    "DeploymentTypeSummary": DeploymentTypeSummary,
    "DeploymentUpgrade": DeploymentUpgrade,
    "DeploymentUpgradeCollection": DeploymentUpgradeCollection,
    "DeploymentUpgradeSummary": DeploymentUpgradeSummary,
    "DeploymentVersionCollection": DeploymentVersionCollection,
    "DeploymentVersionSummary": DeploymentVersionSummary,
    "DeploymentWalletExistsDetails": DeploymentWalletExistsDetails,
    "DeploymentWalletExistsResponseDetails": DeploymentWalletExistsResponseDetails,
    "DeploymentWalletsOperationCollection": DeploymentWalletsOperationCollection,
    "DeploymentWalletsOperationSummary": DeploymentWalletsOperationSummary,
    "ElasticsearchConnection": ElasticsearchConnection,
    "ElasticsearchConnectionSummary": ElasticsearchConnectionSummary,
    "ExportDeploymentWalletDetails": ExportDeploymentWalletDetails,
    "GenerateLibraryUrlDetails": GenerateLibraryUrlDetails,
    "GenerateLogReaderComponentLibraryUrlDetails": GenerateLogReaderComponentLibraryUrlDetails,
    "GenericConnection": GenericConnection,
    "GenericConnectionSummary": GenericConnectionSummary,
    "GoldenGateConnection": GoldenGateConnection,
    "GoldenGateConnectionSummary": GoldenGateConnectionSummary,
    "GoogleBigQueryConnection": GoogleBigQueryConnection,
    "GoogleBigQueryConnectionSummary": GoogleBigQueryConnectionSummary,
    "GoogleCloudStorageConnection": GoogleCloudStorageConnection,
    "GoogleCloudStorageConnectionSummary": GoogleCloudStorageConnectionSummary,
    "HdfsConnection": HdfsConnection,
    "HdfsConnectionSummary": HdfsConnectionSummary,
    "ImportDeploymentWalletDetails": ImportDeploymentWalletDetails,
    "IngressIpDetails": IngressIpDetails,
    "JavaMessageServiceConnection": JavaMessageServiceConnection,
    "JavaMessageServiceConnectionSummary": JavaMessageServiceConnectionSummary,
    "KafkaBootstrapServer": KafkaBootstrapServer,
    "KafkaConnection": KafkaConnection,
    "KafkaConnectionSummary": KafkaConnectionSummary,
    "KafkaSchemaRegistryConnection": KafkaSchemaRegistryConnection,
    "KafkaSchemaRegistryConnectionSummary": KafkaSchemaRegistryConnectionSummary,
    "LibraryUrl": LibraryUrl,
    "MaintenanceConfiguration": MaintenanceConfiguration,
    "MaintenanceWindow": MaintenanceWindow,
    "MessageSummary": MessageSummary,
    "MicrosoftSqlserverConnection": MicrosoftSqlserverConnection,
    "MicrosoftSqlserverConnectionSummary": MicrosoftSqlserverConnectionSummary,
    "MongoDbConnection": MongoDbConnection,
    "MongoDbConnectionSummary": MongoDbConnectionSummary,
    "MysqlConnection": MysqlConnection,
    "MysqlConnectionSummary": MysqlConnectionSummary,
    "NameValuePair": NameValuePair,
    "OciObjectStorageConnection": OciObjectStorageConnection,
    "OciObjectStorageConnectionSummary": OciObjectStorageConnectionSummary,
    "OggDeployment": OggDeployment,
    "OracleConnection": OracleConnection,
    "OracleConnectionSummary": OracleConnectionSummary,
    "OracleNosqlConnection": OracleNosqlConnection,
    "OracleNosqlConnectionSummary": OracleNosqlConnectionSummary,
    "PostgresqlConnection": PostgresqlConnection,
    "PostgresqlConnectionSummary": PostgresqlConnectionSummary,
    "RedisConnection": RedisConnection,
    "RedisConnectionSummary": RedisConnectionSummary,
    "RemoveResourceLockDetails": RemoveResourceLockDetails,
    "RescheduleDeploymentUpgradeDetails": RescheduleDeploymentUpgradeDetails,
    "RescheduleDeploymentUpgradeToDateDetails": RescheduleDeploymentUpgradeToDateDetails,
    "ResourceLock": ResourceLock,
    "RestoreDeploymentDetails": RestoreDeploymentDetails,
    "RollbackDeploymentUpgradeDetails": RollbackDeploymentUpgradeDetails,
    "SnoozeDeploymentUpgradeDetails": SnoozeDeploymentUpgradeDetails,
    "SnowflakeConnection": SnowflakeConnection,
    "SnowflakeConnectionSummary": SnowflakeConnectionSummary,
    "StartDeploymentDetails": StartDeploymentDetails,
    "StopDeploymentDetails": StopDeploymentDetails,
    "TestConnectionAssignmentDetails": TestConnectionAssignmentDetails,
    "TestConnectionAssignmentError": TestConnectionAssignmentError,
    "TestConnectionAssignmentResult": TestConnectionAssignmentResult,
    "TrailFileCollection": TrailFileCollection,
    "TrailFileSummary": TrailFileSummary,
    "TrailSequenceCollection": TrailSequenceCollection,
    "TrailSequenceSummary": TrailSequenceSummary,
    "UpdateAmazonKinesisConnectionDetails": UpdateAmazonKinesisConnectionDetails,
    "UpdateAmazonRedshiftConnectionDetails": UpdateAmazonRedshiftConnectionDetails,
    "UpdateAmazonS3ConnectionDetails": UpdateAmazonS3ConnectionDetails,
    "UpdateAzureDataLakeStorageConnectionDetails": UpdateAzureDataLakeStorageConnectionDetails,
    "UpdateAzureSynapseConnectionDetails": UpdateAzureSynapseConnectionDetails,
    "UpdateConnectionDetails": UpdateConnectionDetails,
    "UpdateDatabaseRegistrationDetails": UpdateDatabaseRegistrationDetails,
    "UpdateDb2ConnectionDetails": UpdateDb2ConnectionDetails,
    "UpdateDeploymentBackupDetails": UpdateDeploymentBackupDetails,
    "UpdateDeploymentDetails": UpdateDeploymentDetails,
    "UpdateElasticsearchConnectionDetails": UpdateElasticsearchConnectionDetails,
    "UpdateGenericConnectionDetails": UpdateGenericConnectionDetails,
    "UpdateGoldenGateConnectionDetails": UpdateGoldenGateConnectionDetails,
    "UpdateGoogleBigQueryConnectionDetails": UpdateGoogleBigQueryConnectionDetails,
    "UpdateGoogleCloudStorageConnectionDetails": UpdateGoogleCloudStorageConnectionDetails,
    "UpdateHdfsConnectionDetails": UpdateHdfsConnectionDetails,
    "UpdateJavaMessageServiceConnectionDetails": UpdateJavaMessageServiceConnectionDetails,
    "UpdateKafkaConnectionDetails": UpdateKafkaConnectionDetails,
    "UpdateKafkaSchemaRegistryConnectionDetails": UpdateKafkaSchemaRegistryConnectionDetails,
    "UpdateMaintenanceConfigurationDetails": UpdateMaintenanceConfigurationDetails,
    "UpdateMaintenanceWindowDetails": UpdateMaintenanceWindowDetails,
    "UpdateMicrosoftSqlserverConnectionDetails": UpdateMicrosoftSqlserverConnectionDetails,
    "UpdateMongoDbConnectionDetails": UpdateMongoDbConnectionDetails,
    "UpdateMysqlConnectionDetails": UpdateMysqlConnectionDetails,
    "UpdateOciObjectStorageConnectionDetails": UpdateOciObjectStorageConnectionDetails,
    "UpdateOggDeploymentDetails": UpdateOggDeploymentDetails,
    "UpdateOracleConnectionDetails": UpdateOracleConnectionDetails,
    "UpdateOracleNosqlConnectionDetails": UpdateOracleNosqlConnectionDetails,
    "UpdatePostgresqlConnectionDetails": UpdatePostgresqlConnectionDetails,
    "UpdateRedisConnectionDetails": UpdateRedisConnectionDetails,
    "UpdateSnowflakeConnectionDetails": UpdateSnowflakeConnectionDetails,
    "UpgradeDeploymentCurrentReleaseDetails": UpgradeDeploymentCurrentReleaseDetails,
    "UpgradeDeploymentDetails": UpgradeDeploymentDetails,
    "UpgradeDeploymentSpecificReleaseDetails": UpgradeDeploymentSpecificReleaseDetails,
    "UpgradeDeploymentUpgradeDetails": UpgradeDeploymentUpgradeDetails,
    "WorkRequest": WorkRequest,
    "WorkRequestError": WorkRequestError,
    "WorkRequestLogEntry": WorkRequestLogEntry,
    "WorkRequestResource": WorkRequestResource
}
