# generated by datamodel-codegen:
#   filename:  googlecloudstorage_definitions.json

from __future__ import annotations

from dataclasses import dataclass


@dataclass
class GoogleCloudStorageConnectorSpec:
    bucket_name: str
    json_key: str
