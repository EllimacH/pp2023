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