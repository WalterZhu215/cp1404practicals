"""
Estimated time: 20min
Real time: 20min
"""

class Guitar:
    def __init__(self, name, year, cost):
        self.name = name
        self.year = year
        self.cost = cost

    def is_vintage(self):
        return 2024 - self.year >= 50

    def __str__(self):
        return f"{self.name} ({self.year}) : ${self.cost:,.2f}"

def main():
    print("My guitars!")
    guitars = []

    name = input("Name: ")
    while name:
        year = int(input("Year: "))
        cost = float(input("Cost: "))

        guitar = Guitar(name, year, cost)
        guitars.append(guitar)
        print(f"{guitar} added.\n")

        name = input("Name: ")

    print("\nThese are my guitars:")
    for i, guitar in enumerate(guitars, 1):
        vintage_string = " (vintage)" if guitar.is_vintage() else ""
        print(f"Guitar {i}: {guitar.name:>20} ({guitar.year}), worth ${guitar.cost:10,.2f}{vintage_string}")


main()

