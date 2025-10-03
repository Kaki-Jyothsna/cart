def checkout(cart):
    if not cart:
        print("Cart is empty, nothing to checkout")
        return
    view_cart(cart)
    print("Checkout complete. Thank you for shopping!")
    cart.clear()