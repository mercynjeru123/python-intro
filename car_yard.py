#car(make,model,date_of_make,drive side)
#age of the car
#allowed in kenya
#print details
class Cars:
    def __init__(self,make,model,date_of_make):
        self.make=make
        self.model=model
        self.date_of_make=date_of_make


    def make_of_car(self,brand):
        self.make=brand
        print(f"The vehicle was manufactured by {self.make}.")

    def car_model(self,design):
        self.model=design
        print(f"This car has a{self.model} design.")

    def make_date(self,m_date):
        self.date_of_make=m_date
        print(f"It was manufactured on : {self.date_of_make}")


    def print_details(self):
        print(f"Make : {self.make}")
        print(f"Model : {self.model}")
        print(f"Date : {self.date_of_make}")
        print("----------------------------------")


car1=Cars("Porsche","cayenne",1998)
car1.print_details()
car2=Cars("Mazda","cx3",1999)
car2.print_details()