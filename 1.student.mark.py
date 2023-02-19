import os
import re

def input_student(students: list) -> None:
    temp = {}
    student_name = input("Enter student name: ")
    student_id = input("Enter student id: ").upper()

    while True:
        # if student id is BIxx-xxx (x is digit)
        if re.match(r"BI\d{2}-\d{3}", student_id):
            break
        else:
            student_id = input("Student id is not valid, please try again: ")
        
    DoB = input("Enter student DoB: ")
    # if DoB is xx-xx-xxxx or xx/xx/xxxx
    while True:
        if re.match(r"\d{2}-\d{2}-\d{4}", DoB) or re.match(r"\d{2}/\d{2}/\d{4}", DoB):
            break
        else:
            DoB = input("DoB is not valid, please try again: ")

    temp["student_name"] = student_name
    temp["student_id"] = student_id
    temp["Date of birth"] = DoB
    temp["course"] = []
    students.append(temp)

def input_course(courses: list) -> None:
    temp = {}
    course_name = input('Enter course name: ')
    course_id = input('Enter course id: ')
    temp["course_name"] = course_name
    temp["course_id"] = course_id
    courses.append(temp)

def input_mark(students: list, courses: list) -> None:
    student_id_input = input("Enter student id you want to input mark: ")
    course_id_input = input("Enter course id to input mark: ")
    mark = input("Enter mark: ")
    course_name_searced = ""

    for course in courses:
        if course["course_id"] == course_id_input:
            course_name = course["course_name"] 
            break
        
    
    for student in students:
        if student["student_id"] == student_id_input:
            student["course"].append({"course_name": course_name, "mark": mark})
            break
    
def main ():
    students = []
    courses = []


    while True:

        print("\033c")

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
                if choice in range (1,7):
                    break
                else:
                    raise ValueError
            except ValueError:
                choice = input("Input not valid , please try again: ")

        match choice:
            case 1: 
                input_student(students)
            case 2:
                input_course(courses)
            case 3:
                input_mark(students,courses)
            case 4:
                for student in students:
                    print("="*20)
                    print("Student name: " + student["student_name"])
                    print("Student id: " + student["student_id"])
                    print("Date of birth: " + student["Date of birth"])
                    for course in student["course"]:
                        # print("Course: " + course["course_name"] + ": " + course["mark"])
                        print(f"Course: {course['course_name']}: {course['mark']}")
            case 5:
                for course in courses:
                    print(course)
            case 6:
                break

        input("Enter to continue...")

if __name__ == "__main__":
    main()
