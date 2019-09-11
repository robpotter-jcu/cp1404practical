"""
CP1404 Practical
Test code for guitar class.
"""

from prac_06.guitar import Guitar


def run_tests():
    """Run tests for guitar class."""
    name = "Gibson L-5 CES"
    year = 1922
    cost = 16035.40

    guitar = Guitar(name, year, cost)
    other = Guitar("Charvette by Charvel", 1990, 1600)

    print("{} get_age() - Expected {}. Got {}".format(guitar.name, 97, guitar.get_age()))
    print("{} get_age() - Expected {}. Got {}".format(other.name, 29, other.get_age()))
    print()
    print("{} is_vintage() - Expected {}. Got {}".format(guitar.name, True, guitar.is_vintage()))
    print("{} is_vintage() - Expected {}. Got {}".format(other.name, False, other.is_vintage()))


if __name__ == "__main__":
    run_tests()
