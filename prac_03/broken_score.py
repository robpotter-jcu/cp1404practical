"""Broken Score Program (fixed)
"""


def main():
    score = get_score()
    print(score)


def get_score():
    score = float(input("Enter score: "))
    if 50 <= score < 90:
        return "Passable"
    elif 90 <= score <= 100:
        return "Excellent"
    elif 0 <= score < 50:
        return "Bad"
    else:
        return "Invalid score"


main()
