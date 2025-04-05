# silver_service_taxi_test.py
from prac_09.silver_service_taxi import SilverServiceTaxi

def main():
    # Create a SilverServiceTaxi
    hummer = SilverServiceTaxi("Hummer", 200, 4)
    print("Initial state:")
    print(hummer)

    # Test a short trip
    hummer.start_fare()
    hummer.drive(10)
    print("\nAfter 10 km trip:")
    print(hummer)
    print(f"Fare: ${hummer.get_fare():.2f}")

    # Test case: 18 km with fanciness 2, should be $48.78
    test_taxi = SilverServiceTaxi("Test Taxi", 100, 2)
    test_taxi.start_fare()
    test_taxi.drive(18)
    expected_fare = 48.78  # 18 * (1.23 * 2) + 4.50
    actual_fare = test_taxi.get_fare()
    print(f"\nTest case (18 km, fanciness 2):")
    print(test_taxi)
    print(f"Expected fare: ${expected_fare:.2f}, Actual fare: ${actual_fare:.2f}")
    assert abs(actual_fare - expected_fare) < 0.01, f"Fare mismatch: expected {expected_fare}, got {actual_fare}"

    print("All tests passed!")

main()