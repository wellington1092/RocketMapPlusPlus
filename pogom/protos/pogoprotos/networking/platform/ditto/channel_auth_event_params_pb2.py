# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/networking/platform/ditto/channel_auth_event_params.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/networking/platform/ditto/channel_auth_event_params.proto',
  package='pogoprotos.networking.platform.ditto',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\nDpogoprotos/networking/platform/ditto/channel_auth_event_params.proto\x12$pogoprotos.networking.platform.ditto\"(\n\x16\x43hannelAuthEventParams\x12\x0e\n\x06status\x18\x01 \x01(\rb\x06proto3')
)




_CHANNELAUTHEVENTPARAMS = _descriptor.Descriptor(
  name='ChannelAuthEventParams',
  full_name='pogoprotos.networking.platform.ditto.ChannelAuthEventParams',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='pogoprotos.networking.platform.ditto.ChannelAuthEventParams.status', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=110,
  serialized_end=150,
)

DESCRIPTOR.message_types_by_name['ChannelAuthEventParams'] = _CHANNELAUTHEVENTPARAMS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ChannelAuthEventParams = _reflection.GeneratedProtocolMessageType('ChannelAuthEventParams', (_message.Message,), dict(
  DESCRIPTOR = _CHANNELAUTHEVENTPARAMS,
  __module__ = 'pogoprotos.networking.platform.ditto.channel_auth_event_params_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.networking.platform.ditto.ChannelAuthEventParams)
  ))
_sym_db.RegisterMessage(ChannelAuthEventParams)


# @@protoc_insertion_point(module_scope)