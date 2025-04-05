# silver_service_taxi.py
from prac_09.taxi import Taxi

class SilverServiceTaxi(Taxi):
    """A specialised version of a Taxi with enhanced fanciness and a flagfall fee."""
    flagfall = 4.50  # Class variable for the fixed fee per trip

    def __init__(self, name, fuel, fanciness):
        """Initialise a SilverServiceTaxi instance.

        fanciness: float, multiplier for price_per_km
        """
        super().__init__(name, fuel)  # Inherits name, fuel, and price_per_km from Taxi
        self.price_per_km = Taxi.price_per_km * fanciness  # Scale price_per_km with fanciness

    def __str__(self):
        """Return a string representation including flagfall."""
        return f"{super().__str__()} plus flagfall of ${self.flagfall:.2f}"

    def get_fare(self):
        """Return the total fare including flagfall."""
        return super().get_fare() + self.flagfall  # Base fare + flagfall