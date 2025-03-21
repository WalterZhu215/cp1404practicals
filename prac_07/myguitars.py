from guitar import Guitar

FILENAME = "guitars.csv"


def main():
    """Main function to manage guitar inventory."""
    guitars = load_guitars(FILENAME)
    display_guitars(guitars, "Current Guitars:")

    # Sort guitars by year and display them
    guitars.sort()
    display_guitars(guitars, "Guitars Sorted by Year:")

    # Get new guitars from the user
    new_guitars = get_new_guitars()
    guitars.extend(new_guitars)

    # Save all guitars back to the file
    save_guitars(FILENAME, guitars)
    print("Guitars saved to file.")


def load_guitars(filename):
    """Load guitars from a CSV file into a list."""
    guitars = []
    try:
        with open(filename, "r") as file:
            for line in file:
                parts = line.strip().split(",")
                if len(parts) == 3:
                    name, year, cost = parts[0], int(parts[1]), float(parts[2])
                    guitars.append(Guitar(name, year, cost))
    except FileNotFoundError:
        print(f"Warning: {filename} not found. Starting with an empty list.")
    return guitars


def display_guitars(guitars, header):
    """Display a list of guitars with a header."""
    print(header)
    for guitar in guitars:
        print(guitar)
    print()


def get_new_guitars():
    """Prompt user for new guitars, returning a list of Guitar objects."""
    new_guitars = []
    name = input("Enter guitar name (or press Enter to finish): ").strip()
    while name:
        try:
            year = int(input("Enter year: "))
            cost = float(input("Enter cost: "))
            new_guitars.append(Guitar(name, year, cost))
        except ValueError:
            print("Invalid input. Please enter numeric values for year and cost.")
        name = input("Enter guitar name (or press Enter to finish): ").strip()
    return new_guitars


def save_guitars(filename, guitars):
    """Save all guitars to a CSV file."""
    with open(filename, "w") as file:
        for guitar in guitars:
            file.write(f"{guitar.name},{guitar.year},{guitar.cost:.2f}\n")


if __name__ == "__main__":
    main()


