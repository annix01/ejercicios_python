frc=(input("Ingresa una frase "))#se solicita la frase
let=len(frc)#saco la logitud original
contsig=0 #contador de letras
for i in range(0,let):
 
     if(frc[i].isalpha()):
        contsig+=1
print("Numero de letras:",contsig)
