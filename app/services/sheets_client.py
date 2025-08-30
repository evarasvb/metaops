"""
Client for interacting with Google Sheets.
"""

from typing import List, Dict, Any


class SheetsClient:
    """Wrapper around gspread for Google Sheets operations."""

    def __init__(self, inventory_key: str, reports_key: str, service_account_json: str):
        self.inventory_key = inventory_key
        self.reports_key = reports_key
        self.service_account_json = service_account_json
        # TODO: Initialize gspread client using service account

    def read_inventory(self) -> List[Dict[str, Any]]:
        """Read products from the inventory sheet. Placeholder."""
        raise NotImplementedError("Google Sheets read not implemented")

    def write_report(self, data: List[List[Any]]):
        """Write report data to the reports sheet. Placeholder."""
        raise NotImplementedError("Google Sheets write report not implemented")


def get_sheets_client() -> SheetsClient:
    """Factory for SheetsClient."""
    from ..config import settings

    return SheetsClient(
        inventory_key=settings.google_sheets_inventory_key,
        reports_key=settings.google_sheets_reports_key,
        service_account_json=settings.gcp_service_account_json_path,
    )
