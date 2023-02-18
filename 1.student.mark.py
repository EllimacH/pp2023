# function to input student information
student_list = []
course_list = []


def input_student():
    global number
    number = int(input("Enter the number of students: "))
    for i in range(number):
        id = str(input("Enter the id of the student: "))
        name = input("Enter the name of the student: ")
        DoB = str(input("Enter the date of birth of the student: "))
        student = {"Name: ": name, "ID: ": id, "DoB: ": DoB}
        student_list.append(student)
    return student_list


def input_course():
    numberCourse = int(input("Enter the number of courses: "))
    for i in range(numberCourse):
        nameCourse = input("Enter the name of the course: ")
        course = {"Name: ": nameCourse}
        corse_id = str(input("Enter the id of the course: "))
        course_list.append(course)
    return course_list


def input_mark(student_list: list, course_list: list):
    Mark = float(input("Enter the mark of the student: "))
    while True:
        try:
            if Mark < 0 or Mark > 20:
                raise ValueError
            break
        except ValueError:
            Mark = float(input("Invalid mark, please try again: "))

    for course in course_list:
        print(course)
    select_course = input("Select the course: ")

    for i in range(number):
        for i in range(number):
            student_list[i].append(int(input("Grade for student " + str(i+1))))


input_student()
input_course()
input_mark(student_list, course_list)
