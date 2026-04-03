from abc import ABC, abstractmethod
from exceptions import InvalidItemException

class Item(ABC):
    __slots__ = ('_item_id', '_name', '_quantity', '_price')
    
    def __init__(self, item_id: str, name: str, quantity: int, price: float) -> None:
        self._item_id = item_id
        self._name = name
        self._quantity = quantity
        self._price = price

    @property
    def item_id(self) -> str:
        return self._item_id
    
    @property
    def name(self) -> str:
        return self._name
    
    @name.setter
    def name(self, value: str) -> None:
        if not value:
            raise ValueError("Name cannot be empty.")
        self._name = value
    
    @property
    def quantity(self) -> int:
        return self._quantity

    @quantity.setter
    def quantity(self, value: int) -> None:
        if value < 0:
            raise InvalidItemException("quantity", value)
        self._quantity = value

    @property
    def price(self) -> float:
        return self._price

    @price.setter
    def price(self, value: float) -> None:
        if value < 0:
            raise InvalidItemException("price", value)
        self._price = value

    @abstractmethod
    def display(self) -> None:
        pass

    @abstractmethod
    def category(self) -> str:
        pass

    def __repr__(self):
        return f"{self.__class__.__name__}(item_id='{self._item_id}', name='{self._name}', quantity={self._quantity}, price={self._price})"
    
    def __str__(self):
        return f"{self._name} (ID: {self._item_id}) - Quantity: {self._quantity}, Price: ${self._price:.2f}"
    

class Electronics(Item):
    __slots__ = ('_warranty_months',)

    def __init__(self, item_id: str, name: str, quantity: int, price: float, warranty_months: int) -> None:
        super().__init__(item_id, name, quantity, price)
        self._warranty_months = warranty_months

    @property
    def warranty_months(self) -> int:
        return self._warranty_months
    
    @warranty_months.setter
    def warranty_months(self, value: int) -> None:
        if value < 0:
            raise ValueError("Warranty months cannot be negative.")
        self._warranty_months = value
    
    def display(self) -> None:
        return f"{self._name} (Electronics) — warranty: {self._warranty_months} months, price: {self._price:.2f}, qty: {self._quantity}"
    
    def category(self) -> str:
        return "Electronics"


class Grocery(Item):
    __slots__ = ('_expiration_date',)

    def __init__(self, item_id: str, name: str, quantity: int, price: float, expiration_date: str) -> None:
        super().__init__(item_id, name, quantity, price)
        self._expiration_date = expiration_date

    @property
    def expiration_date(self) -> str:
        return self._expiration_date

    @expiration_date.setter
    def expiration_date(self, value: str) -> None:
        if not value:
            raise ValueError("Expiration date cannot be empty.")
        self._expiration_date = value

    def display(self) -> None:
        return f"{self._name} (Grocery) — expiration: {self._expiration_date}, price: {self._price:.2f}, qty: {self._quantity}"

    def category(self) -> str:
        return "Grocery"