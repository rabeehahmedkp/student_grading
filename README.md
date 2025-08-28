# 🎓 Student Grading System (Python + SQLite3)

## 📌 Project Overview
This mini-project is a simple **Student Grading System** built with **Python** and **SQLite3**.  
It allows users to manage students and their grades using a **command-line interface (CLI)**.  

The project demonstrates:
- Python + SQL database integration
- CRUD (Create, Read, Update, Delete) operations
- Database schema design with relationships
- Basic error handling and input validation

---

## 🎯 Objectives
- Apply Python programming skills with SQL integration.
- Learn how to design and manage a database.
- Implement a CLI application with CRUD functionality.
- Understand database relationships with **two related tables**.

---

## 🏗️ Database Schema

### **Table 1: students**
| Column      | Type    | Description |
|-------------|---------|-------------|
| student_id  | INTEGER | Primary Key (Auto Increment) |
| name        | TEXT    | Student’s full name |
| age         | INTEGER | Student’s age |
| class       | TEXT    | Student’s class/section |

### **Table 2: grades**
| Column      | Type    | Description |
|-------------|---------|-------------|
| grade_id    | INTEGER | Primary Key (Auto Increment) |
| student_id  | INTEGER | Foreign Key → students.student_id |
| subject     | TEXT    | Subject name |
| marks       | INTEGER | Marks scored in subject |

---

## ⚙️ Features
- **Add Student** → Insert new student records  
- **View Students** → Display all students  
- **Update Student** → Edit student details  
- **Delete Student** → Remove student records  
- **Add Grade** → Assign grades to students  
- **View Grades** → See a student’s marks  
- **Exit** → Quit the program  

---

## ▶️ How to Run the Project

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/student-grading-system.git
   cd student-grading-system

