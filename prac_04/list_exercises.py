"""
CP1404 Practical 04
List exercises
"""


def main():
    """Basic list operations"""
    numbers = []
    for i in range(5):
        numbers.append(int(input("Number: ")))

    print("The first number is {}".format(numbers[0]))
    print("The last number is {}".format(numbers[-1]))
    print("The smallest number is {}".format(min(numbers)))
    print("The largest number is {}".format(max(numbers)))
    print("The average of the numbers is {}".format(sum(numbers) / len(numbers)))

    username = input("Username: ")
    access_outcome = security_checker(username)
    print(access_outcome)


def security_checker(username):
    """Woefully inadequate security checker"""
    usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45',
                 'BaseInterpreterInterface', 'BaseStdIn', 'Command', 'ExecState',
                 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']

    if username in usernames:
        return "Access granted"
    else:
        return "Access denied"


main()
