def menu():
    while True:
        print("\n===== Shopping Cart =====")
        print("1. View Products")
        print("2. Add to Cart")
        print("3. View Cart")
        print("4. Update Cart")
        print("5. Remove from Cart")
        print("6. Checkout")
        print("7. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            list_products()
        elif choice == "2":
            try:
                product_id= int(input("Enter Product ID: "))
                quantity = int(input("Enter Quantity: "))
                add_to_cart(products, cart, product_id, quantity)
            except ValueError:
                print("Invalid input!")
        elif choice == "3":
            view_cart(cart)
        elif choice == "4":
            try:
                product_id = int(input("Enter Product ID to update: "))
                quantity = int(input("Enter new Quantity: "))
                update_cart(cart, product_id, quantity)
            except ValueError:
                print("Invalid input!")
        elif choice == "5":
            try:
                product_id = int(input("Enter Product ID to remove: "))
                remove_from_cart(cart, product_id)
            except ValueError:
                print("Invalid input!")
        elif choice == "6":
            checkout(cart)
        elif choice == "7":
            print("Exiting program")
            break
        else:
            print("Invalid choice!")
menu()