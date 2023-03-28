import zipfile
import os

extension = ".dat"
def compress():
    with zipfile.ZipFile('student.zip', 'w', zipfile.ZIP_DEFLATED) as zip:
        zip.write('students.txt')
        zip.write('courses.txt')
        zip.write('marks.txt')
    print("compressed file successfully")

def extract():
    with zipfile.ZipFile('student.zip', 'r') as zip:
        zip.extractall()
    print("Extracted file successfully")