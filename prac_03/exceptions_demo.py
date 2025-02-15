"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
2. When will a ZeroDivisionError occur?
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
"""
# 1. When will a ValueError occur?
# User enters something that cannot be converted to an integer.
# 2. When will a ZeroDivisionError occur?
# Appears if the user enters zero as the denominator
# 3. Could you change the code to avoid the possibility of a ZeroDivisionError?
# We can verify the denominator before performing the division

"""
try:
    get numerator,denominator
    
    while denominator == 0:
        display "Denominator cannot be zero. Please enter a non-zero number."
        get denominator

    fraction = numerator / denominator
    display fraction

except ValueError:
    display "Numerator and denominator must be valid numbers!"

display "Finished."
"""


try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))

    # Ensure denominator is not zero
    while denominator == 0:
        print("Denominator cannot be zero. Please enter a non-zero number.")
        denominator = int(input("Enter the denominator: "))

    fraction = numerator / denominator
    print(fraction)

except ValueError:
    print("Numerator and denominator must be valid numbers!")

print("Finished.")

