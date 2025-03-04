# generated by datamodel-codegen:
#   filename:  schema/type/storage.json
#   timestamp: 2021-11-20T15:09:34+00:00

from __future__ import annotations

from enum import Enum
from typing import Any, Union

from pydantic import BaseModel, Extra, Field


class Model(BaseModel):
    class Config:
        extra = Extra.forbid

    __root__: Any = Field(..., description='Definitions related to Storage Service')


class StorageServiceType(Enum):
    S3 = 'S3'
    GCS = 'GCS'
    HDFS = 'HDFS'
    ABFS = 'ABFS'


class S3StorageClass(Enum):
    DEEP_ARCHIVE = 'DEEP_ARCHIVE'
    GLACIER = 'GLACIER'
    INTELLIGENT_TIERING = 'INTELLIGENT_TIERING'
    ONEZONE_IA = 'ONEZONE_IA'
    OUTPOSTS = 'OUTPOSTS'
    REDUCED_REDUNDANCY = 'REDUCED_REDUNDANCY'
    STANDARD = 'STANDARD'
    STANDARD_IA = 'STANDARD_IA'


class GcsStorageClass(Enum):
    ARCHIVE = 'ARCHIVE'
    COLDLINE = 'COLDLINE'
    DURABLE_REDUCED_AVAILABILITY = 'DURABLE_REDUCED_AVAILABILITY'
    MULTI_REGIONAL = 'MULTI_REGIONAL'
    NEARLINE = 'NEARLINE'
    REGIONAL = 'REGIONAL'
    STANDARD = 'STANDARD'


class AbfsStorageClass(Enum):
    ARCHIVE = 'ARCHIVE'
    HOT = 'HOT'
    COOL = 'COOL'


class StorageClassType(BaseModel):
    __root__: Union[S3StorageClass, GcsStorageClass, AbfsStorageClass] = Field(
        ..., description='Type of storage class for the storage service'
    )
