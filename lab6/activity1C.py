# Python program to find the largest of 5 numbers

# Taking five numbers as input from the user
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))
num4 = float(input("Enter fourth number: "))
num5 = float(input("Enter fifth number: "))

# Finding the largest number using max() function
largest = max(num1, num2, num3, num4, num5)

# Display the result
print(f"\nThe largest number is: {largest}")
