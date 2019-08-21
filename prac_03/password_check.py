"""Password Check Program
Get password with minimum length
Display asterisks same length as password
"""

MINIMUM_PASSWORD_LENGTH = 8

password = input("Enter minimum {} character password: ".format(MINIMUM_PASSWORD_LENGTH))

while len(password) < MINIMUM_PASSWORD_LENGTH:
    password = input("Enter minimum {} character password: ".format(MINIMUM_PASSWORD_LENGTH))

print('*' * len(password))
