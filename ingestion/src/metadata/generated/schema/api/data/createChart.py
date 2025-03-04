# generated by datamodel-codegen:
#   filename:  schema/api/data/createChart.json
#   timestamp: 2021-11-20T15:09:34+00:00

from __future__ import annotations

from typing import List, Optional

from pydantic import AnyUrl, BaseModel, Field, constr

from ...entity.data import chart
from ...type import entityReference, tagLabel


class CreateChartEntityRequest(BaseModel):
    name: constr(min_length=1, max_length=64) = Field(
        ..., description='Name that identifies this Chart.'
    )
    displayName: Optional[str] = Field(
        None,
        description='Display Name that identifies this Chart. It could be title or label from the source services',
    )
    description: Optional[str] = Field(
        None,
        description='Description of the chart instance. What it has and how to use it.',
    )
    chartType: Optional[chart.ChartType] = None
    chartUrl: Optional[AnyUrl] = Field(
        None, description='Chart URL, pointing to its own Service URL'
    )
    tables: Optional[entityReference.EntityReferenceList] = Field(
        None, description='Link to tables used in this chart.'
    )
    tags: Optional[List[tagLabel.TagLabel]] = Field(
        None, description='Tags for this chart'
    )
    owner: Optional[entityReference.EntityReference] = Field(
        None, description='Owner of this database'
    )
    service: entityReference.EntityReference = Field(
        ..., description='Link to the database service where this database is hosted in'
    )
