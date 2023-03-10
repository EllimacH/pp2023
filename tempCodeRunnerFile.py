while True:
        # using regex to check if student name is valid
        if re.match(r"[a-zA-Z ]+", student_name):
            break
        else:
            student_name = input(
                "Student name is not valid, please try again : ")