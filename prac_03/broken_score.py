"""Broken Score Program (fixed)
"""


"""Broken Score Program (fixed)
"""


def main():
    score = float(input("Enter score: "))
    result = determine_result(score)
    print(result)


def determine_result(score):
    while not 0 <= score <= 100:
        return "Invalid score"
    if score < 50:
        return "Bad"
    elif score < 90:
        return "Passable"
    elif score <= 100:
        return "Excellent"


main()

