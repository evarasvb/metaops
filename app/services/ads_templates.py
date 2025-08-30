from __future__ import annotations
from typing import Dict, Any

from .meta_client import MetaClient


class AdsTemplateService:
    """
    Service for creating simple advertising campaigns via the Meta Marketing API.

    Provides a `create_quick_campaign` method that wraps campaign creation with minimal required
    parameters and basic validations. Actual API communication is delegated to MetaClient.
    """

    def __init__(self, meta_client: MetaClient) -> None:
        self.meta_client = meta_client

    def create_quick_campaign(
        self,
        ad_account_id: str,
        name: str,
        objective: str,
        daily_budget: float,
        start_time: str,
        end_time: str,
        **params: Any,
    ) -> Dict[str, Any]:
        """
        Create a quick advertising campaign.

        Args:
            ad_account_id: The Meta Ad Account ID (with prefix "act_").
            name: Name of the campaign.
            objective: Campaign objective (e.g. "TRAFFIC", "ENGAGEMENT").
            daily_budget: Daily budget in smallest currency unit (e.g. CLP centavos).
            start_time: ISO formatted start time for the campaign.
            end_time: ISO formatted end time for the campaign.
            **params: Additional optional parameters supported by the Marketing API.

        Returns:
            Dictionary with information about the created campaign.

        Raises:
            ValueError: If validations fail.
        """
        if daily_budget <= 0:
            raise ValueError("daily_budget must be positive")
        if not ad_account_id.startswith("act_"):
            raise ValueError("ad_account_id should start with 'act_'")

        # Compose payload for the campaign
        payload: Dict[str, Any] = {
            "name": name,
            "objective": objective,
            "status": "PAUSED",  # start paused by default
            "special_ad_categories": [],
            "daily_budget": str(int(daily_budget)),
            "start_time": start_time,
            "end_time": end_time,
        }
        # Merge extra params (e.g. targeting, bid_strategy)
        payload.update(params)

        # Delegate to MetaClient for API call (should handle errors, rate limits, etc.)
        return self.meta_client.create_campaign(ad_account_id, payload)
