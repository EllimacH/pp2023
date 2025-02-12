import re
import math
import numpy as np


class Classroom:

    def __init__(self) -> None:
        self.student_list = []

    def input_student(self) -> None:

        # -------- Input student name ---------
        student_name = input("Enter student name: ")
        while True:
            if re.match(r"[a-zA-Z ]+", student_name):
                break
            else:
                student_name = input(
                    "Student name is not valid, please try again : ")

        # -------- Input student id ---------
        student_id = input("Enter student id: ").upper()
        #check if student id is follow BIxx-yyy format
        while True:
            if re.match(r"BI\d{2}-\d{3}", student_id):
                break
            else:
                student_id = input(
                    "Student id is not valid, please try again with format BIxx-yyy with x and y is number: ").upper()

        # -------- Input student DoB ---------
        student_DOB = input("Enter student DoB: ")
        while True:
            if re.match(r"\d{2}-\d{2}-\d{4}", student_DOB) or re.match(r"\d{2}/\d{2}/\d{4}", student_DOB):
                break
            else:
                student_DOB = input("DoB is not valid, please try again with format dd-mm-yyyy or dd/mm/yyyy: ")

        self.student_list.append(
            {
                "student_name": student_name,
                "student_id": student_id,
                "student_DOB": student_DOB,
                "marks": []
            }
        )

    def input_mark(self, course_list: list) -> None:

        # -------- Input student id ---------
        student_id_input = input("Enter student id you want to input mark: ").upper()
        while True:
            for student in self.student_list:
                if student["student_id"] == student_id_input:
                    break
            else:
                student_id_input = input("Student id not found, please try again: ").upper()
                continue
            break

        # -------- Input course id ---------
        course_id_input = input("Enter course id you want to input mark: ")
        while True:
            for course in course_list:
                if course["course_id"] == course_id_input:
                    break
            else:
                course_id_input = input("Course id not found, please try again: ")
                continue
            break

        # -------- Input type of mark ---------
        type_of_mark_input = input("Enter type of mark (attend/midterm/final): ")
        while True:
            if type_of_mark_input in ["attend", "midterm", "final"]:
                break
            else:
                type_of_mark_input = input("Type of mark is not valid, please try again: ")

        # -------- Input mark ---------
        mark_input = input("Enter mark: ")
        while True:
            try:
                # use math floor to round down to only one
                mark_input = math.floor(float(mark_input)*10)/10
                if mark_input > 0 and mark_input <= 20:
                    break
                raise ValueError
            except ValueError:
                mark_input = input("Mark is not valid, please try again: ")

        # -------- Add mark to student ---------
        for student in self.student_list:
            if student["student_id"] == student_id_input:
                # 2 cases: if student has mark in course, update mark, else add new mark

                for _, course in enumerate(student["marks"]):
                    if course["course_id"] == course_id_input:
                        course["mark"][type_of_mark_input] = mark_input
                else:
                    student["marks"].append(
                        {
                            "course_id": course_id_input,
                            "mark": {
                                type_of_mark_input: mark_input
                            }
                        }
                    )

    def print_students_infos(self, course_list: list) -> None:
        for student in self.student_list:
            print("="*20)

            print(f"- {student['student_name']} - {student['student_id']} - {student['student_DOB']}")
            print("Marks:")
            for mark in student["marks"]:

                # -------- Get course name ---------
                # We only have course id and mark, given the course_list, we can get the course name by looping through the course_list
                course_name = ""
                for course in course_list:
                    if course["course_id"] == mark["course_id"]:
                        course_name = course["course_name"]

                attend_mark = mark["mark"]["attend"] if "attend" in mark["mark"] else "N/A"
                midterm_mark = mark["mark"]["midterm"] if "midterm" in mark["mark"] else "N/A"
                final_mark = mark["mark"]["final"] if "final" in mark["mark"] else "N/A"
                gpa_mark = mark["mark"]["GPA"] if "GPA" in mark["mark"] else "N/A"

                print(f"Course: {course_name} ({mark['course_id']}): {attend_mark} {midterm_mark} {final_mark} | GPA: {gpa_mark}")

            print("="*20)

    def calculate_GPA(self) -> None:
        for student in self.student_list:
            for course in student["marks"]:
                for item in ["attend", "midterm", "final"]:
                    if item not in course["mark"]:
                        break
                else:
                    attend_mark = course["mark"]["attend"]
                    midterm_mark = course["mark"]["midterm"]
                    final_mark = course["mark"]["final"]
                    mark_array = np.array([attend_mark, midterm_mark, final_mark])
                    mark_array = mark_array * np.array([0.1, 0.3, 0.6])
                    course["mark"]["GPA"] = mark_array.sum()

class Courses:

    def __init__(self) -> None:
        self.course_list = []

    def input_course(self) -> None:
        course_name_input = input("Enter course name: ")

        course_id_input = input("Enter course id: ")
        while True:
            for course in self.course_list:
                if course["course_id"] == course_id_input:
                    course_id_input = input("Course id is already exist, please try again: ")
                    break
            else:
                break

        self.course_list.append(
            {
                "course_name": course_name_input,
                "course_id": course_id_input
            }
        )

    def get_course_list(self) -> list:
        return self.course_list



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

        choice = input("Enter your option: ")
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
                classroom_info.calculate_GPA()
            case 7:
                break

        input("Enter to continue...")


if __name__ == "__main__":
    main()




