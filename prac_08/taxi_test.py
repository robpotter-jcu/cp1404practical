"""
CP1404 Practical
Taxi Test
"""

from prac_08.taxi import Taxi


def main():
    prius_1 = Taxi("Prius 1", 100)
    prius_1.drive(40)
    print(prius_1)
    print(f"Current Fair: ${prius_1.get_fare():.2f}")
    prius_1.start_fare()
    prius_1.drive(100)
    print(prius_1)
    print(f"Current Fair: ${prius_1.get_fare():.2f}")


main()
