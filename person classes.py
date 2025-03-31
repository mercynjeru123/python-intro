#person classes
from datetime import date, datetime


class Person:
    def __init__(self,name,dob,gender,disabled):
        self.name=name
        self.dob=dob
        self.gender=gender
        self.disabled=disabled

    def print_details(self):
        print(f"Name: {self.name}")
        print(f"Dob: {self.dob}")
        print(f"Gender: {self.gender}")
        if self.disabled:
            print("Disabled")
        else:
            print("Enabled")
        print("----------------------")


    def get_age(self):
        current_date=datetime.today()
        date_birth=datetime.strptime(self.dob,"%d-%m-%Y")
        age=current_date-date_birth
        print("age is",age.days//365)




p1=Person("Jack","19-6-2003","Male",False)
p2=Person("Angie","20-8-1999","Female",True)
p1.print_details()
p1.get_age()

p2.print_details()
p2.get_age()