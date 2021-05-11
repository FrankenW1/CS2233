from fastapi import FastAPI
from typing import Optional
import pickle
from datetime import datetime, timedelta
from fastapi import FastAPI, APIRouter, HTTPException
from homework.hw6 import Student, Classroom

student_router = APIRouter(prefix="/students")
classroom_router = APIRouter(prefix="/classroom")

app = FastAPI()

students = []
classrooms = []


#####################SKETYCHY CODE DO NOT TOUCH ############################
#student endpoints
def load_data_students():
    global students
    fileObj = open('students.json', 'rb')
    exampleObj = pickle.load(fileObj)
    fileObj.close()
    students = exampleObj
    #return exampleObj


def load_data_classrooms():
    global classrooms
    fileObj = open('classrooms.json', 'rb')
    exampleObj = pickle.load(fileObj)
    fileObj.close()
    classrooms = exampleObj
    #return exampleObj


def update_data_students(students: any):
    fileObj = open('students.json', 'wb')
    pickle.dump(students, fileObj)
    fileObj.close()


def update_data_classrooms(classrooms: any):
    fileObj = open('classrooms.json', 'wb')
    pickle.dump(classrooms, fileObj)
    fileObj.close()
################## END OF SKETYCHY CODE #####################


def nuke_student(student_id: int):
    load_data_students()
    load_data_classrooms()

    for i in range(len(classrooms)):
        for x in range(len(classrooms[i].students)):
            if classrooms[i].students[x].student_id == student_id:
                del classrooms[i].students[x]
                update_data_classrooms(classrooms)
                update_data_students(students)


def duplicate_students(list_of_students: any, student: any):
    for i in range(len(list_of_students)):
        if list_of_students[i].student_id == student.student_id:
            raise HTTPException(422, "student already in class")

    return False


def duplicate_classrooms(list_of_classrooms: any, classroom: any):
    for i in range(len(list_of_classrooms)):
        if list_of_classrooms[i].identifier == classroom.identifier:
            raise HTTPException(422, "classroom already exists")
    return None


def append_to_classroom(index: int, thing_to_append:any):
    l = classrooms[index].students
    if thing_to_append not in l:
        l.append(thing_to_append)
        classrooms[index].students = l
        update_data_classrooms(classrooms)
    else:
        raise HTTPException(422, "Student is already in classroom")


def convert_student_IDs(student_ids: list):
    for x in range(len(students)):
        for i in range(len(students)):
            if students[x].student_id == int(student_ids[i]):
                students_in_class.append(students[x])

    return students_in_class

def check_classroom(identifier: str):
    load_data_students()
    load_data_classrooms()
    for x in range(len(classrooms)):
        if identifier.upper() == classrooms[x].identifier:
            return x

    raise HTTPException(422, "Classroom not found: Classroom identifier does not match any existing classrooms")

def find_student(student_id: int):
    load_data_students()
    load_data_classrooms()
    for x in range(len(students)):
        if students[x].student_id == student_id:
            return students[x]

    raise HTTPException(422, "Student not found: StudentID does not match students created")


@student_router.post("/create")
def students_create(first_name: str, last_name: str, email: str,
                    phone: str = None, infection_date: datetime = None):
    load_data_students()
    if students == []:
        stu = Student(first_name, last_name, email, phone, infection_date)
        students.append(stu)
        return "StudentID: " + str(students[students.index(stu)].student_id)

    else:
        load_data_students()
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
                    email: str = None,phone: str = None, infection_date: datetime = None):
    load_data_students()
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
                update_data_students(students)
                return students[x]
            else:
                raise HTTPException(422, "Duplicate Entry: Email already in use")


    if found == False:
        raise HTTPException(422, "Student not found: Please check the StudentID and try again")

@student_router.delete("/delete")
def students_delete(student_id: int):
    found = False
    load_data_students()
    for x in range(len(students)):
        if student_id == students[x].student_id:
            nuke_student(student_id)
            del students[x]
            found = True
            update_data_students(students)
            return f"Student with StudentID: {student_id} was deleted"

    if found == False:
        raise HTTPException(422, "Student not found: Please check the StudentID and try again")

#classroom endpoints
@classroom_router.post("/create")
def class_create(abbreviation: str, level: int, description: str, day_of_week: str,
                 start_time: datetime, end_time: datetime, professor: str, students: list):

    """The students must be entered using studentID in list form."""

    time_format = "%H:%M"
    start_time_formatted = start_time.strftime(time_format)
    end_time_formatted = end_time.strftime(time_format)

    clrm = Classroom(abbreviation, level, description, day_of_week, start_time_formatted, end_time_formatted,
                     professor, convert_student_IDs(students))
    load_data_classrooms()
    load_data_students()

    if classrooms == []:

        classrooms.append(clrm)
        update_data_classrooms(classrooms)
        return "Class Abbreviation: " + clrm.identifier
    else:

        if duplicate_classrooms(classrooms, clrm) == False:
            classrooms.append(clrm)
            update_data_classrooms(classrooms)
            return "Class Abbreviation: " + clrm.identifier
        elif duplicate_classrooms(classrooms, clrm) == None:
            classrooms.append(clrm)
            update_data_classrooms(classrooms)
            return "Class Abbreviation: " + clrm.identifier


@classroom_router.post("/read")
def class_read():
    load_data_classrooms()
    return classrooms


@classroom_router.post("/update")
def class_update(identifier: str, new_abbreviation: str = None, new_level: int = None,
                 days_of_week: str = None, start_time: datetime = None, end_time: datetime = None ):

    found = False
    load_data_students()
    load_data_classrooms()
    for x in range(len(classrooms)):
        if new_level != classrooms[x].level and new_abbreviation != classrooms[x].abbreviation:
            if identifier.upper() == classrooms[x].identifier:

                classrooms[x].abbreviation = new_abbreviation.upper() if new_abbreviation != None else classrooms[x].abbreviation
                classrooms[x].level = new_level if new_level != None else classrooms[x].level
                classrooms[x].days_of_week = days_of_week if days_of_week != None else classrooms[x].days_of_week
                classrooms[x].identifier = f"{classrooms[x].abbreviation.upper()}{classrooms[x].level}"

                if end_time != None and start_time != None:
                    time_format = "%H:%M"
                    start_time_formatted = start_time.strftime(time_format)
                    end_time_formatted = end_time.strftime(time_format)

                    classrooms[x].start_time = start_time_formatted
                    classrooms[x].end_time = end_time_formatted
                    update_data_classrooms(classrooms)
                else:
                    classrooms[x].end_time = classrooms[x].end_time
                    classrooms[x].start_time = classrooms[x].start_time
                    update_data_classrooms(classrooms)

                update_data_classrooms(classrooms)
                return classrooms

        else:
            update_data_classrooms(classrooms)
            raise HTTPException(422, "Duplicate entries: Classrooms cannot have the same abbreviation and level")

    if found == False:
        update_data_classrooms(classrooms)
        raise HTTPException(422, "Class not found: Please check the class abbreviation and level")


@classroom_router.get("/students")
def class_students(identifier: str, name: str = None ):
    names_that_begin = []
    found = False
    load_data_classrooms()
    for x in range(len(classrooms)):
        if identifier.upper() == classrooms[x].identifier:
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
def class_attendance(identifier: str, date: datetime):

    load_data_students()
    load_data_classrooms()

    attendance = { "Present": [], "Online": [], "Sick": [] }

    present = 0
    present_l = [present]

    online = 0
    online_l = [online]

    sick = 0
    sick_l = [sick]

    x = check_classroom(identifier.upper())
    temp = classrooms[x].students

    for i in range(len(temp)):
        if temp[i].infection_date == None:
            present += 1
            present_l[0] = present
            present_l.append(temp[i])
        elif timedelta(days=3) >= date - temp[i].infection_date:
            sick += 1
            sick_l[0] = sick
            sick_l.append(temp[i])
        elif timedelta(days=14) >= date - temp[i].infection_date:
            online += 1
            online_l[0] = online
            online_l.append(temp[i])

    attendance.update({"Present": present_l})
    attendance.update({"Online": online_l})
    attendance.update({"Sick": sick_l})

    return attendance


@classroom_router.post("/enroll_student")
def class_enroll_student(identifier: str, student_id: int):
    load_data_students()
    load_data_classrooms()

    for x in range(len(classrooms)):

        if classrooms[x].identifier == identifier.upper():
            if duplicate_students(classrooms[x].students, find_student(student_id)) == False:
                append_to_classroom(x, find_student(student_id))
                #classrooms[x].students.append(find_student(student_id))
                update_data_classrooms(classrooms)

                return classrooms[x]

    raise HTTPException(422, "Classroom doesn't exist: Check identifier")


@classroom_router.post("/remove_student")
def class_remove_student(identifier: str, student_id: int):
    load_data_students()
    load_data_classrooms()

    x = check_classroom(identifier.upper())
    temp = classrooms[x].students

    for i in range(len(temp)):
        if temp[i].student_id == student_id:
            del temp[i]
            update_data_classrooms(classrooms)
            return classrooms[i]

    raise HTTPException(422, "Student is not in classroom.")


@classroom_router.delete("/delete")
def class_delete(identifier: str):
    load_data_students()
    load_data_classrooms()

    idx = check_classroom(identifier)
    if classrooms[idx] in classrooms:
        del classrooms[idx]
        update_data_classrooms(classrooms)
        return f"Classroom Deleted: Class {identifier.upper()} has been deleted"
    else:
        raise HTTPException(422, "Class identifier error: Class doesn't exist")


#general endpoints
@app.delete("/reset")
def reset():
    students.clear()
    classrooms.clear()

    update_data_students(students)
    update_data_classrooms(classrooms)
    return "Success: Data has been wiped"


@app.post("/outbreak")
def outbreak(date: datetime, infection_type: str, identifier: str):
    """Infection Type:
    Class: entire class was infected
    Student: Only one student was infected
    """
    load_data_classrooms()
    load_data_students()

    infection_type = infection_type.lower()
    local_status = ""

    if infection_type[0] == 'c':
        x = check_classroom(identifier.upper())
        members = classrooms[x].students
        for i in range(len(members)):
            members[i].infection_date = date

            if timedelta(days=14) > datetime.now() - members[i].infection_date:
                members[i].status = "quarantined"
                update_data_students(students)
            else:
                members[i].status = "healthy"
                update_data_students(students)

            update_data_classrooms(classrooms)
            return f"Outbreak for Classroom {identifier} has been set infection dates have been set: {date}"

    elif infection_type[0] == "s":
        for i in range(len(students)):
            if students[i].student_id == int(identifier):
                students[i].infection_date = date
                if timedelta(days=14) > datetime.now() - students[i].infection_date:
                    students[i].status = "quarantined"
                    update_data_students(students)
                else:
                    students[i].status = "healthy"
                    update_data_students(students)

                return f"Outbreak for student {identifier} has been set"

    raise HTTPException(422, "Make sure identifier is formated to match infection type")


app.include_router(student_router)
app.include_router(classroom_router)
