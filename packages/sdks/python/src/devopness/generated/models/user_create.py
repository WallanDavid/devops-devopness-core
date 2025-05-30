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


class UserCreate(DevopnessBaseModel):
    """
    UserCreate

    Attributes:
        email (str): The e-mail that will uniquely identify the user on the system and become its login credential. Must be a valid email address. Must not be greater than 255 characters.
    """

    email: StrictStr = Field(
        description="The e-mail that will uniquely identify the user on the system and become its login credential. Must be a valid email address. Must not be greater than 255 characters."
    )


class UserCreatePlain(TypedDict, total=False):
    """
    Plain version of UserCreate.
    """

    email: Required[str]
