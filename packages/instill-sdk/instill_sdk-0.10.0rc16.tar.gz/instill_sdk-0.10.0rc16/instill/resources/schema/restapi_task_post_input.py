# generated by datamodel-codegen:
#   filename:  restapi_task_post_input.json

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Dict, Optional


@dataclass
class Input:
    endpoint_url: str
    body: Optional[Dict[str, Any]] = None
    output_body_schema: Optional[str] = None
