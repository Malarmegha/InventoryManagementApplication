# Inventory list to store items
inventory = []

def add_item():
    name = input("Enter item name: ")
    quantity = input("Enter item quantity: ")
    price = input("Enter item price: ")
    
    item = {
        "name": name,
        "quantity": int(quantity),
        "price": float(price)
    }
    
    inventory.append(item)
    print(f'Item "{name}" added to the inventory!')

def view_inventory():
    if not inventory:
        print("Inventory is empty.")
        return
    
    print("\nInventory:")
    for idx, item in enumerate(inventory):
        print(f"{idx + 1}. Name: {item['name']}, Quantity: {item['quantity']}, Price: ${item['price']:.2f}")

def delete_item():
    view_inventory()
    if not inventory:
        return
    
    try:
        item_number = int(input("Enter the item number to delete: ")) - 1
        if 0 <= item_number < len(inventory):
            deleted_item = inventory.pop(item_number)
            print(f'Item "{deleted_item["name"]}" deleted successfully!')
        else:
            print("Invalid item number.")
    except ValueError:
        print("Please enter a valid number.")

def main():
    while True:
        print("\nSimple Inventory Management System")
        print("1. Add Item")
        print("2. View Inventory")
        print("3. Delete Item")
        print("4. Exit")
        
        choice = input("Choose an option: ")
        
        if choice == "1":
            add_item()
        elif choice == "2":
            view_inventory()
        elif choice == "3":
            delete_item()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
