"""
CP1404/CP5632 Practical
Recursion
"""


def do_it(n):
    """Return the sum of n % 2 for all values from n down to 0."""
    if n <= 0:
        return 0
    return n % 2 + do_it(n - 1)


# Output: 3
print(do_it(5))


def do_something(n):
    """Print the squares of positive numbers from n down to 0."""
    if n < 0:
        return
    print(n ** 2)
    do_something(n - 1)


# Example call
do_something(4)
