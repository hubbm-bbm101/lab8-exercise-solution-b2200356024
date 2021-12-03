import sys

file = sys.argv[1]
students = sys.argv[2]

students_dict = {}
with open(file,"r",encoding="utf-8") as fileobject:
    content = fileobject.readlines()
    for line in content:
        name = line.split(":")[0]
        students_dict[name]=line.split(":")[1].split(",")


print(students_dict)

try:
    for i in students.split(","):
        university = students_dict[i][0]
        department = students_dict[i][1]
        print(f"Name: {i}")
        print(f"University: {university}")
        print(f"Department: {department}")

except KeyError:
    print(f"No record of {i} was found!")


