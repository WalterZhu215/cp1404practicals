# taxi_simulator.py
from prac_09.taxi import Taxi
from prac_09.silver_service_taxi import SilverServiceTaxi

def main():
    """Simulate a taxi service with user choices."""
    taxis = [
        Taxi("Prius", 100),
        SilverServiceTaxi("Limo", 100, 2),
        SilverServiceTaxi("Hummer", 200, 4)
    ]
    current_taxi = None
    total_bill = 0.0

    print("Let's drive!")
    while True:
        print("q)uit, c)hoose taxi, d)rive")
        choice = input(">>> ").lower()

        if choice == 'q':
            print(f"Total trip cost: ${total_bill:.2f}")
            print("Taxis are now:")
            for i, taxi in enumerate(taxis):
                print(f"{i} - {taxi}")
            break

        elif choice == 'c':
            print("Taxis available:")
            for i, taxi in enumerate(taxis):
                print(f"{i} - {taxi}")
            try:
                taxi_choice = int(input("Choose taxi: "))
                if 0 <= taxi_choice < len(taxis):
                    current_taxi = taxis[taxi_choice]
                    current_taxi.start_fare()  # Reset fare for new selection
                    print(f"Bill to date: ${total_bill:.2f}")
                else:
                    print("Invalid taxi choice")
            except ValueError:
                print("Invalid taxi choice")
            print(f"Bill to date: ${total_bill:.2f}")

        elif choice == 'd':
            if current_taxi is None:
                print("You need to choose a taxi before you can drive")
            else:
                try:
                    distance = float(input("Drive how far? "))
                    if distance < 0:
                        print("Distance must be positive")
                    else:
                        current_taxi.drive(distance)
                        trip_cost = current_taxi.get_fare()
                        print(f"Your {current_taxi.name} trip cost you ${trip_cost:.2f}")
                        total_bill += trip_cost
                        current_taxi.start_fare()  # Reset fare after trip
                except ValueError:
                    print("Invalid distance")
            print(f"Bill to date: ${total_bill:.2f}")

        else:
            print("Invalid option")
            print(f"Bill to date: ${total_bill:.2f}")

if __name__ == "__main__":
    main()