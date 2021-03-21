from fastapi import FastAPI
from typing import Optional
from datetime import datetime, timedelta
from fastapi import FastAPI, APIRouter, HTTPException
from homework.hw6 import Student, Classroom

student_router = APIRouter(prefix="/students")
classroom_router = APIRouter(prefix="/classroom")

app = FastAPI()

students = []
students_in_class = []
classrooms = []


# student enpoints


def convert_student_IDs(student_ids: list):
    for x in range(len(students)):
        for i in range(len(students)):
            if students[x].student_id == int(student_ids[i]):
                students_in_class.append(students[x])

    return students_in_class


@student_router.post("/create")
def students_create(first_name: str, last_name: str, email: str,
                    phone: str = None, infection_date: datetime = None):
    if students == []:
        stu = Student(first_name, last_name, email, phone, infection_date)
        students.append(stu)
        return "StudentID: " + str(students[students.index(stu)].student_id)

    else:

        for x in range(len(students)):
            if students[x].email == email:
                raise HTTPException(422, "Duplicate entry: Students cannot have the same email")
            else:
                stu = Student(first_name, last_name, email, phone, infection_date)
                students.append(stu)
                return "StudentID: " + str(students[students.index(stu)].student_id)


@student_router.post("/read")
def students_read():
    # hello this doesnt exist dont look at it
    return students


@student_router.post("/update")
def students_update(student_id: int, first_name: str = None, last_name: str = None,
                    email: str = None, phone: str = None, infection_date: datetime = None):
    found = False

    for x in range(len(students)):
        if student_id == students[x].student_id:
            if students[x].email != email:
                students[x].first_name = first_name if first_name != None else students[x].first_name
                students[x].last_name = last_name if last_name != None else students[x].last_name
                students[x].email = email if email != None else students[x].email
                students[x].phone = phone if phone != None else students[x].phone
                students[x].infection_date = infection_date if infection_date != None else students[x].infection_date
                found = True
                return students[x]
            else:
                raise HTTPException(422, "Duplicate Entry: Email already in use")

    if found == False:
        raise HTTPException(422, "Student not found: Please check the StudentID and try again")


@student_router.delete("/delete")
def students_delete(student_id: int):
    found = False

    for x in range(len(students)):
        if student_id == students[x].student_id:
            del students[x]
            found = True
            return f"Student with StudentID: {student_id} was deleted"

    if found == False:
        raise HTTPException(422, "Student not found: Please check the StudentID and try again")


# classroom endpoints
@classroom_router.post("/create")
def class_create(abbreviation: str, level: int, description: str, day_of_week: str,
                 start_time: datetime, end_time: datetime, professor: str, students: list):
    """The students must be entered using studentID in list form."""

    print(students)

    time_format = "%H:%M"
    start_time_formatted = start_time.strftime(time_format)
    end_time_formatted = end_time.strftime(time_format)

    if classrooms == []:
        clrm = Classroom(abbreviation, level, description, day_of_week, start_time_formatted, end_time_formatted,
                         professor, convert_student_IDs(students))
        classrooms.append(clrm)
        return "Class Abbreviation: " + clrm.identifier
    for x in range(len(classrooms)):
        if classrooms[x].abbreviation == abbreviation and classrooms[x].level == level:
            raise HTTPException(422, "Classroom already exists: Classrooms cannot have the same abbreviation and level")
        else:
            clrm = Classroom(abbreviation, level, description, day_of_week, start_time,
                             end_time, professor, convert_student_IDs(students))
            classrooms.append(clrm)
            return "Class Abbreviation: " + clrm.identifier


@classroom_router.post("/read")
def class_read():
    return classrooms


@classroom_router.post("/update")
def class_update(identifier: str, new_abbreviation: str = None, new_level: int = None,
                 days_of_week: str = None, start_time: datetime = None, end_time: datetime = None):
    found = False

    for x in range(len(classrooms)):
        if new_level != classrooms[x].level and new_abbreviation != classrooms[x].abbreviation:
            if identifier == classrooms[x].identifier:

                classrooms[x].abbreviation = new_abbreviation.upper() if new_abbreviation != None else classrooms[
                    x].abbreviation
                classrooms[x].level = new_level if new_level != None else classrooms[x].level
                classrooms[x].days_of_week = days_of_week if days_of_week != None else classrooms[x].days_of_week
                classrooms[x].identifier = f"{classrooms[x].abbreviation.upper()}{classrooms[x].level}"

                if end_time != None and start_time != None:
                    time_format = "%H:%M"
                    start_time_formatted = start_time.strftime(time_format)
                    end_time_formatted = end_time.strftime(time_format)

                    classrooms[x].start_time = start_time_formatted
                    classrooms[x].end_time = end_time_formatted
                else:
                    classrooms[x].end_time = classrooms[x].end_time
                    classrooms[x].start_time = classrooms[x].start_time

                return classrooms

        else:
            raise HTTPException(422, "Duplicate entries: Classrooms cannot have the same abbreviation and level")

    if found == False:
        raise HTTPException(422, "Class not found: Please check the class abbreviation and level")


@classroom_router.get("/students")
def class_students(identifier: str, name: str = None):
    names_that_begin = []
    found = False
    for x in range(len(classrooms)):
        if identifier == classrooms[x].identifier:
            found = True
            count = len(classrooms[x].students)
            row = classrooms[x].students
            if name != None:
                for i in row:
                    if (i.first_name.lower()).startswith(name.lower()) == True:
                        names_that_begin.append(i)
    if found == True:
        if name != None:
            return {count: names_that_begin}
        else:
            return {count: row}
    else:
        raise HTTPException(422, "Class not found: Please check the class abbreviation and level")


@classroom_router.get("/attendance")
def class_attendance(date: datetime, identifier: str):
    ret = {}
    temp = []
    for i in range(len(classrooms)):
        if classrooms[i].identifier == identifier:
            for x in range(len(classrooms[i].students)):
                datetimeFormat = '%Y-%m-%d %H:%M:%S.%f'
                diff = datetime.datetime.strptime(date, datetimeFormat) \
                       - datetime.datetime.strptime(students[x].infection_date, datetimeFormat)
                if diff.days <= 3:
                    ret["sick"] = classrooms[x].student_id
                elif diff.days > 3 and diff.days <= 14:
                    ret["online"] = classrooms[x].student_id
                else:
                    ret["present"] = classrooms[x].student_id
    return ret


@classroom_router.post("/enroll_student")
def class_enroll_student(class_id: str, student_id: int):
    for x in range(len(classrooms)):
        if classrooms[x].identifier == class_id:
            classrooms[x].students.append(student_id)
            # return classrooms[x].students
    ...


@classroom_router.post("/remove_student")
def class_remove_student(class_id: str, student_id: int):
    for x in range(len(classrooms)):
        if classrooms[x].identifier == class_id:
            classrooms[x].students.remove(student_id)
            # return classrooms[x].students
    ...


@classroom_router.delete("/delete")
def class_delete(class_id: str):
    for x in range(len(classrooms)):
        if classrooms[x].identifier == class_id:
            classrooms[x].clear()

    ...


# general endpoints
@app.delete("/reset")
def reset():
    students.clear()
    classrooms.clear()
    return "Success: Data has been wiped"


@app.post("/outbreak")
def outbreak():
    ...


app.include_router(student_router)
app.include_router(classroom_router)
