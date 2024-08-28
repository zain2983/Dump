from car import Car

car_1 = Car("Chevy","Corvette")
car_2 = Car("Ford","Mustang")

# print(car_1.show())
# print(car_2.show())

print(car_1.get_brand())
print(car_2.get_brand())

# These lines would give error 
# Because "brand" is private 
# print(car_1.model)
# print(car_1.brand)
# print(car_2.model)
# print(car_2.brand)
