import re


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

        # -------- Input mark ---------
        mark_input = input("Enter mark: ")
        while True:
            try:
                mark_input = float(mark_input)
                if mark_input in range(0, 21):
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

                for marks_of_student in student["marks"]:
                    if marks_of_student["course_id"] == course_id_input:
                        to_exit = input("Student has mark in this course, do you want to update mark? (y/n): ")
                        if to_exit == "y":
                            marks_of_student["mark"] = mark_input
                        else:
                            break  # don't update mark, break the if/else of of asking the user whether to update mark or not
                        break  # break the for loop, essentially break the else statement below
                else:
                    student["marks"].append(
                        {
                            "course_id": course_id_input,
                            "mark": mark_input
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

                print(f"Course: {course_name} ({mark['course_id']}): {mark['mark']}")

            print("="*20)


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
        print("6. Exit")

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
                break

        input("Enter to continue...")


if __name__ == "__main__":
    main()
