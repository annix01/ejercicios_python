#Ejercicio voltear frase
class Frase_volteada:
    def longi(self):
        txt = input ("Ingresa un texto en esta linea :  ")
        txtt = txt[::-1]

        print ('El texto original es: ' + txt)
        print('El texto al reves es: ' + txtt)

plint = Frase_volteada()
plint.longi()
