students=[]

def get_students_titlecase():
    students_titlecase=[]
    for student in students:
        students_titlecase.append(student["name"].title())
    return students_titlecase

def print_student_titlecase():
    students_titlecase=get_students_titlecase()
    print(students_titlecase)

def add_student(name, student_id=332):
    student={
        "name":name,
        "student_id":student_id
    }
    students.append(student)

def save_student(student):
    try:
        f= open("./student.txt","a")
        f.write(student+"\n")
        f.close()
    except Exception:
        print("Couldnt write to the file")

def read_student():
    try:
        f=open("./student.txt","r")
        for student in f.readlines():
            add_student(student)
        f.close()
    except Exception:
        print("Could not read student file")


#add_student("john")
#student_name=input("Enter Student Name: ")
#student_id=input("Enter Student Id: ")
#add_student(student_name, student_id)
#print_student_titlecase()

read_student()
print_student_titlecase()

student_name=input("Enter Student Name: ")
student_id=input("Enter Student Id: ")
add_student(student_name, student_id)
save_student(student_name)
print_student_titlecase()