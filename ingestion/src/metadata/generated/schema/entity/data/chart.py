# generated by datamodel-codegen:
#   filename:  schema/entity/data/chart.json
#   timestamp: 2021-11-20T15:09:34+00:00

from __future__ import annotations

from enum import Enum
from typing import List, Optional

from pydantic import AnyUrl, BaseModel, Field, constr

from ...type import basic, entityHistory, entityReference, tagLabel, usageDetails


class ChartType(Enum):
    Line = 'Line'
    Table = 'Table'
    Bar = 'Bar'
    Area = 'Area'
    Pie = 'Pie'
    Histogram = 'Histogram'
    Scatter = 'Scatter'
    Text = 'Text'
    BoxPlot = 'BoxPlot'
    Other = 'Other'


class Chart(BaseModel):
    id: basic.Uuid = Field(
        ..., description='Unique identifier that identifies a chart instance.'
    )
    name: constr(min_length=1, max_length=64) = Field(
        ..., description='Name that identifies this Chart.'
    )
    displayName: Optional[str] = Field(
        None,
        description='Display Name that identifies this Chart. It could be title or label from the source services.',
    )
    fullyQualifiedName: Optional[constr(min_length=1, max_length=64)] = Field(
        None,
        description="A unique name that identifies a dashboard in the format 'ServiceName.ChartName'.",
    )
    description: Optional[str] = Field(
        None, description='Description of the dashboard, what it is, and how to use it.'
    )
    version: Optional[entityHistory.EntityVersion] = Field(
        None, description='Metadata version of the entity.'
    )
    updatedAt: Optional[basic.DateTime] = Field(
        None,
        description='Last update time corresponding to the new version of the entity.',
    )
    updatedBy: Optional[str] = Field(None, description='User who made the update.')
    chartType: Optional[ChartType] = None
    chartUrl: Optional[AnyUrl] = Field(
        None, description='Chart URL, pointing to its own Service URL.'
    )
    href: Optional[basic.Href] = Field(
        None, description='Link to the resource corresponding to this entity.'
    )
    owner: Optional[entityReference.EntityReference] = Field(
        None, description='Owner of this dashboard.'
    )
    tables: Optional[entityReference.EntityReferenceList] = Field(
        None, description='Link to table used in this chart.'
    )
    followers: Optional[entityReference.EntityReferenceList] = Field(
        None, description='Followers of this chart.'
    )
    tags: Optional[List[tagLabel.TagLabel]] = Field(
        None, description='Tags for this chart.'
    )
    service: entityReference.EntityReference = Field(
        ..., description='Link to service where this dashboard is hosted in.'
    )
    usageSummary: Optional[usageDetails.TypeUsedToReturnUsageDetailsOfAnEntity] = Field(
        None, description='Latest usage information for this database.'
    )
    changeDescription: Optional[entityHistory.ChangeDescription] = Field(
        None, description='Change that lead to this version of the entity.'
    )
