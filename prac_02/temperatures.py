"""
function main
    choice = get_user_choice()

    while choice != "Q":
        if choice == "C":
            get celsius
            fahrenheit = convert_celsius_to_fahrenheit(celsius)
            display "Result: {fahrenheit:.2f} F"
        else if choice == "F":
            get fahrenheit
            celsius = convert_fahrenheit_to_celsius(fahrenheit)
            display "Result: {celsius:.2f} C"
        else:
            display "Invalid option"

        choice = get_user_choice()

    display "Thank you."

function convert_celsius_to_fahrenheit(celsius)
    return celsius * 9.0 / 5 + 32

function convert_fahrenheit_to_celsius(fahrenheit)
    return 5 / 9 * (fahrenheit - 32)

function get_user_choice
    display (MENU)
    return input(">>> ")
"""

MENU = """C - Convert Celsius to Fahrenheit
F - Convert Fahrenheit to Celsius
Q - Quit"""

def main():
    choice = get_user_choice()

    while choice != "Q":
        if choice == "C":
            celsius = float(input("Celsius: "))
            fahrenheit = convert_celsius_to_fahrenheit(celsius)
            print(f"Result: {fahrenheit:.2f} F")
        elif choice == "F":
            fahrenheit = float(input("Fahrenheit: "))
            celsius = convert_fahrenheit_to_celsius(fahrenheit)
            print(f"Result: {celsius:.2f} C")
        else:
            print("Invalid option")

        choice = get_user_choice()

    print("Thank you.")

def convert_celsius_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit."""
    return celsius * 9.0 / 5 + 32

def convert_fahrenheit_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius."""
    return 5 / 9 * (fahrenheit - 32)

def get_user_choice():
    """Get the user's menu choice."""
    print(MENU)
    return input(">>> ")

main()