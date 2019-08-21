"""
Exception Handling Program
"""

finished = False
result = 0
while not finished:
    try:
        result = int(input("Enter an integer: "))
        finished = True
    except ValueError:
        print("Only enter an integer.")
print("Integer entered is:", result)
