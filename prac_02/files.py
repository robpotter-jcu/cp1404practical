"""
File reading and writing code.
"""

# Task 1
write_file = open("name.txt", "w")
name = input("What is your name? ")

print(name, file=write_file)
'''alternate code
write_file.write(name)'''

write_file.close()

# Task 2
read_file = open("name.txt", "r")
name = read_file.read().strip()
'''alternate code
with open("name.txt", "r") as read_file:
    name = read_file.read().strip()'''

print("Your name is", name)

read_file.close()

# Task 3
read_file = open("numbers.txt", "r")

number_1 = int(read_file.readline())
number_2 = int(read_file.readline())
result = number_1 + number_2

print("Result is:", result)

read_file.close()

# Task 4
result = 0
read_file = open("numbers.txt", "r")

for line in read_file:
    number = int(line)
    result += number

print("Result is:", result)

read_file.close()
