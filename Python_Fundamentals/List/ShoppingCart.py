#without Ai
"""
For today’s project, we’re going to build an application that stores products within a list. 
We’ll be able to add, remove, clear, and show the products in the cart. All the concepts 
taught throughout the past few weeks will be used.
To follow along with this lesson, let’s continue from our previous notebook file 
“Week_05” and add a markdown cell at the bottom that says, “Friday Project: Creating a 
Shopping Cart.”

"""
# Friday Project: Creating a Shopping Cart (using match-case)

items = []

def show_menu():
    print("\n=== Shopping Cart Menu ===")
    print("1. Add")
    print("2. Remove")
    print("3. Clear")
    print("4. Show")
    print("5. Quit")

def show_list():
    if not items:
        print("🛒 Your cart is empty.")
    else:
        print("\nItems in your cart:")
        for i, item in enumerate(items, start=1):
            print(f"{i}. {item}")

while True:
    show_menu()
    choice = input("Select option (1–5): ")

    match choice:
        case "1":
            item = input("Enter item to add: ")
            items.append(item)
            print(f"✅ {item} added to your cart.")

        case "2":
            show_list()
            remove_item = input("Enter item to remove: ")
            if remove_item in items:
                items.remove(remove_item)
                print(f"❌ {remove_item} removed.")
            else:
                print("⚠️ Item not found.")

        case "3":
            items.clear()
            print("🧹 Cart cleared.")

        case "4":
            show_list()

        case "5":
            print("👋 See you next time!")
            break

        case _:
            print("⚠️ Invalid choice. Try again.")
