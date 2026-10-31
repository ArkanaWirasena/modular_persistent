import os
import json
from inventory import Inventory
from product import Product

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
            product = Product(
                item["id"],
                item["name"],
                float(item["price"]),
                int(item["stock"])
            )
            inventory.add_product(product)

        print("inventory.json found")
        print("Inventory loaded successfully")
    except (json.JSONDecodeError, IOError, KeyError, ValueError) as e:
        print(f"Error reading inventory.json: {e}")    
            

def save_inventory(inventory):
    data = []
    for p in inventory.get_all_products():   
        data.append({
            "id": p.get_id(),
            "name": p.get_name(),
            "price": p.get_price(),
            "stock": p.get_stock()
        })
    
    try:
        with open(INVENTORY_FILE, "w") as f:
            json.dump(data, f, indent =4)
        print(f"Inventory saved to inventory.json.")
    except IOError as e:
        print(f"Error saving inventory: {e}")    


def display_all(inventory):
    inventory.display_all()


def add_product(inventory):
    print("\nAdd New Product")
    product_id = input("Product ID:").strip()
    name = input("Product Name: ").strip()

    try:
        price = float(input("Product Price: "))
        stock = int(input("Stock Quantity: "))
    except ValueError:
        print("Invalid price or stock.")
        return
    

    inventory.add_product(Product(product_id, name, price, stock))


def update_stock(inventory):
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

   
def search_product(inventory):
    print("\nSearch Product")
    item = inventory.search_product(input("Enter Product ID to search: "))

    if item is None:
        print("Product not found.")
        return

    print("\nProduct found:")
    print("-------------------------------")
    item.display_information()
    print("-------------------------------")


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