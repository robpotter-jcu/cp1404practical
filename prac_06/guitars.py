"""
CP1404 Practical
Client code using guitar class.
"""

from prac_06.guitar import Guitar


def main():
    """Program using guitar class."""
    guitars = []

    print("My guitars!")
    name = input("Name: ")
    while name != '':
        year = int(input("Year: "))
        cost = float(input("Cost: $"))
        guitar_add = Guitar(name, year, cost)
        guitars.append(guitar_add)
        print(guitar_add, "added.")
        name = input("Name: ")

    guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
    guitars.append(Guitar("Charvette by Charvel", 1990, 800))

    if guitars:
        guitars.sort()
        print("These are my guitars:")
        for i, guitar in enumerate(guitars):
            vintage_string = ''
            if guitar.is_vintage():
                vintage_string = "(vintage)"
            print("Guitar {}: {:>20} ({}), worth ${:8.2f}{}".format(i + 1, guitar.name, guitar.year, guitar.cost, vintage_string))
    else:
        print("No guitars!")


main()
