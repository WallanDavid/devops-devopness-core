"""
Devopness API Python SDK - Painless essential DevOps to everyone

Note:
    This is auto generated by OpenAPI Generator.
    https://openapi-generator.tech
"""

from typing import (
    List,
    Optional,
    Required,
    TypedDict,
    Union,
)

from pydantic import Field, StrictInt, StrictStr

from .. import DevopnessBaseModel
from .resource_summary_item import ResourceSummaryItem, ResourceSummaryItemPlain
from .user_relation import UserRelation, UserRelationPlain


class Organization(DevopnessBaseModel):
    """
    Organization

    Attributes:
        id (int): The unique identifier for the organization
        name (str): The name of the organization
        url_slug (str): The URL Slug of the organization
        resource_summary (List[ResourceSummaryItem], optional): Summary of the resource
        owner (UserRelation):
        created_at (str): The date and time when the organization was created
        updated_at (str): The date and time when the organization was last updated
    """

    id: StrictInt = Field(description="The unique identifier for the organization")
    name: StrictStr = Field(description="The name of the organization")
    url_slug: StrictStr = Field(description="The URL Slug of the organization")
    resource_summary: Optional[List[ResourceSummaryItem]] = Field(
        default=None, description="Summary of the resource"
    )
    owner: UserRelation
    created_at: StrictStr = Field(
        description="The date and time when the organization was created"
    )
    updated_at: StrictStr = Field(
        description="The date and time when the organization was last updated"
    )


class OrganizationPlain(TypedDict, total=False):
    """
    Plain version of Organization.
    """

    id: Required[int]
    name: Required[str]
    url_slug: Required[str]
    resource_summary: Optional[
        List[
            Union[
                ResourceSummaryItem,
                ResourceSummaryItemPlain,
            ]
        ]
    ]
    owner: Required[
        Union[
            UserRelation,
            UserRelationPlain,
        ]
    ]
    created_at: Required[str]
    updated_at: Required[str]
