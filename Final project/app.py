import json
import os

# Define the file paths for the JSON Items files
food_file = 'menu.json'
user_file = 'users.json'
order_file = 'orders.json'


# Load the initial Items from the JSON files
with open(food_file, 'r') as f:
    food_items = json.load(f)

with open(user_file, 'r') as f:
    user = json.load(f)

with open(order_file, 'r') as f:
    order_items = json.load(f)


class Order:
    def __init__(self):
        with open('menu.json') as f:
            self.menu = json.load(f)['items']
        with open('orders.json') as f:
            self.orders = json.load(f)['orders']
        
        
    # Function for order placement

    def place_order(self):
        order_items = {}
        print("\nPlease select the food items to order:")
        for i, item in enumerate(self.menu):
            print(f"{i+1}. {item['Name']} ({item['Price']}/- each)")
        while True:
            item_number = input("Enter the item number (0 to end): ")
            if item_number == '0':
                break
            try:
                item_number = int(item_number)
                if item_number < 1 or item_number > len(self.menu):
                    raise ValueError
            except ValueError:
                print("Invalid input. Please enter a valid item number.")
                continue
            quantity = input(f"How many {self.menu[item_number-1]['Name']} do you want to order? ")
            try:
                quantity = int(quantity)
                if quantity < 1:
                    raise ValueError
            except ValueError:
                print("Invalid input. Please enter a valid quantity.")
                continue
            food_id = self.menu[item_number-1]['FoodID']
            item_price = float(self.menu[item_number-1]['Price']) * quantity
            order_items[food_id] = {
                'Name': self.menu[item_number-1]['Name'],
                'Price': self.menu[item_number-1]['Price'],
                'Quantity': quantity,
                'Total': str(item_price)
            }
            

        if not order_items:
            print("No items ordered.")
            input("Press any key to continue??")
            os.system('cls')
            return

        items = []
        total_price = 0
        for food_id, item in order_items.items():
            items.append(item)
            total_price += float(item['Total'])

        print("\nOrder Summary:")
        for item in items:
            print(f"{item['Name']} x {item['Quantity']} = {item['Total']}/-")
        print(f"Total Price: {total_price}/-")

        # add order to order history
        with open("orders.json", "r") as file:
            data = json.load(file)

        # Get the maximum OrderID
        order_id = max(int(order["OrderID"]) for order in data["orders"])
        order_id = int(order_id) + 1
        customer_name = name
        
        order = {
            "OrderID": order_id,
            "CustomerName": customer_name,
            "Items": items,
            "OrderTotal": str(total_price)
        }
        self.orders.append(order)
        with open('orders.json', 'w') as f:
            json.dump({"orders": self.orders}, f)
        
         
        print(f"Order placed successfully! Your order ID is {order_id}.")
        input("Press any key to continue??")
        os.system('cls')



def view_orders(name):
    with open('orders.json', 'r') as f:
        orders_data = json.load(f)
    
    orders = orders_data['orders']
    found_customer_orders = False

    for order in orders:
        if order['CustomerName'] == name:
            print("Order ID:", order['OrderID'])
            print("Customer Name:", order['CustomerName'])
            print("Items:")
            for item in order['Items']:
                print("    Name:", item['Name'])
                print("    Price:", item['Price'])
                print("    Quantity:", item['Quantity'])
                print("    Total:", item['Total'])
            print("Order Total:", order['OrderTotal'])
            print()
            found_customer_orders = True

    if not found_customer_orders:
        print("No orders found for customer", name)
    input("Press any key to continue??")
    os.system('cls')



def auth():
    email = input("Enter Email: ")
    passwd = input("Enter Password: ")
    if email=="admin" and passwd=="admin":
        return True
    else:
        return False

def admin_function():
    while True:
        os.system('cls')
        print("************************************************")
        print("1. Add food item")
        print("2. Edit food item")
        print("3. View food items")
        print("4. Remove food item")
        print("5. Exit")
        print("************************************************")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            admin.add_food_item()
        elif choice == 2:
            admin.edit_food_item()
        elif choice == 3:
            admin.view_food_item()
        elif choice == 4:
            admin.remove_food_item()
        elif choice == 5:
            break
        else:
            print("Invalid choice! Try again.")
            input("Press any key to continue??")
         


#user registration function if present the he will get logged in
def register_user():
    with open('users.json', 'r') as f:
        Items = json.load(f)

    global email 
    email = input("Enter Email: ")
    global name 
    name = input("Enter Name: ")
    
    # Check if user already exists
    print("Checking if user is registered")
    for user in Items['users']:
        if user['Email'] == email:
            print("User already registered. \n Logging in...")
            input("Press any key to continue??")
            return user

    # Get user registration details from user input
    print("User Not Registered")
    msg = input("Do you want to register a new user?\n1. Yes\n2. No\n")
    if msg != "1":
        return None
    os.system('cls')
    phone_number = input("Enter Phone Number: ")
    address = input("Enter Address: ")
    password = input("Enter Password: ")

    
    
    # Add new user to JSON file if user does not exist
    new_user = {
        "Full Name": name,
        "Phone Number": phone_number,
        "Email": email,
        "Address": address,
        "Password": password
    }
    Items['users'].append(new_user)
    
    with open('users.json', 'w') as f:
        json.dump(Items, f, indent=4)
    
    print("User registered successfully.")
    input("Press any key to continue??")
    return new_user

# update user
def update_user_profile(email):
    with open('users.json', 'r') as f:
        data = json.load(f)

    # Find the index of the user with the specified email address
    index = -1
    for i, user in enumerate(data['users']):
        if user['Email'] == email:
            index = i
            break

    if index == -1:
        print(f"No user found with email '{email}'")
        input("Press any key to continue??")
        return

    # Prompt the user to enter the updated details
    print(f"Updating user with email '{email}'")
    new_full_name = input("Enter new Full Name: ")
    new_phone_number = input("Enter new Phone Number: ")
    new_address = input("Enter new Address: ")
    new_password = input("Enter new Password: ")

    # Update the user's details in the JSON data
    data['users'][index]['Full Name'] = new_full_name
    data['users'][index]['Phone Number'] = new_phone_number
    data['users'][index]['Address'] = new_address
    data['users'][index]['Password'] = new_password

    # Write the updated JSON data back to the file
    with open('users.json', 'w') as f:
        json.dump(data, f, indent=4)

    print(f"User with email '{email}' updated successfully")
    input("Press any key to continue??")
        

class Admin:
    def __init__(self):
        try:
            with open("menu.json", "r") as file:
                self.menu = json.load(file)
                self.max_food_id = max([int(item["FoodID"]) for item in self.menu["items"]])
        except:
            self.menu = {"items": []}
            self.max_food_id = 0

    def add_food_item(self):
       
        os.system('cls')
        name = input("Enter food item Name: ")
        quantity = input("Enter food item Quantity: ")
        price = float(input("Enter food item Price in float: "))
        discount = float(input("Enter food item Discount in float: "))
        stock = int(input("Enter food item Stock in int: "))

        self.max_food_id += 1
        new_item = {
            "FoodID": str(self.max_food_id),
            "Name": name,
            "Quantity": quantity,
            "Price": str(price),
            "Discount": str(discount),
            "Stock": str(stock)
        }
        self.menu["items"].append(new_item)
        with open("menu.json", "w") as file:
            json.dump(self.menu, file, indent=4)
        os.system('cls')
        print("Food item added successfully!")
        input("Press any key to continue??")
        os.system('cls')


    def edit_food_item(self):
        food_id = input("Enter food item id: ")
        food_index = -1
        for i, item in enumerate(self.menu["items"]):
            if item["FoodID"] == food_id:
                food_index = i
                break
        if food_index != -1:
            name = input(f"Enter new name for {self.menu['items'][food_index]['Name']}: ")
            quantity = input(f"Enter new quantity for {self.menu['items'][food_index]['Quantity']}: ")
            price = input(f"Enter new price for {self.menu['items'][food_index]['Price']}: ")
            discount = input(f"Enter new discount for {self.menu['items'][food_index]['Discount']}: ")
            stock = input(f"Enter new stock for {self.menu['items'][food_index]['Stock']}: ")

            self.menu["items"][food_index]["Name"] = name
            self.menu["items"][food_index]["Quantity"] = quantity
            self.menu["items"][food_index]["Price"] = price
            self.menu["items"][food_index]["Discount"] = discount
            self.menu["items"][food_index]["Stock"] = stock
            with open("menu.json", "w") as file:
                json.dump(self.menu, file, indent=4)
            os.system('cls')
            print("Food item updated successfully!")
        else:
            print("Food item not found!")
        input("Press any key to continue??")
        os.system('cls')

    def view_food_item(self):
        with open('menu.json') as f:
            data = json.load(f)
            
        os.system('cls')
        print("Food ID\t\tName\t\tQuantity\tPrice\tDiscount\tStock")
        for food_item in data['items']:
            print(f"{food_item['FoodID']}\t{food_item['Name']}\t\t{food_item['Quantity']}\t{food_item['Price']}\t{food_item['Discount']}\t{food_item['Stock']} \n")
        input("Press any key to continue??")
        os.system('cls')

    def remove_food_item(self):
        food_id = input("Enter food item id: ")
        food_index = -1
        for i, item in enumerate(self.menu["items"]):
            if item["FoodID"] == food_id:
                food_index = i
                break
        if food_index != -1:
            del self.menu["items"][food_index]
            with open("menu.json", "w") as file:
                json.dump(self.menu, file, indent=4)
            os.system('cls')
            print("Food item removed successfully!")
        else:
            os.system('cls')
            print("Food item not found!")
        input("Press any key to continue??")
        os.system('cls')




#######################



while True:
    os.system('cls')
    print("************************************************")
    print("*** WELCOME TO THE FOOD ORDERING APP ***\n\n")
    print("1. ADMIN LOGIN ")
    print("2. USER LOGIN ")
    print("3. Exit")
    print("************************************************\n")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        if(auth()):
            admin = Admin()
            admin_function()
        else:
            print("Invalid username or password")
            input("Press any key to continue??")
    elif choice == 2:
        order = Order()
        user_details = register_user()
        if user_details is None:
            continue
        os.system('cls')
        print("Welcome back! \t{}".format(user_details['Full Name']))
        input("Press any key to continue??")
        os.system('cls')
        while True:
            os.system('cls')
            print("************************************************")
            print("1. Place new order")
            print("2. Order History")
            print("3. Update Profile")
            print("4. Exit")
            print("************************************************")
            choice = int(input("Enter your choice: "))
            if choice == 1:
                order.place_order()
            elif choice == 2:
                Name=name
                view_orders(Name)
            elif choice == 3:
                Email=email
                update_user_profile(Email)
            elif choice == 4:
                break
            else:
                print("Invalid choice! Try again.")
                input("Press any key to continue??")

    elif choice == 3:
        break
    else:
        print("Invalid choice! Try again.")
        input("Press any key to continue??")
