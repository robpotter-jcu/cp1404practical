"""
CP1404 Practical
Taxi Simulator Test
"""

from prac_08.car import Car
from prac_08.taxi import Taxi
from prac_08.silver_service_taxi import SilverServiceTaxi


def main():
    this_car = Car("Hummer", 200)
    this_car.drive(25)
    print(f"{this_car.name} Fuel: ", this_car.fuel)
    print(f"{this_car.name} Odometer: ", this_car.odometer)
    this_car.drive(50)
    print(f"{this_car.name} Fuel: ", this_car.fuel)
    print(f"{this_car.name} Odometer ", this_car.odometer)
    print(this_car)

    distance = int(input("Distance to drive: "))
    while distance > 0:
        distance_travelled = this_car.drive(distance)
        print(f"{this_car} travelled {distance_travelled}")
        distance = int(input("Distance to drive: "))

    this_taxi = Taxi("Prius 1", 100)
    print(this_taxi)
    this_taxi.drive(25)
    print(this_taxi, this_taxi.get_fare())
    this_taxi.start_fare()
    this_taxi.drive(50)
    print(this_taxi, this_taxi.get_fare())

    this_ss_taxi = SilverServiceTaxi("Limo", 100, 2)
    print(this_ss_taxi, this_ss_taxi.get_fare())
    this_ss_taxi.drive(75)
    print(this_ss_taxi, this_ss_taxi.get_fare())


main()
