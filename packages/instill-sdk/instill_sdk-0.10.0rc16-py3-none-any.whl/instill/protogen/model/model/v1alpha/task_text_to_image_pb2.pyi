"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import collections.abc
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.message
import google.protobuf.struct_pb2
import sys
import typing

if sys.version_info >= (3, 8):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing_extensions.final
class TextToImageInput(google.protobuf.message.Message):
    """TextToImageInput represents the input of a text-to-image task."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    PROMPT_FIELD_NUMBER: builtins.int
    PROMPT_IMAGE_URL_FIELD_NUMBER: builtins.int
    PROMPT_IMAGE_BASE64_FIELD_NUMBER: builtins.int
    STEPS_FIELD_NUMBER: builtins.int
    CFG_SCALE_FIELD_NUMBER: builtins.int
    SEED_FIELD_NUMBER: builtins.int
    SAMPLES_FIELD_NUMBER: builtins.int
    EXTRA_PARAMS_FIELD_NUMBER: builtins.int
    prompt: builtins.str
    """Prompt text."""
    prompt_image_url: builtins.str
    """Image URL."""
    prompt_image_base64: builtins.str
    """Base64-encoded image."""
    steps: builtins.int
    """Steps, defaults to 5."""
    cfg_scale: builtins.float
    """Guidance scale, defaults to 7.5."""
    seed: builtins.int
    """Seed, defaults to 0."""
    samples: builtins.int
    """Number of generated samples, default is 1."""
    @property
    def extra_params(self) -> google.protobuf.struct_pb2.Struct:
        """Extra parameters."""
    def __init__(
        self,
        *,
        prompt: builtins.str = ...,
        prompt_image_url: builtins.str = ...,
        prompt_image_base64: builtins.str = ...,
        steps: builtins.int | None = ...,
        cfg_scale: builtins.float | None = ...,
        seed: builtins.int | None = ...,
        samples: builtins.int | None = ...,
        extra_params: google.protobuf.struct_pb2.Struct | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["_cfg_scale", b"_cfg_scale", "_samples", b"_samples", "_seed", b"_seed", "_steps", b"_steps", "cfg_scale", b"cfg_scale", "extra_params", b"extra_params", "prompt_image_base64", b"prompt_image_base64", "prompt_image_url", b"prompt_image_url", "samples", b"samples", "seed", b"seed", "steps", b"steps", "type", b"type"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["_cfg_scale", b"_cfg_scale", "_samples", b"_samples", "_seed", b"_seed", "_steps", b"_steps", "cfg_scale", b"cfg_scale", "extra_params", b"extra_params", "prompt", b"prompt", "prompt_image_base64", b"prompt_image_base64", "prompt_image_url", b"prompt_image_url", "samples", b"samples", "seed", b"seed", "steps", b"steps", "type", b"type"]) -> None: ...
    @typing.overload
    def WhichOneof(self, oneof_group: typing_extensions.Literal["_cfg_scale", b"_cfg_scale"]) -> typing_extensions.Literal["cfg_scale"] | None: ...
    @typing.overload
    def WhichOneof(self, oneof_group: typing_extensions.Literal["_samples", b"_samples"]) -> typing_extensions.Literal["samples"] | None: ...
    @typing.overload
    def WhichOneof(self, oneof_group: typing_extensions.Literal["_seed", b"_seed"]) -> typing_extensions.Literal["seed"] | None: ...
    @typing.overload
    def WhichOneof(self, oneof_group: typing_extensions.Literal["_steps", b"_steps"]) -> typing_extensions.Literal["steps"] | None: ...
    @typing.overload
    def WhichOneof(self, oneof_group: typing_extensions.Literal["type", b"type"]) -> typing_extensions.Literal["prompt_image_url", "prompt_image_base64"] | None: ...

global___TextToImageInput = TextToImageInput

@typing_extensions.final
class TextToImageOutput(google.protobuf.message.Message):
    """TextToImageOutput contains the result of a text-to-image task."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    IMAGES_FIELD_NUMBER: builtins.int
    @property
    def images(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]:
        """A list of generated images, encoded in base64."""
    def __init__(
        self,
        *,
        images: collections.abc.Iterable[builtins.str] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["images", b"images"]) -> None: ...

global___TextToImageOutput = TextToImageOutput
