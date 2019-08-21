"""
Broken Score Program (fixed)
"""

score = float(input("Enter score: "))
if 50 <= score < 90:
    print("Passable")
elif 90 <= score <= 100:
    print("Excellent")
elif 0 <= score < 50:
    print("Bad")
else:
    print("Invalid score")
