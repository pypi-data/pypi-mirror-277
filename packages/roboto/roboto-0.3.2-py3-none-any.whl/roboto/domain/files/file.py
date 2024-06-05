import collections.abc
import pathlib
import typing
from typing import Any, Optional

from ...query import QuerySpecification
from ...serde import pydantic_jsonable_dict
from .delegate import (
    CredentialProvider,
    FileDelegate,
)
from .file_requests import UpdateFileRecordRequest
from .progress import (
    NoopProgressMonitorFactory,
    ProgressMonitorFactory,
)
from .record import FileRecord


class File:
    __delegate: FileDelegate
    __record: FileRecord

    @staticmethod
    def construct_s3_obj_arn(bucket: str, key: str) -> str:
        return f"arn:aws:s3:::{bucket}/{key}"

    @staticmethod
    def construct_s3_obj_uri(
        bucket: str, key: str, version: Optional[str] = None
    ) -> str:
        base_uri = f"s3://{bucket}/{key}"
        if version:
            base_uri += f"?versionId={version}"
        return base_uri

    @classmethod
    def from_id(
        cls,
        file_id: str,
        delegate: FileDelegate,
    ) -> "File":
        record = delegate.get_record_by_primary_key(file_id)
        return cls(record, delegate)

    @classmethod
    def query(
        cls,
        query: QuerySpecification,
        delegate: FileDelegate,
        org_id: Optional[str] = None,
    ) -> collections.abc.Generator["File", None, None]:
        known = set(FileRecord.model_fields.keys())
        actual = set()
        for field in query.fields():
            # Support dot notation for nested fields
            # E.g., "metadata.SoftwareVersion"
            if "." in field:
                actual.add(field.split(".")[0])
            else:
                actual.add(field)
        unknown = actual - known
        if unknown:
            plural = len(unknown) > 1
            msg = (
                "are not known attributes of File"
                if plural
                else "is not a known attribute of File"
            )
            raise ValueError(f"{unknown} {msg}. Known attributes: {known}")

        paginated_results = delegate.query_files(query, org_id=org_id)
        while True:
            for record in paginated_results.items:
                yield cls(record, delegate)
            if paginated_results.next_token:
                query.after = paginated_results.next_token
                paginated_results = delegate.query_files(query, org_id=org_id)
            else:
                break

    def __init__(self, record: FileRecord, delegate: FileDelegate):
        self.__record = record
        self.__delegate = delegate

    @property
    def file_id(self) -> str:
        return self.__record.file_id

    @property
    def org_id(self) -> str:
        return self.__record.org_id

    @property
    def uri(self) -> str:
        return self.__record.uri

    @property
    def record(self) -> FileRecord:
        return self.__record

    @property
    def relative_path(self) -> str:
        return self.__record.relative_path

    @property
    def metadata(self) -> dict[str, typing.Any]:
        return self.__record.metadata

    @property
    def tags(self) -> list[str]:
        return self.__record.tags

    @property
    def description(self) -> Optional[str]:
        return self.__record.description

    def delete(self) -> None:
        self.__delegate.delete_file(self.__record)

    def download(
        self,
        local_path: pathlib.Path,
        credential_provider: CredentialProvider,
        progress_monitor_factory: ProgressMonitorFactory = NoopProgressMonitorFactory(),
    ):
        self.__delegate.download_file(
            self.__record,
            local_path,
            credential_provider,
            progress_monitor_factory=progress_monitor_factory,
        )

    def update(self, request: UpdateFileRecordRequest) -> "File":
        self.__record = self.__delegate.update_file(self.__record, request)
        return self

    def get_signed_url(
        self,
        override_content_type: typing.Optional[str] = None,
        override_content_disposition: typing.Optional[str] = None,
    ) -> str:
        return self.__delegate.get_signed_url(
            self.__record,
            override_content_type=override_content_type,
            override_content_disposition=override_content_disposition,
        )

    def to_dict(self) -> dict[str, Any]:
        return pydantic_jsonable_dict(self.__record)
