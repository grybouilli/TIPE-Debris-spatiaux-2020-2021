import numpy as np

class Vecteur:
    def __init__ (self,x,y,z):
        self.x = x
        self.y = y
        self.z = z

    def get_x(self):
        return(self.x)
    def get_y(self):
        return(self.y)
    def get_z(self):
        return(self.z)

    def set_x(self,x1):
        self.x = x1
    def set_y(self,y1):
        self.y = y1
    def set_z(self,z1):
        self.z = z1

    def __add__(self, other):
        return Vecteur(self.x+other.get_x(), self.y+other.get_y(), self.z+other.get_z())
    
    def __str__(self):
        return "(x = %s, y = %s, z = %s)" % (self.get_x(), self.get_y(), self.get_z())
    

def prod_scal(vect1,vect2):
    (x1,x2) = (vect1.get_x(),vect2.get_x())
    (y1,y2) = (vect1.get_y(),vect2.get_y())
    (z1,z2) = (vect1.get_z(),vect2.get_z())
    return x1*x2 + y1*y2 + z1*z2
    
def prod_vec(vec1, vec2):
    (x1,x2) = vec1.get_x(), vec2.get_x()
    (y1,y2) = vec1.get_y(), vec2.get_y()
    (z1,z2) = vec1.get_z(), vec2.get_z()

    return Vecteur(y1*z2-y2*z1, z1*x2-x1*z2, y2*x1-y1*x2)
    
def polar_of_cart(vec):
    r = np.sqrt(vec.get_x()**2 + vec.get_y()**2)
    if r == 0:
        return Vecteur(0,0,0)
    return Vecteur(r, np.arccos( vec.get_x() / r ),vec.get_z())