"""
Exception Handling Program

Answer the following questions:
1. When will a ValueError occur?
When entry is anything other than an integer like floats and strings.
2. When will a ZeroDivisionError occur?
When entry for denominator is zero.
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
Yes by using a while loop.
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    while denominator == 0:
        print("Cannot divide by zero!")
        denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
print("Finished.")
