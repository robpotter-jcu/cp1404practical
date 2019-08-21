"""Password Check Program
Get password with minimum length
Display asterisks same length as password
"""

MINIMUM_PASSWORD_LENGTH = 8


def main():
    password = get_password(MINIMUM_PASSWORD_LENGTH)
    print_asterisks(password)


def get_password(minimum_password_length):
    password = input("Enter minimum {} character password: ".format(minimum_password_length))
    while len(password) < minimum_password_length:
        password = input("Enter minimum {} character password: ".format(minimum_password_length))
    return password


def print_asterisks(password):
    print('*' * len(password))


main()
