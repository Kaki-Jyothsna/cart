def add_to_cart(products,cart, product_id,quantity):
        if len(cart)>=8: 
            print("items reached limit")
            return
        for p in products:
            if p["id"]==product_id:
                 # if already in cart
                for c in cart:
                    if c["id"]==product_id:
                        c["quantity"]+=quantity
                        print("name:" ,p["name"], "quantity:",c["quantity"], )
                        return
            # adding new item in cart
                cart.append({"id": p["id"], "name": p["name"],
                "price": p["price"], "quantity": quantity})
                print("Added", p["name"], "to cart","Qty:", quantity)
                return 