from dracon_types.v1 import issue_pb2 as _issue_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ScanInfo(_message.Message):
    __slots__ = ("scan_uuid", "scan_start_time", "scan_tags")
    class ScanTagsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    SCAN_UUID_FIELD_NUMBER: _ClassVar[int]
    SCAN_START_TIME_FIELD_NUMBER: _ClassVar[int]
    SCAN_TAGS_FIELD_NUMBER: _ClassVar[int]
    scan_uuid: str
    scan_start_time: _timestamp_pb2.Timestamp
    scan_tags: _containers.ScalarMap[str, str]
    def __init__(self, scan_uuid: _Optional[str] = ..., scan_start_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., scan_tags: _Optional[_Mapping[str, str]] = ...) -> None: ...

class LaunchToolResponse(_message.Message):
    __slots__ = ("scan_info", "tool_name", "issues")
    SCAN_INFO_FIELD_NUMBER: _ClassVar[int]
    TOOL_NAME_FIELD_NUMBER: _ClassVar[int]
    ISSUES_FIELD_NUMBER: _ClassVar[int]
    scan_info: ScanInfo
    tool_name: str
    issues: _containers.RepeatedCompositeFieldContainer[_issue_pb2.Issue]
    def __init__(self, scan_info: _Optional[_Union[ScanInfo, _Mapping]] = ..., tool_name: _Optional[str] = ..., issues: _Optional[_Iterable[_Union[_issue_pb2.Issue, _Mapping]]] = ...) -> None: ...

class EnrichedLaunchToolResponse(_message.Message):
    __slots__ = ("original_results", "issues")
    ORIGINAL_RESULTS_FIELD_NUMBER: _ClassVar[int]
    ISSUES_FIELD_NUMBER: _ClassVar[int]
    original_results: LaunchToolResponse
    issues: _containers.RepeatedCompositeFieldContainer[_issue_pb2.EnrichedIssue]
    def __init__(self, original_results: _Optional[_Union[LaunchToolResponse, _Mapping]] = ..., issues: _Optional[_Iterable[_Union[_issue_pb2.EnrichedIssue, _Mapping]]] = ...) -> None: ...
