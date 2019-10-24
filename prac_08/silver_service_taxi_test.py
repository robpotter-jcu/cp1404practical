"""
CP1404 Practical
Silver Service Taxi Test
"""

from prac_08.silver_service_taxi import SilverServiceTaxi


def main():
    hummer = SilverServiceTaxi("Hummer", 200, 2)
    hummer.drive(18)
    print(hummer)
    print(f"Current Fair: ${hummer.get_fare():.2f}")


main()
