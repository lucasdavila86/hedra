# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: worker.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='worker.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x0cworker.proto\x1a\x1cgoogle/protobuf/struct.proto\">\n\x13LeaderUpdateRequest\x12\x14\n\x0chost_address\x18\x01 \x01(\t\x12\x11\n\thost_port\x18\x02 \x01(\x03\"u\n\x1aWorkerServerUpdateResponse\x12\x16\n\x0e\x63lient_address\x18\x01 \x01(\t\x12\x13\n\x0b\x63lient_port\x18\x02 \x01(\x03\x12*\n\tcompleted\x18\x03 \x01(\x0b\x32\x17.google.protobuf.Struct\"\x88\x01\n\rNewJobRequest\x12\x14\n\x0chost_address\x18\x01 \x01(\t\x12\x0f\n\x07host_id\x18\x02 \x01(\t\x12\x0e\n\x06job_id\x18\x03 \x01(\t\x12+\n\njob_config\x18\x04 \x01(\x0b\x32\x17.google.protobuf.Struct\x12\x13\n\x0bjob_timeout\x18\x05 \x01(\x03\"G\n\x0eNewJobResponse\x12\x14\n\x0chost_address\x18\x01 \x01(\t\x12\x0f\n\x07host_id\x18\x02 \x01(\t\x12\x0e\n\x06job_id\x18\x03 \x01(\t\"J\n\x11PollWorkerRequest\x12\x14\n\x0chost_address\x18\x01 \x01(\t\x12\x0f\n\x07host_id\x18\x02 \x01(\t\x12\x0e\n\x06job_id\x18\x03 \x01(\t\"N\n\x12PollWorkerResponse\x12\x14\n\x0chost_address\x18\x01 \x01(\t\x12\x0f\n\x07host_id\x18\x02 \x01(\t\x12\x11\n\tcompleted\x18\x03 \x01(\x08\"K\n\x12JobCompleteRequest\x12\x14\n\x0chost_address\x18\x01 \x01(\t\x12\x0f\n\x07host_id\x18\x02 \x01(\t\x12\x0e\n\x06job_id\x18\x03 \x01(\t\"U\n\x13JobCompleteResponse\x12\x14\n\x0chost_address\x18\x01 \x01(\t\x12\x0f\n\x07host_id\x18\x02 \x01(\t\x12\x17\n\x0freporter_fields\x18\x03 \x03(\t\"O\n\x16WorkerHeartbeatRequest\x12\x14\n\x0chost_address\x18\x01 \x01(\t\x12\x0f\n\x07host_id\x18\x02 \x01(\t\x12\x0e\n\x06status\x18\x03 \x01(\t\"P\n\x17WorkerHeartbeatResponse\x12\x14\n\x0chost_address\x18\x01 \x01(\t\x12\x0f\n\x07host_id\x18\x02 \x01(\t\x12\x0e\n\x06status\x18\x03 \x01(\t\"D\n\x1bLeaderRegisterWorkerRequest\x12\x14\n\x0chost_address\x18\x01 \x01(\t\x12\x0f\n\x07host_id\x18\x02 \x01(\t\"]\n\x1cLeaderRegisterWorkerResponse\x12\x14\n\x0chost_address\x18\x01 \x01(\t\x12\x0f\n\x07host_id\x18\x02 \x01(\t\x12\x16\n\x0eserver_address\x18\x03 \x01(\t2\xaf\x03\n\x0cWorkerServer\x12K\n\x14GetRequestsCompleted\x12\x14.LeaderUpdateRequest\x1a\x1b.WorkerServerUpdateResponse\"\x00\x12\x37\n\x12\x43reateNewWorkerJob\x12\x0e.NewJobRequest\x1a\x0f.NewJobResponse\"\x00\x12\x39\n\x0cGetJobStatus\x12\x12.PollWorkerRequest\x1a\x13.PollWorkerResponse\"\x00\x12<\n\rGetJobResults\x12\x13.JobCompleteRequest\x1a\x14.JobCompleteResponse\"\x00\x12K\n\x14\x43heckWorkerHeartbeat\x12\x17.WorkerHeartbeatRequest\x1a\x18.WorkerHeartbeatResponse\"\x00\x12S\n\x14LeaderRegisterWorker\x12\x1c.LeaderRegisterWorkerRequest\x1a\x1d.LeaderRegisterWorkerResponseb\x06proto3'
  ,
  dependencies=[google_dot_protobuf_dot_struct__pb2.DESCRIPTOR,])




_LEADERUPDATEREQUEST = _descriptor.Descriptor(
  name='LeaderUpdateRequest',
  full_name='LeaderUpdateRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='host_address', full_name='LeaderUpdateRequest.host_address', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='host_port', full_name='LeaderUpdateRequest.host_port', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=46,
  serialized_end=108,
)


_WORKERSERVERUPDATERESPONSE = _descriptor.Descriptor(
  name='WorkerServerUpdateResponse',
  full_name='WorkerServerUpdateResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='client_address', full_name='WorkerServerUpdateResponse.client_address', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='client_port', full_name='WorkerServerUpdateResponse.client_port', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='completed', full_name='WorkerServerUpdateResponse.completed', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=110,
  serialized_end=227,
)


_NEWJOBREQUEST = _descriptor.Descriptor(
  name='NewJobRequest',
  full_name='NewJobRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='host_address', full_name='NewJobRequest.host_address', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='host_id', full_name='NewJobRequest.host_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='job_id', full_name='NewJobRequest.job_id', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='job_config', full_name='NewJobRequest.job_config', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='job_timeout', full_name='NewJobRequest.job_timeout', index=4,
      number=5, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=230,
  serialized_end=366,
)


_NEWJOBRESPONSE = _descriptor.Descriptor(
  name='NewJobResponse',
  full_name='NewJobResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='host_address', full_name='NewJobResponse.host_address', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='host_id', full_name='NewJobResponse.host_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='job_id', full_name='NewJobResponse.job_id', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=368,
  serialized_end=439,
)


_POLLWORKERREQUEST = _descriptor.Descriptor(
  name='PollWorkerRequest',
  full_name='PollWorkerRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='host_address', full_name='PollWorkerRequest.host_address', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='host_id', full_name='PollWorkerRequest.host_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='job_id', full_name='PollWorkerRequest.job_id', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=441,
  serialized_end=515,
)


_POLLWORKERRESPONSE = _descriptor.Descriptor(
  name='PollWorkerResponse',
  full_name='PollWorkerResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='host_address', full_name='PollWorkerResponse.host_address', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='host_id', full_name='PollWorkerResponse.host_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='completed', full_name='PollWorkerResponse.completed', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=517,
  serialized_end=595,
)


_JOBCOMPLETEREQUEST = _descriptor.Descriptor(
  name='JobCompleteRequest',
  full_name='JobCompleteRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='host_address', full_name='JobCompleteRequest.host_address', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='host_id', full_name='JobCompleteRequest.host_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='job_id', full_name='JobCompleteRequest.job_id', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=597,
  serialized_end=672,
)


_JOBCOMPLETERESPONSE = _descriptor.Descriptor(
  name='JobCompleteResponse',
  full_name='JobCompleteResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='host_address', full_name='JobCompleteResponse.host_address', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='host_id', full_name='JobCompleteResponse.host_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='reporter_fields', full_name='JobCompleteResponse.reporter_fields', index=2,
      number=3, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=674,
  serialized_end=759,
)


_WORKERHEARTBEATREQUEST = _descriptor.Descriptor(
  name='WorkerHeartbeatRequest',
  full_name='WorkerHeartbeatRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='host_address', full_name='WorkerHeartbeatRequest.host_address', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='host_id', full_name='WorkerHeartbeatRequest.host_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='status', full_name='WorkerHeartbeatRequest.status', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=761,
  serialized_end=840,
)


_WORKERHEARTBEATRESPONSE = _descriptor.Descriptor(
  name='WorkerHeartbeatResponse',
  full_name='WorkerHeartbeatResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='host_address', full_name='WorkerHeartbeatResponse.host_address', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='host_id', full_name='WorkerHeartbeatResponse.host_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='status', full_name='WorkerHeartbeatResponse.status', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=842,
  serialized_end=922,
)


_LEADERREGISTERWORKERREQUEST = _descriptor.Descriptor(
  name='LeaderRegisterWorkerRequest',
  full_name='LeaderRegisterWorkerRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='host_address', full_name='LeaderRegisterWorkerRequest.host_address', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='host_id', full_name='LeaderRegisterWorkerRequest.host_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=924,
  serialized_end=992,
)


_LEADERREGISTERWORKERRESPONSE = _descriptor.Descriptor(
  name='LeaderRegisterWorkerResponse',
  full_name='LeaderRegisterWorkerResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='host_address', full_name='LeaderRegisterWorkerResponse.host_address', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='host_id', full_name='LeaderRegisterWorkerResponse.host_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='server_address', full_name='LeaderRegisterWorkerResponse.server_address', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=994,
  serialized_end=1087,
)

_WORKERSERVERUPDATERESPONSE.fields_by_name['completed'].message_type = google_dot_protobuf_dot_struct__pb2._STRUCT
_NEWJOBREQUEST.fields_by_name['job_config'].message_type = google_dot_protobuf_dot_struct__pb2._STRUCT
DESCRIPTOR.message_types_by_name['LeaderUpdateRequest'] = _LEADERUPDATEREQUEST
DESCRIPTOR.message_types_by_name['WorkerServerUpdateResponse'] = _WORKERSERVERUPDATERESPONSE
DESCRIPTOR.message_types_by_name['NewJobRequest'] = _NEWJOBREQUEST
DESCRIPTOR.message_types_by_name['NewJobResponse'] = _NEWJOBRESPONSE
DESCRIPTOR.message_types_by_name['PollWorkerRequest'] = _POLLWORKERREQUEST
DESCRIPTOR.message_types_by_name['PollWorkerResponse'] = _POLLWORKERRESPONSE
DESCRIPTOR.message_types_by_name['JobCompleteRequest'] = _JOBCOMPLETEREQUEST
DESCRIPTOR.message_types_by_name['JobCompleteResponse'] = _JOBCOMPLETERESPONSE
DESCRIPTOR.message_types_by_name['WorkerHeartbeatRequest'] = _WORKERHEARTBEATREQUEST
DESCRIPTOR.message_types_by_name['WorkerHeartbeatResponse'] = _WORKERHEARTBEATRESPONSE
DESCRIPTOR.message_types_by_name['LeaderRegisterWorkerRequest'] = _LEADERREGISTERWORKERREQUEST
DESCRIPTOR.message_types_by_name['LeaderRegisterWorkerResponse'] = _LEADERREGISTERWORKERRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

LeaderUpdateRequest = _reflection.GeneratedProtocolMessageType('LeaderUpdateRequest', (_message.Message,), {
  'DESCRIPTOR' : _LEADERUPDATEREQUEST,
  '__module__' : 'worker_pb2'
  # @@protoc_insertion_point(class_scope:LeaderUpdateRequest)
  })
_sym_db.RegisterMessage(LeaderUpdateRequest)

WorkerServerUpdateResponse = _reflection.GeneratedProtocolMessageType('WorkerServerUpdateResponse', (_message.Message,), {
  'DESCRIPTOR' : _WORKERSERVERUPDATERESPONSE,
  '__module__' : 'worker_pb2'
  # @@protoc_insertion_point(class_scope:WorkerServerUpdateResponse)
  })
_sym_db.RegisterMessage(WorkerServerUpdateResponse)

NewJobRequest = _reflection.GeneratedProtocolMessageType('NewJobRequest', (_message.Message,), {
  'DESCRIPTOR' : _NEWJOBREQUEST,
  '__module__' : 'worker_pb2'
  # @@protoc_insertion_point(class_scope:NewJobRequest)
  })
_sym_db.RegisterMessage(NewJobRequest)

NewJobResponse = _reflection.GeneratedProtocolMessageType('NewJobResponse', (_message.Message,), {
  'DESCRIPTOR' : _NEWJOBRESPONSE,
  '__module__' : 'worker_pb2'
  # @@protoc_insertion_point(class_scope:NewJobResponse)
  })
_sym_db.RegisterMessage(NewJobResponse)

PollWorkerRequest = _reflection.GeneratedProtocolMessageType('PollWorkerRequest', (_message.Message,), {
  'DESCRIPTOR' : _POLLWORKERREQUEST,
  '__module__' : 'worker_pb2'
  # @@protoc_insertion_point(class_scope:PollWorkerRequest)
  })
_sym_db.RegisterMessage(PollWorkerRequest)

PollWorkerResponse = _reflection.GeneratedProtocolMessageType('PollWorkerResponse', (_message.Message,), {
  'DESCRIPTOR' : _POLLWORKERRESPONSE,
  '__module__' : 'worker_pb2'
  # @@protoc_insertion_point(class_scope:PollWorkerResponse)
  })
_sym_db.RegisterMessage(PollWorkerResponse)

JobCompleteRequest = _reflection.GeneratedProtocolMessageType('JobCompleteRequest', (_message.Message,), {
  'DESCRIPTOR' : _JOBCOMPLETEREQUEST,
  '__module__' : 'worker_pb2'
  # @@protoc_insertion_point(class_scope:JobCompleteRequest)
  })
_sym_db.RegisterMessage(JobCompleteRequest)

JobCompleteResponse = _reflection.GeneratedProtocolMessageType('JobCompleteResponse', (_message.Message,), {
  'DESCRIPTOR' : _JOBCOMPLETERESPONSE,
  '__module__' : 'worker_pb2'
  # @@protoc_insertion_point(class_scope:JobCompleteResponse)
  })
_sym_db.RegisterMessage(JobCompleteResponse)

WorkerHeartbeatRequest = _reflection.GeneratedProtocolMessageType('WorkerHeartbeatRequest', (_message.Message,), {
  'DESCRIPTOR' : _WORKERHEARTBEATREQUEST,
  '__module__' : 'worker_pb2'
  # @@protoc_insertion_point(class_scope:WorkerHeartbeatRequest)
  })
_sym_db.RegisterMessage(WorkerHeartbeatRequest)

WorkerHeartbeatResponse = _reflection.GeneratedProtocolMessageType('WorkerHeartbeatResponse', (_message.Message,), {
  'DESCRIPTOR' : _WORKERHEARTBEATRESPONSE,
  '__module__' : 'worker_pb2'
  # @@protoc_insertion_point(class_scope:WorkerHeartbeatResponse)
  })
_sym_db.RegisterMessage(WorkerHeartbeatResponse)

LeaderRegisterWorkerRequest = _reflection.GeneratedProtocolMessageType('LeaderRegisterWorkerRequest', (_message.Message,), {
  'DESCRIPTOR' : _LEADERREGISTERWORKERREQUEST,
  '__module__' : 'worker_pb2'
  # @@protoc_insertion_point(class_scope:LeaderRegisterWorkerRequest)
  })
_sym_db.RegisterMessage(LeaderRegisterWorkerRequest)

LeaderRegisterWorkerResponse = _reflection.GeneratedProtocolMessageType('LeaderRegisterWorkerResponse', (_message.Message,), {
  'DESCRIPTOR' : _LEADERREGISTERWORKERRESPONSE,
  '__module__' : 'worker_pb2'
  # @@protoc_insertion_point(class_scope:LeaderRegisterWorkerResponse)
  })
_sym_db.RegisterMessage(LeaderRegisterWorkerResponse)



_WORKERSERVER = _descriptor.ServiceDescriptor(
  name='WorkerServer',
  full_name='WorkerServer',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=1090,
  serialized_end=1521,
  methods=[
  _descriptor.MethodDescriptor(
    name='GetRequestsCompleted',
    full_name='WorkerServer.GetRequestsCompleted',
    index=0,
    containing_service=None,
    input_type=_LEADERUPDATEREQUEST,
    output_type=_WORKERSERVERUPDATERESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='CreateNewWorkerJob',
    full_name='WorkerServer.CreateNewWorkerJob',
    index=1,
    containing_service=None,
    input_type=_NEWJOBREQUEST,
    output_type=_NEWJOBRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='GetJobStatus',
    full_name='WorkerServer.GetJobStatus',
    index=2,
    containing_service=None,
    input_type=_POLLWORKERREQUEST,
    output_type=_POLLWORKERRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='GetJobResults',
    full_name='WorkerServer.GetJobResults',
    index=3,
    containing_service=None,
    input_type=_JOBCOMPLETEREQUEST,
    output_type=_JOBCOMPLETERESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='CheckWorkerHeartbeat',
    full_name='WorkerServer.CheckWorkerHeartbeat',
    index=4,
    containing_service=None,
    input_type=_WORKERHEARTBEATREQUEST,
    output_type=_WORKERHEARTBEATRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='LeaderRegisterWorker',
    full_name='WorkerServer.LeaderRegisterWorker',
    index=5,
    containing_service=None,
    input_type=_LEADERREGISTERWORKERREQUEST,
    output_type=_LEADERREGISTERWORKERRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_WORKERSERVER)

DESCRIPTOR.services_by_name['WorkerServer'] = _WORKERSERVER

# @@protoc_insertion_point(module_scope)
