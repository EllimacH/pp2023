from domains.classroom import Classroom
from domains.course import Courses
from domains import compress
from domains import deletefile
def main():

    classroom_info = Classroom()
    courses_info = Courses()

    while True:
        print("\033c")
        print("1. Input student")
        print("2. Input course")
        print("3. Input mark")
        print("4. Print student")
        print("5. Print courses")
        print("6. GPA")
        print("7. Exit")
        print("8. Sample data")
        print("9. Extract previous data")
#print student into txt
        f = open("students.txt", "a")
        f.write(str(classroom_info.student_list))
        f.close()
#print course into txt
        f = open("courses.txt", "a")
        f.write(str(courses_info.course_list))
        f.close()
#print mark into txt
        f = open("marks.txt", "a")
        f.write(str(classroom_info.student_list))
        f.close()

        choice = input("Enter your option: ")
        while True:  # ----- Check if choice is valid -----
            try:
                choice = int(choice)
                if choice in range(1, 10):
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
                classroom_info.print_students_infos(
                    courses_info.get_course_list())
            case 5:
                print("="*20)
                course_list = courses_info.get_course_list()
                for course in course_list:
                    print(f"{course['course_name']} ({course['course_id']})")

                print("="*20)
            case 6:
                classroom_info.calculate_GPA_for_all()
            case 7:
                break
            case 8:
                # make some sample data
                classroom_info.student_list = [
                    {
                        "student_name": "Nguyen Van A",
                        "student_id": "B20DCCN001",
                        "student_DOB": "01/01/2000",
                        "marks": [
                            {
                                "course_name": "ICT",
                                "course_id": "ICT001",
                                "mark": {
                                    "attend": 10,
                                    "midterm": 10,
                                    "final": 10,
                                    "GPA": 10
                                }
                            },
                            {   "course_name": "DS",
                                "course_id": "DS001",
                                "mark": {
                                    "attend": 10,
                                    "midterm": 10,
                                    "final": 10,
                                    "GPA": 10
                                }
                            }
                        ]
                    },
                    {
                        "student_name": "Nguyen Van B",
                        "student_id": "B20DCCN002",
                        "student_DOB": "01/01/2000",
                        "marks": [
                            {
                                "course_id": "INT2208",
                                "mark": {
                                    "attend": 10,
                                    "midterm": 10,
                                    "final": 10,
                                    "GPA": 10
                                }
                            },
                            {
                                "course_id": "INT2209",
                                "mark": {
                                    "attend": 10,
                                    "midterm": 10,
                                    "final": 10,
                                    "GPA": 10
                                }
                            }
                        ]
                    }
                ]
            case 9: 
                compress.extract()
        input("Enter to continue...")


if __name__ == "__main__":
    main()

# compress file when exit the program
compress.compress()


# delete leftover text file
deletefile.delete()
