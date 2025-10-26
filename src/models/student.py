# src/models/student.py

class Student:
    def __init__(self, student_id, name, age, course, year_level):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.course = course
        self.year_level = year_level

    def to_dict(self):
        """Convert the student object to a dictionary (for JSON storage)."""
        return {
            "student_id": self.student_id,
            "name": self.name,
            "age": self.age,
            "course": self.course,
            "year_level": self.year_level
        }

    @staticmethod
    def from_dict(data):
        """Create a Student object from a dictionary."""
        return Student(
            student_id=data["student_id"],
            name=data["name"],
            age=data["age"],
            course=data["course"],
            year_level=data["year_level"]
        )
