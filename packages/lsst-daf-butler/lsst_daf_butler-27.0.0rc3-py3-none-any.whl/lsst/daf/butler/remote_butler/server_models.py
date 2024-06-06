# This file is part of daf_butler.
#
# Developed for the LSST Data Management System.
# This product includes software developed by the LSST Project
# (http://www.lsst.org).
# See the COPYRIGHT file at the top-level directory of this distribution
# for details of code ownership.
#
# This software is dual licensed under the GNU General Public License and also
# under a 3-clause BSD license. Recipients may choose which of these licenses
# to use; please see the files gpl-3.0.txt and/or bsd_license.txt,
# respectively.  If you choose the GPL option then the following text applies
# (but note that there is still no warranty even if you opt for BSD instead):
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

"""Models used for client/server communication."""

__all__ = [
    "CLIENT_REQUEST_ID_HEADER_NAME",
    "DatasetTypeName",
    "FindDatasetRequestModel",
    "FindDatasetResponseModel",
    "GetFileResponseModel",
    "GetCollectionInfoResponseModel",
    "GetCollectionSummaryResponseModel",
]

from typing import NewType

import pydantic
from lsst.daf.butler import CollectionType, SerializedDataId, SerializedDatasetRef, Timespan
from lsst.daf.butler.datastores.fileDatastoreClient import FileDatastoreGetPayload
from lsst.daf.butler.registry import SerializedCollectionSummary

CLIENT_REQUEST_ID_HEADER_NAME = "X-Butler-Client-Request-Id"
ERROR_STATUS_CODE = 422

CollectionList = NewType("CollectionList", list[str])
"""A list of search patterns for collection names.  May use glob
syntax to specify wildcards."""
DatasetTypeName = NewType("DatasetTypeName", str)


class FindDatasetRequestModel(pydantic.BaseModel):
    """Request model for find_dataset."""

    data_id: SerializedDataId
    collections: CollectionList
    timespan: Timespan | None
    dimension_records: bool = False
    datastore_records: bool = False


class FindDatasetResponseModel(pydantic.BaseModel):
    """Response model for find_dataset."""

    dataset_ref: SerializedDatasetRef | None


class GetFileByDataIdRequestModel(pydantic.BaseModel):
    """Request model for ``get_file_by_data_id``."""

    dataset_type_name: DatasetTypeName
    data_id: SerializedDataId
    collections: CollectionList
    timespan: Timespan | None = None


class GetFileResponseModel(pydantic.BaseModel):
    """Response model for get_file and get_file_by_data_id."""

    dataset_ref: SerializedDatasetRef
    artifact: FileDatastoreGetPayload | None
    """The data needed to retrieve and use an artifact. If this is `None`, that
    means this dataset is known to the Butler but the associated files are no
    longer available ("known to registry but not known to datastore".)

    An example of a situation where this would be `None` is a per-visit image
    that is an intermediate file in the processing pipelines.  It is deleted to
    save space, but the fact that it was once available must be recorded for
    provenance tracking.
    """


class ErrorResponseModel(pydantic.BaseModel):
    """Error response sent with a 422 status code, to propagate server
    exceptions with user-facing error messages to the client.
    """

    error_type: str
    """The ``error_type`` string from one of the subclasses of
    `ButlerUserError`.
    """
    detail: str
    """Detailed explanation of the error that will be sent to the client."""


class GetCollectionInfoResponseModel(pydantic.BaseModel):
    """Response model for get_collection_info."""

    name: str
    type: CollectionType
    children: list[str]
    doc: str | None = None
    """Will be `None` unless requested with ``include_doc=True`` query
    parameter."""
    parents: set[str] | None = None
    """Chained collections that directly contain this collection. Will be
    `None` unless requested with ``include_parents=True`` query parameter."""


class GetCollectionSummaryResponseModel(pydantic.BaseModel):
    """Response model for get_collection_summary."""

    summary: SerializedCollectionSummary


class QueryCollectionsRequestModel(pydantic.BaseModel):
    """Request model for query_collections."""

    search: CollectionList
    collection_types: list[CollectionType]
    flatten_chains: bool
    include_chains: bool


class QueryCollectionsResponseModel(pydantic.BaseModel):
    """Response model for query_collections."""

    collections: list[str]
    """Collection names that match the search."""
