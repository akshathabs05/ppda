def calculator():
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
    except ValueError:
        print("Invalid input. Please enter numbers.")
        return

    print("\nSelect operation:")
    print("1. Add (+)")
    print("2. Subtract (-)")
    print("3. Multiply (*)")
    print("4. Divide (/)")
    print("5. Modulus (%)")
    print("6. Exponential (**)")
    print("7. Floor Division (//)")

    try:
        choice = int(input("Enter choice (1-7): "))
    except ValueError:
        print("Invalid choice. Please enter a number between 1 and 7.")
        return

    if choice == 1:
        result = num1 + num2
        operation = "+"
    elif choice == 2:
        result = num1 - num2
        operation = "-"
    elif choice == 3:
        result = num1 * num2
        operation = "*"
    elif choice == 4:
        if num2 == 0:
            print("Cannot divide by zero.")
            return
        result = num1 / num2
        operation = "/"
    elif choice == 5:
        if num2 == 0:
            print("Cannot perform modulus with zero divisor.")
            return
        result = num1 % num2
        operation = "%"
    elif choice == 6:
        result = num1 ** num2
        operation = "**"
    elif choice == 7:
        if num2 == 0:
            print("Cannot perform floor division with zero divisor.")
            return
        result = num1 // num2
        operation = "//"
    else:
        print("Invalid choice.")
        return

    print(f"{num1} {operation} {num2} = {result}")

if __name__ == "__main__":
    calculator()
