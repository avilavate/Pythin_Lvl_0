students=[]

class Student:
        def __init__(self,name, student_id=332):
            student={
                "name":name,
                "student_id":student_id
            }
            students.append(student)

        def __str__(self):
             return "Student"

#s1= Student()
s2= Student("Avil1",213)
#s1.add_student("Avil",112)
print(students)

print(s2)