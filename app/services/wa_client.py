"""
Client for interacting with WhatsApp Business Cloud API.
"""

from typing import Dict, Any


class WhatsAppClient:
    """Wrapper for WhatsApp Cloud API."""

    def __init__(self, phone_number_id: str, token: str):
        self.phone_number_id = phone_number_id
        self.token = token

    def send_message(self, to: str, template_name: str, variables: Dict[str, str]) -> Any:
        """Send a templated message to WhatsApp. Placeholder."""
        # TODO: Implement actual API call to WhatsApp Cloud API
        raise NotImplementedError("WhatsApp send message not implemented")


def get_wa_client() -> WhatsAppClient:
    """Factory for WhatsAppClient."""
    from ..config import settings

    return WhatsAppClient(
        phone_number_id=settings.wa_phone_number_id, token=settings.wa_token
    )
