import math

class FooParameterization:
    def __init__(self, radius):
        #initializes the FooParameterization
        if radius <= 0:
            raise ValueError("Radius must be a positive number.")
        self.radius = radius

    def calculate_volume(self):
        #calulating the volumne of the sphere
        #Foo el al. parameterization -> returning the volume of the sphere 

        #logic
        volume = (4/3) * math.pi * (self.radius ** 3)
        return volume

    def __str__(self):
        return f'FooParameterization(radius={self.radius})'

