from datetime import datetime, timedelta


class Classroom:
    def __init__(self, abbreviation: str, level: int, description: str, days_of_week: str,
                 start_time: datetime, end_time: datetime, professor: str, students: list):
        self.identifier = f"{abbreviation.upper()}{str(level)}"
        self.abbreviation = abbreviation.upper()
        self.level = level
        self.description = description
        self.days_of_week = days_of_week
        self.start_time = start_time
        self.end_time = end_time
        self.professor = professor
        self.students = students
        self.shh_key = self.new_id()

    @classmethod
    def new_id(self):
        self.newid += 1
        return self.newid



class Student():

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

        if self.infection_date == None:
            self.status = "healthy"
        elif timedelta(days=14) > datetime.now() - self.infection_date:
            self.status = "quarantined"
        elif timedelta(days=14) < datetime.now() - self.infection_date:
            self.status = "vaccinated"

    @classmethod
    def new_id(self):
        self.newid += 1
        return self.newid
