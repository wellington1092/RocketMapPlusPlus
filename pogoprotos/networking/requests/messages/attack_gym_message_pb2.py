# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/networking/requests/messages/attack_gym_message.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pogoprotos.data.battle import battle_action_pb2 as pogoprotos_dot_data_dot_battle_dot_battle__action__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/networking/requests/messages/attack_gym_message.proto',
  package='pogoprotos.networking.requests.messages',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n@pogoprotos/networking/requests/messages/attack_gym_message.proto\x12\'pogoprotos.networking.requests.messages\x1a*pogoprotos/data/battle/battle_action.proto\"\xeb\x01\n\x10\x41ttackGymMessage\x12\x0e\n\x06gym_id\x18\x01 \x01(\t\x12\x11\n\tbattle_id\x18\x02 \x01(\t\x12<\n\x0e\x61ttack_actions\x18\x03 \x03(\x0b\x32$.pogoprotos.data.battle.BattleAction\x12\x43\n\x15last_retrieved_action\x18\x04 \x01(\x0b\x32$.pogoprotos.data.battle.BattleAction\x12\x17\n\x0fplayer_latitude\x18\x05 \x01(\x01\x12\x18\n\x10player_longitude\x18\x06 \x01(\x01\x62\x06proto3')
  ,
  dependencies=[pogoprotos_dot_data_dot_battle_dot_battle__action__pb2.DESCRIPTOR,])




_ATTACKGYMMESSAGE = _descriptor.Descriptor(
  name='AttackGymMessage',
  full_name='pogoprotos.networking.requests.messages.AttackGymMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='gym_id', full_name='pogoprotos.networking.requests.messages.AttackGymMessage.gym_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='battle_id', full_name='pogoprotos.networking.requests.messages.AttackGymMessage.battle_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='attack_actions', full_name='pogoprotos.networking.requests.messages.AttackGymMessage.attack_actions', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='last_retrieved_action', full_name='pogoprotos.networking.requests.messages.AttackGymMessage.last_retrieved_action', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='player_latitude', full_name='pogoprotos.networking.requests.messages.AttackGymMessage.player_latitude', index=4,
      number=5, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='player_longitude', full_name='pogoprotos.networking.requests.messages.AttackGymMessage.player_longitude', index=5,
      number=6, type=1, cpp_type=5, label=1,
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
  serialized_start=154,
  serialized_end=389,
)

_ATTACKGYMMESSAGE.fields_by_name['attack_actions'].message_type = pogoprotos_dot_data_dot_battle_dot_battle__action__pb2._BATTLEACTION
_ATTACKGYMMESSAGE.fields_by_name['last_retrieved_action'].message_type = pogoprotos_dot_data_dot_battle_dot_battle__action__pb2._BATTLEACTION
DESCRIPTOR.message_types_by_name['AttackGymMessage'] = _ATTACKGYMMESSAGE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

AttackGymMessage = _reflection.GeneratedProtocolMessageType('AttackGymMessage', (_message.Message,), dict(
  DESCRIPTOR = _ATTACKGYMMESSAGE,
  __module__ = 'pogoprotos.networking.requests.messages.attack_gym_message_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.networking.requests.messages.AttackGymMessage)
  ))
_sym_db.RegisterMessage(AttackGymMessage)


# @@protoc_insertion_point(module_scope)
