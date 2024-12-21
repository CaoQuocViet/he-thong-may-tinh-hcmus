# Create a Class with instance attributes
# Write a Python program to create a Vehicle class with max_speed and mileage instance attributes.

class Vehicle:
    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage

vehicle = Vehicle(240, 18)
print(vehicle.max_speed, vehicle.mileage)

# 240 18