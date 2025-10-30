# src/main.py

from src.models.student import Student
from src.services.student_service import StudentService

def main():
    service = StudentService()

    while True:
        print("\n==== Student Information System ====")
        print("1. Add Student")
        print("2. View Students")
        print("3. Update Student")
        print("4. Delete Student")
        print("5. Exit")

        choice = input("Enter choice (1-5): ")

        if choice == "1":
            student_id = input("Enter student ID: ")
            name = input("Enter student name: ")
            age = input("Enter age: ")
            course = input("Enter course: ")
            year_level = input("Enter year level: ")

            student = Student(student_id, name, age, course, year_level)
            service.add_student(student)

        elif choice == "2":
            service.view_students()

        elif choice == "3":
            student_id = input("Enter ID of student to update: ")
            print("Leave blank if you don’t want to change a field.")
            name = input("New name: ")
            age = input("New age: ")
            course = input("New course: ")
            year_level = input("New year level: ")

            updates = {}
            if name:
                updates["name"] = name
            if age:
                updates["age"] = age
            if course:
                updates["course"] = course
            if year_level:
                updates["year_level"] = year_level

            service.update_student(student_id, **updates)

        elif choice == "4":
            student_id = input("Enter ID of student to delete: ")
            service.delete_student(student_id)

        elif choice == "5":
            print("👋 Exiting... Goodbye!")
            break

        else:
            print("❌ Invalid choice, please try again.")


if __name__ == "__main__":
    main()
