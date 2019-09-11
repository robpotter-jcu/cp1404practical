"""
CP1404 Practical
Class for guitar
"""

CURRENT_YEAR = 2019
VINTAGE = 50


class Guitar:
    """Represents a guitar object"""
    def __init__(self, name='', year=0, cost=0):
        """Initialise a guitar instance."""
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Return a string representation of a guitar object."""
        return "{} ({}) : ${:.2f}".format(self.name, self.year, self.cost)

    def get_age(self):
        """Return guitar age."""
        return CURRENT_YEAR - self.year

    def is_vintage(self):
        """Returns true of false if the guitar age is >= 50 years or not."""
        return self.get_age() >= VINTAGE

    def __lt__(self, other):
        """Used for to sort guitars by year."""
        return self.year < other.year
