# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: avod/protos/pipeline.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import avod.protos.model_pb2
import avod.protos.train_pb2
import avod.protos.eval_pb2
import avod.protos.kitti_dataset_pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='avod/protos/pipeline.proto',
  package='avod.protos',
  serialized_pb=_b('\n\x1a\x61vod/protos/pipeline.proto\x12\x0b\x61vod.protos\x1a\x17\x61vod/protos/model.proto\x1a\x17\x61vod/protos/train.proto\x1a\x16\x61vod/protos/eval.proto\x1a\x1f\x61vod/protos/kitti_dataset.proto\"\xde\x01\n\x15NetworkPipelineConfig\x12.\n\x0cmodel_config\x18\x01 \x01(\x0b\x32\x18.avod.protos.ModelConfig\x12.\n\x0ctrain_config\x18\x02 \x01(\x0b\x32\x18.avod.protos.TrainConfig\x12,\n\x0b\x65val_config\x18\x03 \x01(\x0b\x32\x17.avod.protos.EvalConfig\x12\x37\n\x0e\x64\x61taset_config\x18\x04 \x01(\x0b\x32\x1f.avod.protos.KittiDatasetConfig')
  ,
  dependencies=[avod.protos.model_pb2.DESCRIPTOR,avod.protos.train_pb2.DESCRIPTOR,avod.protos.eval_pb2.DESCRIPTOR,avod.protos.kitti_dataset_pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_NETWORKPIPELINECONFIG = _descriptor.Descriptor(
  name='NetworkPipelineConfig',
  full_name='avod.protos.NetworkPipelineConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='model_config', full_name='avod.protos.NetworkPipelineConfig.model_config', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='train_config', full_name='avod.protos.NetworkPipelineConfig.train_config', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='eval_config', full_name='avod.protos.NetworkPipelineConfig.eval_config', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='dataset_config', full_name='avod.protos.NetworkPipelineConfig.dataset_config', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=151,
  serialized_end=373,
)

_NETWORKPIPELINECONFIG.fields_by_name['model_config'].message_type = avod.protos.model_pb2._MODELCONFIG
_NETWORKPIPELINECONFIG.fields_by_name['train_config'].message_type = avod.protos.train_pb2._TRAINCONFIG
_NETWORKPIPELINECONFIG.fields_by_name['eval_config'].message_type = avod.protos.eval_pb2._EVALCONFIG
_NETWORKPIPELINECONFIG.fields_by_name['dataset_config'].message_type = avod.protos.kitti_dataset_pb2._KITTIDATASETCONFIG
DESCRIPTOR.message_types_by_name['NetworkPipelineConfig'] = _NETWORKPIPELINECONFIG

NetworkPipelineConfig = _reflection.GeneratedProtocolMessageType('NetworkPipelineConfig', (_message.Message,), dict(
  DESCRIPTOR = _NETWORKPIPELINECONFIG,
  __module__ = 'avod.protos.pipeline_pb2'
  # @@protoc_insertion_point(class_scope:avod.protos.NetworkPipelineConfig)
  ))
_sym_db.RegisterMessage(NetworkPipelineConfig)


# @@protoc_insertion_point(module_scope)
