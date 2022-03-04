def add_to_cart():
    while True:

        item = input("What are you adding to the cart: ").title()

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
            try:
                price = float(input("Price: "))
                quant = float(input("How many: "))
                shopping_cart[item] = item
                cart_item = {'Item' : item, 'Price' : price, 'Quantity' : quant}
                shopping_cart[item] = cart_item
            except:
                print("Make sure you're using digits for price and quantity.")
                
            
        
        leave = input("Would you like to add another item? (Y/N) ").lower()
        if leave == 'y':
            continue
        else:
            break

def remove_from_cart():
    if len(shopping_cart) > 0:
        remove_cart = input("What would you like to remove from your cart: ").title()

        if remove_cart in shopping_cart.keys():
            remove_quant = input("How many would you like to remove? (#/all) ").strip()

            try:
                if remove_quant in {'all', 'All', "ALL"}:
                    del shopping_cart[remove_cart]
            
                elif remove_quant.isdigit():
                    #Test quant against users
                    if shopping_cart[remove_cart]['Quantity'] <= int(remove_quant):
                        remove_quant = input(f"You don't have that many {remove_cart} in the cart, would you like to remove the item from your shopping cart? (Y/N) ").lower()
                        if remove_quant == 'y':
                            del shopping_cart[remove_cart]
                        else:
                            pass
    
                    else:
                        shopping_cart[remove_cart]['Quantity'] -= int(remove_quant)
                
                else:
                    print("Please enter either 'all' or a numeric value.")
            
            except:
                pass
        else:
            print("Item not in cart.")
    else:
        print("Your cart is empty. Consider adding some items to it!")

def list_cart():
    if len(shopping_cart) > 0:
        total = 0
        for item, values in shopping_cart.items():
            # print(item, values)
            print("----")
            print(item)
            for k,v  in values.items():
                if k == 'Price':
                    total += v * shopping_cart[item]['Quantity']
                    print(f"\t{k}: ${v:,.2f}")
                else:
                    print(f"\t{k}: {v}")

        print("----")
        print(f"Total: ${total:,.2f}")
    else:
        print("Your cart is empty. Consider adding some items to it!")

def clear_cart():
    if len(shopping_cart) > 0:
        clear_input = input("Are you sure you want to empty your cart? (Y/N) ").lower()
        if clear_input == 'y':
            shopping_cart.clear()
            print("Your shopping cart is now empty.")
    else:
        print("Shopping cart is already empty.")

def reprice():
    reprice_item = input("What would you like to reprice? ").title()
    if reprice_item in shopping_cart.keys():
        try:
            new_price = float(input("New Price: "))
            shopping_cart[reprice_item]['Price'] = new_price
        except:
            print("Prices are digits only.")
    else:
        print("not here")

def main():
    print("Thank you for shopping at BobMart!")

    while True:
        user_input = input("What would you like to do? (Add/Remove/List/Clear/Reprice/Quit) ").lower()

        if user_input == "add":
            add_to_cart()
        elif user_input == "remove":
            remove_from_cart()
        elif user_input == "list":
            list_cart()
        elif user_input == "clear":
            clear_cart()
        elif user_input == 'reprice':
            reprice()
        elif user_input == "quit":
            break
        else:
            print("Unknown input, please try again.")
            continue


shopping_cart = {}
main()