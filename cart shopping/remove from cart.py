def remove_from_cart(cart, product_id):
    for c in cart:
        if c["id"]==product_id:
            cart.remove(c)
            print("removed",c["name"],"from cart")
            return
    print("no item found to delete")