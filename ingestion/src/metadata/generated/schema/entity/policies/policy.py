# generated by datamodel-codegen:
#   filename:  schema/entity/policies/policy.json
#   timestamp: 2021-11-20T15:09:34+00:00

from __future__ import annotations

from enum import Enum
from typing import List, Optional, Union

from pydantic import AnyUrl, BaseModel, Field, constr

from ...type import basic, entityHistory, entityReference
from .accessControl import rule
from .lifecycle import rule as rule_1


class PolicyType(Enum):
    AccessControl = 'AccessControl'
    Lifecycle = 'Lifecycle'


class Policy(BaseModel):
    id: basic.Uuid = Field(
        ..., description='Unique identifier that identifies this Policy.'
    )
    name: constr(min_length=1, max_length=64) = Field(
        ..., description='Name that identifies this Policy.'
    )
    fullyQualifiedName: Optional[constr(min_length=1, max_length=128)] = Field(
        None, description='Name that uniquely identifies a Policy.'
    )
    displayName: Optional[str] = Field(None, description='Title for this Policy.')
    description: Optional[str] = Field(
        None,
        description='A short description of the Policy, comprehensible to regular users.',
    )
    owner: entityReference.EntityReference = Field(
        ..., description='Owner of this Policy.'
    )
    policyUrl: Optional[AnyUrl] = Field(
        None, description='Link to a well documented definition of this Policy.'
    )
    href: Optional[basic.Href] = Field(
        None, description='Link to the resource corresponding to this entity.'
    )
    policyType: PolicyType
    enabled: Optional[bool] = Field(True, description='Is the policy enabled.')
    version: Optional[entityHistory.EntityVersion] = Field(
        None, description='Metadata version of the Policy.'
    )
    updatedAt: Optional[basic.DateTime] = Field(
        None,
        description='Last update time corresponding to the new version of the Policy.',
    )
    updatedBy: Optional[str] = Field(None, description='User who made the update.')
    changeDescription: Optional[entityHistory.ChangeDescription] = Field(
        None, description='Change that led to this version of the Policy.'
    )
    rules: Optional[List[Union[rule.AccessControlRule, rule_1.LifecycleRule]]] = Field(
        None, description='A set of rules associated with this Policy.', min_length=1
    )
