import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
INVENTORY_FILE = os.path.join(SCRIPT_DIR, "inventory.txt")

inventory = [
    {"id": "1001", "product": "wireless mouse", "qty": 2},
    {"id": "1002", "product": "keyboard", "qty": 1},
    {"id": "1003", "product": "USB Cable", "qty": 3}
]

def get_valid_input():
    enter_stock = input("Enter stock quantity or 'quit' to stop: ") 

    if enter_stock.lower() == "quit":
        return "quit" 

    if not enter_stock.isdigit():
        print("Invalid input. Please enter a valid stock quantity.")
        return None

    quantity = int(enter_stock)

    if quantity < 0:
        print("Stock quantity cannot be negative")
        return None

    if quantity > 500:
        print("Stock quantity exceeds the maximum limit of 500")
        return None

    return quantity


def process_delivery(current_total, new_value):
    return current_total + new_value


def calculate_tax(amount):
    return amount * 0.10


def generate_report(total_units, failed_attempts):
    print(total_units)
    print(failed_attempts)


def add_item(item_id, name, price, quantity):
    new_item = {"id": item_id, "product": name, "price": price, "qty": quantity}
    inventory.append(new_item)
    print(f"Item '{name}' added to inventory.")

def update_stock(item_id, new_quantity):
    for item in inventory:
        if item["id"] == item_id:
            item["qty"] = new_quantity
            print(f"Stock for item '{item['product']}' updated to {new_quantity}.")
            return
    print(f"Item with ID '{item_id}' not found in inventory.")


def display_inventory():
    print("Current Inventory:")
    for item in inventory:
        print(f"ID: {item['id']}, Product: {item['product']},"
              f"Price: {item.get('price', 0)}, Quantity: {item['qty']}")   

def save_inventory():
    with open(INVENTORY_FILE, "w") as f:
        for item in inventory:
            f.write(f"ID: {item['id']}, Product: {item['product']}, Price: {item.get('price', 0)}, Quantity: {item['qty']}\n")
    print(f"Inventory saved to {INVENTORY_FILE}")


def load_inventory():
    global inventory
    try:
        loaded = []
        with open(INVENTORY_FILE, "r") as f: 
            for line in f:
                parts = [p.strip() for p in line.split(",")]
                if len(parts) == 4:
                        id_, product, price, qty = parts
                        loaded.append({"id": id_, "product": product,
                                       "price": float(price), "qty": int(qty)})
                        
        if loaded:
            inventory = loaded
            print("Inventory loaded from file.")
        else:
            print("inventory file empty.")
    except FileNotFoundError:
        print("Inventory file not found.")


def main():
    total_stock = 0
    total_units_processed = 0
    rejected_entries = 0

    print("inventory Auditor started.")
    load_inventory()
    display_inventory()


    while True:
        result = get_valid_input()
        
        if result == 'quit':
            break
        
        if result is None:
            rejected_entries += 1
            continue
        
        quantity = result

        item_id = input("Enter item ID to update stock: ").strip()
        if item_id:
            update_stock(item_id, quantity)
        else:
            print("No product ID given, only total will be given")    
    
        total_stock = process_delivery(total_stock, quantity)
        tax = calculate_tax(quantity)
        total_units_processed += 1

        print(f'Stock entry recorded successfully. Added {quantity}. tax for delivery {tax:.2f}')
        print(f"current total stock: {total_stock}")


        display_inventory()
        generate_report(total_units_processed, rejected_entries) 
        
    save_inventory()
    print("Final report")
    generate_report(total_units_processed, rejected_entries)
    display_inventory()
    print("Inventory auditor finished")

if __name__ == "__main__":
      main()            
