"""
CP1404 Practical
Taxi Simulator
"""

from prac_08.taxi import Taxi
from prac_08.silver_service_taxi import SilverServiceTaxi

MENU = "q)uit, c)hoose taxi, d)rive"


def main():
    total_bill = 0
    this_taxi = None
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]

    print("Let's drive!")
    print(MENU)
    menu_choice = input(">>> ").upper()
    while menu_choice != "Q":
        if menu_choice == "C":
            print("Taxis available: ")
            display_taxis(taxis)
            taxi_choice = int(input("Choose taxi: "))
            this_taxi = taxis[taxi_choice]
        elif menu_choice == "D":
            if this_taxi is None:
                print("Choose a taxi first!")
                menu_choice = "C"
                continue
            this_taxi.start_fare()
            distance_to_drive = float(input("Drive how far? "))
            this_taxi.drive(distance_to_drive)
            trip_cost = this_taxi.get_fare()
            print(f"Your {this_taxi.name} trip cost you ${trip_cost:.2f}")
            total_bill += trip_cost
        else:
            print("Invalid option")
        print(f"Bill to date: ${total_bill:.2f}")
        print(MENU)
        menu_choice = input(">>> ").upper()

    print(f"Total trip cost: ${total_bill:.2f}")
    print("Taxis are now:")
    display_taxis(taxis)


def display_taxis(taxis):
    for i, taxi in enumerate(taxis):
        print(f"{i} - {taxi}")


main()
