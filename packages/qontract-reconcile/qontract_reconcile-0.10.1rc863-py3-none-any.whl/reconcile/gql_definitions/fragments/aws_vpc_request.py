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

from reconcile.gql_definitions.fragments.terraform_state import TerraformState
from reconcile.gql_definitions.fragments.vault_secret import VaultSecret


class ConfiguredBaseModel(BaseModel):
    class Config:
        smart_union=True
        extra=Extra.forbid


class AWSAccountV1(ConfiguredBaseModel):
    name: str = Field(..., alias="name")
    uid: str = Field(..., alias="uid")
    terraform_username: Optional[str] = Field(..., alias="terraformUsername")
    automation_token: VaultSecret = Field(..., alias="automationToken")
    supported_deployment_regions: Optional[list[str]] = Field(..., alias="supportedDeploymentRegions")
    resources_default_region: str = Field(..., alias="resourcesDefaultRegion")
    provider_version: str = Field(..., alias="providerVersion")
    terraform_state: Optional[TerraformState] = Field(..., alias="terraformState")


class NetworkV1(ConfiguredBaseModel):
    network_address: str = Field(..., alias="networkAddress")


class VPCRequestSubnetsListsV1(ConfiguredBaseModel):
    private: Optional[list[str]] = Field(..., alias="private")
    public: Optional[list[str]] = Field(..., alias="public")
    availability_zones: Optional[list[str]] = Field(..., alias="availability_zones")


class VPCRequest(ConfiguredBaseModel):
    identifier: str = Field(..., alias="identifier")
    delete: Optional[bool] = Field(..., alias="delete")
    account: AWSAccountV1 = Field(..., alias="account")
    region: str = Field(..., alias="region")
    cidr_block: NetworkV1 = Field(..., alias="cidr_block")
    subnets: Optional[VPCRequestSubnetsListsV1] = Field(..., alias="subnets")
