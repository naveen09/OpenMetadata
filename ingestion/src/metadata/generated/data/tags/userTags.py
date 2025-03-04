# generated by datamodel-codegen:
#   filename:  data/tags/userTags.json
#   timestamp: 2021-11-20T15:09:34+00:00

from __future__ import annotations

from typing import Any

from pydantic import BaseModel, Extra, Field


class Model(BaseModel):
    class Config:
        extra = Extra.forbid

    __root__: Any = Field(
        ...,
        description='Tags related to describing User related data. These tags are used to label data assets to describe the user data in those assets. Example - a table column can be labeled with `User.PhoneNumber` tag. The associated `PII` and `PersonalData` tags are automatically applied. This is done to help users producing the data  focus on describing the data without being policy experts. The associated tags take care of applying classification tags automatically.',
    )
