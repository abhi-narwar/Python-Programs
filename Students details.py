students={}
for i in range(3):
    name=input("enter the  name")
    rollno=int(input("enter the roll number"))
    dep=input("enter the department name")

    students[name]={'name':name,'rollno':rollno,'dep':dep}
print(students)
    
