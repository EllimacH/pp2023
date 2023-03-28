import os
#delete leftover text file
def delete():
    os.remove("students.txt")
    os.remove("courses.txt")
    os.remove("marks.txt")
print("Delete file successfully")

