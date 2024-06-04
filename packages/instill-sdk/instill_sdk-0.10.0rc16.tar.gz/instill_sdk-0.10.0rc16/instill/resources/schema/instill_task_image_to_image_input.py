# generated by datamodel-codegen:
#   filename:  instill_task_image_to_image_input.json

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Dict, Optional


@dataclass
class Input:
    image_base64: str
    model_name: str
    prompt: str
    cfg_scale: Optional[float] = None
    extra_params: Optional[Dict[str, Any]] = None
    samples: Optional[int] = None
    seed: Optional[int] = None
    top_k: Optional[int] = 10
