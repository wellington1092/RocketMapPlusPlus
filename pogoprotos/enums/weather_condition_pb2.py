# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/enums/weather_condition.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/enums/weather_condition.proto',
  package='pogoprotos.enums',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n(pogoprotos/enums/weather_condition.proto\x12\x10pogoprotos.enums*q\n\x10WeatherCondition\x12\x08\n\x04NONE\x10\x00\x12\t\n\x05\x43LEAR\x10\x01\x12\t\n\x05RAINY\x10\x02\x12\x11\n\rPARTLY_CLOUDY\x10\x03\x12\x0c\n\x08OVERCAST\x10\x04\x12\t\n\x05WINDY\x10\x05\x12\x08\n\x04SNOW\x10\x06\x12\x07\n\x03\x46OG\x10\x07\x62\x06proto3')
)

_WEATHERCONDITION = _descriptor.EnumDescriptor(
  name='WeatherCondition',
  full_name='pogoprotos.enums.WeatherCondition',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='NONE', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CLEAR', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='RAINY', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PARTLY_CLOUDY', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='OVERCAST', index=4, number=4,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='WINDY', index=5, number=5,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SNOW', index=6, number=6,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FOG', index=7, number=7,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=62,
  serialized_end=175,
)
_sym_db.RegisterEnumDescriptor(_WEATHERCONDITION)

WeatherCondition = enum_type_wrapper.EnumTypeWrapper(_WEATHERCONDITION)
NONE = 0
CLEAR = 1
RAINY = 2
PARTLY_CLOUDY = 3
OVERCAST = 4
WINDY = 5
SNOW = 6
FOG = 7


DESCRIPTOR.enum_types_by_name['WeatherCondition'] = _WEATHERCONDITION
_sym_db.RegisterFileDescriptor(DESCRIPTOR)


# @@protoc_insertion_point(module_scope)
