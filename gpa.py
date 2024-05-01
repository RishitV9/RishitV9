grade1 = {
    "H*1": 93.28, # math
    "AP1": 91.26, # bio
    "AP2": 100, # csa
    "AP3": 93.2, # world
    "X1": 94.79, # french
    "H1": 85,    # lit
}
grade2 = {
    "H*1": 92.18, # math
    "AP1": 92.42, # bio
    "AP2": 99.9, # csa
    "AP3": 84.15, # world
    "X1": 99.81,  # french
    "H1": 88,  # lit
}

######################################### CALCULATIONS:
#============================ GPA (weighted)
def conversions_ap(x: int):
    if x > 94:
        if x >= 98:
            return 5.3
        else:
            return 5.25
    else:
        return round(x * 0.1 - 4.2, 2)

def conversions_h(x: int):
    if x > 94:
        if x >= 98:
            return 5
        else:
            return 4.95
    else:
        return round(x * 0.1 - 4.5, 2)

def conversions_x(x: int):
    if x > 94:
        if x >= 98:
            return 4.5
        else:
            return 4.45
    else:
        return round(x * 0.1 - 5.0, 2)

def convert_to_gpa(x: float, t: str):
    x = round(x)
    if (t == "AP" or t == "H*"):            
        x = conversions_ap(x)
    elif (t == "H"):  
        x = conversions_h(x)
    elif (t == "X"):
        x = conversions_x(x)
    else:
        raise ValueError("type of grade is illegal.")

    return x

grade = 0
count = 0
for i in grade1:
    gpa = convert_to_gpa((grade1[i] + grade2[i]) / 2.0, i[:len(i)-1])
    grade += gpa
    count += 1

print("\nEach Class GPA Weighted:")
for key in grade1:
    print(key + " -> " + str(round((grade1[key] + grade2[key]) / 2.0, 3)))

print(f"\nYour total GPA (weighted): {round(grade / count, 2)}")
#=========================== GPA (unweighted)
def convert_gpa_unweighted(x: int):
    return (x) * (4.0 / 100)

count = 0
grade = 0
for key in grade1:
    count += 1
    grade += convert_gpa_unweighted((grade1[key] + grade2[key]) / 2.0)
print(f"Your total GPA (unweighted): {round(grade / count, 2)}\n")
#=========================== Honor Scociety Eligibility
count = 0
grade = 0
for key in grade1:
    count += 1
    grade += (grade1[key] + grade2[key]) / 2.0

grade = round(grade / count)
if (grade >= 95):
    print("Elligible for Distinguised Honors Society.")
elif (grade >= 90):
    print("Elligible for First Honors Society.")
elif (grade >= 85):
    print("Elligible for Second Honors Society.")
else:
    print("Not elligible for Honors Society")

print("\nPress enter to continue...")
input()
