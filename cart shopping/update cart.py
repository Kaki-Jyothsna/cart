def update_cart(cart, product_id, quantity):
    for c in cart:
        if c["id"] == product_id:
            c["quantity"] = quantity
            print("updated ",c["name"],"quantity is",c["quantity"])
            return
    print("item not found")