# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/networking/requests/social/delete_gift_from_inventory_message.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/networking/requests/social/delete_gift_from_inventory_message.proto',
  package='pogoprotos.networking.requests.social',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\nNpogoprotos/networking/requests/social/delete_gift_from_inventory_message.proto\x12%pogoprotos.networking.requests.social\"4\n\x1e\x44\x65leteGiftFromInventoryMessage\x12\x12\n\ngiftbox_id\x18\x01 \x03(\x04\x62\x06proto3')
)




_DELETEGIFTFROMINVENTORYMESSAGE = _descriptor.Descriptor(
  name='DeleteGiftFromInventoryMessage',
  full_name='pogoprotos.networking.requests.social.DeleteGiftFromInventoryMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='giftbox_id', full_name='pogoprotos.networking.requests.social.DeleteGiftFromInventoryMessage.giftbox_id', index=0,
      number=1, type=4, cpp_type=4, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=121,
  serialized_end=173,
)

DESCRIPTOR.message_types_by_name['DeleteGiftFromInventoryMessage'] = _DELETEGIFTFROMINVENTORYMESSAGE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

DeleteGiftFromInventoryMessage = _reflection.GeneratedProtocolMessageType('DeleteGiftFromInventoryMessage', (_message.Message,), dict(
  DESCRIPTOR = _DELETEGIFTFROMINVENTORYMESSAGE,
  __module__ = 'pogoprotos.networking.requests.social.delete_gift_from_inventory_message_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.networking.requests.social.DeleteGiftFromInventoryMessage)
  ))
_sym_db.RegisterMessage(DeleteGiftFromInventoryMessage)


# @@protoc_insertion_point(module_scope)
