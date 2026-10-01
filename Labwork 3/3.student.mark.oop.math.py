import curses
import math
import numpy as np


students = []
courses = []
marks = {}


# ==========================================
# STUDENT
# ==========================================

def input_students(stdscr):
    stdscr.clear()

    n = int(input_curses(stdscr, "Enter number of students: "))

    for i in range(n):
        stdscr.clear()

        student_id = input_curses(stdscr, "Enter student ID: ")
        name = input_curses(stdscr, "Enter student name: ")
        dob = input_curses(stdscr, "Enter date of birth: ")

        student = {
            "id": student_id,
            "name": name,
            "dob": dob
        }

        students.append(student)
        marks[student_id] = {}

    message(stdscr, "Students added successfully!")


# ==========================================
# COURSE
# ==========================================

def input_courses(stdscr):
    stdscr.clear()

    n = int(input_curses(stdscr, "Enter number of courses: "))

    for i in range(n):
        stdscr.clear()

        course_id = input_curses(stdscr, "Enter course ID: ")
        name = input_curses(stdscr, "Enter course name: ")
        credit = int(input_curses(stdscr, "Enter number of credits: "))

        course = {
            "id": course_id,
            "name": name,
            "credit": credit
        }

        courses.append(course)

    message(stdscr, "Courses added successfully!")


# ==========================================
# MARKS
# ==========================================

def input_marks(stdscr):

    if len(courses) == 0:
        message(stdscr, "There are no courses!")
        return

    stdscr.clear()

    stdscr.addstr(0, 0, "COURSE LIST", curses.A_BOLD)

    for i, course in enumerate(courses):
        stdscr.addstr(
            i + 2,
            0,
            f"{course['id']} - {course['name']} "
            f"({course['credit']} credits)"
        )

    course_id = input_curses(
        stdscr,
        "\nEnter course ID: "
    )

    course_found = False

    for course in courses:
        if course["id"] == course_id:
            course_found = True
            break

    if not course_found:
        message(stdscr, "Course not found!")
        return

    for student in students:

        mark = float(
            input_curses(
                stdscr,
                f"Enter mark for {student['name']}: "
            )
        )

        # Round DOWN to 1 decimal place
        mark = math.floor(mark * 10) / 10

        marks[student["id"]][course_id] = mark

    message(stdscr, "Marks saved successfully!")


# ==========================================
# LIST STUDENTS
# ==========================================

def list_students(stdscr):

    stdscr.clear()

    stdscr.addstr(
        0,
        0,
        "STUDENT LIST",
        curses.A_BOLD
    )

    row = 2

    for student in students:

        stdscr.addstr(
            row,
            0,
            f"ID: {student['id']} | "
            f"Name: {student['name']} | "
            f"DoB: {student['dob']}"
        )

        row += 1

    if len(students) == 0:
        stdscr.addstr(2, 0, "No students.")

    wait_key(stdscr)


# ==========================================
# LIST COURSES
# ==========================================

def list_courses(stdscr):

    stdscr.clear()

    stdscr.addstr(
        0,
        0,
        "COURSE LIST",
        curses.A_BOLD
    )

    row = 2

    for course in courses:

        stdscr.addstr(
            row,
            0,
            f"ID: {course['id']} | "
            f"Name: {course['name']} | "
            f"Credits: {course['credit']}"
        )

        row += 1

    if len(courses) == 0:
        stdscr.addstr(2, 0, "No courses.")

    wait_key(stdscr)


# ==========================================
# SHOW MARKS
# ==========================================

def show_marks(stdscr):

    if len(courses) == 0:
        message(stdscr, "There are no courses!")
        return

    stdscr.clear()

    stdscr.addstr(
        0,
        0,
        "COURSE LIST",
        curses.A_BOLD
    )

    for i, course in enumerate(courses):
        stdscr.addstr(
            i + 2,
            0,
            f"{course['id']} - {course['name']}"
        )

    course_id = input_curses(
        stdscr,
        "\nEnter course ID: "
    )

    course_name = ""

    for course in courses:
        if course["id"] == course_id:
            course_name = course["name"]
            break

    if course_name == "":
        message(stdscr, "Course not found!")
        return

    stdscr.clear()

    stdscr.addstr(
        0,
        0,
        f"MARKS - {course_name}",
        curses.A_BOLD
    )

    row = 2

    for student in students:

        student_id = student["id"]

        if course_id in marks[student_id]:
            mark = marks[student_id][course_id]

            stdscr.addstr(
                row,
                0,
                f"{student['id']} - "
                f"{student['name']} : {mark}"
            )
        else:
            stdscr.addstr(
                row,
                0,
                f"{student['id']} - "
                f"{student['name']} : No mark"
            )

        row += 1

    wait_key(stdscr)


# ==========================================
# GPA
# ==========================================

def calculate_gpa(student_id):

    mark_list = []
    credit_list = []

    for course in courses:

        course_id = course["id"]

        if course_id in marks[student_id]:

            mark_list.append(
                marks[student_id][course_id]
            )

            credit_list.append(
                course["credit"]
            )

    if len(mark_list) == 0:
        return 0

    marks_array = np.array(mark_list)
    credits_array = np.array(credit_list)

    gpa = np.average(
        marks_array,
        weights=credits_array
    )

    return gpa


# ==========================================
# SHOW GPA
# ==========================================

def show_gpa(stdscr):

    stdscr.clear()

    stdscr.addstr(
        0,
        0,
        "STUDENT GPA",
        curses.A_BOLD
    )

    row = 2

    for student in students:

        gpa = calculate_gpa(student["id"])

        stdscr.addstr(
            row,
            0,
            f"{student['id']} - "
            f"{student['name']} : "
            f"GPA = {gpa:.2f}"
        )

        row += 1

    if len(students) == 0:
        stdscr.addstr(2, 0, "No students.")

    wait_key(stdscr)


# ==========================================
# SORT GPA
# ==========================================

def sort_students_by_gpa(stdscr):

    students.sort(
        key=lambda student:
        calculate_gpa(student["id"]),
        reverse=True
    )

    stdscr.clear()

    stdscr.addstr(
        0,
        0,
        "STUDENTS SORTED BY GPA",
        curses.A_BOLD
    )

    row = 2

    for student in students:

        gpa = calculate_gpa(student["id"])

        stdscr.addstr(
            row,
            0,
            f"{student['id']} - "
            f"{student['name']} : "
            f"GPA = {gpa:.2f}"
        )

        row += 1

    wait_key(stdscr)


# ==========================================
# CURSES INPUT
# ==========================================

def input_curses(stdscr, text):

    stdscr.addstr(
        curses.LINES - 2,
        0,
        text
    )

    stdscr.refresh()

    curses.echo()

    value = stdscr.getstr(
        curses.LINES - 1,
        0
    ).decode("utf-8")

    curses.noecho()

    return value


# ==========================================
# MESSAGE
# ==========================================

def message(stdscr, text):

    stdscr.clear()

    stdscr.addstr(
        2,
        2,
        text,
        curses.A_BOLD
    )

    wait_key(stdscr)


# ==========================================
# WAIT
# ==========================================

def wait_key(stdscr):

    stdscr.addstr(
        curses.LINES - 2,
        2,
        "Press any key to continue..."
    )

    stdscr.refresh()
    stdscr.getch()


# ==========================================
# MAIN MENU
# ==========================================

def main(stdscr):

    curses.curs_set(0)

    menu = [
        "Input students",
        "Input courses",
        "Input marks",
        "List students",
        "List courses",
        "Show student marks",
        "Show GPA",
        "Sort students by GPA",
        "Exit"
    ]

    current = 0

    while True:

        stdscr.clear()

        # Title
        stdscr.addstr(
            1,
            5,
            "STUDENT MARK MANAGEMENT",
            curses.A_BOLD
        )

        stdscr.addstr(
            2,
            5,
            "Practical Work 3",
            curses.A_BOLD
        )

        # Menu
        for i, item in enumerate(menu):

            if i == current:

                stdscr.addstr(
                    5 + i,
                    5,
                    "> " + item,
                    curses.A_REVERSE
                )

            else:

                stdscr.addstr(
                    5 + i,
                    5,
                    "  " + item
                )

        stdscr.addstr(
            curses.LINES - 2,
            5,
            "Use UP/DOWN to move, ENTER to select"
        )

        key = stdscr.getch()

        # Move up
        if key == curses.KEY_UP:

            current -= 1

            if current < 0:
                current = len(menu) - 1

        # Move down
        elif key == curses.KEY_DOWN:

            current += 1

            if current >= len(menu):
                current = 0

        # Enter
        elif key == curses.KEY_ENTER or key in [10, 13]:

            if current == 0:
                input_students(stdscr)

            elif current == 1:
                input_courses(stdscr)

            elif current == 2:
                input_marks(stdscr)

            elif current == 3:
                list_students(stdscr)

            elif current == 4:
                list_courses(stdscr)

            elif current == 5:
                show_marks(stdscr)

            elif current == 6:
                show_gpa(stdscr)

            elif current == 7:
                sort_students_by_gpa(stdscr)

            elif current == 8:
                break


# ==========================================
# START PROGRAM
# ==========================================

curses.wrapper(main)