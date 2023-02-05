# Wayne Bell Ivy Tech Community College
# date: 2023-02-05
# description: This program asks a user for the year, make, model, number of doors, and type of roof for a car. It then displays the information.
# It contains the classes Vehicle and Automobile. The Vehicle class has a constructor that accepts a vehicle type. 
# The Automobile class inherits from the Vehicle class. 
# The Automobile class has a constructor that accepts the year, make, model, number of doors, and type of roof. 
# The Automobile class also has a constructor that accepts a vehicle type. The vehicle type should be set to "car" by default. 
# The main function asks the user for the year, make, model, number of doors, and type of roof for a car. 
# It then creates an Automobile object and displays the information.


class Vehicle:
    def __init__(self, vehicle_type):
        self.vehicle_type = vehicle_type

class Automobile(Vehicle):
    def __init__(self, year, make, model, doors, roof, vehicle_type="car"):
        super().__init__(vehicle_type)
        self.year = year
        self.make = make
        self.model = model
        self.doors = doors
        self.roof = roof

def main():
    year = input("Enter the year of the car: ")
    make = input("Enter the make of the car: ")
    model = input("Enter the model of the car: ")
    doors = input("Enter the number of doors (2 or 4): ")
    roof = input("Enter the type of roof (solid or sun roof): ")

    car = Automobile(year, make, model, doors, roof)

    print("Vehicle type:", car.vehicle_type)
    print("Year:", car.year)
    print("Make:", car.make)
    print("Model:", car.model)
    print("Number of doors:", car.doors)
    print("Type of roof:", car.roof)

if __name__ == "__main__":
    main()

