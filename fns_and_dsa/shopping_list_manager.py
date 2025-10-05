def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list=[]
    while True:
        display_menu()
        choice=input("Enter your choice: ")
        if choice == "1":
            item=str(input("Enter an item to add: "))
            shopping_list.append(item)
            print("new list",shopping_list)
        if choice == "2":
            item=str(input("What do you want to remove: "))
            shopping_list.remove(item)
        if choice == "3":
            print(shopping_list)
        if choice=="4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

main()
