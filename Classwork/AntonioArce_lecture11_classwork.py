#Antonio Arce
#Emrehan Seferoglu

#Part 1
class Course:
    def __init__(self,section_id):
        self.section_id = section_id
        self.enrolled_students = []

    def enroll(self,name):
        self.enrolled_students.append(name)

    def is_enrolled(self, name):
        if name in self.enrolled_students:
            return True
        else:
            return False
        
#Section 2        
#from Section import Course

section = Course("Math111_101")

section.enroll("Joe Josephson")

section.enroll("Mary Smith")

print(section.is_enrolled("Mary Josephson"))

#exercise 2

class CollegeDictionary:
    '''Directory of Students in College'''

    def __init__(self,name):
        self.name = name
        self.students = {}
    def addStudent(self,studentname,emailaddress):
        self.students[studentname] = emailaddress
    def getemaillist(self):
        for student,email in self.students.items():
            print("{} <{}>".format(student,email))
        

'''from college_directory import CollegeDictionary'''

cd = CollegeDictionary('Hawthrone College')