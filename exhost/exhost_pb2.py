# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: exhost.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0c\x65xhost.proto\x12\x06\x65xhost\"L\n\x12MarketOrderRequest\x12\x0c\n\x04\x62\x61se\x18\x01 \x01(\t\x12\r\n\x05quote\x18\x02 \x01(\t\x12\x0b\n\x03qty\x18\x03 \x01(\x02\x12\x0c\n\x04side\x18\x04 \x01(\t\"Z\n\x11LimitOrderRequest\x12\x0c\n\x04\x62\x61se\x18\x01 \x01(\t\x12\r\n\x05quote\x18\x02 \x01(\t\x12\r\n\x05price\x18\x03 \x01(\x02\x12\x0b\n\x03qty\x18\x04 \x01(\x02\x12\x0c\n\x04side\x18\x05 \x01(\t\"\x12\n\x04Hash\x12\n\n\x02id\x18\x01 \x01(\t\"\x07\n\x05\x45mpty2\x86\x01\n\x08\x45xchange\x12=\n\x0fSendMarketOrder\x12\x1a.exhost.MarketOrderRequest\x1a\x0c.exhost.Hash0\x01\x12;\n\x0eSendLimitOrder\x12\x19.exhost.LimitOrderRequest\x1a\x0c.exhost.Hash0\x01\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'exhost_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_MARKETORDERREQUEST']._serialized_start=24
  _globals['_MARKETORDERREQUEST']._serialized_end=100
  _globals['_LIMITORDERREQUEST']._serialized_start=102
  _globals['_LIMITORDERREQUEST']._serialized_end=192
  _globals['_HASH']._serialized_start=194
  _globals['_HASH']._serialized_end=212
  _globals['_EMPTY']._serialized_start=214
  _globals['_EMPTY']._serialized_end=221
  _globals['_EXCHANGE']._serialized_start=224
  _globals['_EXCHANGE']._serialized_end=358
# @@protoc_insertion_point(module_scope)
