total_stock = 0
total_units_processed = 0
rejected_entries = 0

while True:
    enter_stock = input("Enter the stock quantity or type 'quit' to stop: ")

    if enter_stock.lower() == 'quit':
        break
    if not enter_stock.isdigit():
        print("Invalid input. Please enter a valid stock quantity.")
        rejected_entries += 1
        continue

    stock_quantity = int(enter_stock)
    
    if stock_quantity < 0:
        rejected_entries += 1
        continue
    
    if stock_quantity > 500:
        print("Stock quantity exceeds the maximum limit of 500. Please enter a valid quantity.")
        break 

    total_stock += stock_quantity 
    total_units_processed += 1
    print("Stock entry recorded successfully.") 

    #reporting
    print(f"Total stock quantity: {total_stock}")
    print(f"Total units processed: {total_units_processed}")
    print(f"Rejected entries: {rejected_entries}")
    