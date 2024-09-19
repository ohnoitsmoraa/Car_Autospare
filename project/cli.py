import sys
from model import setup_db, Product, User, Purchased

session = setup_db()

def main_menu():
    while True:
        print("\nCar Shop CLI")
        print("1. Manage Products")
        print("2. Manage Users")
        print("3. Manage Purchases")
        print("4. Exit")
        
        choice = input("Choose an option: ")
        if choice == "1":
            manage_products()
        elif choice == "2":
            manage_users()
        elif choice == "3":
            manage_purchases()
        elif choice == "4":
            sys.exit()
        else:
            print("Invalid choice, please try again.")

def manage_products():
    while True:
        print("\nManage Products")
        print("1. Create Product")
        print("2. Delete Product")
        print("3. View All Products")
        print("4. Find Product by ID")
        print("5. Back to Main Menu")
        
        choice = input("Choose an option: ")
        if choice == "1":
            name = input("Enter product name: ")
            type = input("Enter product type: ")
            price = float(input("Enter product price: "))
            Product.create(session, name, type, price)
            print("Product created successfully.")
        elif choice == "2":
            product_id = int(input("Enter product ID to delete: "))
            if Product.delete(session, product_id):
                print("Product deleted successfully.")
            else:
                print("Product not found.")
        elif choice == "3":
            products = Product.get_all(session)
            for product in products:
                print(f"ID: {product.id}, Name: {product.product_name}, Type: {product.type}, Price: {product.price}")
        elif choice == "4":
            product_id = int(input("Enter product ID: "))
            product = Product.find_by_id(session, product_id)
            if product:
                print(f"ID: {product.id}, Name: {product.product_name}, Type: {product.type}, Price: {product.price}")
            else:
                print("Product not found.")
        elif choice == "5":
            break
        else:
            print("Invalid choice, please try again.")

def manage_users():
    while True:
        print("\nManage Users")
        print("1. Create User")
        print("2. Delete User")
        print("3. View All Users")
        print("4. Find User by ID")
        print("5. Back to Main Menu")
        
        choice = input("Choose an option: ")
        if choice == "1":
            name = input("Enter user name: ")
            contact = input("Enter user contact: ")
            User.create(session, name, contact)
            print("User created successfully.")
        elif choice == "2":
            user_id = int(input("Enter user ID to delete: "))
            if User.delete(session, user_id):
                print("User deleted successfully.")
            else:
                print("User not found.")
        elif choice == "3":
            users = User.get_all(session)
            for user in users:
                print(f"ID: {user.id}, Name: {user.name}, Contact: {user.contact}")
        elif choice == "4":
            user_id = int(input("Enter user ID: "))
            user = User.find_by_id(session, user_id)
            if user:
                print(f"ID: {user.id}, Name: {user.name}, Contact: {user.contact}")
            else:
                print("User not found.")
        elif choice == "5":
            break
        else:
            print("Invalid choice, please try again.")

def manage_purchases():
    while True:
        print("\nManage Purchases")
        print("1. Create Purchase")
        print("2. Delete Purchase")
        print("3. View All Purchases")
        print("4. Find Purchase by ID")
        print("5. Back to Main Menu")
        
        choice = input("Choose an option: ")
        if choice == "1":
            user_id = int(input("Enter user ID: "))
            product_name = input("Enter product name: ")
            price = float(input("Enter product price: "))
            quantity = int(input("Enter quantity: "))
            Purchased.create(session, user_id, product_name, price, quantity)
            print("Purchase created successfully.")
        elif choice == "2":
            purchase_id = int(input("Enter purchase ID to delete: "))
            if Purchased.delete(session, purchase_id):
                print("Purchase deleted successfully.")
            else:
                print("Purchase not found.")
        elif choice == "3":
            purchases = Purchased.get_all(session)
            for purchase in purchases:
                print(f"ID: {purchase.id}, User ID: {purchase.user_id}, Product Name: {purchase.product_name}, Quantity: {purchase.quantity}, Total Cost: {purchase.total_cost}")
        elif choice == "4":
            purchase_id = int(input("Enter purchase ID: "))
            purchase = Purchased.find_by_id(session, purchase_id)
            if purchase:
                print(f"ID: {purchase.id}, User ID: {purchase.user_id}, Product Name: {purchase.product_name}, Quantity: {purchase.quantity}, Total Cost: {purchase.total_cost}")
            else:
                print("Purchase not found.")
        elif choice == "5":
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main_menu()