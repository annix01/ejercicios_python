#funcion que calcula el area de un circulo
from math import pi
class Circulo:
    def __init__(self, radio):
        self.radio=radio

    def area(self):
        return pi*(self.radio**2)
radio = float(input("radio en cm:"))
r=Circulo(radio)

print("el area del circulo es:", (r.area()))
