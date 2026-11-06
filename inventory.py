from product import Product

class Inventory:
    def __init__(self):
        self._products = []

    def add_product(self, product: Product) -> bool:
        if self.search_product(product.get_id()) is not None:
            print("Product ID already exists.")
            return False
        self._products.append(product)
        print("Product added successfully.")
        return True

    def search_product(self, product_id: str):
        product_id = product_id.strip().upper()
        for p in self._products:
            if p.get_id().upper() == product_id:
                return p
        return None

    def display_all(self):
        print("\nCurrent Inventory: ")
        print("-" * 95)
        if not self._products:
            print("Inventory is empty.")
        else:
            for p in self._products:
                p.display_information()
        print("-" * 95)

    def get_all_products(self):
        # used by save/load to convert to JSON
        return list(self._products)

    def clear(self):
        self._products = []
