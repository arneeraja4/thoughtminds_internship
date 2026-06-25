students = []
def add_student():
    student_id = input("Enter Student ID: ")
    name = input("Enter Name: ")
    course = input("Enter Course: ")
    student = {
        "id": student_id,
        "name": name,
        "course": course
    }
    students.append(student)
    print("Student Added Successfully!\n")
def view_students():
    if len(students) == 0:
        print("No Students Found!\n")
        return
    print("\nStudent List")
   
    for student in students:
        print(f"ID     : {student['id']}")
        print(f"Name   : {student['name']}")
        print(f"Course : {student['course']}")

def delete_student():
    student_id = input("Enter Student ID to Delete: ")
    for student in students:
        if student["id"] == student_id:
            students.remove(student)
            print("Student Deleted Successfully!\n")
            return
    print("Student Not Found!\n")
def menu():
    while True:
        print("\n===== STUDENT MANAGEMENT SYSTEM =====")
        print("1. Add Student")
        print("2. View Students")
        print("3. Delete Student")
        print("4. Exit")
        choice = input("Enter Choice: ")
        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            delete_student()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid Choice!")
menu()