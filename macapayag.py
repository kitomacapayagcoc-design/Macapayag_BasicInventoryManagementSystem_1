InventoryManagementSystem.py
users = {}
user_items = {}

def register_user():
    print("\n Register User")
    username = input("Enter username: ")
    if username in users:
        print("Username already exists! Please try another.\n")
        return
    password = input("Enter password: ")
    users[username] = password
    user_items[username] = []
    print("Registration successful!\n")

def login():
    print("\n Log In")
    username = input("Enter username: ")
    password = input("Enter password: ")

    if username in users and users[username] == password:
        print(f"Welcome back, {username}!\n")
        return username
    else:
        print("Login failed! Wrong username or password.\n")
        return None

def add_item(username):
    print("\n--- Add Item ---")
    name = input("Enter item name: ")
    try:
        price = float(input("Enter item price (₱): "))
        qty = int(input("Enter quantity: "))
        total = price * qty

        for item in user_items[username]:
            if item['name'] == name and item['price'] == price:
                
                item['qty'] += qty
                item['total'] += total
                print("Item quantity updated successfully!\n")
                return

       
        user_items[username].append({"name": name, "price": price, "qty": qty, "total": total})
        print("Item added successfully!\n")
    except ValueError:
        print("Invalid input! Price must be a number and quantity must be an integer.\n")

def view_items(username):
    print("\n--- View Items ---")
    items = user_items[username]
    if items:
        print("{:<5} {:<20} {:<12} {:<10} {:<12}".format("No.", "Item Name", "Price (₱)", "Qty", "Total (₱)"))
        print("-" * 60)
        for i, item in enumerate(items, 1):
            print(f"{i:<5} {item['name']:<20} ₱{item['price']:<10.2f} {item['qty']:<10} ₱{item['total']:<10.2f}")
        grand_total = sum(i['total'] for i in items)
        print("-" * 60)
        print(f"{'':<5} {'TOTAL VALUE:':<20} {'':<12} {'':<10} ₱{grand_total:<10.2f}\n")
    else:
        print("No items available.\n")

def update_item(username):
    print("\n--- Update Item ---")
    items = user_items[username]
    view_items(username)
    if not items:
        return
    try:
        index = int(input("Enter item number to edit: ")) - 1
        if 0 <= index < len(items):
            new_name = input("Enter new item name: ")
            new_price = float(input("Enter new price (₱): "))
            new_qty = int(input("Enter new quantity: "))
            confirm = input("Confirm changes? (y/n): ").lower()
            if confirm == 'y':
                new_total = new_price * new_qty
                items[index] = {"name": new_name, "price": new_price, "qty": new_qty, "total": new_total}
                print("Item updated successfully!\n")
        else:
            print("Invalid item number!\n")
    except ValueError:
        print("Invalid input!\n")

def delete_item(username):
    print("\n--- Delete Item ---")
    items = user_items[username]
    view_items(username)
    if not items:
        return
    try:
        name = input("Enter item name to delete: ")
        
        indices_to_delete = [i for i, item in enumerate(items) if item['name'] == name]
        
        if not indices_to_delete:
            print("No item found with that name!\n")
            return
        
        confirm = input(f"Confirm deletion of {len(indices_to_delete)} item(s)? (y/n): ").lower()
        if confirm == 'y':
          
            for index in sorted(indices_to_delete, reverse=True):
                items.pop(index)
            print("Item(s) deleted successfully!\n")
                
        
    except ValueError:
        print("Invalid input!\n")

def dashboard(username):
    while True:
        print(f"\n=== Dashboard ({username}) ===")
        print("1. Add Item")
        print("2. View Items")
        print("3. Update Item")
        print("4. Delete Item")
        print("5. Log Out")

        choice = input("Select an option: ")

        if choice == '1':
            add_item(username)
        elif choice == '2':
            view_items(username)
        elif choice == '3':
            update_item(username)
        elif choice == '4':
            delete_item(username)
        elif choice == '5':
            print(f"Logging out {username}... Goodbye!\n")
            break
        else:
            print("Invalid option. Try again.\n")

def main():
    print("=== Inventory Management System ===")
    while True:
        print("\n1. Log In")
        print("2. Register")
        print("3. Exit")
        choice = input("Select an option: ")

        if choice == '1':
            username = login()
            if username:
                dashboard(username)
        elif choice == '2':
            register_user()
        elif choice == '3':
            print("Goodbye!")
            break
        else:
            print("Invalid option.\n")

if __name__ == "__main__":
    main()