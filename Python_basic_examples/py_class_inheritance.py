class Automobile:
    fuelType = ["Petrol", "Diesel"]

    def __init__(self, color, no_of_wheels):
        self.color = color
        self.no_of_wheels = no_of_wheels
        print(f"Details: Color {self.color}")

    def details(self):
        print("Color :", self.color)
        print('No of wheels :', self.no_of_wheels)

    def start(self):
        print("Its starting")

    def stop(self):
        print("Stopped")

class Car(Automobile):
    typeVehicle = "Car"

    def __init__(self,color, no_of_wheels):
        super().__init__(color, no_of_wheels)
        print(f"Type is {self.typeVehicle}")
    
    def stop(self):
        print("Car stopped")

bmw = Car("White", 4)
bmw.start()
bmw.stop()
