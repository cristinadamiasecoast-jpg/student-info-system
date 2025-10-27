# src/services/student_service.py

import json
import os
from src.models.student import Student


class StudentService:
    def __init__(self, data_file="data/students.json"):
        self.data_file = data_file
        # Make sure the data file exists
        if not os.path.exists(self.data_file):
            with open(self.data_file, "w") as f:
                json.dump([], f)

    def load_students(self):
        """Load all students from JSON file."""
        with open(self.data_file, "r") as f:
            data = json.load(f)
        return [Student.from_dict(item) for item in data]

    def save_students(self, students):
        """Save all students to JSON file."""
        with open(self.data_file, "w") as f:
            json.dump([student.to_dict() for student in students], f, indent=4)

    def add_student(self, student):
        """Add a new student record."""
        students = self.load_students()
        # Prevent duplicate IDs
        if any(s.student_id == student.student_id for s in students):
            print("❌ Student ID already exists!")
            return
        students.append(student)
        self.save_students(students)
        print("✅ Student added successfully!")

    def view_students(self):
        """Display all students."""
        students = self.load_students()
        if not students:
            print("⚠️ No students found.")
            return
        print("\n=== Student Records ===")
        for s in students:
            print(f"ID: {s.student_id}, Name: {s.name}, Age: {s.age}, Course: {s.course}, Year: {s.year_level}")

    def update_student(self, student_id, **kwargs):
        """Update existing student information."""
        students = self.load_students()
        found = False
        for s in students:
            if s.student_id == student_id:
                found = True
                for key, value in kwargs.items():
                    if hasattr(s, key):
                        setattr(s, key, value)
                print("✅ Student updated successfully!")
                break
        if not found:
            print("❌ Student not found.")
        else:
            self.save_students(students)

    def delete_student(self, student_id):
        """Delete a student by ID."""
        students = self.load_students()
        new_students = [s for s in students if s.student_id != student_id]
        if len(new_students) == len(students):
            print("❌ Student not found.")
            return
        self.save_students(new_students)
        print("✅ Student deleted successfully!")
