from inventory import Inventory
from models import Electronics, Grocery
from exceptions import InventoryException
from utils import most_expensive, below_quantity_threshold, sort_items

def get_input(prompt: str, cast=str):
    return cast(input(prompt).strip())

def add_electronics(inventory: Inventory) -> None:
    item_id = get_input("ID: ")
    name = get_input("Name: ")
    quantity = get_input("Quantity: ", int)
    price = get_input("Price: ", float)
    warranty = get_input("Warranty (months): ", int)
    inventory.add_item(Electronics(item_id, name, quantity, price, warranty))
    print("Electronics added.")

def add_grocery(inventory: Inventory) -> None:
    item_id = get_input("ID: ")
    name = get_input("Name: ")
    quantity = get_input("Quantity: ", int)
    price = get_input("Price: ", float)
    expiration = get_input("Expiration date: ")
    inventory.add_item(Grocery(item_id, name, quantity, price, expiration))
    print("Grocery added.")

def remove_item(inventory: Inventory) -> None:
    item_id = get_input("Item ID to remove: ")
    inventory.remove_item(item_id)
    print("Item removed.")

def update_quantity(inventory: Inventory) -> None:
    item_id = get_input("Item ID: ")
    quantity = get_input("New quantity: ", int)
    inventory.update_quantity(item_id, quantity)
    print("Quantity updated.")

def read_from_file(inventory: Inventory) -> None:
    filename = get_input("Filename: ")
    inventory.read_from_file(filename)
    print("Inventory loaded.")

def write_to_file(inventory: Inventory) -> None:
    filename = get_input("Filename: ")
    inventory.write_to_file(filename)
    print("Inventory saved.")

def find_most_expensive(inventory: Inventory) -> None:
    item = most_expensive(inventory)
    print(item.display())

def find_below_threshold(inventory: Inventory) -> None:
    threshold = get_input("Quantity threshold: ", int)
    items = below_quantity_threshold(inventory, threshold)
    for item in items:
        print(item.display())

def sort_by_price(inventory: Inventory) -> None:
    items = sort_items(inventory, key_fn=lambda item: item.price)
    for item in items:
        print(item.display())

MENU = """
1. Add Electronics
2. Add Grocery
3. Remove Item
4. Update Quantity
5. Display Inventory
6. Read from File
7. Write to File
8. Find Most Expensive Item
9. Find Items Below Quantity Threshold
10. Sort by Price
11. Exit
"""

ACTIONS = {
    "1":  add_electronics,
    "2":  add_grocery,
    "3":  remove_item,
    "4":  update_quantity,
    "5":  lambda inv: inv.display_inventory(),
    "6":  read_from_file,
    "7":  write_to_file,
    "8":  find_most_expensive,
    "9":  find_below_threshold,
    "10": sort_by_price,
}

def main() -> None:
    inventory = Inventory()
    while True:
        print(MENU)
        choice = input("Choice: ").strip()
        if choice == "11":
            print("Goodbye.")
            break
        action = ACTIONS.get(choice)
        if action is None:
            print("Invalid choice.")
            continue
        try:
            action(inventory)
        except InventoryException as e:
            print(f"Error: {e}")
        except ValueError as e:
            print(f"Invalid input: {e}")

if __name__ == "__main__":
    main()