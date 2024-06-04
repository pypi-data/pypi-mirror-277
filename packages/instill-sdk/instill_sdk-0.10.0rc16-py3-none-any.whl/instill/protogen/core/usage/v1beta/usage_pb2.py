# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: core/usage/v1beta/usage.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from common.healthcheck.v1beta import healthcheck_pb2 as common_dot_healthcheck_dot_v1beta_dot_healthcheck__pb2
from common.task.v1alpha import task_pb2 as common_dot_task_dot_v1alpha_dot_task__pb2
from core.mgmt.v1beta import metric_pb2 as core_dot_mgmt_dot_v1beta_dot_metric__pb2
from core.mgmt.v1beta import mgmt_pb2 as core_dot_mgmt_dot_v1beta_dot_mgmt__pb2
from google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1d\x63ore/usage/v1beta/usage.proto\x12\x11\x63ore.usage.v1beta\x1a+common/healthcheck/v1beta/healthcheck.proto\x1a\x1e\x63ommon/task/v1alpha/task.proto\x1a\x1d\x63ore/mgmt/v1beta/metric.proto\x1a\x1b\x63ore/mgmt/v1beta/mgmt.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a\x1fgoogle/protobuf/timestamp.proto\"\x96\x01\n\x0fLivenessRequest\x12j\n\x14health_check_request\x18\x01 \x01(\x0b\x32-.common.healthcheck.v1beta.HealthCheckRequestB\x04\xe2\x41\x01\x01H\x00R\x12healthCheckRequest\x88\x01\x01\x42\x17\n\x15_health_check_request\"v\n\x10LivenessResponse\x12\x62\n\x15health_check_response\x18\x01 \x01(\x0b\x32..common.healthcheck.v1beta.HealthCheckResponseR\x13healthCheckResponse\"\x97\x01\n\x10ReadinessRequest\x12j\n\x14health_check_request\x18\x01 \x01(\x0b\x32-.common.healthcheck.v1beta.HealthCheckRequestB\x04\xe2\x41\x01\x01H\x00R\x12healthCheckRequest\x88\x01\x01\x42\x17\n\x15_health_check_request\"w\n\x11ReadinessResponse\x12\x62\n\x15health_check_response\x18\x01 \x01(\x0b\x32..common.healthcheck.v1beta.HealthCheckResponseR\x13healthCheckResponse\"\xd5\x05\n\x07Session\x12\x18\n\x04name\x18\x01 \x01(\tB\x04\xe2\x41\x01\x03R\x04name\x12\x16\n\x03uid\x18\x02 \x01(\tB\x04\xe2\x41\x01\x03R\x03uid\x12\x42\n\x07service\x18\x03 \x01(\x0e\x32\".core.usage.v1beta.Session.ServiceB\x04\xe2\x41\x01\x02R\x07service\x12\x1e\n\x07\x65\x64ition\x18\x04 \x01(\tB\x04\xe2\x41\x01\x02R\x07\x65\x64ition\x12\x1e\n\x07version\x18\x05 \x01(\tB\x04\xe2\x41\x01\x02R\x07version\x12\x18\n\x04\x61rch\x18\x06 \x01(\tB\x04\xe2\x41\x01\x02R\x04\x61rch\x12\x14\n\x02os\x18\x07 \x01(\tB\x04\xe2\x41\x01\x02R\x02os\x12\x1c\n\x06uptime\x18\x08 \x01(\x03\x42\x04\xe2\x41\x01\x02R\x06uptime\x12\x41\n\x0breport_time\x18\t \x01(\x0b\x32\x1a.google.protobuf.TimestampB\x04\xe2\x41\x01\x02R\nreportTime\x12\x1a\n\x05token\x18\n \x01(\tB\x04\xe2\x41\x01\x03R\x05token\x12\x41\n\x0b\x63reate_time\x18\x0b \x01(\x0b\x32\x1a.google.protobuf.TimestampB\x04\xe2\x41\x01\x03R\ncreateTime\x12\x41\n\x0bupdate_time\x18\x0c \x01(\x0b\x32\x1a.google.protobuf.TimestampB\x04\xe2\x41\x01\x03R\nupdateTime\x12!\n\towner_uid\x18\r \x01(\tB\x04\xe2\x41\x01\x02R\x08ownerUid\"\x8a\x01\n\x07Service\x12\x17\n\x13SERVICE_UNSPECIFIED\x10\x00\x12\x10\n\x0cSERVICE_MGMT\x10\x01\x12\x15\n\x11SERVICE_CONNECTOR\x10\x02\x12\x11\n\rSERVICE_MODEL\x10\x03\x12\x14\n\x10SERVICE_PIPELINE\x10\x04\x12\x14\n\x10SERVICE_ARTIFACT\x10\x05:1\xea\x41.\n\x18\x61pi.instill.tech/Session\x12\x12sessions/{session}\"\x94\x01\n\rMgmtUsageData\x12\x44\n\x0buser_usages\x18\x01 \x03(\x0b\x32#.core.mgmt.v1beta.AuthenticatedUserR\nuserUsages\x12=\n\norg_usages\x18\x02 \x03(\x0b\x32\x1e.core.mgmt.v1beta.OrganizationR\torgUsages\"\xe8\x05\n\x12\x43onnectorUsageData\x12K\n\x06usages\x18\x01 \x03(\x0b\x32\x33.core.usage.v1beta.ConnectorUsageData.UserUsageDataR\x06usages\x1a\x84\x05\n\rUserUsageData\x12!\n\towner_uid\x18\x01 \x01(\tB\x04\xe2\x41\x01\x02R\x08ownerUid\x12\x84\x01\n\x16\x63onnector_execute_data\x18\x02 \x03(\x0b\x32H.core.usage.v1beta.ConnectorUsageData.UserUsageData.ConnectorExecuteDataB\x04\xe2\x41\x01\x02R\x14\x63onnectorExecuteData\x12@\n\nowner_type\x18\x03 \x01(\x0e\x32\x1b.core.mgmt.v1beta.OwnerTypeB\x04\xe2\x41\x01\x02R\townerType\x1a\x86\x03\n\x14\x43onnectorExecuteData\x12)\n\rconnector_uid\x18\x01 \x01(\tB\x04\xe2\x41\x01\x02R\x0c\x63onnectorUid\x12%\n\x0b\x65xecute_uid\x18\x02 \x01(\tB\x04\xe2\x41\x01\x02R\nexecuteUid\x12\x43\n\x0c\x65xecute_time\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.TimestampB\x04\xe2\x41\x01\x02R\x0b\x65xecuteTime\x12>\n\x18\x63onnector_definition_uid\x18\x04 \x01(\tB\x04\xe2\x41\x01\x02R\x16\x63onnectorDefinitionUid\x12\x36\n\x06status\x18\x05 \x01(\x0e\x32\x18.core.mgmt.v1beta.StatusB\x04\xe2\x41\x01\x02R\x06status\x12\x1f\n\x08user_uid\x18\x08 \x01(\tB\x04\xe2\x41\x01\x02R\x07userUid\x12>\n\tuser_type\x18\t \x01(\x0e\x32\x1b.core.mgmt.v1beta.OwnerTypeB\x04\xe2\x41\x01\x02R\x08userType\"\xfb\x05\n\x0eModelUsageData\x12G\n\x06usages\x18\x01 \x03(\x0b\x32/.core.usage.v1beta.ModelUsageData.UserUsageDataR\x06usages\x1a\x9f\x05\n\rUserUsageData\x12!\n\towner_uid\x18\x01 \x01(\tB\x04\xe2\x41\x01\x02R\x08ownerUid\x12t\n\x12model_trigger_data\x18\x02 \x03(\x0b\x32@.core.usage.v1beta.ModelUsageData.UserUsageData.ModelTriggerDataB\x04\xe2\x41\x01\x02R\x10modelTriggerData\x12@\n\nowner_type\x18\x03 \x01(\x0e\x32\x1b.core.mgmt.v1beta.OwnerTypeB\x04\xe2\x41\x01\x02R\townerType\x1a\xb2\x03\n\x10ModelTriggerData\x12!\n\tmodel_uid\x18\x01 \x01(\tB\x04\xe2\x41\x01\x02R\x08modelUid\x12%\n\x0btrigger_uid\x18\x02 \x01(\tB\x04\xe2\x41\x01\x02R\ntriggerUid\x12\x43\n\x0ctrigger_time\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.TimestampB\x04\xe2\x41\x01\x02R\x0btriggerTime\x12\x36\n\x14model_definition_uid\x18\x04 \x01(\tB\x04\xe2\x41\x01\x02R\x12modelDefinitionUid\x12>\n\nmodel_task\x18\x05 \x01(\x0e\x32\x19.common.task.v1alpha.TaskB\x04\xe2\x41\x01\x02R\tmodelTask\x12\x36\n\x06status\x18\x06 \x01(\x0e\x32\x18.core.mgmt.v1beta.StatusB\x04\xe2\x41\x01\x02R\x06status\x12\x1f\n\x08user_uid\x18\x07 \x01(\tB\x04\xe2\x41\x01\x02R\x07userUid\x12>\n\tuser_type\x18\x08 \x01(\x0e\x32\x1b.core.mgmt.v1beta.OwnerTypeB\x04\xe2\x41\x01\x02R\x08userType\"\xf5\x06\n\x11PipelineUsageData\x12J\n\x06usages\x18\x01 \x03(\x0b\x32\x32.core.usage.v1beta.PipelineUsageData.UserUsageDataR\x06usages\x1a\x93\x06\n\rUserUsageData\x12!\n\towner_uid\x18\x01 \x01(\tB\x04\xe2\x41\x01\x02R\x08ownerUid\x12\x80\x01\n\x15pipeline_trigger_data\x18\x02 \x03(\x0b\x32\x46.core.usage.v1beta.PipelineUsageData.UserUsageData.PipelineTriggerDataB\x04\xe2\x41\x01\x02R\x13pipelineTriggerData\x12@\n\nowner_type\x18\x03 \x01(\x0e\x32\x1b.core.mgmt.v1beta.OwnerTypeB\x04\xe2\x41\x01\x02R\townerType\x1a\x99\x04\n\x13PipelineTriggerData\x12\'\n\x0cpipeline_uid\x18\x01 \x01(\tB\x04\xe2\x41\x01\x02R\x0bpipelineUid\x12%\n\x0btrigger_uid\x18\x02 \x01(\tB\x04\xe2\x41\x01\x02R\ntriggerUid\x12\x43\n\x0ctrigger_time\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.TimestampB\x04\xe2\x41\x01\x02R\x0btriggerTime\x12?\n\x0ctrigger_mode\x18\x04 \x01(\x0e\x32\x16.core.mgmt.v1beta.ModeB\x04\xe2\x41\x01\x02R\x0btriggerMode\x12\x36\n\x06status\x18\x05 \x01(\x0e\x32\x18.core.mgmt.v1beta.StatusB\x04\xe2\x41\x01\x02R\x06status\x12\x34\n\x13pipeline_release_id\x18\x06 \x01(\tB\x04\xe2\x41\x01\x02R\x11pipelineReleaseId\x12\x36\n\x14pipeline_release_uid\x18\x07 \x01(\tB\x04\xe2\x41\x01\x02R\x12pipelineReleaseUid\x12\x1f\n\x08user_uid\x18\x08 \x01(\tB\x04\xe2\x41\x01\x02R\x07userUid\x12>\n\tuser_type\x18\t \x01(\x0e\x32\x1b.core.mgmt.v1beta.OwnerTypeB\x04\xe2\x41\x01\x02R\x08userType\x12%\n\x0bpipeline_id\x18\n \x01(\tB\x04\xe2\x41\x01\x02R\npipelineId\"\xd5\x01\n\x11\x41rtifactUsageData\x12J\n\x06usages\x18\x01 \x03(\x0b\x32\x32.core.usage.v1beta.ArtifactUsageData.UserUsageDataR\x06usages\x1at\n\rUserUsageData\x12!\n\towner_uid\x18\x01 \x01(\tB\x04\xe2\x41\x01\x02R\x08ownerUid\x12@\n\nowner_type\x18\x02 \x01(\x0e\x32\x1b.core.mgmt.v1beta.OwnerTypeB\x04\xe2\x41\x01\x02R\townerType\"\xda\x04\n\rSessionReport\x12%\n\x0bsession_uid\x18\x01 \x01(\tB\x04\xe2\x41\x01\x02R\nsessionUid\x12\x1a\n\x05token\x18\x02 \x01(\tB\x04\xe2\x41\x01\x02R\x05token\x12\x16\n\x03pow\x18\x03 \x01(\tB\x04\xe2\x41\x01\x02R\x03pow\x12:\n\x07session\x18\x04 \x01(\x0b\x32\x1a.core.usage.v1beta.SessionB\x04\xe2\x41\x01\x02R\x07session\x12J\n\x0fmgmt_usage_data\x18\x05 \x01(\x0b\x32 .core.usage.v1beta.MgmtUsageDataH\x00R\rmgmtUsageData\x12Y\n\x14\x63onnector_usage_data\x18\x06 \x01(\x0b\x32%.core.usage.v1beta.ConnectorUsageDataH\x00R\x12\x63onnectorUsageData\x12M\n\x10model_usage_data\x18\x07 \x01(\x0b\x32!.core.usage.v1beta.ModelUsageDataH\x00R\x0emodelUsageData\x12V\n\x13pipeline_usage_data\x18\x08 \x01(\x0b\x32$.core.usage.v1beta.PipelineUsageDataH\x00R\x11pipelineUsageData\x12V\n\x13\x61rtifact_usage_data\x18\t \x01(\x0b\x32$.core.usage.v1beta.ArtifactUsageDataH\x00R\x11\x61rtifactUsageDataB\x0c\n\nusage_data\"R\n\x14\x43reateSessionRequest\x12:\n\x07session\x18\x01 \x01(\x0b\x32\x1a.core.usage.v1beta.SessionB\x04\xe2\x41\x01\x02R\x07session\"M\n\x15\x43reateSessionResponse\x12\x34\n\x07session\x18\x01 \x01(\x0b\x32\x1a.core.usage.v1beta.SessionR\x07session\"Z\n\x18SendSessionReportRequest\x12>\n\x06report\x18\x01 \x01(\x0b\x32 .core.usage.v1beta.SessionReportB\x04\xe2\x41\x01\x02R\x06report\"\x1b\n\x19SendSessionReportResponseB\xca\x01\n\x15\x63om.core.usage.v1betaB\nUsageProtoP\x01Z?github.com/instill-ai/protogen-go/core/usage/v1beta;usagev1beta\xa2\x02\x03\x43UX\xaa\x02\x11\x43ore.Usage.V1beta\xca\x02\x11\x43ore\\Usage\\V1beta\xe2\x02\x1d\x43ore\\Usage\\V1beta\\GPBMetadata\xea\x02\x13\x43ore::Usage::V1betab\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'core.usage.v1beta.usage_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\025com.core.usage.v1betaB\nUsageProtoP\001Z?github.com/instill-ai/protogen-go/core/usage/v1beta;usagev1beta\242\002\003CUX\252\002\021Core.Usage.V1beta\312\002\021Core\\Usage\\V1beta\342\002\035Core\\Usage\\V1beta\\GPBMetadata\352\002\023Core::Usage::V1beta'
  _LIVENESSREQUEST.fields_by_name['health_check_request']._options = None
  _LIVENESSREQUEST.fields_by_name['health_check_request']._serialized_options = b'\342A\001\001'
  _READINESSREQUEST.fields_by_name['health_check_request']._options = None
  _READINESSREQUEST.fields_by_name['health_check_request']._serialized_options = b'\342A\001\001'
  _SESSION.fields_by_name['name']._options = None
  _SESSION.fields_by_name['name']._serialized_options = b'\342A\001\003'
  _SESSION.fields_by_name['uid']._options = None
  _SESSION.fields_by_name['uid']._serialized_options = b'\342A\001\003'
  _SESSION.fields_by_name['service']._options = None
  _SESSION.fields_by_name['service']._serialized_options = b'\342A\001\002'
  _SESSION.fields_by_name['edition']._options = None
  _SESSION.fields_by_name['edition']._serialized_options = b'\342A\001\002'
  _SESSION.fields_by_name['version']._options = None
  _SESSION.fields_by_name['version']._serialized_options = b'\342A\001\002'
  _SESSION.fields_by_name['arch']._options = None
  _SESSION.fields_by_name['arch']._serialized_options = b'\342A\001\002'
  _SESSION.fields_by_name['os']._options = None
  _SESSION.fields_by_name['os']._serialized_options = b'\342A\001\002'
  _SESSION.fields_by_name['uptime']._options = None
  _SESSION.fields_by_name['uptime']._serialized_options = b'\342A\001\002'
  _SESSION.fields_by_name['report_time']._options = None
  _SESSION.fields_by_name['report_time']._serialized_options = b'\342A\001\002'
  _SESSION.fields_by_name['token']._options = None
  _SESSION.fields_by_name['token']._serialized_options = b'\342A\001\003'
  _SESSION.fields_by_name['create_time']._options = None
  _SESSION.fields_by_name['create_time']._serialized_options = b'\342A\001\003'
  _SESSION.fields_by_name['update_time']._options = None
  _SESSION.fields_by_name['update_time']._serialized_options = b'\342A\001\003'
  _SESSION.fields_by_name['owner_uid']._options = None
  _SESSION.fields_by_name['owner_uid']._serialized_options = b'\342A\001\002'
  _SESSION._options = None
  _SESSION._serialized_options = b'\352A.\n\030api.instill.tech/Session\022\022sessions/{session}'
  _CONNECTORUSAGEDATA_USERUSAGEDATA_CONNECTOREXECUTEDATA.fields_by_name['connector_uid']._options = None
  _CONNECTORUSAGEDATA_USERUSAGEDATA_CONNECTOREXECUTEDATA.fields_by_name['connector_uid']._serialized_options = b'\342A\001\002'
  _CONNECTORUSAGEDATA_USERUSAGEDATA_CONNECTOREXECUTEDATA.fields_by_name['execute_uid']._options = None
  _CONNECTORUSAGEDATA_USERUSAGEDATA_CONNECTOREXECUTEDATA.fields_by_name['execute_uid']._serialized_options = b'\342A\001\002'
  _CONNECTORUSAGEDATA_USERUSAGEDATA_CONNECTOREXECUTEDATA.fields_by_name['execute_time']._options = None
  _CONNECTORUSAGEDATA_USERUSAGEDATA_CONNECTOREXECUTEDATA.fields_by_name['execute_time']._serialized_options = b'\342A\001\002'
  _CONNECTORUSAGEDATA_USERUSAGEDATA_CONNECTOREXECUTEDATA.fields_by_name['connector_definition_uid']._options = None
  _CONNECTORUSAGEDATA_USERUSAGEDATA_CONNECTOREXECUTEDATA.fields_by_name['connector_definition_uid']._serialized_options = b'\342A\001\002'
  _CONNECTORUSAGEDATA_USERUSAGEDATA_CONNECTOREXECUTEDATA.fields_by_name['status']._options = None
  _CONNECTORUSAGEDATA_USERUSAGEDATA_CONNECTOREXECUTEDATA.fields_by_name['status']._serialized_options = b'\342A\001\002'
  _CONNECTORUSAGEDATA_USERUSAGEDATA_CONNECTOREXECUTEDATA.fields_by_name['user_uid']._options = None
  _CONNECTORUSAGEDATA_USERUSAGEDATA_CONNECTOREXECUTEDATA.fields_by_name['user_uid']._serialized_options = b'\342A\001\002'
  _CONNECTORUSAGEDATA_USERUSAGEDATA_CONNECTOREXECUTEDATA.fields_by_name['user_type']._options = None
  _CONNECTORUSAGEDATA_USERUSAGEDATA_CONNECTOREXECUTEDATA.fields_by_name['user_type']._serialized_options = b'\342A\001\002'
  _CONNECTORUSAGEDATA_USERUSAGEDATA.fields_by_name['owner_uid']._options = None
  _CONNECTORUSAGEDATA_USERUSAGEDATA.fields_by_name['owner_uid']._serialized_options = b'\342A\001\002'
  _CONNECTORUSAGEDATA_USERUSAGEDATA.fields_by_name['connector_execute_data']._options = None
  _CONNECTORUSAGEDATA_USERUSAGEDATA.fields_by_name['connector_execute_data']._serialized_options = b'\342A\001\002'
  _CONNECTORUSAGEDATA_USERUSAGEDATA.fields_by_name['owner_type']._options = None
  _CONNECTORUSAGEDATA_USERUSAGEDATA.fields_by_name['owner_type']._serialized_options = b'\342A\001\002'
  _MODELUSAGEDATA_USERUSAGEDATA_MODELTRIGGERDATA.fields_by_name['model_uid']._options = None
  _MODELUSAGEDATA_USERUSAGEDATA_MODELTRIGGERDATA.fields_by_name['model_uid']._serialized_options = b'\342A\001\002'
  _MODELUSAGEDATA_USERUSAGEDATA_MODELTRIGGERDATA.fields_by_name['trigger_uid']._options = None
  _MODELUSAGEDATA_USERUSAGEDATA_MODELTRIGGERDATA.fields_by_name['trigger_uid']._serialized_options = b'\342A\001\002'
  _MODELUSAGEDATA_USERUSAGEDATA_MODELTRIGGERDATA.fields_by_name['trigger_time']._options = None
  _MODELUSAGEDATA_USERUSAGEDATA_MODELTRIGGERDATA.fields_by_name['trigger_time']._serialized_options = b'\342A\001\002'
  _MODELUSAGEDATA_USERUSAGEDATA_MODELTRIGGERDATA.fields_by_name['model_definition_uid']._options = None
  _MODELUSAGEDATA_USERUSAGEDATA_MODELTRIGGERDATA.fields_by_name['model_definition_uid']._serialized_options = b'\342A\001\002'
  _MODELUSAGEDATA_USERUSAGEDATA_MODELTRIGGERDATA.fields_by_name['model_task']._options = None
  _MODELUSAGEDATA_USERUSAGEDATA_MODELTRIGGERDATA.fields_by_name['model_task']._serialized_options = b'\342A\001\002'
  _MODELUSAGEDATA_USERUSAGEDATA_MODELTRIGGERDATA.fields_by_name['status']._options = None
  _MODELUSAGEDATA_USERUSAGEDATA_MODELTRIGGERDATA.fields_by_name['status']._serialized_options = b'\342A\001\002'
  _MODELUSAGEDATA_USERUSAGEDATA_MODELTRIGGERDATA.fields_by_name['user_uid']._options = None
  _MODELUSAGEDATA_USERUSAGEDATA_MODELTRIGGERDATA.fields_by_name['user_uid']._serialized_options = b'\342A\001\002'
  _MODELUSAGEDATA_USERUSAGEDATA_MODELTRIGGERDATA.fields_by_name['user_type']._options = None
  _MODELUSAGEDATA_USERUSAGEDATA_MODELTRIGGERDATA.fields_by_name['user_type']._serialized_options = b'\342A\001\002'
  _MODELUSAGEDATA_USERUSAGEDATA.fields_by_name['owner_uid']._options = None
  _MODELUSAGEDATA_USERUSAGEDATA.fields_by_name['owner_uid']._serialized_options = b'\342A\001\002'
  _MODELUSAGEDATA_USERUSAGEDATA.fields_by_name['model_trigger_data']._options = None
  _MODELUSAGEDATA_USERUSAGEDATA.fields_by_name['model_trigger_data']._serialized_options = b'\342A\001\002'
  _MODELUSAGEDATA_USERUSAGEDATA.fields_by_name['owner_type']._options = None
  _MODELUSAGEDATA_USERUSAGEDATA.fields_by_name['owner_type']._serialized_options = b'\342A\001\002'
  _PIPELINEUSAGEDATA_USERUSAGEDATA_PIPELINETRIGGERDATA.fields_by_name['pipeline_uid']._options = None
  _PIPELINEUSAGEDATA_USERUSAGEDATA_PIPELINETRIGGERDATA.fields_by_name['pipeline_uid']._serialized_options = b'\342A\001\002'
  _PIPELINEUSAGEDATA_USERUSAGEDATA_PIPELINETRIGGERDATA.fields_by_name['trigger_uid']._options = None
  _PIPELINEUSAGEDATA_USERUSAGEDATA_PIPELINETRIGGERDATA.fields_by_name['trigger_uid']._serialized_options = b'\342A\001\002'
  _PIPELINEUSAGEDATA_USERUSAGEDATA_PIPELINETRIGGERDATA.fields_by_name['trigger_time']._options = None
  _PIPELINEUSAGEDATA_USERUSAGEDATA_PIPELINETRIGGERDATA.fields_by_name['trigger_time']._serialized_options = b'\342A\001\002'
  _PIPELINEUSAGEDATA_USERUSAGEDATA_PIPELINETRIGGERDATA.fields_by_name['trigger_mode']._options = None
  _PIPELINEUSAGEDATA_USERUSAGEDATA_PIPELINETRIGGERDATA.fields_by_name['trigger_mode']._serialized_options = b'\342A\001\002'
  _PIPELINEUSAGEDATA_USERUSAGEDATA_PIPELINETRIGGERDATA.fields_by_name['status']._options = None
  _PIPELINEUSAGEDATA_USERUSAGEDATA_PIPELINETRIGGERDATA.fields_by_name['status']._serialized_options = b'\342A\001\002'
  _PIPELINEUSAGEDATA_USERUSAGEDATA_PIPELINETRIGGERDATA.fields_by_name['pipeline_release_id']._options = None
  _PIPELINEUSAGEDATA_USERUSAGEDATA_PIPELINETRIGGERDATA.fields_by_name['pipeline_release_id']._serialized_options = b'\342A\001\002'
  _PIPELINEUSAGEDATA_USERUSAGEDATA_PIPELINETRIGGERDATA.fields_by_name['pipeline_release_uid']._options = None
  _PIPELINEUSAGEDATA_USERUSAGEDATA_PIPELINETRIGGERDATA.fields_by_name['pipeline_release_uid']._serialized_options = b'\342A\001\002'
  _PIPELINEUSAGEDATA_USERUSAGEDATA_PIPELINETRIGGERDATA.fields_by_name['user_uid']._options = None
  _PIPELINEUSAGEDATA_USERUSAGEDATA_PIPELINETRIGGERDATA.fields_by_name['user_uid']._serialized_options = b'\342A\001\002'
  _PIPELINEUSAGEDATA_USERUSAGEDATA_PIPELINETRIGGERDATA.fields_by_name['user_type']._options = None
  _PIPELINEUSAGEDATA_USERUSAGEDATA_PIPELINETRIGGERDATA.fields_by_name['user_type']._serialized_options = b'\342A\001\002'
  _PIPELINEUSAGEDATA_USERUSAGEDATA_PIPELINETRIGGERDATA.fields_by_name['pipeline_id']._options = None
  _PIPELINEUSAGEDATA_USERUSAGEDATA_PIPELINETRIGGERDATA.fields_by_name['pipeline_id']._serialized_options = b'\342A\001\002'
  _PIPELINEUSAGEDATA_USERUSAGEDATA.fields_by_name['owner_uid']._options = None
  _PIPELINEUSAGEDATA_USERUSAGEDATA.fields_by_name['owner_uid']._serialized_options = b'\342A\001\002'
  _PIPELINEUSAGEDATA_USERUSAGEDATA.fields_by_name['pipeline_trigger_data']._options = None
  _PIPELINEUSAGEDATA_USERUSAGEDATA.fields_by_name['pipeline_trigger_data']._serialized_options = b'\342A\001\002'
  _PIPELINEUSAGEDATA_USERUSAGEDATA.fields_by_name['owner_type']._options = None
  _PIPELINEUSAGEDATA_USERUSAGEDATA.fields_by_name['owner_type']._serialized_options = b'\342A\001\002'
  _ARTIFACTUSAGEDATA_USERUSAGEDATA.fields_by_name['owner_uid']._options = None
  _ARTIFACTUSAGEDATA_USERUSAGEDATA.fields_by_name['owner_uid']._serialized_options = b'\342A\001\002'
  _ARTIFACTUSAGEDATA_USERUSAGEDATA.fields_by_name['owner_type']._options = None
  _ARTIFACTUSAGEDATA_USERUSAGEDATA.fields_by_name['owner_type']._serialized_options = b'\342A\001\002'
  _SESSIONREPORT.fields_by_name['session_uid']._options = None
  _SESSIONREPORT.fields_by_name['session_uid']._serialized_options = b'\342A\001\002'
  _SESSIONREPORT.fields_by_name['token']._options = None
  _SESSIONREPORT.fields_by_name['token']._serialized_options = b'\342A\001\002'
  _SESSIONREPORT.fields_by_name['pow']._options = None
  _SESSIONREPORT.fields_by_name['pow']._serialized_options = b'\342A\001\002'
  _SESSIONREPORT.fields_by_name['session']._options = None
  _SESSIONREPORT.fields_by_name['session']._serialized_options = b'\342A\001\002'
  _CREATESESSIONREQUEST.fields_by_name['session']._options = None
  _CREATESESSIONREQUEST.fields_by_name['session']._serialized_options = b'\342A\001\002'
  _SENDSESSIONREPORTREQUEST.fields_by_name['report']._options = None
  _SENDSESSIONREPORTREQUEST.fields_by_name['report']._serialized_options = b'\342A\001\002'
  _globals['_LIVENESSREQUEST']._serialized_start=283
  _globals['_LIVENESSREQUEST']._serialized_end=433
  _globals['_LIVENESSRESPONSE']._serialized_start=435
  _globals['_LIVENESSRESPONSE']._serialized_end=553
  _globals['_READINESSREQUEST']._serialized_start=556
  _globals['_READINESSREQUEST']._serialized_end=707
  _globals['_READINESSRESPONSE']._serialized_start=709
  _globals['_READINESSRESPONSE']._serialized_end=828
  _globals['_SESSION']._serialized_start=831
  _globals['_SESSION']._serialized_end=1556
  _globals['_SESSION_SERVICE']._serialized_start=1367
  _globals['_SESSION_SERVICE']._serialized_end=1505
  _globals['_MGMTUSAGEDATA']._serialized_start=1559
  _globals['_MGMTUSAGEDATA']._serialized_end=1707
  _globals['_CONNECTORUSAGEDATA']._serialized_start=1710
  _globals['_CONNECTORUSAGEDATA']._serialized_end=2454
  _globals['_CONNECTORUSAGEDATA_USERUSAGEDATA']._serialized_start=1810
  _globals['_CONNECTORUSAGEDATA_USERUSAGEDATA']._serialized_end=2454
  _globals['_CONNECTORUSAGEDATA_USERUSAGEDATA_CONNECTOREXECUTEDATA']._serialized_start=2064
  _globals['_CONNECTORUSAGEDATA_USERUSAGEDATA_CONNECTOREXECUTEDATA']._serialized_end=2454
  _globals['_MODELUSAGEDATA']._serialized_start=2457
  _globals['_MODELUSAGEDATA']._serialized_end=3220
  _globals['_MODELUSAGEDATA_USERUSAGEDATA']._serialized_start=2549
  _globals['_MODELUSAGEDATA_USERUSAGEDATA']._serialized_end=3220
  _globals['_MODELUSAGEDATA_USERUSAGEDATA_MODELTRIGGERDATA']._serialized_start=2786
  _globals['_MODELUSAGEDATA_USERUSAGEDATA_MODELTRIGGERDATA']._serialized_end=3220
  _globals['_PIPELINEUSAGEDATA']._serialized_start=3223
  _globals['_PIPELINEUSAGEDATA']._serialized_end=4108
  _globals['_PIPELINEUSAGEDATA_USERUSAGEDATA']._serialized_start=3321
  _globals['_PIPELINEUSAGEDATA_USERUSAGEDATA']._serialized_end=4108
  _globals['_PIPELINEUSAGEDATA_USERUSAGEDATA_PIPELINETRIGGERDATA']._serialized_start=3571
  _globals['_PIPELINEUSAGEDATA_USERUSAGEDATA_PIPELINETRIGGERDATA']._serialized_end=4108
  _globals['_ARTIFACTUSAGEDATA']._serialized_start=4111
  _globals['_ARTIFACTUSAGEDATA']._serialized_end=4324
  _globals['_ARTIFACTUSAGEDATA_USERUSAGEDATA']._serialized_start=4208
  _globals['_ARTIFACTUSAGEDATA_USERUSAGEDATA']._serialized_end=4324
  _globals['_SESSIONREPORT']._serialized_start=4327
  _globals['_SESSIONREPORT']._serialized_end=4929
  _globals['_CREATESESSIONREQUEST']._serialized_start=4931
  _globals['_CREATESESSIONREQUEST']._serialized_end=5013
  _globals['_CREATESESSIONRESPONSE']._serialized_start=5015
  _globals['_CREATESESSIONRESPONSE']._serialized_end=5092
  _globals['_SENDSESSIONREPORTREQUEST']._serialized_start=5094
  _globals['_SENDSESSIONREPORTREQUEST']._serialized_end=5184
  _globals['_SENDSESSIONREPORTRESPONSE']._serialized_start=5186
  _globals['_SENDSESSIONREPORTRESPONSE']._serialized_end=5213
# @@protoc_insertion_point(module_scope)
