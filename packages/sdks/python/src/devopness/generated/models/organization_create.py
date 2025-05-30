"""
Devopness API Python SDK - Painless essential DevOps to everyone

Note:
    This is auto generated by OpenAPI Generator.
    https://openapi-generator.tech
"""

from typing import (
    Required,
    TypedDict,
)

from pydantic import Field, StrictStr

from .. import DevopnessBaseModel


class OrganizationCreate(DevopnessBaseModel):
    """
    OrganizationCreate

    Attributes:
        name (str): The Name of the organization. Must not be greater than 255 characters.
        url_slug (str): The URL Slug of the organization. Must not be greater than 255 characters.
    """

    name: StrictStr = Field(
        description="The Name of the organization. Must not be greater than 255 characters."
    )
    url_slug: StrictStr = Field(
        description="The URL Slug of the organization. Must not be greater than 255 characters."
    )


class OrganizationCreatePlain(TypedDict, total=False):
    """
    Plain version of OrganizationCreate.
    """

    name: Required[str]
    url_slug: Required[str]
