# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/networking/responses/social/get_friend_code_response.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/networking/responses/social/get_friend_code_response.proto',
  package='pogoprotos.networking.responses.social',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\nEpogoprotos/networking/responses/social/get_friend_code_response.proto\x12&pogoprotos.networking.responses.social\"\xa4\x01\n\x15GetFriendCodeResponse\x12T\n\x06result\x18\x01 \x01(\x0e\x32\x44.pogoprotos.networking.responses.social.GetFriendCodeResponse.Result\x12\x13\n\x0b\x66riend_code\x18\x02 \x01(\t\" \n\x06Result\x12\t\n\x05UNSET\x10\x00\x12\x0b\n\x07SUCCESS\x10\x01\x62\x06proto3')
)



_GETFRIENDCODERESPONSE_RESULT = _descriptor.EnumDescriptor(
  name='Result',
  full_name='pogoprotos.networking.responses.social.GetFriendCodeResponse.Result',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNSET', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SUCCESS', index=1, number=1,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=246,
  serialized_end=278,
)
_sym_db.RegisterEnumDescriptor(_GETFRIENDCODERESPONSE_RESULT)


_GETFRIENDCODERESPONSE = _descriptor.Descriptor(
  name='GetFriendCodeResponse',
  full_name='pogoprotos.networking.responses.social.GetFriendCodeResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='result', full_name='pogoprotos.networking.responses.social.GetFriendCodeResponse.result', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='friend_code', full_name='pogoprotos.networking.responses.social.GetFriendCodeResponse.friend_code', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _GETFRIENDCODERESPONSE_RESULT,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=114,
  serialized_end=278,
)

_GETFRIENDCODERESPONSE.fields_by_name['result'].enum_type = _GETFRIENDCODERESPONSE_RESULT
_GETFRIENDCODERESPONSE_RESULT.containing_type = _GETFRIENDCODERESPONSE
DESCRIPTOR.message_types_by_name['GetFriendCodeResponse'] = _GETFRIENDCODERESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GetFriendCodeResponse = _reflection.GeneratedProtocolMessageType('GetFriendCodeResponse', (_message.Message,), dict(
  DESCRIPTOR = _GETFRIENDCODERESPONSE,
  __module__ = 'pogoprotos.networking.responses.social.get_friend_code_response_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.networking.responses.social.GetFriendCodeResponse)
  ))
_sym_db.RegisterMessage(GetFriendCodeResponse)


# @@protoc_insertion_point(module_scope)
