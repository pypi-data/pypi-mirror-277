# generated by datamodel-codegen:
#   filename:  huggingface_task_text_generation_input.json

from __future__ import annotations

from dataclasses import dataclass
from typing import Optional


@dataclass
class Options:
    use_cache: Optional[bool] = None
    wait_for_model: Optional[bool] = None


@dataclass
class Parameters:
    do_sample: Optional[bool] = None
    max_new_tokens: Optional[int] = None
    max_time: Optional[float] = None
    num_return_sequences: Optional[int] = None
    repetition_penalty: Optional[float] = None
    return_full_text: Optional[bool] = None
    temperature: Optional[float] = None
    top_k: Optional[int] = None
    top_p: Optional[float] = None


@dataclass
class Input:
    inputs: str
    model: Optional[str] = None
    options: Optional[Options] = None
    parameters: Optional[Parameters] = None
