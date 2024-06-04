# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: model/model/v1alpha/task_image_to_image.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n-model/model/v1alpha/task_image_to_image.proto\x12\x13model.model.v1alpha\x1a\x1fgoogle/api/field_behavior.proto\x1a\x1cgoogle/protobuf/struct.proto\"\xa3\x03\n\x11ImageToImageInput\x12*\n\x10prompt_image_url\x18\x01 \x01(\tH\x00R\x0epromptImageUrl\x12\x30\n\x13prompt_image_base64\x18\x02 \x01(\tH\x00R\x11promptImageBase64\x12!\n\x06prompt\x18\x03 \x01(\tB\x04\xe2\x41\x01\x02H\x01R\x06prompt\x88\x01\x01\x12\x1f\n\x05steps\x18\x04 \x01(\x05\x42\x04\xe2\x41\x01\x01H\x02R\x05steps\x88\x01\x01\x12&\n\tcfg_scale\x18\x05 \x01(\x02\x42\x04\xe2\x41\x01\x01H\x03R\x08\x63\x66gScale\x88\x01\x01\x12\x1d\n\x04seed\x18\x06 \x01(\x05\x42\x04\xe2\x41\x01\x01H\x04R\x04seed\x88\x01\x01\x12#\n\x07samples\x18\x07 \x01(\x05\x42\x04\xe2\x41\x01\x01H\x05R\x07samples\x88\x01\x01\x12@\n\x0c\x65xtra_params\x18\t \x01(\x0b\x32\x17.google.protobuf.StructB\x04\xe2\x41\x01\x01R\x0b\x65xtraParamsB\x06\n\x04typeB\t\n\x07_promptB\x08\n\x06_stepsB\x0c\n\n_cfg_scaleB\x07\n\x05_seedB\n\n\x08_samples\"2\n\x12ImageToImageOutput\x12\x1c\n\x06images\x18\x01 \x03(\tB\x04\xe2\x41\x01\x03R\x06imagesB\xe2\x01\n\x17\x63om.model.model.v1alphaB\x15TaskImageToImageProtoP\x01ZBgithub.com/instill-ai/protogen-go/model/model/v1alpha;modelv1alpha\xa2\x02\x03MMX\xaa\x02\x13Model.Model.V1alpha\xca\x02\x13Model\\Model\\V1alpha\xe2\x02\x1fModel\\Model\\V1alpha\\GPBMetadata\xea\x02\x15Model::Model::V1alphab\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'model.model.v1alpha.task_image_to_image_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\027com.model.model.v1alphaB\025TaskImageToImageProtoP\001ZBgithub.com/instill-ai/protogen-go/model/model/v1alpha;modelv1alpha\242\002\003MMX\252\002\023Model.Model.V1alpha\312\002\023Model\\Model\\V1alpha\342\002\037Model\\Model\\V1alpha\\GPBMetadata\352\002\025Model::Model::V1alpha'
  _IMAGETOIMAGEINPUT.fields_by_name['prompt']._options = None
  _IMAGETOIMAGEINPUT.fields_by_name['prompt']._serialized_options = b'\342A\001\002'
  _IMAGETOIMAGEINPUT.fields_by_name['steps']._options = None
  _IMAGETOIMAGEINPUT.fields_by_name['steps']._serialized_options = b'\342A\001\001'
  _IMAGETOIMAGEINPUT.fields_by_name['cfg_scale']._options = None
  _IMAGETOIMAGEINPUT.fields_by_name['cfg_scale']._serialized_options = b'\342A\001\001'
  _IMAGETOIMAGEINPUT.fields_by_name['seed']._options = None
  _IMAGETOIMAGEINPUT.fields_by_name['seed']._serialized_options = b'\342A\001\001'
  _IMAGETOIMAGEINPUT.fields_by_name['samples']._options = None
  _IMAGETOIMAGEINPUT.fields_by_name['samples']._serialized_options = b'\342A\001\001'
  _IMAGETOIMAGEINPUT.fields_by_name['extra_params']._options = None
  _IMAGETOIMAGEINPUT.fields_by_name['extra_params']._serialized_options = b'\342A\001\001'
  _IMAGETOIMAGEOUTPUT.fields_by_name['images']._options = None
  _IMAGETOIMAGEOUTPUT.fields_by_name['images']._serialized_options = b'\342A\001\003'
  _globals['_IMAGETOIMAGEINPUT']._serialized_start=134
  _globals['_IMAGETOIMAGEINPUT']._serialized_end=553
  _globals['_IMAGETOIMAGEOUTPUT']._serialized_start=555
  _globals['_IMAGETOIMAGEOUTPUT']._serialized_end=605
# @@protoc_insertion_point(module_scope)
