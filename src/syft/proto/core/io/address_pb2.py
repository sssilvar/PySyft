# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: proto/core/io/address.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from syft.proto.core.io import location_pb2 as proto_dot_core_dot_io_dot_location__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
    name="proto/core/io/address.proto",
    package="syft.core.io",
    syntax="proto3",
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
    serialized_pb=b'\n\x1bproto/core/io/address.proto\x12\x0csyft.core.io\x1a\x1cproto/core/io/location.proto"\xb3\x02\n\x07\x41\x64\x64ress\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x10\n\x08obj_type\x18\x02 \x01(\t\x12\x13\n\x0bhas_network\x18\x03 \x01(\x08\x12/\n\x07network\x18\x04 \x01(\x0b\x32\x1e.syft.core.io.SpecificLocation\x12\x12\n\nhas_domain\x18\x05 \x01(\x08\x12.\n\x06\x64omain\x18\x06 \x01(\x0b\x32\x1e.syft.core.io.SpecificLocation\x12\x12\n\nhas_device\x18\x07 \x01(\x08\x12.\n\x06\x64\x65vice\x18\x08 \x01(\x0b\x32\x1e.syft.core.io.SpecificLocation\x12\x0e\n\x06has_vm\x18\t \x01(\x08\x12*\n\x02vm\x18\n \x01(\x0b\x32\x1e.syft.core.io.SpecificLocationb\x06proto3',
    dependencies=[proto_dot_core_dot_io_dot_location__pb2.DESCRIPTOR,],
)


_ADDRESS = _descriptor.Descriptor(
    name="Address",
    full_name="syft.core.io.Address",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="name",
            full_name="syft.core.io.Address.name",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="obj_type",
            full_name="syft.core.io.Address.obj_type",
            index=1,
            number=2,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="has_network",
            full_name="syft.core.io.Address.has_network",
            index=2,
            number=3,
            type=8,
            cpp_type=7,
            label=1,
            has_default_value=False,
            default_value=False,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="network",
            full_name="syft.core.io.Address.network",
            index=3,
            number=4,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="has_domain",
            full_name="syft.core.io.Address.has_domain",
            index=4,
            number=5,
            type=8,
            cpp_type=7,
            label=1,
            has_default_value=False,
            default_value=False,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="domain",
            full_name="syft.core.io.Address.domain",
            index=5,
            number=6,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="has_device",
            full_name="syft.core.io.Address.has_device",
            index=6,
            number=7,
            type=8,
            cpp_type=7,
            label=1,
            has_default_value=False,
            default_value=False,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="device",
            full_name="syft.core.io.Address.device",
            index=7,
            number=8,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="has_vm",
            full_name="syft.core.io.Address.has_vm",
            index=8,
            number=9,
            type=8,
            cpp_type=7,
            label=1,
            has_default_value=False,
            default_value=False,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="vm",
            full_name="syft.core.io.Address.vm",
            index=9,
            number=10,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=76,
    serialized_end=383,
)

_ADDRESS.fields_by_name[
    "network"
].message_type = proto_dot_core_dot_io_dot_location__pb2._SPECIFICLOCATION
_ADDRESS.fields_by_name[
    "domain"
].message_type = proto_dot_core_dot_io_dot_location__pb2._SPECIFICLOCATION
_ADDRESS.fields_by_name[
    "device"
].message_type = proto_dot_core_dot_io_dot_location__pb2._SPECIFICLOCATION
_ADDRESS.fields_by_name[
    "vm"
].message_type = proto_dot_core_dot_io_dot_location__pb2._SPECIFICLOCATION
DESCRIPTOR.message_types_by_name["Address"] = _ADDRESS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Address = _reflection.GeneratedProtocolMessageType(
    "Address",
    (_message.Message,),
    {
        "DESCRIPTOR": _ADDRESS,
        "__module__": "proto.core.io.address_pb2"
        # @@protoc_insertion_point(class_scope:syft.core.io.Address)
    },
)
_sym_db.RegisterMessage(Address)


# @@protoc_insertion_point(module_scope)
