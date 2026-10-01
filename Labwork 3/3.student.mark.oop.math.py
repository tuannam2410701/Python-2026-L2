import math
import numpy as np


# Store students, courses and marks
students = []
courses = []
marks = {}


# ==========================================
# INPUT STUDENTS
# ==========================================

def input_number_of_students():
    n = int(input("Enter number of students: "))

    for i in range(n):
        input_student_information()


def input_student_information():
    student_id = input("Enter student ID: ")
    name = input("Enter student name: ")
    dob = input("Enter date of birth: ")

    student = {
        "id": student_id,
        "name": name,
        "dob": dob
    }

    students.append(student)
    marks[student_id] = {}


# ==========================================
# INPUT COURSES
# ==========================================

def input_number_of_courses():
    n = int(input("Enter number of courses: "))

    for i in range(n):
        input_course_information()


def input_course_information():
    course_id = input("Enter course ID: ")
    name = input("Enter course name: ")
    credit = int(input("Enter number of credits: "))

    course = {
        "id": course_id,
        "name": name,
        "credit": credit
    }

    courses.append(course)


# ==========================================
# INPUT MARKS
# ==========================================

def input_marks():

    if len(courses) == 0:
        print("There are no courses.")
        return

    print("\n--- Course List ---")

    for course in courses:
        print(
            course["id"],
            "-",
            course["name"],
            "(",
            course["credit"],
            "credits)"
        )

    course_id = input("Select course ID: ")

    # Find course
    course_found = False

    for course in courses:
        if course["id"] == course_id:
            course_found = True
            break

    if not course_found:
        print("Course not found.")
        return

    # Input mark for every student
    for student in students:

        mark = float(
            input("Enter mark for " + student["name"] + ": ")
        )

        # Round DOWN to 1 decimal place
        mark = math.floor(mark * 10) / 10

        marks[student["id"]][course_id] = mark

        print("Saved mark:", mark)


# ==========================================
# LIST STUDENTS
# ==========================================

def list_students():

    print("\n--- Student List ---")

    for student in students:
        print(
            "ID:", student["id"],
            "| Name:", student["name"],
            "| DoB:", student["dob"]
        )


# ==========================================
# LIST COURSES
# ==========================================

def list_courses():

    print("\n--- Course List ---")

    for course in courses:
        print(
            "ID:", course["id"],
            "| Name:", course["name"],
            "| Credit:", course["credit"]
        )


# ==========================================
# SHOW MARKS
# ==========================================

def show_student_marks():

    course_id = input("Enter course ID: ")

    course_found = False

    for course in courses:
        if course["id"] == course_id:
            course_found = True
            course_name = course["name"]
            break

    if not course_found:
        print("Course not found.")
        return

    print("\n--- Marks for", course_name, "---")

    for student in students:

        student_id = student["id"]

        if course_id in marks[student_id]:

            mark = marks[student_id][course_id]

            print(
                student["id"],
                "-",
                student["name"],
                ":",
                mark
            )

        else:

            print(
                student["id"],
                "-",
                student["name"],
                ": No mark"
            )


# ==========================================
# CALCULATE GPA
# ==========================================

def calculate_gpa(student_id):

    mark_list = []
    credit_list = []

    for course in courses:

        course_id = course["id"]

        if course_id in marks[student_id]:

            mark = marks[student_id][course_id]
            credit = course["credit"]

            mark_list.append(mark)
            credit_list.append(credit)

    if len(mark_list) == 0:
        return 0

    # Convert lists to numpy arrays
    marks_array = np.array(mark_list)
    credits_array = np.array(credit_list)

    # Weighted average
    gpa = np.average(
        marks_array,
        weights=credits_array
    )

    return gpa


# ==========================================
# SHOW ALL GPA
# ==========================================

def show_gpa():

    print("\n--- Student GPA ---")

    for student in students:

        gpa = calculate_gpa(student["id"])

        print(
            student["id"],
            "-",
            student["name"],
            ": GPA =",
            round(gpa, 2)
        )


# ==========================================
# SORT STUDENTS BY GPA
# ==========================================

def sort_students_by_gpa():

    students.sort(
        key=lambda student: calculate_gpa(student["id"]),
        reverse=True
    )

    print("\n--- Students sorted by GPA ---")

    for student in students:

        gpa = calculate_gpa(student["id"])

        print(
            student["id"],
            "-",
            student["name"],
            ": GPA =",
            round(gpa, 2)
        )


# ==========================================
# MAIN MENU
# ==========================================

def main():

    while True:

        print("\n")
        print("====================================")
        print("      STUDENT MARK MANAGEMENT")
        print("====================================")
        print("1. Input students")
        print("2. Input courses")
        print("3. Input marks")
        print("4. List students")
        print("5. List courses")
        print("6. Show student marks")
        print("7. Calculate GPA")
        print("8. Sort students by GPA")
        print("0. Exit")
        print("====================================")

        choice = input("Enter your choice: ")

        if choice == "1":
            input_number_of_students()

        elif choice == "2":
            input_number_of_courses()

        elif choice == "3":
            input_marks()

        elif choice == "4":
            list_students()

        elif choice == "5":
            list_courses()

        elif choice == "6":
            show_student_marks()

        elif choice == "7":
            show_gpa()

        elif choice == "8":
            sort_students_by_gpa()

        elif choice == "0":
            print("Goodbye!")
            break

        else:
            print("Invalid choice!")


main()