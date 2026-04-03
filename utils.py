from inventory import Inventory
from models import Item

def filter_items(inventory: Inventory, predicate) -> list[Item]:
    """Returns items matching the predicate."""
    return list(filter(predicate, inventory))

def sort_items(inventory: Inventory, key_fn, reverse: bool = False) -> list[Item]:
    """Returns items sorted by the given key function."""
    return sorted(inventory, key=key_fn, reverse=reverse)

def most_expensive(inventory: Inventory) -> Item:
    """Returns the item with the highest price."""
    return max(inventory, key=lambda item: item.price)

def below_quantity_threshold(inventory: Inventory, threshold: int) -> list[Item]:
    """Returns items with quantity below the threshold."""
    return list(filter(lambda item: item.quantity < threshold, inventory))