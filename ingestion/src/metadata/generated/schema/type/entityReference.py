# generated by datamodel-codegen:
#   filename:  schema/type/entityReference.json
#   timestamp: 2021-11-20T15:09:34+00:00

from __future__ import annotations

from typing import List, Optional

from pydantic import BaseModel, Extra, Field

from . import basic


class EntityReference(BaseModel):
    class Config:
        extra = Extra.forbid

    id: basic.Uuid = Field(
        ..., description='Unique identifier that identifies an entity instance.'
    )
    type: str = Field(
        ...,
        description='Entity type/class name - Examples: `database`, `table`, `metrics`, `redshift`, `mysql`, `bigquery`, `snowflake`...',
    )
    name: Optional[str] = Field(
        None,
        description='Name of the entity instance. For entities such as tables, databases where the name is not unique, fullyQualifiedName is returned in this field.',
    )
    description: Optional[str] = Field(
        None, description='Optional description of entity.'
    )
    displayName: Optional[str] = Field(
        None, description='Display Name that identifies this entity.'
    )
    href: Optional[basic.Href] = Field(None, description='Link to the entity resource.')


class EntityReferenceList(BaseModel):
    __root__: List[EntityReference]
