from decorators import log_operation
from models import Item
from exceptions import DuplicateItemException, ItemNotFoundException, InvalidItemException

class Inventory:
    def __init__(self) -> None:
        self._items: dict[str, Item] = {}

    @log_operation
    def add_item(self, item: Item) -> None:
        if item.item_id in self._items:
            raise DuplicateItemException(item.item_id)
        self._items[item.item_id] = item

    @log_operation
    def remove_item(self, item_id: str) -> None:
        if item_id not in self._items:
            raise ItemNotFoundException(item_id)
        del self._items[item_id]

    @log_operation
    def update_quantity(self, item_id: str, quantity: int) -> None:
        if item_id not in self._items:
            raise ItemNotFoundException(item_id)
        try:
            self._items[item_id].quantity = quantity
        except InvalidItemException as e:
            raise InvalidItemException("quantity", quantity) from e

    def display_inventory(self) -> None:
        if not self._items:
            print("Inventory is empty.")
            return
        for item in self._items.values():
            print(item.display())

    def items_by_category(self, category: str):
        """Yields items matching the given category."""
        for item in self._items.values():
            if item.category() == category:
                yield item

    @classmethod
    def from_list(cls, items: list[Item]) -> 'Inventory':
        inventory = cls()
        for item in items:
            inventory._items[item.item_id] = item
        return inventory
    
    @staticmethod
    def is_valid_id(item_id: str) -> bool:
        return isinstance(item_id, str) and len(item_id) > 0 and item_id.isalnum()

    def __len__(self) -> int:
        return len(self._items)
    
    def __contains__(self, item_id: str) -> bool:
        return item_id in self._items
    
    def __iter__(self):
        return iter(self._items.values())