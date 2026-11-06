from product import Product
from can_be_shipped import CanBeShipped

class PhysicalProduct(Product, CanBeShipped):
    TYPE = "physical"
    BASE_SHIPPING_FEE = 5.00
    RATE_PER_KG = 2.00

    def __init__(self, product_id: str, name: str, price: float, stock: int, weight: float):
        super().__init__(product_id, name, price, stock)
        if weight < 0:
            raise ValueError("Weight cannot be negative.")
        self.weight = weight

    def get_weight(self):
        return self.weight

    def display_information(self):
        super().display_information()
        print(f" | type: Physical | Weight: {self.weight:.2f} kg")

    def to_dict(self):
        data = super().to_dict()
        data["type"] = self.TYPE
        data["weight"] = self.weight
        return data

    #Abstract method frpm the product
    def get_fulfilment_info(self) -> str:
        return f"'{self._name}' will be shipped to the customer's address."

    #Interface method from CanBeShipped
    def calculate_shipping_cost(self) -> float:
        return round(self.BASE_SHIPPING_FEE + (self.RATE_PER_KG * self.weight), 2)
