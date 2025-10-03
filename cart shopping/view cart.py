def view_cart(cart):
    if not cart:
        print("cart is empty")
        return
    total=0
    for c in cart:
        sub_total=c["price"] * c["quantity"]
        total+=sub_total
        print("item:",c["name"],"quantity:",c["quantity"],"total:",total)
        