from __future__ import annotations
from typing import Dict, Optional
from datetime import datetime

from .meta_client import MetaClient
from .wa_client import WaClient


class InboxAutomation:
    """
    Basic inbox automation service for Facebook/Instagram DMs, comments and WhatsApp messages.
    Allows defining simple keyword-based auto responses and a silent hour window.
    """

    def __init__(self, meta_client: MetaClient, wa_client: WaClient) -> None:
        self.meta_client = meta_client
        self.wa_client = wa_client
        # map of lowercase keyword -> canned response
        self.rules: Dict[str, str] = {}
        # tuple of (start_hour, end_hour) for silent mode
        self.silent_hours: Optional[tuple[int, int]] = None

    def set_rules(self, rules: Dict[str, str]) -> None:
        """Define or update automation rules.

        Args:
            rules: A dictionary mapping keywords to responses. Keywords are case-insensitive.
        """
        self.rules = {k.lower(): v for k, v in rules.items()}

    def set_silent_hours(self, start_hour: int, end_hour: int) -> None:
        """Set quiet hours when no automatic responses should be sent.

        Args:
            start_hour: Hour in 24h format to start silence (inclusive).
            end_hour: Hour in 24h format to end silence (exclusive).
        """
        self.silent_hours = (start_hour % 24, end_hour % 24)

    def is_silent_time(self) -> bool:
        """Return True if current time falls within the silent hours window."""
        if not self.silent_hours:
            return False
        start, end = self.silent_hours
        current_hour = datetime.now().hour
        # handle wrapping around midnight
        if start <= end:
            return start <= current_hour < end
        else:
            return current_hour >= start or current_hour < end

    def process_message(self, channel: str, message: str, sender_id: str) -> None:
        """
        Process an incoming message and reply based on rules.

        Args:
            channel: 'fb', 'ig' or 'wa' representing Facebook, Instagram or WhatsApp.
            message: The incoming message text.
            sender_id: ID of the user who sent the message (recipient for reply).
        """
        if self.is_silent_time():
            # do nothing during silent hours
            return

        lowered = message.lower()
        for keyword, response in self.rules.items():
            if keyword in lowered:
                # send response via appropriate channel
                if channel == "wa":
                    self.wa_client.send_message(sender_id, response)
                else:
                    # default to Meta client for FB/IG
                    self.meta_client.send_message(channel, sender_id, response)
                return
        # no rules matched; optionally route to human
        # you could log or enqueue the message for manual handling here
        return
