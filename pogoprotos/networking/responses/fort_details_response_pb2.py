# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/networking/responses/fort_details_response.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pogoprotos.data import pokemon_data_pb2 as pogoprotos_dot_data_dot_pokemon__data__pb2
from pogoprotos.data.raid import event_info_pb2 as pogoprotos_dot_data_dot_raid_dot_event__info__pb2
from pogoprotos.enums import team_color_pb2 as pogoprotos_dot_enums_dot_team__color__pb2
from pogoprotos.map.fort import fort_type_pb2 as pogoprotos_dot_map_dot_fort_dot_fort__type__pb2
from pogoprotos.map.fort import fort_modifier_pb2 as pogoprotos_dot_map_dot_fort_dot_fort__modifier__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/networking/responses/fort_details_response.proto',
  package='pogoprotos.networking.responses',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n;pogoprotos/networking/responses/fort_details_response.proto\x12\x1fpogoprotos.networking.responses\x1a\"pogoprotos/data/pokemon_data.proto\x1a%pogoprotos/data/raid/event_info.proto\x1a!pogoprotos/enums/team_color.proto\x1a#pogoprotos/map/fort/fort_type.proto\x1a\'pogoprotos/map/fort/fort_modifier.proto\"\xe0\x03\n\x13\x46ortDetailsResponse\x12\x0f\n\x07\x66ort_id\x18\x01 \x01(\t\x12/\n\nteam_color\x18\x02 \x01(\x0e\x32\x1b.pogoprotos.enums.TeamColor\x12\x32\n\x0cpokemon_data\x18\x03 \x01(\x0b\x32\x1c.pogoprotos.data.PokemonData\x12\x0c\n\x04name\x18\x04 \x01(\t\x12\x12\n\nimage_urls\x18\x05 \x03(\t\x12\n\n\x02\x66p\x18\x06 \x01(\x05\x12\x0f\n\x07stamina\x18\x07 \x01(\x05\x12\x13\n\x0bmax_stamina\x18\x08 \x01(\x05\x12+\n\x04type\x18\t \x01(\x0e\x32\x1d.pogoprotos.map.fort.FortType\x12\x10\n\x08latitude\x18\n \x01(\x01\x12\x11\n\tlongitude\x18\x0b \x01(\x01\x12\x13\n\x0b\x64\x65scription\x18\x0c \x01(\t\x12\x34\n\tmodifiers\x18\r \x03(\x0b\x32!.pogoprotos.map.fort.FortModifier\x12\x12\n\nclose_soon\x18\x0e \x01(\x08\x12\x19\n\x11\x63heckin_image_url\x18\x0f \x01(\t\x12\x33\n\nevent_info\x18\x10 \x01(\x0b\x32\x1f.pogoprotos.data.raid.EventInfob\x06proto3')
  ,
  dependencies=[pogoprotos_dot_data_dot_pokemon__data__pb2.DESCRIPTOR,pogoprotos_dot_data_dot_raid_dot_event__info__pb2.DESCRIPTOR,pogoprotos_dot_enums_dot_team__color__pb2.DESCRIPTOR,pogoprotos_dot_map_dot_fort_dot_fort__type__pb2.DESCRIPTOR,pogoprotos_dot_map_dot_fort_dot_fort__modifier__pb2.DESCRIPTOR,])




_FORTDETAILSRESPONSE = _descriptor.Descriptor(
  name='FortDetailsResponse',
  full_name='pogoprotos.networking.responses.FortDetailsResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='fort_id', full_name='pogoprotos.networking.responses.FortDetailsResponse.fort_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='team_color', full_name='pogoprotos.networking.responses.FortDetailsResponse.team_color', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='pokemon_data', full_name='pogoprotos.networking.responses.FortDetailsResponse.pokemon_data', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='pogoprotos.networking.responses.FortDetailsResponse.name', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='image_urls', full_name='pogoprotos.networking.responses.FortDetailsResponse.image_urls', index=4,
      number=5, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='fp', full_name='pogoprotos.networking.responses.FortDetailsResponse.fp', index=5,
      number=6, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='stamina', full_name='pogoprotos.networking.responses.FortDetailsResponse.stamina', index=6,
      number=7, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='max_stamina', full_name='pogoprotos.networking.responses.FortDetailsResponse.max_stamina', index=7,
      number=8, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='type', full_name='pogoprotos.networking.responses.FortDetailsResponse.type', index=8,
      number=9, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='latitude', full_name='pogoprotos.networking.responses.FortDetailsResponse.latitude', index=9,
      number=10, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='longitude', full_name='pogoprotos.networking.responses.FortDetailsResponse.longitude', index=10,
      number=11, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='description', full_name='pogoprotos.networking.responses.FortDetailsResponse.description', index=11,
      number=12, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='modifiers', full_name='pogoprotos.networking.responses.FortDetailsResponse.modifiers', index=12,
      number=13, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='close_soon', full_name='pogoprotos.networking.responses.FortDetailsResponse.close_soon', index=13,
      number=14, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='checkin_image_url', full_name='pogoprotos.networking.responses.FortDetailsResponse.checkin_image_url', index=14,
      number=15, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='event_info', full_name='pogoprotos.networking.responses.FortDetailsResponse.event_info', index=15,
      number=16, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=285,
  serialized_end=765,
)

_FORTDETAILSRESPONSE.fields_by_name['team_color'].enum_type = pogoprotos_dot_enums_dot_team__color__pb2._TEAMCOLOR
_FORTDETAILSRESPONSE.fields_by_name['pokemon_data'].message_type = pogoprotos_dot_data_dot_pokemon__data__pb2._POKEMONDATA
_FORTDETAILSRESPONSE.fields_by_name['type'].enum_type = pogoprotos_dot_map_dot_fort_dot_fort__type__pb2._FORTTYPE
_FORTDETAILSRESPONSE.fields_by_name['modifiers'].message_type = pogoprotos_dot_map_dot_fort_dot_fort__modifier__pb2._FORTMODIFIER
_FORTDETAILSRESPONSE.fields_by_name['event_info'].message_type = pogoprotos_dot_data_dot_raid_dot_event__info__pb2._EVENTINFO
DESCRIPTOR.message_types_by_name['FortDetailsResponse'] = _FORTDETAILSRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

FortDetailsResponse = _reflection.GeneratedProtocolMessageType('FortDetailsResponse', (_message.Message,), dict(
  DESCRIPTOR = _FORTDETAILSRESPONSE,
  __module__ = 'pogoprotos.networking.responses.fort_details_response_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.networking.responses.FortDetailsResponse)
  ))
_sym_db.RegisterMessage(FortDetailsResponse)


# @@protoc_insertion_point(module_scope)
