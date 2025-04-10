def temperature_converter():
    """Converts temperatures between Celsius, Fahrenheit, and Kelvin."""

    try:
        temp = float(input("Enter the temperature: "))
        unit = input("Enter the original unit (C, F, or K): ").upper()
    except ValueError:
        print("Invalid input. Please enter a number for temperature and a valid unit.")
        return

    if unit not in ("C", "F", "K"):
        print("Invalid unit. Please enter C, F, or K.")
        return

    if unit == "C":
        fahrenheit = (temp * 9/5) + 32
        kelvin = temp + 273.15
        print(f"{temp}°C is {fahrenheit}°F and {kelvin}K")
    elif unit == "F":
        celsius = (temp - 32) * 5/9
        kelvin = (temp - 32) * 5/9 + 273.15
        print(f"{temp}°F is {celsius}°C and {kelvin}K")
    elif unit == "K":
        celsius = temp - 273.15
        fahrenheit = (temp - 273.15) * 9/5 + 32
        print(f"{temp}K is {celsius}°C and {fahrenheit}°F")

if __name__ == "__main__":
    temperature_converter()
