# student_list = [
#     {
#         "student_id": "123",
#         "student_name": "hmq",
#         "course": [
#             {"course_name": "as", "mark": "14"}
#         ],
#     },
#     {
#         "student_id": "124",
#         "student_name": "ntk",
#         "course": [
#             {"course_name": "ass", "mark": "17"}
#         ],
#     },
#     {
#         "student_id": "125",
#         "student_name": "dqn",
#         "course": [
#             {
#                 "course_name": "qma",
#                 "mark": "10"
#             }],
#     },
# ]
# courses_list = [
#     {
#         "course_name": "as",
#         "course_id": "13"
#     }
#     {
#         "course_name": "ass",
#         "course_id": "19"
#     }
#     {
#         "course_name": "qma",
#         "course_id": "11"
#     }
# ]
def input_student(students: list) -> None:
    temp = {}
    student_name = input("Enter student name: ")
    student_id = input("Enter student id: ")
    #add info to temp
    temp["student_name"] = student_name
    temp["student_id"] = student_id
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
    student_id = input("Enter student id: ")
    course_id = input("Enter course id: ")
    mark = input("Enter mark: ")

    course_name = ""
    for course in courses:
        if course["course_id"] == course_id:
            course_name = 

def main ():
    students = []
    courses = []
   

if __name__ == "__main__":
    main()
