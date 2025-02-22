"""
function main

    numbers = []

    for i in range(5):
        get number
        numbers.append(float(number))

    display "\nThe first number is {numbers[0]}"
    display "The last number is {numbers[-1]}"
    display "The smallest number is {min(numbers)}"
    display "The largest number is {max(numbers)}"
    display "The average of the numbers is {sum(numbers) / len(numbers)}"

"""

def main():
    """Prompt user for 5 numbers"""
    numbers = []

    # Get 5 numbers from the user
    for i in range(5):
        number = input("Number: ")
        numbers.append(float(number))

    print(f"\nThe first number is {numbers[0]}")
    print(f"The last number is {numbers[-1]}")
    print(f"The smallest number is {min(numbers)}")
    print(f"The largest number is {max(numbers)}")
    print(f"The average of the numbers is {sum(numbers) / len(numbers)}")

main()

