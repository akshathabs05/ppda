# Function to display menu options
def display_menu():
    print("\nChoose an operation:")
    print("1. Insert an element")
    print("2. Delete an element")
    print("3. Find an element")
    print("4. Sort the list")
    print("5. Reverse the list")
    print("6. Display the list")
    print("7. Exit")

# Initialize an empty list
my_list = []

while True:
    display_menu()
    choice = input("Enter your choice (1-7): ")

    if choice == "1":
        # Insert element
        element = input("Enter element to insert: ")
        my_list.append(element)
        print(f"{element} added to the list.")

    elif choice == "2":
        # Delete element
        element = input("Enter element to delete: ")
        if element in my_list:
            my_list.remove(element)
            print(f"{element} removed from the list.")
        else:
            print(f"{element} not found in the list.")

    elif choice == "3":
        # Find element
        element = input("Enter element to find: ")
        if element in my_list:
            print(f"{element} found at index {my_list.index(element)}.")
        else:
            print(f"{element} not found in the list.")

    elif choice == "4":
        # Sort the list
        my_list.sort()
        print("List sorted.")

    elif choice == "5":
        # Reverse the list
        my_list.reverse()
        print("List reversed.")

    elif choice == "6":
        # Display the list
        print("Current List:", my_list)

    elif choice == "7":
        # Exit program
        print("Exiting program. Goodbye!")
        break

    else:
        print("Invalid choice! Please enter a number between 1 and 7.")
