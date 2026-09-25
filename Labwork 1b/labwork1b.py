students = []
courses = []
marks = {}


# 1. Input number of students
def input_number_of_students():
    n = int(input("Enter number of students: "))

    for i in range(n):
        input_student_information()


# 2. Input student information
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


# 3. Input number of courses
def input_number_of_courses():
    n = int(input("Enter number of courses: "))

    for i in range(n):
        input_course_information()


# 4. Input course information
def input_course_information():
    course_id = input("Enter course ID: ")
    name = input("Enter course name: ")

    course = {
        "id": course_id,
        "name": name
    }

    courses.append(course)


# 5. Input marks for students in a selected course
def input_marks():
    if len(courses) == 0:
        print("There are no courses.")
        return

    print("\nCourses:")
    list_courses()

    course_id = input("Select course ID: ")

    # Check whether course exists
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
        print("\nStudent:", student["name"])

        mark = float(input("Enter mark: "))

        marks[student["id"]][course_id] = mark


# 6. List courses
def list_courses():
    print("\n--- Course List ---")

    for course in courses:
        print("ID:", course["id"], "| Name:", course["name"])


# 7. List students
def list_students():
    print("\n--- Student List ---")

    for student in students:
        print(
            "ID:", student["id"],
            "| Name:", student["name"],
            "| DoB:", student["dob"]
        )


# 8. Show student marks for a given course
def show_student_marks():
    if len(courses) == 0:
        print("There are no courses.")
        return

    list_courses()

    course_id = input("Enter course ID: ")

    # Find course
    course_name = ""

    for course in courses:
        if course["id"] == course_id:
            course_name = course["name"]
            break

    if course_name == "":
        print("Course not found.")
        return

    print("\n--- Marks for", course_name, "---")

    for student in students:
        student_id = student["id"]

        if course_id in marks[student_id]:
            mark = marks[student_id][course_id]
            print(student["id"], "-", student["name"], ":", mark)
        else:
            print(student["id"], "-", student["name"], ": No mark")


# Main program
def main():
    while True:

        print("\n==============================")
        print(" STUDENT MARK MANAGEMENT")
        print("==============================")
        print("1. Input students")
        print("2. Input courses")
        print("3. Input marks")
        print("4. List students")
        print("5. List courses")
        print("6. Show student marks")
        print("0. Exit")

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

        elif choice == "0":
            print("Goodbye!")
            break

        else:
            print("Invalid choice.")


main()