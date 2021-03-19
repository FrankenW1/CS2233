from fastapi import FastAPI
from typing import Optional
from typing import Optional
from datetime import datetime
from loguru import logger
from pydantic import BaseModel
from fastapi import FastAPI, APIRouter, HTTPException
from homework.hw6 import Student, Classroom

student_router = APIRouter(prefix="/students")
classroom_router = APIRouter(prefix="/classroom")

app = FastAPI()

students = []
classrooms = []


# student enpoints


@student_router.get("/create")
def students_create(first_name: str, last_name: str, email: str,
                    phone: str = None, infection_date: datetime = None):
    if students == []:
        stu = Student(first_name, last_name, email, phone, infection_date)
        students.append(stu)
        return "StudentID: " + str(students[students.index(stu)].student_id)
    else:

        for x in range(len(students)):
            if students[x].first_name == first_name and students[x].last_name == last_name and students[
                x].email == email:
                raise HTTPException(422,
                                    "Student already Exists: Students Cannot have the same Name, Last Name or Email")
            else:
                stu = Student(first_name, last_name, email, phone, infection_date)
                students.append(stu)
                return "StudentID: " + str(students[students.index(stu)].student_id)


@student_router.get("/read")
def students_read():
    # hello this doesnt exist dont look at it
    return students


@student_router.get("/update")
def students_update(student_id: int, first_name: str = None, last_name: str = None,
                    email: str = None, phone: str = None, infection_date: datetime = None):
    found = False

    for x in range(len(students)):
        if student_id == students[x].student_id:
            students[x].first_name = first_name if first_name != None else students[x].first_name
            students[x].last_name = last_name if last_name != None else students[x].last_name
            students[x].email = email if email != None else students[x].email
            students[x].phone = phone if phone != None else students[x].phone
            students[x].infection_date = infection_date if infection_date != None else students[x].infection_date
            found = True
            return students[x]

    if found == False:
        raise HTTPException(422, "Student not found: Please check the StudentID and try again")


@student_router.get("/delete")
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
@classroom_router.get("/create")
def class_create(abbreviation: float, level: int, description: str, day_of_week: str, professor: str, students: list,
                 start_time: datetime = None, end_time: datetime = None):
    if classrooms == []:
        clrm = Classroom(abbreviation, level, description, day_of_week, start_time, end_time,
                         professor, students)
        classrooms.append(clrm)
        return "Class Abbreviation:" + str(classrooms[classrooms.index(clrm)].abbreviation) + '-' + str(
            classrooms[classrooms.index(clrm)].level)
    for x in range(len(classrooms)):
        if classrooms[x].abbreviation == abbreviation and classrooms[x].level == level:
            raise HTTPException(422, "Classroom already Exists: Classrooms cannot have the same Abbreviation and level")
        else:
            clrm = Classroom(abbreviation, level, description, day_of_week, start_time,
                             end_time, professor, students)
            classrooms.append(clrm)
            return "Class Abbreviation:" + str(classrooms[classrooms.index(clrm)].abbreviation) + '-' + str(
                classrooms[classrooms.index(clrm)].level)


@classroom_router.get("/read")
def class_read():
    # Hey now why are you looking at this? P.S. The cake is a lie
    return classrooms


@classroom_router.get("/update")
def class_update(abbreviation: float, level: int, description: str, day_of_week: str, professor: str, students: list,
                 start_time: datetime = None, end_time: datetime = None):
    # found = False
    # for x in range(len(classrooms)):
    # if
    ...


@classroom_router.get("/students")
def class_students():
    ...


@classroom_router.get("/attendance")
def class_attendance():
    ...


@classroom_router.get("/enroll_student")
def class_enroll_student():
    ...


@classroom_router.get("/remove_student")
def class_remove_student():
    ...


@classroom_router.get("/delete")
def class_delete():
    ...


# general endpoints
@app.get("/reset")
def reset():
    students.clear()
    classrooms.clear()
    return "Success: Data has been wiped"


@app.get("/outbreak")
def outbreak():
    ...


app.include_router(student_router)
app.include_router(classroom_router)
