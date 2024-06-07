from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Confidence(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    CONFIDENCE_UNSPECIFIED: _ClassVar[Confidence]
    CONFIDENCE_INFO: _ClassVar[Confidence]
    CONFIDENCE_LOW: _ClassVar[Confidence]
    CONFIDENCE_MEDIUM: _ClassVar[Confidence]
    CONFIDENCE_HIGH: _ClassVar[Confidence]
    CONFIDENCE_CRITICAL: _ClassVar[Confidence]

class Severity(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SEVERITY_UNSPECIFIED: _ClassVar[Severity]
    SEVERITY_INFO: _ClassVar[Severity]
    SEVERITY_LOW: _ClassVar[Severity]
    SEVERITY_MEDIUM: _ClassVar[Severity]
    SEVERITY_HIGH: _ClassVar[Severity]
    SEVERITY_CRITICAL: _ClassVar[Severity]
CONFIDENCE_UNSPECIFIED: Confidence
CONFIDENCE_INFO: Confidence
CONFIDENCE_LOW: Confidence
CONFIDENCE_MEDIUM: Confidence
CONFIDENCE_HIGH: Confidence
CONFIDENCE_CRITICAL: Confidence
SEVERITY_UNSPECIFIED: Severity
SEVERITY_INFO: Severity
SEVERITY_LOW: Severity
SEVERITY_MEDIUM: Severity
SEVERITY_HIGH: Severity
SEVERITY_CRITICAL: Severity

class Issue(_message.Message):
    __slots__ = ("target", "type", "title", "severity", "cvss", "confidence", "description", "source", "cve", "uuid", "cyclone_d_x_s_b_o_m", "context_segment", "cwe")
    TARGET_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    SEVERITY_FIELD_NUMBER: _ClassVar[int]
    CVSS_FIELD_NUMBER: _ClassVar[int]
    CONFIDENCE_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    SOURCE_FIELD_NUMBER: _ClassVar[int]
    CVE_FIELD_NUMBER: _ClassVar[int]
    UUID_FIELD_NUMBER: _ClassVar[int]
    CYCLONE_D_X_S_B_O_M_FIELD_NUMBER: _ClassVar[int]
    CONTEXT_SEGMENT_FIELD_NUMBER: _ClassVar[int]
    CWE_FIELD_NUMBER: _ClassVar[int]
    target: str
    type: str
    title: str
    severity: Severity
    cvss: float
    confidence: Confidence
    description: str
    source: str
    cve: str
    uuid: str
    cyclone_d_x_s_b_o_m: str
    context_segment: str
    cwe: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, target: _Optional[str] = ..., type: _Optional[str] = ..., title: _Optional[str] = ..., severity: _Optional[_Union[Severity, str]] = ..., cvss: _Optional[float] = ..., confidence: _Optional[_Union[Confidence, str]] = ..., description: _Optional[str] = ..., source: _Optional[str] = ..., cve: _Optional[str] = ..., uuid: _Optional[str] = ..., cyclone_d_x_s_b_o_m: _Optional[str] = ..., context_segment: _Optional[str] = ..., cwe: _Optional[_Iterable[int]] = ...) -> None: ...

class EnrichedIssue(_message.Message):
    __slots__ = ("raw_issue", "first_seen", "count", "false_positive", "updated_at", "hash", "annotations")
    class AnnotationsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    RAW_ISSUE_FIELD_NUMBER: _ClassVar[int]
    FIRST_SEEN_FIELD_NUMBER: _ClassVar[int]
    COUNT_FIELD_NUMBER: _ClassVar[int]
    FALSE_POSITIVE_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    HASH_FIELD_NUMBER: _ClassVar[int]
    ANNOTATIONS_FIELD_NUMBER: _ClassVar[int]
    raw_issue: Issue
    first_seen: _timestamp_pb2.Timestamp
    count: int
    false_positive: bool
    updated_at: _timestamp_pb2.Timestamp
    hash: str
    annotations: _containers.ScalarMap[str, str]
    def __init__(self, raw_issue: _Optional[_Union[Issue, _Mapping]] = ..., first_seen: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., count: _Optional[int] = ..., false_positive: bool = ..., updated_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., hash: _Optional[str] = ..., annotations: _Optional[_Mapping[str, str]] = ...) -> None: ...
