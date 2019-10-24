"""
CP1404 Practical
Unreliable Car Test
"""

from prac_08.unreliable_car import UnreliableCar


def main():
    pretty_good_car = UnreliableCar("Pretty Good Car", 600, 80)
    pretty_bad_car = UnreliableCar("Pretty Bad Car", 600, 20)

    for distance in range(10, 101, 10):
        print(f"{pretty_good_car} tried to drive {distance}km, drove {pretty_good_car.drive(distance)}km")
        print(pretty_good_car)
        print(f"{pretty_bad_car} tried to drive {distance}km, drove {pretty_bad_car.drive(distance)}km")
        print(pretty_bad_car)
        print()


main()
