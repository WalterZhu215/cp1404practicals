"""
Wimbledon Champions Data Processing
Estimate time: 30 minutes
Actual time: 35 minutes

This program reads the wimbledon.csv file, processes the data, and displays:
1. The champions and how many times they have won.
2. The countries of the champions in alphabetical order.
"""

FILENAME = "wimbledon.csv"


def main():
    """Read the data file, process it, and display results."""
    data = read_wimbledon_data(FILENAME)
    champion_wins, champion_countries = process_wimbledon_data(data)
    display_results(champion_wins, champion_countries)


def read_wimbledon_data(filename):
    """Read Wimbledon data from a CSV file and return a list of lists."""
    try:
        with open(filename, "r", encoding="utf-8-sig") as in_file:
            lines = in_file.readlines()[1:]  # Skip the header line
        return [line.strip().split(",") for line in lines]
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return []


def process_wimbledon_data(data):
    """Process the data to count wins and collect countries."""
    champion_wins = {}
    countries = set()

    for entry in data:
        champion = entry[2]  # Champion's name
        country = entry[1]   # Country code

        # Count wins per champion
        champion_wins[champion] = champion_wins.get(champion, 0) + 1

        # Collect countries
        countries.add(country)

    return champion_wins, sorted(countries)


def display_results(champion_wins, champion_countries):
    """Display the champions with their win counts and countries in order."""
    print("Wimbledon Champions:")
    for champion, wins in sorted(champion_wins.items()):
        print(f"{champion} {wins}")

    print("\nThese", len(champion_countries), "countries have won Wimbledon:")
    print(", ".join(champion_countries))


main()
