# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: model/model/v1alpha/common.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n model/model/v1alpha/common.proto\x12\x13model.model.v1alpha\x1a\x1fgoogle/api/field_behavior.proto\"y\n\x0b\x42oundingBox\x12\x16\n\x03top\x18\x01 \x01(\x02\x42\x04\xe2\x41\x01\x03R\x03top\x12\x18\n\x04left\x18\x02 \x01(\x02\x42\x04\xe2\x41\x01\x03R\x04left\x12\x1a\n\x05width\x18\x03 \x01(\x02\x42\x04\xe2\x41\x01\x03R\x05width\x12\x1c\n\x06height\x18\x04 \x01(\x02\x42\x04\xe2\x41\x01\x03R\x06height\"s\n\x0bPromptImage\x12*\n\x10prompt_image_url\x18\x01 \x01(\tH\x00R\x0epromptImageUrl\x12\x30\n\x13prompt_image_base64\x18\x02 \x01(\tH\x00R\x11promptImageBase64B\x06\n\x04type\"u\n\x0cImageContent\x12=\n\timage_url\x18\x01 \x01(\x0b\x32 .model.model.v1alpha.PromptImageR\x08imageUrl\x12\x1b\n\x06\x64\x65tail\x18\x02 \x01(\tH\x00R\x06\x64\x65tail\x88\x01\x01\x42\t\n\x07_detail\"\x87\x01\n\x0eMessageContent\x12\x12\n\x04type\x18\x01 \x01(\tR\x04type\x12@\n\timage_url\x18\x02 \x01(\x0b\x32!.model.model.v1alpha.ImageContentH\x00R\x08imageUrl\x12\x14\n\x04text\x18\x03 \x01(\tH\x00R\x04textB\t\n\x07\x63ontent\"\\\n\x07Message\x12\x12\n\x04role\x18\x01 \x01(\tR\x04role\x12=\n\x07\x63ontent\x18\x02 \x03(\x0b\x32#.model.model.v1alpha.MessageContentR\x07\x63ontentB\xd8\x01\n\x17\x63om.model.model.v1alphaB\x0b\x43ommonProtoP\x01ZBgithub.com/instill-ai/protogen-go/model/model/v1alpha;modelv1alpha\xa2\x02\x03MMX\xaa\x02\x13Model.Model.V1alpha\xca\x02\x13Model\\Model\\V1alpha\xe2\x02\x1fModel\\Model\\V1alpha\\GPBMetadata\xea\x02\x15Model::Model::V1alphab\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'model.model.v1alpha.common_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\027com.model.model.v1alphaB\013CommonProtoP\001ZBgithub.com/instill-ai/protogen-go/model/model/v1alpha;modelv1alpha\242\002\003MMX\252\002\023Model.Model.V1alpha\312\002\023Model\\Model\\V1alpha\342\002\037Model\\Model\\V1alpha\\GPBMetadata\352\002\025Model::Model::V1alpha'
  _BOUNDINGBOX.fields_by_name['top']._options = None
  _BOUNDINGBOX.fields_by_name['top']._serialized_options = b'\342A\001\003'
  _BOUNDINGBOX.fields_by_name['left']._options = None
  _BOUNDINGBOX.fields_by_name['left']._serialized_options = b'\342A\001\003'
  _BOUNDINGBOX.fields_by_name['width']._options = None
  _BOUNDINGBOX.fields_by_name['width']._serialized_options = b'\342A\001\003'
  _BOUNDINGBOX.fields_by_name['height']._options = None
  _BOUNDINGBOX.fields_by_name['height']._serialized_options = b'\342A\001\003'
  _globals['_BOUNDINGBOX']._serialized_start=90
  _globals['_BOUNDINGBOX']._serialized_end=211
  _globals['_PROMPTIMAGE']._serialized_start=213
  _globals['_PROMPTIMAGE']._serialized_end=328
  _globals['_IMAGECONTENT']._serialized_start=330
  _globals['_IMAGECONTENT']._serialized_end=447
  _globals['_MESSAGECONTENT']._serialized_start=450
  _globals['_MESSAGECONTENT']._serialized_end=585
  _globals['_MESSAGE']._serialized_start=587
  _globals['_MESSAGE']._serialized_end=679
# @@protoc_insertion_point(module_scope)
