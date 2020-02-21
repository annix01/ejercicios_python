#funcion que calcula el area de un triangulo

class Triangulo:
    def __init__(self, base, altura):
        self.base=base
        self.altura=altura

    def area(self):
        return (self.base*self.altura)/2
base = float(input("Base"))
altura = float(input("Altura"))
r=Triangulo(base,altura)
print("el area del triangulo es:", (r.area()))
