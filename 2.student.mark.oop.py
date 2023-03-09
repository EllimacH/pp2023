import os
import re

students = []
courses = []
marks = []

# Function to input student information


class student:
    def __init__(self, student_name: str, student_id: str, student_DOB=str) -> None:
        self.student_name = student_name
        self.student_id = student_id
        self.student_DOB = student_DOB

    def get_student_name(self) -> str:
        return self.student_name

    def get_student_id(self) -> str:
        return self.student_id

    def get_student_DOB(self) -> str:
        return self.student_DOB


class course:

    def __init__(self, course_name: str, course_id: str) -> None:
        self.course_name = course_name
        self.course_id = course_id

    def get_course_name(self) -> str:
        return self.course_name

    def get_course_id(self) -> str:
        return self.course_id


class mark:

    def __init__(self, mark: float) -> None:
        self.mark = mark

    def get_mark(self) -> float:
        return self.mark


def input_student() -> None:

    student_name = input("Enter student name: ")
    # check to see if student name is valid
    while True:
        # using regex to check if student name is valid
        if re.match(r"[a-zA-Z ]+", student_name):
            break
        else:
            student_name = input(
                "Student name is not valid, please try again: ")

    student_id = input("Enter student id: ").upper()
    #if student id is BIxx-xxx (x is digit)
    while True:
        if re.match(r"BI\d{2}-\d{3}", student_id):
            break
        else:
            student_id = input("Student id is not valid, please try again: ")

    student_DOB = input("Enter student DoB: ")
    # if DoB is xx-xx-xxxx or xx/xx/xxxx
    while True:
        if re.match(r"\d{2}-\d{2}-\d{4}", student_DOB) or re.match(r"\d{2}/\d{2}/\d{4}", student_DOB):
            break
        else:
            student_DOB = input("DoB is not valid, please try again: ")

    studentt = student(student_name=student_name, student_id=student_id, student_DOB=student_DOB)
    students.append(studentt)


def input_course() -> None:
    course_name = input('Enter course name: ')
    course_id = input('Enter course id: ')
    courses.append(course(course_name, course_id))


def input_mark() -> None:
    student_id_input = input("Enter student id you want to input mark: ")
    course_id_input = input("Enter course id you want to input mark: ")
    mark_input = input("Enter mark: ")
    selected_student = None
    selected_course = None

    for student in students:
        if student.student_id == student_id_input:
            selected_student = student
            break

    for course in courses:
        if course.course_id == course_id_input:
            selected_course = course
            break
    
    if selected_student is not None and selected_course is not None:
        mark = mark(mark_input)
        marks.append(mark)  
        
    # for course in courses:
    #     if course.id == course_id_input:
    #         course_name = course.name

    # for student in students:
    #     if student.student_id == student_id_input:
    #         student["course"].append(
    #             {"course_name": course_name, "mark": mark_input})
    #         break


def print_student() -> None:
    for student in students:
                    print("="*20)
                    print("Student name: " + student["student_name"])
                    print("Student id: " + student["student_id"])
                    print("Date of birth: " + student["Date of birth"])
                    for course in student["course"]:
                        # print("Course: " + course["course_name"] + ": " + course["mark"])
                        print(
                            f"Course: {course['course_name']}: {course['mark']}")


def print_course() -> None:
    for course in courses:
        print(course)

def main():

    while True:

        print("\033c")  # clear screen
        # print out all the options
        print("1. Input student")
        print("2. Input course")
        print("3. Input mark")
        print("4. Print student")
        print("5. Print courses")
        print("6. Exit")

        choice = input("Enter your option: ")
        while True:
            try:
                choice = int(choice)
                if choice in range(1, 7):
                    break
                else:
                    raise ValueError
            except ValueError:
                choice = input("Input not valid , please try again: ")

        match choice:  # match the choice with the function
            case 1:
                input_student()
            case 2:
                input_course()
            case 3:
                input_mark()
            case 4:
                print_student()
            case 5:
                print_course()
            case 6:
                break

        input("Enter to continue...")


if __name__ == "__main__":
    main()


# courses = []
# input_course(courses)
# print(courses)
# students = []
# input_student(students)
# print(students)
