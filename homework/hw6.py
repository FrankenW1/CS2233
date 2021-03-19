import datetime

class Classroom:
    def __init__(self, abbreviation: str, level: int, description: str = None, day_of_week: str = None,
                 start_time: datetime = None, end_time: datetime = None, professor: str = None, students: list = None):
        self.abbreviation = abbreviation
        self.level = level
        self.description = description
        self.days_of_week = day_of_week
        self.start_time = start_time
        self.end_time = end_time
        self.professor = professor
        self.students = students


class Student:

    newid = 0

    def __init__(self,first_name: str, last_name: str, email: str,
                 phone: str = None, infection_date: datetime = None):

        self.student_id = self.new_id()
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone = phone
        self.infection_date = infection_date
        self.status = None
        if self.infection_date != None:
            self.status = "infected"
        elif self.infection_date == None:
            self.status = "healthy"

    @classmethod
    def new_id(self):
        self.newid += 1
        return self.newid


"""stu1 = student("c", "h", "email@jbu.edu", 4789995563)
stu2 = student("c", "h", "email@jbu.edu", 4789995563)
stu3 = student("c", "h", "email@jbu.edu", 4789995563)
stu4 = student("c", "h", "email@jbu.edu", 4789995563)
students.append(stu1)
students.append(stu2)
students.append(stu3)
students.append(stu4)
print(stu1.student_id)
print(stu2.student_id)
print(stu3.student_id)
print(stu4.student_id)"""


#students[0].phone = 1
#print(students[0])
