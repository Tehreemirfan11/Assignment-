score = int(input("Enter the numeric score: "))

if 90 <= score <= 100:
    grade = "A1"
elif 80 <= score < 90:
    grade = "A"
elif 70 <= score < 80:
    grade = "B"
elif 60 <= score < 70:
    grade = "C"
else:
    grade = "D"

print(f"Your grade is: {grade}")