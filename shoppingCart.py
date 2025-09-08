from IPython.display import clear_output
cart = []

def addItem(item):
    clear_output()
    cart.append(item)
    print(f"{item} has been added to your cart")

#Removing items from the cart

def removeItem(item):
    clear_output()
    try:
        cart.remove(item)
        print(f"{item} has been removed from the cart")
    
    except:
        print("Sorry item does not exist")

def showCart():
    clear_output()

    if cart:
        print("Here is your virtual cart 😎")

        for item in cart :
            print(f"-{item}")
        else:
            print("Your cart is empty")

#clearing the cart

def clearCart():
    clear_output()

    cart.clear()
    print("Your cart is now empty😔")

#Main loop

def main():
    done = False

    while not done:
        ans = input("Key in what you want to do next: quit, add, remove, show, clear: ").lower()

        if ans == "quit":
            print("Thank you for using our program 🥰, see next time.")
            showCart()
            done = True
      

        elif ans == "add" :
            item = input("What would you like to add? ")
            addItem(item)
        elif ans =="remove":
            showCart()
            item = input("Key in the item you wish to remove: ").title()
            removeItem(item)
        elif ans == "show":
            showCart()
        elif ans == "clear":
            clearCart()
        else:
            print("Kindly enter a viable option")
        
main()
