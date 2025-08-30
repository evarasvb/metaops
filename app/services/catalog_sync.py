from typing import List, Dict, Any

from .sheets_client import SheetsClient
from .meta_client import MetaClient
from ..utils.backoff import retry_on_exception


class CatalogSyncService:
    """
    Service to synchronize product inventory from Google Sheets to Meta (Facebook/Instagram) Catalog.
    Reads rows from a Google Sheet and ensures each item exists in the Meta catalog.
    """

    def __init__(self, sheets_client: SheetsClient, meta_client: MetaClient, catalog_id: str) -> None:
        self.sheets_client = sheets_client
        self.meta_client = meta_client
        self.catalog_id = catalog_id

    def fetch_inventory(self, sheet_key: str, worksheet_name: str | None = None) -> List[Dict[str, Any]]:
        """
        Fetch inventory data from Google Sheets.

        Args:
            sheet_key: Spreadsheet key of the inventory sheet.
            worksheet_name: Specific worksheet/tab name (optional).

        Returns:
            A list of product dictionaries formatted for the Meta catalog.
        """
        rows = self.sheets_client.read_sheet(sheet_key, worksheet_name)
        products: List[Dict[str, Any]] = []
        for row in rows:
            # Expect columns: SKU, Nombre, Descripción, Precio, Stock, ImagenURL, Categoría
            try:
                sku = row.get("SKU")
                name = row.get("Nombre")
                description = row.get("Descripción") or row.get("Descripción")
                price = row.get("Precio")
                stock = int(row.get("Stock", 0) or 0)
                image_url = row.get("ImagenURL")
                category = row.get("Categoría") or row.get("Categoria")

                if not sku or not name:
                    # skip incomplete rows
                    continue

                product = {
                    "retailer_id": str(sku),
                    "name": str(name),
                    "description": str(description) if description else "",
                    # price must include currency code, assume CLP (Chilean Peso)
                    "price": f"{price} CLP" if price else "0 CLP",
                    "availability": "in stock" if stock > 0 else "out of stock",
                    "image_url": image_url,
                    "category": category,
                }
                products.append(product)
            except Exception:
                # Ignore malformed rows
                continue
        return products

    def sync_catalog(self, sheet_key: str, worksheet_name: str | None = None) -> None:
        """
        Synchronize the Meta catalog with products from the inventory sheet.

        Args:
            sheet_key: Spreadsheet key of the inventory sheet.
            worksheet_name: Specific worksheet/tab name (optional).
        """
        products = self.fetch_inventory(sheet_key, worksheet_name)
        for product in products:
            # Use meta_client to create or update product in the catalog
            # meta_client should handle API specifics, including rate limiting and retries
            self.meta_client.create_or_update_product(self.catalog_id, product)
