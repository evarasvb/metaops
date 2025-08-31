from app.services.catalog_sync import CatalogSyncService


class DummySheetsClient:
    def read_sheet(self, sheet_key, worksheet_name):
        return [{"SKU": "SKU1", "Nombre": "Producto 1", "Descripción": "Desc 1", "Precio": "1000", "Stock": "5", "ImagenURL": "url", "Categoría": "Categoria"}]


class DummyMetaClient:
    def __init__(self):
        self.items = []

    def create_or_update_product(self, product):
        self.items.append(product)


def test_fetch_inventory():
    service = CatalogSyncService(DummySheetsClient(), DummyMetaClient(), catalog_id="dummy")
    inventory = service.fetch_inventory("sheet_key", "worksheet")
    assert isinstance(inventory, list)
    assert len(inventory) == 1


def test_sync_catalog():
    meta_client = DummyMetaClient()
    service = CatalogSyncService(DummySheetsClient(), meta_client, catalog_id="dummy")
    service.sync_catalog("sheet_key", "worksheet")
    assert len(meta_client.items) > 0
