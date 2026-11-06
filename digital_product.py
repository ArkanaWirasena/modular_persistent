from product import Product

class DigitalProduct(Product):
    TYPE = "digital"

    def __init__(self, product_id: str, name: str, price: float, stock: int, download_size: float):
        super().__init__(product_id, name, price, stock)
        self.download_size = download_size
        if download_size <= 0:
            raise ValueError("Download size must be positive.")
        self._download_size = download_size

    def get_download_size(self):
        return self._download_size

    def display_information(self):
        super().display_information()
        print(f" | type: Digital | Download Size: {self._download_size:.1f} MB")

    def to_dict(self):
        data = super().to_dict()
        data["type"] = self.TYPE
        data["download_size"] = self._download_size
        return data

    def get_fulfilment_info(self) -> str:
        return f"'{self._name}' is delivered digitally via download link."