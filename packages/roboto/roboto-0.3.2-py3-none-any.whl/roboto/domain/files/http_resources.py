import typing

import pydantic
from pydantic import ConfigDict


class FileRecordRequest(pydantic.BaseModel):
    """Upsert a file record."""

    file_id: str
    tags: list[str] = pydantic.Field(default_factory=list)
    metadata: dict[str, typing.Any] = pydantic.Field(default_factory=dict)


class DeleteFileRequest(pydantic.BaseModel):
    uri: str


class QueryFilesRequest(pydantic.BaseModel):
    filters: dict[str, typing.Any] = pydantic.Field(default_factory=dict)
    model_config = ConfigDict(extra="forbid")


class SignedUrlResponse(pydantic.BaseModel):
    url: str
