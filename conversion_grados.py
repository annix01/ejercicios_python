#conversion de grados farenheit-celsius
class Conversion:
    
    def grado(self):
        si = input("¿De que grado va a convertir? Celsius = c Farenheit = f ")
        print("")
        if si == "c":
            celsius = float(input("Ingresa una temperatura en celsius: "))
            print("")
            fahrenheit = (celsius * 9/5) + 32
            print('%.2f Celsius es: %0.2f Fahrenheit' %(celsius, fahrenheit))
        else:
            fahrenheit = float(input("Ingresa una temperatura en fahrenheit: "))
            print("")
            celsius = (fahrenheit - 32) * 5/9
            print('%.2f Fahrenheit es: %0.2f Celsius' %(fahrenheit, celsius))
            print("")
    
calcular = Conversion()
calcular.grado()
