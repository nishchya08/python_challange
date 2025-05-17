# Topic: Variables, Naming Rules, and Datatypes

# A Function to represent introduction of this assignment. Starting with a little welcome message.
def show_intro():
    print(" <UNK> Welcome to python 100 days challange")
    print("<UNK> Topic: Variables, Naming Rules, Datatypes")
    print(" Let's build an Inventory Tracker!\n")

# Empty inventory dictionary , to insert item names with their quantites in further.
inventory = {}

# Add or update a product in the inventory
def add_product(item_name, qty):
    #If the product name is already exists, UPDATE it's quantity in inventory dictionary.
    if item_name in inventory:
        inventory[item_name] += qty
        print(f" Updated {item_name} : now has {inventory[item_name]} items.")

    # if the product name isn't already exists, ADD to inventory with {qty} items. ")
    else:
        inventory[item_name] = qty
        print(f" Added {item_name} : now has {inventory[item_name]} items.")

# Display the existing invntory items.
def view_inventory():
    print(f"Current Inventory:")

    # if the inventory dictionary is empty
    if len(inventory) == 0:
        print(" Inventory is is empty!")

    # if Inventory dictionary isn't empty
    else:
        for item, count in inventory.items():
            print(f"= {item}: {count} (type: {type(count).__name__})")
    # To print an empty line for readibility.
    print()

# Main function
def main():
    # Calling intro function
    show_intro()

    while True:
        print("1> Add/update product")
        print("2> view inventory")
        print(" 3> Exit")

        # Taking input from user to choose option
        user_choice = input("Choose an option (1/2/3): ")
        # if user chooses 1:
        if user_choice == "1":
            # Adding a new item with its quantity
            item = input("Enter product name: ").strip()
            qty_str = input("Enter quantity: ").strip()

            # converting the quantity value into integer and then adding into inventory dictionary.
            if qty_str.isdigit():
                qty_val= int(qty_str)
                # Adding the item with quantity into inventory by calling add_product() function.
                add_product(item, qty_val)
            ## if user chooses option 2:
            else:
                print(" Quantity must be a whole number!\n")
        ## if user chooses option 2:
        elif user_choice == "2":
            view_inventory()
        ## if user option 3:
        elif user_choice == "3":
            print(" Exiting Inventory app.. ")
            break
        # if the user choice option isn't available
        else:
            print(" Invalid option. Try again. \n")

#  Calling main function to start execution
if  __name__ == "__main__":
    main()