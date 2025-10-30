# 🎓 Student Information System (Python + JSON)

A simple **Student Information System** built in **Python**, demonstrating CRUD operations, JSON data storage, logging, configuration management, and GitHub integration.

---

## 📘 Project Overview

This project allows users to **add, view, update, and delete** student records using a command-line interface.  
All data is stored in a **JSON file**, making it portable and cloud-ready.  
It also includes a **logging system** that tracks every operation for accountability.

---

## 🧩 Features Implemented

✅ Add new student  
✅ View all student records  
✅ Update existing student information  
✅ Delete student records  
✅ JSON data persistence  
✅ Logging system (`logs/system.log`)  
✅ Error handling and configuration management (`config/config.json`)  
✅ Modular structure for scalability and cloud deployment  

---


## 🏗️ Project Structure

student-info-system/
│
├── data/
│ └── students.json # Stores student records in JSON format
│
├── logs/
│ └── system.log # Automatically records add/update/delete actions
│
├── src/
│ ├── main.py # Entry point — runs the whole system
│ ├── models/
│ │ └── student.py # Student class definition
│ ├── services/
│ │ └── student_service.py # Handles CRUD logic
│ └── utils/
│ └── logger.py # Logging utility for tracking actions
│
└── README.md # Project documentation

---

## ⚙️ How to Run the Program

---

## 🧾 Sample Output

```bash
==== Student Information System ====
1. Add Student
2. View Students
3. Update Student
4. Delete Student
5. Exit
Enter choice (1-5): 1
Enter student ID: 1230729
Enter student name: Cristina Damias
Enter age: 21
Enter course: BSIT
Enter year level: 3
✅ Student added successfully!

==== Student Information System ====
1. Add Student
2. View Students
3. Update Student
4. Delete Student
5. Exit
Enter choice (1-5):


### 🧰 Prerequisites
- Python 3 installed on your computer  
- VS Code or any IDE  
- Git installed and configured  

### 🪜 Steps
1. Clone this repository:
   ```bash
   git clone https://github.com/<cristinadamiasecoast-jpg>/student-info-system.git
2. Navigate to the project folder:
   ```bash
   cd student-info-system


---

## 🧠 Concepts Used
- Python OOP (Classes & Methods)
- File Handling with JSON
- Exception Handling
- Logging System
- Modular Programming

---

## 🤝 Contributor
- **Cristina Damias** — Developer

---

## 📄 License
This project is open-source under the [MIT License](LICENSE).
