"""
Client for interacting with Meta Graph API and Marketing API.
This module wraps requests to the official Meta endpoints.
"""

from typing import Dict, Any


class MetaClient:
    """Simple wrapper around Meta Graph API."""

    def __init__(self, access_token: str, app_id: str, app_secret: str):
        self.access_token = access_token
        self.app_id = app_id
        self.app_secret = app_secret

    def get_catalog_items(self) -> Dict[str, Any]:
        """Fetch items from Meta catalog. Placeholder implementation."""
        # TODO: Implement call to Meta catalog API
        raise NotImplementedError("Meta catalog fetch not implemented")


def get_meta_client() -> MetaClient:
    """Factory for MetaClient. Replace with dependency injection as needed."""
    from ..config import settings

    return MetaClient(
        access_token=settings.meta_page_access_token,
        app_id=settings.meta_app_id,
        app_secret=settings.meta_app_secret,
    )
