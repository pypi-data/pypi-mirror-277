# generated by datamodel-codegen:
#   filename:  instill_task_ocr_output.json

from __future__ import annotations

from dataclasses import dataclass
from typing import List


@dataclass
class BoundingBox:
    height: float
    left: float
    top: float
    width: float


@dataclass
class Object:
    bounding_box: BoundingBox
    score: float
    text: str


@dataclass
class Model:
    objects: List[Object]
