class Vehicle:
    total_vehicle = 0
    
    def __init__(self,name,make,model,year):
        self.name = name
        self.make = make
        self.model = model
        self.valid_year(year)
        self.year = year
        Vehicle.total_vehicle += 1

    def __str__(self):
        return f"Name: {self.name}, Make: {self.make}, Model: {self.model}, Year: {self.year}"
    
    def display_vehicle(self):
        print(self.__str__())


    @staticmethod
    def valid_year(year):
        if len(str(year)) < 4 or not isinstance(year,int):
            raise ValueError("4 Digit and Only Number like: 2024")
        return True
    
    @classmethod
    def update_totla_vehicles(cls):
        print(f"Updated The Number of Total Vehicle : {cls.total_vehicle}")
    

if __name__ == "__main__":
    try:
            
        v1=Vehicle("n1","m1","mo1",2023)
        print(v1)
    except ValueError as e:
        print(e)
v2=Vehicle("n2","m2","mo2",2022)
v3=Vehicle("n3","m2","mo2",2021)

v1.display_vehicle()
v2.display_vehicle()
v3.display_vehicle()

v4=Vehicle("n4","m4","mo4",2020)
Vehicle.update_totla_vehicles()