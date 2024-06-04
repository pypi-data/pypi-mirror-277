# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: model/model/v1alpha/model_private_service.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.api import client_pb2 as google_dot_api_dot_client__pb2
from google.api import visibility_pb2 as google_dot_api_dot_visibility__pb2
from model.model.v1alpha import model_pb2 as model_dot_model_dot_v1alpha_dot_model__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n/model/model/v1alpha/model_private_service.proto\x12\x13model.model.v1alpha\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1bgoogle/api/visibility.proto\x1a\x1fmodel/model/v1alpha/model.proto2\xab\x07\n\x13ModelPrivateService\x12\x8b\x01\n\x0fListModelsAdmin\x12+.model.model.v1alpha.ListModelsAdminRequest\x1a,.model.model.v1alpha.ListModelsAdminResponse\"\x1d\x82\xd3\xe4\x93\x02\x17\x12\x15/v1alpha/admin/models\x12\xaf\x01\n\x10LookUpModelAdmin\x12,.model.model.v1alpha.LookUpModelAdminRequest\x1a-.model.model.v1alpha.LookUpModelAdminResponse\">\xda\x41\tpermalink\x82\xd3\xe4\x93\x02,\x12*/v1alpha/admin/{permalink=models/*}/lookUp\x12\xb7\x01\n\x0f\x43heckModelAdmin\x12+.model.model.v1alpha.CheckModelAdminRequest\x1a,.model.model.v1alpha.CheckModelAdminResponse\"I\xda\x41\x0fmodel_permalink\x82\xd3\xe4\x93\x02\x31\x12//v1alpha/admin/{model_permalink=models/*}/check\x12\xbe\x01\n\x10\x44\x65ployModelAdmin\x12,.model.model.v1alpha.DeployModelAdminRequest\x1a-.model.model.v1alpha.DeployModelAdminResponse\"M\xda\x41\x0fmodel_permalink\x82\xd3\xe4\x93\x02\x35\"0/v1alpha/admin/{model_permalink=models/*}/deploy:\x01*\x12\xc6\x01\n\x12UndeployModelAdmin\x12..model.model.v1alpha.UndeployModelAdminRequest\x1a/.model.model.v1alpha.UndeployModelAdminResponse\"O\xda\x41\x0fmodel_permalink\x82\xd3\xe4\x93\x02\x37\"2/v1alpha/admin/{model_permalink=models/*}/undeploy:\x01*\x1a\x10\xfa\xd2\xe4\x93\x02\n\x12\x08INTERNALB\xe5\x01\n\x17\x63om.model.model.v1alphaB\x18ModelPrivateServiceProtoP\x01ZBgithub.com/instill-ai/protogen-go/model/model/v1alpha;modelv1alpha\xa2\x02\x03MMX\xaa\x02\x13Model.Model.V1alpha\xca\x02\x13Model\\Model\\V1alpha\xe2\x02\x1fModel\\Model\\V1alpha\\GPBMetadata\xea\x02\x15Model::Model::V1alphab\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'model.model.v1alpha.model_private_service_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\027com.model.model.v1alphaB\030ModelPrivateServiceProtoP\001ZBgithub.com/instill-ai/protogen-go/model/model/v1alpha;modelv1alpha\242\002\003MMX\252\002\023Model.Model.V1alpha\312\002\023Model\\Model\\V1alpha\342\002\037Model\\Model\\V1alpha\\GPBMetadata\352\002\025Model::Model::V1alpha'
  _MODELPRIVATESERVICE._options = None
  _MODELPRIVATESERVICE._serialized_options = b'\372\322\344\223\002\n\022\010INTERNAL'
  _MODELPRIVATESERVICE.methods_by_name['ListModelsAdmin']._options = None
  _MODELPRIVATESERVICE.methods_by_name['ListModelsAdmin']._serialized_options = b'\202\323\344\223\002\027\022\025/v1alpha/admin/models'
  _MODELPRIVATESERVICE.methods_by_name['LookUpModelAdmin']._options = None
  _MODELPRIVATESERVICE.methods_by_name['LookUpModelAdmin']._serialized_options = b'\332A\tpermalink\202\323\344\223\002,\022*/v1alpha/admin/{permalink=models/*}/lookUp'
  _MODELPRIVATESERVICE.methods_by_name['CheckModelAdmin']._options = None
  _MODELPRIVATESERVICE.methods_by_name['CheckModelAdmin']._serialized_options = b'\332A\017model_permalink\202\323\344\223\0021\022//v1alpha/admin/{model_permalink=models/*}/check'
  _MODELPRIVATESERVICE.methods_by_name['DeployModelAdmin']._options = None
  _MODELPRIVATESERVICE.methods_by_name['DeployModelAdmin']._serialized_options = b'\332A\017model_permalink\202\323\344\223\0025\"0/v1alpha/admin/{model_permalink=models/*}/deploy:\001*'
  _MODELPRIVATESERVICE.methods_by_name['UndeployModelAdmin']._options = None
  _MODELPRIVATESERVICE.methods_by_name['UndeployModelAdmin']._serialized_options = b'\332A\017model_permalink\202\323\344\223\0027\"2/v1alpha/admin/{model_permalink=models/*}/undeploy:\001*'
  _globals['_MODELPRIVATESERVICE']._serialized_start=190
  _globals['_MODELPRIVATESERVICE']._serialized_end=1129
# @@protoc_insertion_point(module_scope)
