import sqlite3
con = sqlite3.connect("student_grading.db")
cur = con.cursor()

def create_tables():
    conn = sqlite3.connect("student_grading.db")
    cur = conn.cursor()

    # Create Students Table
    cur.execute('''CREATE TABLE IF NOT EXISTS students (
                    student_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    age INTEGER,
                    class TEXT)''')

    # Create Grades Table
    cur.execute('''CREATE TABLE IF NOT EXISTS grades (
                    grade_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    student_id INTEGER,
                    subject TEXT,
                    marks INTEGER,
                    FOREIGN KEY(student_id) REFERENCES students(student_id))''')

    conn.commit()
    conn.close()



# Add Student
def add_student(name, age, student_class):
    conn = sqlite3.connect("student_grading.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO students (name, age, class) VALUES (?, ?, ?)", (name, age, student_class))
    conn.commit()
    conn.close()

# View Students
def view_students():
    conn = sqlite3.connect("student_grading.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM students")
    rows = cur.fetchall()
    conn.close()
    return rows

# Update Student
def update_student(student_id, name, age, student_class):
    conn = sqlite3.connect("student_grading.db")
    cur = conn.cursor()
    cur.execute("UPDATE students SET name=?, age=?, class=? WHERE student_id=?", (name, age, student_class, student_id))
    conn.commit()
    conn.close()

# Delete Student
def delete_student(student_id):
    conn = sqlite3.connect("student_grading.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM students WHERE student_id=?", (student_id,))
    conn.commit()
    conn.close()

# Add Grade
def add_grade(student_id, subject, marks):
    conn = sqlite3.connect("student_grading.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO grades (student_id, subject, marks) VALUES (?, ?, ?)", (student_id, subject, marks))
    conn.commit()
    conn.close()

# View Grades
def view_grades(student_id):
    conn = sqlite3.connect("student_grading.db")
    cur = conn.cursor()
    cur.execute("SELECT subject, marks FROM grades WHERE student_id=?", (student_id,))
    rows = cur.fetchall()
    conn.close()
    return rows


def menu():
    create_tables()
    while True:
        print("\n===== Student Grading System =====")
        print("1. Add Student")
        print("2. View Students")
        print("3. Update Student")
        print("4. Delete Student")
        print("5. Add Grade")
        print("6. View Grades of a Student")
        print("7. Exit")

        choice = input("Enter your choice (1-7): ")

        if choice == "1":
            name = input("Enter name: ")
            age = int(input("Enter age: "))
            student_class = input("Enter class: ")
            add_student(name, age, student_class)
            print("✅ Student added successfully!")

        elif choice == "2":
            students = view_students()
            print("\n--- Student List ---")
            for s in students:
                print(s)

        elif choice == "3":
            sid = int(input("Enter Student ID to update: "))
            name = input("Enter new name: ")
            age = int(input("Enter new age: "))
            student_class = input("Enter new class: ")
            update_student(sid, name, age, student_class)
            print("✅ Student updated successfully!")

        elif choice == "4":
            sid = int(input("Enter Student ID to delete: "))
            delete_student(sid)
            print("✅ Student deleted successfully!")

        elif choice == "5":
            sid = int(input("Enter Student ID to add grade: "))
            subject = input("Enter subject: ")
            marks = int(input("Enter marks: "))
            add_grade(sid, subject, marks)
            print("✅ Grade added successfully!")

        elif choice == "6":
            sid = int(input("Enter Student ID to view grades: "))
            grades = view_grades(sid)
            print(f"\n--- Grades for Student {sid} ---")
            for g in grades:
                print(g)

        elif choice == "7":
            print("👋 Exiting the system. Goodbye!")
            break

        else:
            print("❌ Invalid choice. Try again.")


if __name__ == "__main__":
    menu()
