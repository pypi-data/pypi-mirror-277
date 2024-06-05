from foo_et_al_JK.sphere import Sphere

class foo_et():
    def __init__(self, shape = None):
        if(shape == None):
            self.shape = "sphere"
        else:
            self.shape = shape
    def getVolume(self, radius):
        match self.shape.lower(): 
            case "sphere":
                self.object = Sphere(radius)
                return self.object.volume()