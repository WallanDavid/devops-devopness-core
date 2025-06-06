"""
Devopness API Python SDK - Painless essential DevOps to everyone

Note:
    This is auto generated by OpenAPI Generator.
    https://openapi-generator.tech
"""

from typing import List, Optional, Union

from .. import DevopnessBaseService, DevopnessBaseServiceAsync, DevopnessResponse
from ..models import (
    Network,
    NetworkEnvironmentCreate,
    NetworkEnvironmentCreatePlain,
    NetworkRelation,
    NetworkUpdate,
    NetworkUpdatePlain,
)
from ..utils import parse_query_string


class NetworksApiService(DevopnessBaseService):
    """
    NetworksApiService - Auto Generated
    """

    def add_environment_network(
        self,
        environment_id: int,
        network_environment_create: Union[
            NetworkEnvironmentCreate,
            NetworkEnvironmentCreatePlain,
        ],
    ) -> DevopnessResponse[Network]:
        """
        Create a new network for the given environment

        Raises:
            DevopnessApiError: If an API request error occurs.
            DevopnessNetworkError: If a network error occurs.
        """

        endpoint_parts = [
            f"/environments/{environment_id}/networks",
        ]

        endpoint: str = "".join(endpoint_parts)

        response = self._post(endpoint, network_environment_create)

        return DevopnessResponse(response, Network)

    def delete_network(
        self,
        network_id: int,
    ) -> DevopnessResponse[None]:
        """
        Delete a given network

        Raises:
            DevopnessApiError: If an API request error occurs.
            DevopnessNetworkError: If a network error occurs.
        """

        endpoint_parts = [
            f"/networks/{network_id}",
        ]

        endpoint: str = "".join(endpoint_parts)

        response = self._delete(endpoint)

        return DevopnessResponse(response, None)

    def get_network(
        self,
        network_id: int,
    ) -> DevopnessResponse[Network]:
        """
        Get a network by ID

        Raises:
            DevopnessApiError: If an API request error occurs.
            DevopnessNetworkError: If a network error occurs.
        """

        endpoint_parts = [
            f"/networks/{network_id}",
        ]

        endpoint: str = "".join(endpoint_parts)

        response = self._get(endpoint)

        return DevopnessResponse(response, Network)

    def get_status_network(
        self,
        network_id: int,
    ) -> DevopnessResponse[None]:
        """
        Get current status of a network

        Raises:
            DevopnessApiError: If an API request error occurs.
            DevopnessNetworkError: If a network error occurs.
        """

        endpoint_parts = [
            f"/networks/{network_id}/get-status",
        ]

        endpoint: str = "".join(endpoint_parts)

        response = self._post(endpoint)

        return DevopnessResponse(response, None)

    def list_environment_networks(
        self,
        environment_id: int,
        page: Optional[int] = None,
        per_page: Optional[int] = None,
        include_default_network: Optional[bool] = None,
        provider_name: Optional[str] = None,
        region: Optional[str] = None,
    ) -> DevopnessResponse[List[NetworkRelation]]:
        """
        Return a list of all networks belonging to an environment

        Raises:
            DevopnessApiError: If an API request error occurs.
            DevopnessNetworkError: If a network error occurs.
        """

        query_string = parse_query_string(
            {
                "page": page,
                "per_page": per_page,
                "include_default_network": include_default_network,
                "provider_name": provider_name,
                "region": region,
            }
        )

        endpoint_parts = [
            f"/environments/{environment_id}/networks",
            f"?{query_string}",
        ]

        endpoint: str = "".join(endpoint_parts)

        response = self._get(endpoint)

        return DevopnessResponse(response, List[NetworkRelation])

    def update_network(
        self,
        network_id: int,
        network_update: Union[
            NetworkUpdate,
            NetworkUpdatePlain,
        ],
    ) -> DevopnessResponse[None]:
        """
        Update an existing Network

        Raises:
            DevopnessApiError: If an API request error occurs.
            DevopnessNetworkError: If a network error occurs.
        """

        endpoint_parts = [
            f"/networks/{network_id}",
        ]

        endpoint: str = "".join(endpoint_parts)

        response = self._put(endpoint, network_update)

        return DevopnessResponse(response, None)


class NetworksApiServiceAsync(DevopnessBaseServiceAsync):
    """
    NetworksApiServiceAsync - Auto Generated
    """

    async def add_environment_network(
        self,
        environment_id: int,
        network_environment_create: Union[
            NetworkEnvironmentCreate,
            NetworkEnvironmentCreatePlain,
        ],
    ) -> DevopnessResponse[Network]:
        """
        Create a new network for the given environment

        Raises:
            DevopnessApiError: If an API request error occurs.
            DevopnessNetworkError: If a network error occurs.
        """

        endpoint_parts = [
            f"/environments/{environment_id}/networks",
        ]

        endpoint: str = "".join(endpoint_parts)

        response = await self._post(endpoint, network_environment_create)

        return DevopnessResponse(response, Network)

    async def delete_network(
        self,
        network_id: int,
    ) -> DevopnessResponse[None]:
        """
        Delete a given network

        Raises:
            DevopnessApiError: If an API request error occurs.
            DevopnessNetworkError: If a network error occurs.
        """

        endpoint_parts = [
            f"/networks/{network_id}",
        ]

        endpoint: str = "".join(endpoint_parts)

        response = await self._delete(endpoint)

        return DevopnessResponse(response, None)

    async def get_network(
        self,
        network_id: int,
    ) -> DevopnessResponse[Network]:
        """
        Get a network by ID

        Raises:
            DevopnessApiError: If an API request error occurs.
            DevopnessNetworkError: If a network error occurs.
        """

        endpoint_parts = [
            f"/networks/{network_id}",
        ]

        endpoint: str = "".join(endpoint_parts)

        response = await self._get(endpoint)

        return DevopnessResponse(response, Network)

    async def get_status_network(
        self,
        network_id: int,
    ) -> DevopnessResponse[None]:
        """
        Get current status of a network

        Raises:
            DevopnessApiError: If an API request error occurs.
            DevopnessNetworkError: If a network error occurs.
        """

        endpoint_parts = [
            f"/networks/{network_id}/get-status",
        ]

        endpoint: str = "".join(endpoint_parts)

        response = await self._post(endpoint)

        return DevopnessResponse(response, None)

    async def list_environment_networks(
        self,
        environment_id: int,
        page: Optional[int] = None,
        per_page: Optional[int] = None,
        include_default_network: Optional[bool] = None,
        provider_name: Optional[str] = None,
        region: Optional[str] = None,
    ) -> DevopnessResponse[List[NetworkRelation]]:
        """
        Return a list of all networks belonging to an environment

        Raises:
            DevopnessApiError: If an API request error occurs.
            DevopnessNetworkError: If a network error occurs.
        """

        query_string = parse_query_string(
            {
                "page": page,
                "per_page": per_page,
                "include_default_network": include_default_network,
                "provider_name": provider_name,
                "region": region,
            }
        )

        endpoint_parts = [
            f"/environments/{environment_id}/networks",
            f"?{query_string}",
        ]

        endpoint: str = "".join(endpoint_parts)

        response = await self._get(endpoint)

        return DevopnessResponse(response, List[NetworkRelation])

    async def update_network(
        self,
        network_id: int,
        network_update: Union[
            NetworkUpdate,
            NetworkUpdatePlain,
        ],
    ) -> DevopnessResponse[None]:
        """
        Update an existing Network

        Raises:
            DevopnessApiError: If an API request error occurs.
            DevopnessNetworkError: If a network error occurs.
        """

        endpoint_parts = [
            f"/networks/{network_id}",
        ]

        endpoint: str = "".join(endpoint_parts)

        response = await self._put(endpoint, network_update)

        return DevopnessResponse(response, None)
