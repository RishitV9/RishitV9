grade1 = {
    "AP4": 5.1,
    "AP1": 4.9,
    "AP2": 5.3,
    "AP3": 5.1,
    "X1": 4.45,
    "H2": 4,
}
grade2 = {
    "AP4": 4.9,
    "AP1": 4.7,
    "AP2": 5.3,
    "AP3": 4,
    "X1": 4.5,
    "H2": 4.95,
}

# average everything first:
def convert_to_gpa(x: float, type: str):
    return x

grade = 0
count = 0
for i in grade1:
    gpa = convert_to_gpa((grade1[i] + grade2[i]) / 2.0, i[:len(i)-1])
    grade += gpa
    count += 1

print(f"Your GPA (weighted): {grade / count}")
