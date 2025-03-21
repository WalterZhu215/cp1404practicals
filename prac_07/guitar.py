"""
Estimated time: 10min
Real time: 8min
"""

class Guitar:
    def __init__(self, name="", year=0, cost=0):
        """Initialize a Guitar object with name, year, and cost."""
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Return string representation of the Guitar."""
        return f"{self.name} ({self.year}) : ${self.cost:,.2f}"

    def get_age(self):
        """Calculate the age of the guitar based on the reference year."""
        reference_year = 2024  # Updated to be current
        return reference_year - self.year

    def is_vintage(self):
        """Determine if the guitar is vintage (50+ years old)."""
        return self.get_age() >= 50

    def __lt__(self, other):
        """Less than operator for sorting guitars by year."""
        return self.year < other.year

