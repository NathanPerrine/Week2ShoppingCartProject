def add_to_cart():
    item = input("What are you adding to the cart: ")
    
    # find if already in cart
    for cart_item in shopping_cart.keys():
        # item in cart
        if cart_item == item:
            print("Already in cart")

            quant = input("How many would you like to add? ")
            shopping_cart[item]['Quantity'] += int(quant)

            break
        # item not in cart
        else:   
            price = input("Price: ")
            quant = input("How many: ")



            shopping_cart[item] = item
            cart_item = {'Item' : item, 'Price' : price, 'Quantity' : quant}
            shopping_cart[item] = cart_item



def remove_from_cart():
    pass

def list_cart():
    pass

def clear_cart():
    pass

def main():

    print("Thank you for shopping at BobMart!")

    while True:
        user_input = input("What would you like to do? (Add/Remove/List/Clear/Quit").lower()

        if user_input == "add":
            add_to_cart()
        elif user_input == "remove":
            remove_from_cart()
        elif user_input == "list":
            list_cart()
        elif user_input == "clear":
            clear_cart()
        elif user_input == "quit":
            break
        else:
            print("Unknown input, please try again.")
            continue


shopping_cart = {'apples': {'Price': 0.50, 'Quantity': 2},
                'Bananas': {'Price': .27, 'Quantity': 4}
}
print(shopping_cart)


# main()
add_to_cart()