import math

import numpy as np


class Classroom:

    def __init__(self) -> None:
        self.student_list = []

    def input_student(self) -> None:

        # -------- Input student name ---------
        student_name = input("Enter student name: ")
        # while True:
        #     if re.match(r"[a-zA-Z ]+", student_name):
        #         break
        #     else:
        #         student_name = input(
        #             "Student name is not valid, please try again : ")

        # -------- Input student id ---------
        student_id = input("Enter student id: ").upper()
        # while True:
        #     if re.match(r"BI\d{2}-\d{3}", student_id):
        #         break
        #     else:
        #         student_id = input(
        #             "Student id is not valid, please try again with format BIxx-yyy with x and y is number: ").upper()

        # -------- Input student DoB ---------
        student_DOB = input("Enter student DoB: ")
        # while True:
        #     if re.match(r"\d{2}-\d{2}-\d{4}", student_DOB) or re.match(r"\d{2}/\d{2}/\d{4}", student_DOB):
        #         break
        #     else:
        #         student_DOB = input("DoB is not valid, please try again with format dd-mm-yyyy or dd/mm/yyyy: ")

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

                # is_course_exist = False
                # for marks_of_student in student["marks"]:
                #     if marks_of_student["course_id"] == course_id_input:
                #         is_course_exist = True
                #         break

                # if is_course_exist:
                #     to_exit = input("Student has mark in this course, do you want to update mark? (y/n): ")
                #     if to_exit == "y":
                #         marks_of_student["mark"] = mark_input
                #     else:
                #         break

                # else:
                #     student["marks"].append(
                #         {
                #             "course_id": course_id_input,
                #             "mark": mark_input
                #         }
                #     )

                # for marks_of_student in student["marks"]:
                #     if marks_of_student["course_id"] == course_id_input:
                #         to_exit = input("Student has mark in this course, do you want to update mark? (y/n): ")
                #         if to_exit == "y":
                #             marks_of_student["mark"][type_of_mark_input] = mark_input
                #         else:
                #             break  # don't update mark, break the if/else of of asking the user whether to update mark or not
                #         break  # break the for loop, essentially break the else statement below
                # else:
                #     student["marks"].append(
                #         {
                #             "course_id": course_id_input,
                #             "mark": {
                #                 type_of_mark_input: mark_input
                #             }
                #         }
                #     )

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

    def calculate_GPA_for_all(self) -> None:
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