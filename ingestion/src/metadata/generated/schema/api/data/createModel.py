# generated by datamodel-codegen:
#   filename:  schema/api/data/createModel.json
#   timestamp: 2021-11-20T15:09:34+00:00

from __future__ import annotations

from typing import List, Optional

from pydantic import BaseModel, Field

from ...entity.data import model, table
from ...type import basic, entityReference, tagLabel


class CreateModelEntityRequest(BaseModel):
    name: model.ModelName = Field(
        ...,
        description='Name that identifies the this entity instance uniquely. Same as id if when name is not unique',
    )
    description: Optional[str] = Field(
        None, description='Description of entity instance.'
    )
    nodeType: Optional[model.NodeType] = None
    columns: List[table.Column] = Field(..., description='Schema of the Model')
    owner: Optional[entityReference.EntityReference] = Field(
        None, description='Owner of this entity'
    )
    database: Optional[basic.Uuid] = Field(
        None, description='Database corresponding to this table'
    )
    tags: Optional[List[tagLabel.TagLabel]] = Field(
        None, description='Tags for this model'
    )
    viewDefinition: Optional[basic.SqlQuery] = Field(
        None, description='View Definition in SQL.'
    )
