# generated by datamodel-codegen:
#   filename:  restapi_task_head_output.json

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Dict


@dataclass
class Output:
    body: Dict[str, Any]
    header: Dict[str, Any]
    status_code: int
