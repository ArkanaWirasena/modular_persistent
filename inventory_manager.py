import os
import json
from inventory import Inventory
from can_be_shipped import CanBeShipped
import product_factory

#File handling
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
INVENTORY_FILE = os.path.join(SCRIPT_DIR, "inventory.json")

def load_inventory(inventory: Inventory):
    if not os.path.exists(INVENTORY_FILE):
        print("inventory.json not found")
        return 
    
    try:
        with open(INVENTORY_FILE, "r") as f:
            data = json.load(f)

        inventory.clear()
        for item in data:
            try:
                inventory.add_product(product_factory.from_dict(item))
            except (KeyError, ValueError, TypeError) as e:
                print(f"Skipped invalid record {item.get('id','?')}: {e}")

        print("inventory.json found")
        print("Inventory loaded successfully")
    except (json.JSONDecodeError, IOError) as e:
        print(f"Error reading inventory.json: {e}")
            

def save_inventory(inventory: Inventory):
    data = [p.to_dict() for p in inventory.get_all_products()]
    
    try:
        with open(INVENTORY_FILE, "w") as f:
            json.dump(data, f, indent =4)
        print(f"Inventory saved to inventory.json.")
    except IOError as e:
        print(f"Error saving inventory: {e}")    


def display_all(inventory):
    inventory.display_all()

def choose_product_type():
    keys = product_factory.get_type_keys()
    print("Product type:")
    for i, key in enumerate(keys, start=1):
        print(f"{i}. {product_factory.get_label(key)}")
    choice = input(f"Choose product type (1-{len(keys)}): ").strip()
    if not choice.isdigit() or not (1 <= int(choice) <= len(keys)):
        return None
    return keys[int(choice) - 1]


def add_product(inventory: Inventory):
    print("\nAdd New Product")
    type_key = choose_product_type()
    if type_key is None:
        print("Invalid product type.")
        return

    product_id = input("Product ID: ").strip()
    name = input("Product Name: ").strip()
    if not product_id or not name:
        print("Product ID and Name cannot be empty.")
        return
    
    try:
        price = float(input("Product Price: "))
        stock = int(input("Stock Quantity: "))
        extra = {field: conv(input(prompt))
                 for field, prompt, conv in product_factory.get_extra_fields(type_key)}
        if price < 0 or stock < 0:
            raise ValueError("Price and cannot be negative.")
        product = product_factory.create_product(type_key, product_id, name,
                                                 price, stock, **extra)
    except ValueError as e:
        print(f"Invalid input: {e}")
        return
    
    inventory.add_product(product)


def update_stock(inventory: Inventory):
    print("\nUpdate Stock")
    item = inventory.search_product(input("Enter Product ID: "))
    
    if item is None:
        print("Product not found.")
        return

    try:
        new_stock = int(input("Enter new stock quantity: "))
    except ValueError:
        print("Invalid stock quantity.")
        return

    item.update_stock(new_stock)
    print("Stock updated successfully.")

   
def search_product(inventory: Inventory):
    print("\nSearch Product")
    item = inventory.search_product(input("Enter Product ID to search: "))

    if item is None:
        print("Product not found.")
        return

    print("\nProduct found:")
    print("-" * 95)
    item.display_information()
    print(f"Fulfilment Info: {item.get_fulfilment_info()}")
    #only objects that signed the CanBeShipped contract have a shipping cost
    if isinstance(item, CanBeShipped):
        print(f"Shipping Cost: ${item.calculate_shipping_cost():.2f}")
    print("-" * 95)


def menu():
    print("----------MENU----------")
    print("1. Display All Products")
    print("2. Add Product")
    print("3. Update Stock")
    print("4. Search Product")
    print("5. Save Inventory")
    print("6. Exit")
    print("------------------------")


def main():
    print("====================================")
    print("INVENTORY MANAGEMENT SYSTEM")
    print("====================================")
    inventory = Inventory()
    load_inventory(inventory)
    
    while True:
        menu()
        choice = input("Enter your choice (1-6): ").strip()

        if choice == "1":
            display_all(inventory)
        elif choice == "2":
            add_product(inventory)
        elif choice == "3":
            update_stock(inventory)
        elif choice == "4":
            search_product(inventory)
        elif choice == "5":
            save_inventory(inventory)
        elif choice == "6":
            if input("Save before exiting? (y/n): ").strip().lower() == "y":
                save_inventory(inventory)
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please enter 1-6")

        input("\nPress Enter to continue")            

if __name__ == "__main__":
    main()