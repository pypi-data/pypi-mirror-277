# generated by datamodel-codegen:
#   filename:  airbyte_definitions.json

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from typing import Optional


class AuthType(Enum):
    OAuth2_0 = 'OAuth2.0'


@dataclass
class Field0:
    access_token: str
    refresh_token: str
    auth_type: AuthType = OAuth2.AuthType.OAuth2_0
    client_id: Optional[str] = None
    client_secret: Optional[str] = None
