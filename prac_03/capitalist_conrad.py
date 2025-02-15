"""
CP1404/CP5632 - Practical
Capitalist Conrad wants a stock price simulator for a volatile stock.
The price starts off at $10.00, and, at the end of every day there is
a 50% chance it increases by 0 to 10%, and
a 50% chance that it decreases by 0 to 5%.
If the price rises above $1000, or falls below $0.01, the program should end.
The price should be displayed to the nearest cent (e.g. $33.59, not $33.5918232901)
"""


import random

# Constants for the simulation
MAX_INCREASE = 0.175  # 17.5%
MAX_DECREASE = 0.05   # 5%
MIN_PRICE = 1.0       # Minimum allowed price
MAX_PRICE = 100.0     # Maximum allowed price
INITIAL_PRICE = 10.0  # Starting price
FILENAME = "prices.txt"  # Output file name

# Open the file for writing
out_file = open(FILENAME, 'w')

# Initialize price and day counter
price = INITIAL_PRICE
number_of_days = 0

# Write initial price to file
print(f"Starting price: ${price:,.2f}", file=out_file)

# Simulate price changes
while MIN_PRICE <= price <= MAX_PRICE:
    number_of_days += 1  # Increment the day count
    price_change = 0

    # Determine if the price increases or decreases
    if random.randint(1, 2) == 1:
        price_change = random.uniform(0, MAX_INCREASE)  # Increase up to 17.5%
    else:
        price_change = random.uniform(-MAX_DECREASE, 0)  # Decrease up to 5%

    price *= (1 + price_change)
    print(f"On day {number_of_days} price is: ${price:,.2f}", file=out_file)

# Close the file after simulation
out_file.close()

