"""
Devopness API Python SDK - Painless essential DevOps to everyone

Note:
    This is auto generated by OpenAPI Generator.
    https://openapi-generator.tech
"""

from typing import (
    Required,
    TypedDict,
    Union,
)

from pydantic import Field, StrictStr

from .. import DevopnessBaseModel
from .commit import Commit, CommitPlain


class RepositoryBranch(DevopnessBaseModel):
    """
    RepositoryBranch

    Attributes:
        name (str): The name of the branch
        repo_full_name (str): The full name of the repository (&#x60;owner/repository&#x60;)
        commit (Commit):
    """

    name: StrictStr = Field(description="The name of the branch")
    repo_full_name: StrictStr = Field(
        description="The full name of the repository (`owner/repository`)"
    )
    commit: Commit


class RepositoryBranchPlain(TypedDict, total=False):
    """
    Plain version of RepositoryBranch.
    """

    name: Required[str]
    repo_full_name: Required[str]
    commit: Required[
        Union[
            Commit,
            CommitPlain,
        ]
    ]
