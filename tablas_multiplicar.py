#ejercicio tablas de multiplicar
class Tablas_multiplicar:
    def multi(self):
        for n in range (1,11):
            for i in range(1, 11):
               print(n, 'x', i, '=', n*i)
            print("")
            n + 1

multiplicar = Tablas_multiplicar()
multiplicar.multi()


   
