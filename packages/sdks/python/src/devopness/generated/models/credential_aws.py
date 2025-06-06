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


class CredentialAws(DevopnessBaseModel):
    """
    CredentialAws

    Attributes:
        access_key_id (str): The key used to authenticate on AWS cloud provider
        secret_access_key (str): The secret used to authenticate on AWS cloud provider
    """

    access_key_id: StrictStr = Field(
        description="The key used to authenticate on AWS cloud provider"
    )
    secret_access_key: StrictStr = Field(
        description="The secret used to authenticate on AWS cloud provider"
    )


class CredentialAwsPlain(TypedDict, total=False):
    """
    Plain version of CredentialAws.
    """

    access_key_id: Required[str]
    secret_access_key: Required[str]
