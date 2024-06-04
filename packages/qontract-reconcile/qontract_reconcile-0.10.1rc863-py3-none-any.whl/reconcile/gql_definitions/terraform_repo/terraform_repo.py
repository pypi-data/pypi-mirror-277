"""
Generated by qenerate plugin=pydantic_v1. DO NOT MODIFY MANUALLY!
"""
from collections.abc import Callable  # noqa: F401 # pylint: disable=W0611
from datetime import datetime  # noqa: F401 # pylint: disable=W0611
from enum import Enum  # noqa: F401 # pylint: disable=W0611
from typing import (  # noqa: F401 # pylint: disable=W0611
    Any,
    Optional,
    Union,
)

from pydantic import (  # noqa: F401 # pylint: disable=W0611
    BaseModel,
    Extra,
    Field,
    Json,
)

from reconcile.gql_definitions.fragments.vault_secret import VaultSecret


DEFINITION = """
fragment VaultSecret on VaultSecret_v1 {
    path
    field
    version
    format
}

query TerraformRepo {
  repos: terraform_repo_v1 {
    account {
      name
      uid
      automationToken {
        ...VaultSecret
      }
      terraformState {
        provider
        bucket
        region
        integrations {
          integration
          key
        }
      }
    }
    name
    repository
    ref
    projectPath
    delete
    requireFips
    tfVersion
    variables {
      inputs {
        ...VaultSecret
      }
      outputs {
        ...VaultSecret
      }
    }
  }
}
"""


class ConfiguredBaseModel(BaseModel):
    class Config:
        smart_union=True
        extra=Extra.forbid


class AWSTerraformStateIntegrationsV1(ConfiguredBaseModel):
    integration: str = Field(..., alias="integration")
    key: str = Field(..., alias="key")


class TerraformStateAWSV1(ConfiguredBaseModel):
    provider: str = Field(..., alias="provider")
    bucket: str = Field(..., alias="bucket")
    region: str = Field(..., alias="region")
    integrations: list[AWSTerraformStateIntegrationsV1] = Field(..., alias="integrations")


class AWSAccountV1(ConfiguredBaseModel):
    name: str = Field(..., alias="name")
    uid: str = Field(..., alias="uid")
    automation_token: VaultSecret = Field(..., alias="automationToken")
    terraform_state: Optional[TerraformStateAWSV1] = Field(..., alias="terraformState")


class TerraformRepoVariablesV1(ConfiguredBaseModel):
    inputs: VaultSecret = Field(..., alias="inputs")
    outputs: VaultSecret = Field(..., alias="outputs")


class TerraformRepoV1(ConfiguredBaseModel):
    account: AWSAccountV1 = Field(..., alias="account")
    name: str = Field(..., alias="name")
    repository: str = Field(..., alias="repository")
    ref: str = Field(..., alias="ref")
    project_path: str = Field(..., alias="projectPath")
    delete: Optional[bool] = Field(..., alias="delete")
    require_fips: Optional[bool] = Field(..., alias="requireFips")
    tf_version: str = Field(..., alias="tfVersion")
    variables: Optional[TerraformRepoVariablesV1] = Field(..., alias="variables")


class TerraformRepoQueryData(ConfiguredBaseModel):
    repos: Optional[list[TerraformRepoV1]] = Field(..., alias="repos")


def query(query_func: Callable, **kwargs: Any) -> TerraformRepoQueryData:
    """
    This is a convenience function which queries and parses the data into
    concrete types. It should be compatible with most GQL clients.
    You do not have to use it to consume the generated data classes.
    Alternatively, you can also mime and alternate the behavior
    of this function in the caller.

    Parameters:
        query_func (Callable): Function which queries your GQL Server
        kwargs: optional arguments that will be passed to the query function

    Returns:
        TerraformRepoQueryData: queried data parsed into generated classes
    """
    raw_data: dict[Any, Any] = query_func(DEFINITION, **kwargs)
    return TerraformRepoQueryData(**raw_data)
