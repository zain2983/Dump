class Car:

    def __init__(self,brand,model):
        self.__brand = brand
        self.model = model

    def drive(self):
        print("This "+self.model+" is driving")

    def stop(self):
        print("This "+self.model+" is stopped")

    def get_brand(self):
        return self.__brand
    
    def show(self):
        return f"\nModel : {self.model}\nBrand : {self.__brand}\n"
