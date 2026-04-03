class InventoryException(Exception):
    pass

class ItemNotFoundException(InventoryException):
    def __init__(self, item_id: str) -> None:
        self.item_id = item_id
        super().__init__(f"Item with ID {item_id} not found.")

class DuplicateItemException(InventoryException):
    def __init__(self, item_id: str) -> None:
        self.item_id = item_id
        super().__init__(f"Item with ID {item_id} already exists.")

class InvalidItemException(InventoryException):
    def __init__(self, field: str, value) -> None:
        super().__init__(f"Invalid value for {field}: {value}")