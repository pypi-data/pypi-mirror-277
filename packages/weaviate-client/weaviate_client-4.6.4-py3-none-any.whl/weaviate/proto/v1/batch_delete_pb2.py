# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: v1/batch_delete.proto
# Protobuf Python Version: 4.25.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from weaviate.proto.v1 import base_pb2 as v1_dot_base__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n\x15v1/batch_delete.proto\x12\x0bweaviate.v1\x1a\rv1/base.proto"\xe6\x01\n\x12\x42\x61tchDeleteRequest\x12\x12\n\ncollection\x18\x01 \x01(\t\x12%\n\x07\x66ilters\x18\x02 \x01(\x0b\x32\x14.weaviate.v1.Filters\x12\x0f\n\x07verbose\x18\x03 \x01(\x08\x12\x0f\n\x07\x64ry_run\x18\x04 \x01(\x08\x12=\n\x11\x63onsistency_level\x18\x05 \x01(\x0e\x32\x1d.weaviate.v1.ConsistencyLevelH\x00\x88\x01\x01\x12\x13\n\x06tenant\x18\x06 \x01(\tH\x01\x88\x01\x01\x42\x14\n\x12_consistency_levelB\t\n\x07_tenant"\x86\x01\n\x10\x42\x61tchDeleteReply\x12\x0c\n\x04took\x18\x01 \x01(\x02\x12\x0e\n\x06\x66\x61iled\x18\x02 \x01(\x03\x12\x0f\n\x07matches\x18\x03 \x01(\x03\x12\x12\n\nsuccessful\x18\x04 \x01(\x03\x12/\n\x07objects\x18\x05 \x03(\x0b\x32\x1e.weaviate.v1.BatchDeleteObject"S\n\x11\x42\x61tchDeleteObject\x12\x0c\n\x04uuid\x18\x01 \x01(\x0c\x12\x12\n\nsuccessful\x18\x02 \x01(\x08\x12\x12\n\x05\x65rror\x18\x03 \x01(\tH\x00\x88\x01\x01\x42\x08\n\x06_errorBo\n#io.weaviate.client.grpc.protocol.v1B\x12WeaviateProtoBatchZ4github.com/weaviate/weaviate/grpc/generated;protocolb\x06proto3'
)

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, "v1.batch_delete_pb2", _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
    _globals["DESCRIPTOR"]._options = None
    _globals[
        "DESCRIPTOR"
    ]._serialized_options = b"\n#io.weaviate.client.grpc.protocol.v1B\022WeaviateProtoBatchZ4github.com/weaviate/weaviate/grpc/generated;protocol"
    _globals["_BATCHDELETEREQUEST"]._serialized_start = 54
    _globals["_BATCHDELETEREQUEST"]._serialized_end = 284
    _globals["_BATCHDELETEREPLY"]._serialized_start = 287
    _globals["_BATCHDELETEREPLY"]._serialized_end = 421
    _globals["_BATCHDELETEOBJECT"]._serialized_start = 423
    _globals["_BATCHDELETEOBJECT"]._serialized_end = 506
# @@protoc_insertion_point(module_scope)
