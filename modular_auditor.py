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


def main():
    total_stock = 0
    total_units_processed = 0
    rejected_entries = 0


    print('Inventory Auditor started. Inventory initialized')
    
    while True:
        result = get_valid_input()
        
        if result == 'quit':
            break
        
        if result is None:
            rejected_entries += 1
            continue
        
        quantity = result
        total_stock = process_delivery(total_stock, quantity)
        tax = calculate_tax(quantity)
        total_units_processed += 1
        
        print(f'Stock entry recorded successfully. Added {quantity}. tax for delivery {tax:.2f}')
        print(f'Current total stock: {total_stock}')
        
        generate_report(total_units_processed, rejected_entries)


if __name__ == "__main__":
      main()            