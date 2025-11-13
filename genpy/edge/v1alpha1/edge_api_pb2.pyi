import datetime

from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class JobType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    JOB_TYPE_UNSPECIFIED: _ClassVar[JobType]
    JOB_TYPE_SCHEDULED: _ClassVar[JobType]
JOB_TYPE_UNSPECIFIED: JobType
JOB_TYPE_SCHEDULED: JobType

class RegisterRequest(_message.Message):
    __slots__ = ()
    DEVICE_FINGERPRINT_FIELD_NUMBER: _ClassVar[int]
    device_fingerprint: str
    def __init__(self, device_fingerprint: _Optional[str] = ...) -> None: ...

class RegisterResponse(_message.Message):
    __slots__ = ()
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class SubscribeRequest(_message.Message):
    __slots__ = ()
    AGENT_ID_FIELD_NUMBER: _ClassVar[int]
    TIMEOUT_FIELD_NUMBER: _ClassVar[int]
    agent_id: str
    timeout: _duration_pb2.Duration
    def __init__(self, agent_id: _Optional[str] = ..., timeout: _Optional[_Union[datetime.timedelta, _duration_pb2.Duration, _Mapping]] = ...) -> None: ...

class SubscribeResponse(_message.Message):
    __slots__ = ()
    JOB_ID_FIELD_NUMBER: _ClassVar[int]
    JOB_DESCRIBE_FIELD_NUMBER: _ClassVar[int]
    JOB_TYPE_FIELD_NUMBER: _ClassVar[int]
    job_id: str
    job_describe: str
    job_type: JobType
    def __init__(self, job_id: _Optional[str] = ..., job_describe: _Optional[str] = ..., job_type: _Optional[_Union[JobType, str]] = ...) -> None: ...
