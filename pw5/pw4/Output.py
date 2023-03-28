from domains.classroom import Classroom

def output():
    while True:  # ----- Check if choice is valid -----
                try:
                    choice = int(choice)
                    if choice in range(1, 7):
                        break
                    raise ValueError
                except ValueError:
                    choice = input("Input not valid , please try again: ")

                match choice:
                  case 1:
                    classroom_info.input_student()
                  case 2:
                    courses_info.input_course()
                  case 3:
                    classroom_info.input_mark(courses_info.get_course_list())
                  case 4:
                    classroom_info.print_students_infos(courses_info.get_course_list())
                  case 5:
                    print("="*20)
                    course_list = courses_info.get_course_list()
                    for course in course_list:
                        print(f"{course['course_name']} ({course['course_id']})")

                    print("="*20)
                  case 6:
                    calculate_GPA(student_marks, course_list)
                  case 7:
                    break

                input("Enter to continue...")