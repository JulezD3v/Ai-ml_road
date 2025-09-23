# Goal: Create a simple contact book where the user can:
# 1. Add a contact (name, number, email).
# 2. View all saved contacts.
# 3. Search for a contact by name.
# 4. Exit the program.

user_info ={}


def add_contact():
    name = input("Name: ")
    number= input("Number: ")
    email = input("E-mail: ")

    user_info[name] ={"Name":name, "Number":number, "E-mail": email}
    info = user_info[name]  
    print(f"{name} has been added to the contact list")
    
    

def view_contacts():
    if not user_info:
        print("Your contact list is empty")
    else:
        print("\n--Contact List---")

        for name, info in user_info.items() :
            print(f"Name: {name}, Number: {info['Number']}, Email: {info['E-mail']}")
            print()
 

def search_contact():
    name = input("Enter the name to search: ")
    if name in user_info:
        info = user_info[name]
        print(f"Found! Name: {name}, Number: {info['Number']}, Email: {info['E-mail']}\n")
    else:
        print("Contact not found.\n")


#MAIN CODE
while True:
     print("1. Add Contact")
     print("2. View All Contacts")
     print("3. Search Contact")
     print("4. Exit")


     choice = input("Enter the number of your choice: ")

     match choice:
        case "1":
            add_contact()
        case "2":
            view_contacts()
        case "3":
            search_contact()
        case "4":
            print("You quite, see you soon")
            break
        case _:
             print("Wrong entry. Try again")

    
