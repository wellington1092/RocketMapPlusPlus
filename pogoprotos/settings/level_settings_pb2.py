# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/settings/level_settings.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/settings/level_settings.proto',
  package='pogoprotos.settings',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n(pogoprotos/settings/level_settings.proto\x12\x13pogoprotos.settings\"Q\n\rLevelSettings\x12\x1b\n\x13trainer_cp_modifier\x18\x02 \x01(\x01\x12#\n\x1btrainer_difficulty_modifier\x18\x03 \x01(\x01\x62\x06proto3')
)




_LEVELSETTINGS = _descriptor.Descriptor(
  name='LevelSettings',
  full_name='pogoprotos.settings.LevelSettings',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='trainer_cp_modifier', full_name='pogoprotos.settings.LevelSettings.trainer_cp_modifier', index=0,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='trainer_difficulty_modifier', full_name='pogoprotos.settings.LevelSettings.trainer_difficulty_modifier', index=1,
      number=3, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
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
  serialized_start=65,
  serialized_end=146,
)

DESCRIPTOR.message_types_by_name['LevelSettings'] = _LEVELSETTINGS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

LevelSettings = _reflection.GeneratedProtocolMessageType('LevelSettings', (_message.Message,), dict(
  DESCRIPTOR = _LEVELSETTINGS,
  __module__ = 'pogoprotos.settings.level_settings_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.settings.LevelSettings)
  ))
_sym_db.RegisterMessage(LevelSettings)


# @@protoc_insertion_point(module_scope)
