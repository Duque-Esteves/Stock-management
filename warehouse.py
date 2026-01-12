import os

stock = [{"name":"tenis", "type":"calcado", "quantity":"10"},
         {"name":"camiseta", "type":"roupa", "quantity":"20"},
         {"name":"bone", "type":"acessorio", "quantity":"15"},
         {"name":"calca", "type":"roupa", "quantity":"5"}]

def createItem ():
    print("Create new item:\n")
    item_name = input("Enter item name: ")
    item_type = input("Enter item type: ")
    item_quantity = input("Enter item quantity: ")
    sku = {"name": item_name, "type": item_type, "quantity": item_quantity}
    stock.append(sku)
    print(f"Item created: {item_name}\n")
    input("Press Enter to continue...")
    main ()

def list_items ():
    print("Items List with type and quantity:\n")
    print ("name | type | quantity")
    for item in stock:
        name = item["name"]
        type = item["type"]
        quantity = item["quantity"]
        print (f'-{name} | {type} | {quantity}')
    input("\nPress Enter to continue...")
    main ()

def welcome_message ():
    os.system("cls")
    print("Welcome to the Inventory Management System (IMS)\n")

def menu():
    print("1. Create Item")
    print("2. List Items")
    print("3. Exit\n")
    choice = input("Select a menu item: ")
    try:
        if choice == '1':
            createItem()
        elif choice == '2':
            list_items()
        elif choice == '3':
            end_program()
        else:
            print("Invalid choice. Please try again.\n")
            main()
    except Exception as e:
        print(f"An error occurred: {e}\n")
        input("Press Enter to continue...")
        main()

def end_program():
    print ("Exiting IMS")

def main ():
    welcome_message()
    menu()
   
if __name__ == "__main__":
    main()