class Car:

    def __init__(self,brand,model):
        self.brand = brand
        self.model = model


    def drive(self):
        print("This "+self.model+" is driving")

    def stop(self):
        print("This "+self.model+" is stopped")




class ElectricCar(Car):
    def __init__(self,brand,model,battery_size):
        super().__init__(brand,model)
        self.battery_size = battery_size

    def show(self):
        return f"Model : {self.model}\nBrand : {self.brand}\nBattery size : {self.battery_size}"