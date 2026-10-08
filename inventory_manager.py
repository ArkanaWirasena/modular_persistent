import os
import json

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
INVENTORY_FILE = os.path.join(SCRIPT_DIR, "inventory.json")

inventory = [
    {"id": "P001", "name": "Laptop", "price": 120.00, "stock": 15},
    {"id": "P002", "name": "Mouse", "price": 25.00, "stock": 40},
    {"id": "P003", "name": "USB Cable", "price": 45.00, "stock": 25}
]

def load_inventory():
    global inventory
    if os.path.exists(INVENTORY_FILE):
        try:
            with open(INVENTORY_FILE, "r") as f:
                inventory = json.load(f)
            print("inventory.json found.")
            print("Inventory loaded successfully.")
        except (json.JSONDecodeError, IOError):
            print("Error reading inventory.json.")
    else:
        print("inventory.json not found.")


def save_inventory():
    try:
        with open(INVENTORY_FILE, "w") as f:
            json.dump(inventory, f, indent =4)
        print(f"Inventory saved to inventory.json.")
    except IOError as e:
        print(f"Error saving inventory: {e}")    


def display_all():
    print("\nCurrent Inventory: ")
    print("-------------------------------")
    if not inventory:
        print("Inventory is empty.")
    else:
        for item in inventory:
            print(f"id: {item['id']:6} | name: {item['name']:12} |", 
                  f"price: ${item['price']:7.2f} | stock: {item['stock']}")
    print("-------------------------------")

def add_product():
    print("\nAdd New Product")
    product_id = input("Product ID:").strip()
    name = input("Product Name: ").strip()

    try:
        price = float(input("Product Price: "))
        stock = int(input("Stock Quantity: "))
    except ValueError:
        print("Invalid price or stock.")
        return
    
    for item in inventory:
        if item["id"] == product_id:
            print("Product ID already exists.")
            return

    inventory.append({
        "id": product_id,
        "name": name,
        "price": price,
        "stock": stock
    })
    print("Product added successfully.")


def find_product(product_id):
    product_id = product_id.strip().upper()
    for item in inventory:
        if item["id"].upper() == product_id:
            return item
    return None    


def update_stock():
    print("\nUpdate Stock")
    item = find_product(input("Enter Product ID: "))
    
    if item is None:
        print("Product not found.")
        return

    try:
        new_stock = int(input("Enter new stock quantity: "))
    except ValueError:
        print("Invalid stock quantity.")
        return
    
    if new_stock < 0:
        print("Stock quantity cannot be negative.")
        return

    item["stock"] = new_stock
    print("Stock updated successfully.")

   
def search_product():
    print("\nSearch Product")
    item = find_product(input("Enter Product ID to search: "))

    if item is None:
        print("Product not found.")
        return

    print("\nProduct found:")
    print("-------------------------------")
    print(f"id: {item['id']}")
    print(f"name: {item['name']}")
    print(f"price: ${item['price']:.2f}")
    print(f"stock: {item['stock']}")
    print("-------------------------------")
    return

    print("Product not found.")


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

    load_inventory()
    
    while True:
        menu()
        choice = input("Enter your choice (1-6): ").strip()

        if choice == "1":
            display_all()
        elif choice == "2":
            add_product()
        elif choice == "3":
            update_stock()
        elif choice == "4":
            search_product()
        elif choice == "5":
            save_inventory()
        elif choice == "6":
            if input("Save before exiting? (y/n): ").strip().lower() == "y":
                save_inventory()
            print("Exiting the program.")
            break        

if __name__ == "__main__":
    main()