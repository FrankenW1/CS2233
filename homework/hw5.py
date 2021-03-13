class Employee:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname

    def fullname(self):
        return self.firstname + ' ' + self.lastname
    def email(self):
        a = self.firstname + '.' + self.lastname
        a = a.lower()
        email = a + '@comany.com'
        return email

class Football:
    def __init__(self, name:str, age: int, height: int, weight: int):
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight

    def get_age(self):
        age = str(self.age)
        ret = self.name + ' is age ' + age
        return ret

    def get_height(self):
        height = str(self.height)
        ret = self.name + ' is ' + height + ' cm'
        return ret

    def get_weight(self):
        weight = str(self.weight)
        ret = self.name + ' weighs ' + weight + ' kg'
        return ret


class Name:
    def __init__(self, fname: str, lname: str):
        self.fname = fname
        self.lname = lname


    def fullname(self):
        return self.fname + self.lname

    def initials(self):
        f = self.fname[0]
        l = self.lname[0]
        return f + '.' + l

