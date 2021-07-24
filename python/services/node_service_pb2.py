# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: services/node_service.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from entity import request_pb2 as entity_dot_request__pb2
from entity import response_pb2 as entity_dot_response__pb2
from entity import stream_message_pb2 as entity_dot_stream__message__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='services/node_service.proto',
  package='grpc',
  syntax='proto3',
  serialized_options=b'Z\006.;grpc',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x1bservices/node_service.proto\x12\x04grpc\x1a\x14\x65ntity/request.proto\x1a\x15\x65ntity/response.proto\x1a\x1b\x65ntity/stream_message.proto2\xfa\x01\n\x0bNodeService\x12+\n\x08Register\x12\r.grpc.Request\x1a\x0e.grpc.Response\"\x00\x12\x30\n\rSendHeartbeat\x12\r.grpc.Request\x1a\x0e.grpc.Response\"\x00\x12\'\n\x04Ping\x12\r.grpc.Request\x1a\x0e.grpc.Response\"\x00\x12\x33\n\tSubscribe\x12\r.grpc.Request\x1a\x13.grpc.StreamMessage\"\x00\x30\x01\x12.\n\x0bUnsubscribe\x12\r.grpc.Request\x1a\x0e.grpc.Response\"\x00\x42\x08Z\x06.;grpcb\x06proto3'
  ,
  dependencies=[entity_dot_request__pb2.DESCRIPTOR,entity_dot_response__pb2.DESCRIPTOR,entity_dot_stream__message__pb2.DESCRIPTOR,])



_sym_db.RegisterFileDescriptor(DESCRIPTOR)


DESCRIPTOR._options = None

_NODESERVICE = _descriptor.ServiceDescriptor(
  name='NodeService',
  full_name='grpc.NodeService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=112,
  serialized_end=362,
  methods=[
  _descriptor.MethodDescriptor(
    name='Register',
    full_name='grpc.NodeService.Register',
    index=0,
    containing_service=None,
    input_type=entity_dot_request__pb2._REQUEST,
    output_type=entity_dot_response__pb2._RESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='SendHeartbeat',
    full_name='grpc.NodeService.SendHeartbeat',
    index=1,
    containing_service=None,
    input_type=entity_dot_request__pb2._REQUEST,
    output_type=entity_dot_response__pb2._RESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Ping',
    full_name='grpc.NodeService.Ping',
    index=2,
    containing_service=None,
    input_type=entity_dot_request__pb2._REQUEST,
    output_type=entity_dot_response__pb2._RESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Subscribe',
    full_name='grpc.NodeService.Subscribe',
    index=3,
    containing_service=None,
    input_type=entity_dot_request__pb2._REQUEST,
    output_type=entity_dot_stream__message__pb2._STREAMMESSAGE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Unsubscribe',
    full_name='grpc.NodeService.Unsubscribe',
    index=4,
    containing_service=None,
    input_type=entity_dot_request__pb2._REQUEST,
    output_type=entity_dot_response__pb2._RESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_NODESERVICE)

DESCRIPTOR.services_by_name['NodeService'] = _NODESERVICE

# @@protoc_insertion_point(module_scope)
