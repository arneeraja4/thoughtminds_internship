class Student:
    def __init__(self, student_id, name, course):
        self.student_id = student_id
        self.name = name
        self.course = course


class StudentManagementSystem:
    def __init__(self):
        self.students = []

    def add_student(self):
        student_id = input("Enter Student ID: ")
        name = input("Enter Name: ")
        course = input("Enter Course: ")

        student = Student(student_id, name, course)
        self.students.append(student)

        print("Student Added Successfully!\n")

    def view_students(self):
        if len(self.students) == 0:
            print("No Students Found!\n")
            return

        print("\nStudent List")
        print("-" * 30)

        for student in self.students:
            print(f"ID     : {student.student_id}")
            print(f"Name   : {student.name}")
            print(f"Course : {student.course}")
            print("-" * 30)

    def delete_student(self):
        student_id = input("Enter Student ID to Delete: ")

        for student in self.students:
            if student.student_id == student_id:
                self.students.remove(student)
                print("Student Deleted Successfully!\n")
                return

        print("Student Not Found!\n")

    def menu(self):
        while True:
            print("\n===== STUDENT MANAGEMENT SYSTEM =====")
            print("1. Add Student")
            print("2. View Students")
            print("3. Delete Student")
            print("4. Exit")

            choice = input("Enter Choice: ")

            if choice == "1":
                self.add_student()

            elif choice == "2":
                self.view_students()

            elif choice == "3":
                self.delete_student()

            elif choice == "4":
                print("Goodbye!")
                break

            else:
                print("Invalid Choice!")


sms = StudentManagementSystem()
sms.menu()