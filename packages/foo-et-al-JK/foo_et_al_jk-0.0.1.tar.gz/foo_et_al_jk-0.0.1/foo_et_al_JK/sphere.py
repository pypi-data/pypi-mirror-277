import math
#This class is used to depict a sphere object that is initialized with a radius
#and has a method to return the volume
class Sphere: 
    def __init__(self, radius):
        self.radius = radius
    def volume(self):
        return ((4/3)*(math.pi)*(self.radius**3))