from abc import ABC, abstractmethod

class Product(ABC):
    def __init__(self, product_id: str, name: str, price: float, stock: int):
        self._id = product_id
        self._name = name
        self._price = price
        self._stock = stock

    def get_id(self):
        return self._id

    def get_name(self):
        return self._name

    def get_price(self):
        return self._price

    def get_stock(self):
        return self._stock

    #Behaviour
    def update_stock(self, quantity: int):
        if quantity < 0:
            print("Stock quantity cannot be negative.")
            return
        self._stock = quantity
        print("Stock updated successfully.")

    def display_information(self):
        print(f"id: {self._id:6} | name: {self._name:12} | "
              f"price: ${self._price:7.2f} | stock: {self._stock}", end='')

    def to_dict(self):
        return {
            "id": self._id,
            "name": self._name,
            "price": self._price,
            "stock": self._stock
        }

    @abstractmethod
    def get_fulfilment_info(self) -> str:
        """Every concrete prdouct must explain how it is deliveered."""
        pass
