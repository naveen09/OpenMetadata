# generated by datamodel-codegen:
#   filename:  schema/entity/data/location.json
#   timestamp: 2021-11-20T15:09:34+00:00

from __future__ import annotations

from enum import Enum
from typing import List, Optional

from pydantic import BaseModel, Field

from ...type import basic, entityHistory, entityReference, tagLabel


class LocationType(Enum):
    Bucket = 'Bucket'
    Prefix = 'Prefix'
    Database = 'Database'
    Table = 'Table'


class Table(BaseModel):
    class Config:
        extra = Extra.forbid

    id: Optional[basic.Uuid] = Field(
        None, description='Unique identifier of this location instance.'
    )
    name: str = Field(
        ...,
        description='Name of a location without the service. For example s3://bucket/path1/path2.',
    )
    displayName: Optional[str] = Field(
        None,
        description='Display Name that identifies this table. It could be title or label from the source services.',
    )
    fullyQualifiedName: Optional[str] = Field(
        None,
        description='Fully qualified name of a location in the form `serviceName.locationName`.',
    )
    description: Optional[str] = Field(None, description='Description of a location.')
    version: Optional[entityHistory.EntityVersion] = Field(
        None, description='Metadata version of the entity.'
    )
    updatedAt: Optional[basic.DateTime] = Field(
        None,
        description='Last update time corresponding to the new version of the entity.',
    )
    updatedBy: Optional[str] = Field(None, description='User who made the update.')
    href: Optional[basic.Href] = Field(
        None, description='Link to this location resource.'
    )
    locationType: Optional[LocationType] = None
    owner: Optional[entityReference.EntityReference] = Field(
        None, description='Owner of this location.'
    )
    followers: Optional[entityReference.EntityReferenceList] = Field(
        None, description='Followers of this location.'
    )
    tags: Optional[List[tagLabel.TagLabel]] = Field(
        None, description='Tags for this location.'
    )
    service: entityReference.EntityReference = Field(
        ...,
        description='Link to the database cluster/service where this database is hosted in.',
    )
    changeDescription: Optional[entityHistory.ChangeDescription] = Field(
        None, description='Change that lead to this version of the entity.'
    )
