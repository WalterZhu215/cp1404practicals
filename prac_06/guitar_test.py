"""
Estimated time: 20min
Real time: 15min
"""

from guitar import Guitar

def test_guitar():
    # Create two test guitars
    guitar1 = Guitar("Gibson L-5 CES", 1922, 16035.40)
    guitar2 = Guitar("Another Guitar", 2013, 999.99)

    # Test get_age() method
    expected_age1 = 100  # Expected age for Gibson L-5 CES
    expected_age2 = 9    # Expected age for Another Guitar
    print(f"{guitar1.name} get_age() - Expected {expected_age1}. Got {guitar1.get_age()}")
    print(f"{guitar2.name} get_age() - Expected {expected_age2}. Got {guitar2.get_age()}")

    # Test is_vintage() method
    expected_vintage1 = True   # Gibson L-5 CES should be vintage (100 >= 50)
    expected_vintage2 = False  # Another Guitar should not be vintage (9 < 50)
    print(f"{guitar1.name} is_vintage() - Expected {expected_vintage1}. Got {guitar1.is_vintage()}")
    print(f"{guitar2.name} is_vintage() - Expected {expected_vintage2}. Got {guitar2.is_vintage()}")

# Run the tests
if __name__ == "__main__":
    test_guitar()
