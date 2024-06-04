"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import collections.abc
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.message
import model.model.v1alpha.common_pb2
import sys

if sys.version_info >= (3, 8):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing_extensions.final
class Keypoint(google.protobuf.message.Message):
    """Keypoint contains the coordinates and visibility of a keypoint in an object."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    X_FIELD_NUMBER: builtins.int
    Y_FIELD_NUMBER: builtins.int
    V_FIELD_NUMBER: builtins.int
    x: builtins.float
    """X coordinate."""
    y: builtins.float
    """Y coordinate."""
    v: builtins.float
    """Visibility."""
    def __init__(
        self,
        *,
        x: builtins.float = ...,
        y: builtins.float = ...,
        v: builtins.float = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["v", b"v", "x", b"x", "y", b"y"]) -> None: ...

global___Keypoint = Keypoint

@typing_extensions.final
class KeypointObject(google.protobuf.message.Message):
    """KeypointObject is a detected object with its keypoints, e.g. a detected
    human shape with its legs, arms, core, etc.
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    KEYPOINTS_FIELD_NUMBER: builtins.int
    SCORE_FIELD_NUMBER: builtins.int
    BOUNDING_BOX_FIELD_NUMBER: builtins.int
    @property
    def keypoints(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___Keypoint]:
        """Keypoints."""
    score: builtins.float
    """Score."""
    @property
    def bounding_box(self) -> model.model.v1alpha.common_pb2.BoundingBox:
        """Bounding box."""
    def __init__(
        self,
        *,
        keypoints: collections.abc.Iterable[global___Keypoint] | None = ...,
        score: builtins.float = ...,
        bounding_box: model.model.v1alpha.common_pb2.BoundingBox | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["bounding_box", b"bounding_box"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["bounding_box", b"bounding_box", "keypoints", b"keypoints", "score", b"score"]) -> None: ...

global___KeypointObject = KeypointObject

@typing_extensions.final
class KeypointInput(google.protobuf.message.Message):
    """KeypointInput represents the input of a keypoint detection task."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    IMAGE_URL_FIELD_NUMBER: builtins.int
    IMAGE_BASE64_FIELD_NUMBER: builtins.int
    image_url: builtins.str
    """Image URL."""
    image_base64: builtins.str
    """Base64-encoded image."""
    def __init__(
        self,
        *,
        image_url: builtins.str = ...,
        image_base64: builtins.str = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["image_base64", b"image_base64", "image_url", b"image_url", "type", b"type"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["image_base64", b"image_base64", "image_url", b"image_url", "type", b"type"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions.Literal["type", b"type"]) -> typing_extensions.Literal["image_url", "image_base64"] | None: ...

global___KeypointInput = KeypointInput

@typing_extensions.final
class KeypointInputStream(google.protobuf.message.Message):
    """KeypointInputStream represents the input of a keypoint detection task when
    the input is streamed as binary files.
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    FILE_LENGTHS_FIELD_NUMBER: builtins.int
    CONTENT_FIELD_NUMBER: builtins.int
    @property
    def file_lengths(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.int]:
        """File length for each uploaded binary file."""
    content: builtins.bytes
    """Byte representation of the images."""
    def __init__(
        self,
        *,
        file_lengths: collections.abc.Iterable[builtins.int] | None = ...,
        content: builtins.bytes = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["content", b"content", "file_lengths", b"file_lengths"]) -> None: ...

global___KeypointInputStream = KeypointInputStream

@typing_extensions.final
class KeypointOutput(google.protobuf.message.Message):
    """KeypointOutput represents the result of a keypoint detection task."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    OBJECTS_FIELD_NUMBER: builtins.int
    @property
    def objects(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___KeypointObject]:
        """A list of keypoint objects."""
    def __init__(
        self,
        *,
        objects: collections.abc.Iterable[global___KeypointObject] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["objects", b"objects"]) -> None: ...

global___KeypointOutput = KeypointOutput
