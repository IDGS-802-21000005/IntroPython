num1 = 1
num2 = 2

print("La suma es :",(num1+num2))
print("La resta es :",(num1-num2))
print("La multiplicación es :",(num1*num2))
print("La division es :",(num1/num2))
print("La exacta es :",(num1//num2))
print("La potencia es :",(num1**num2))


#concatenacion en python

texto1="Hola"
texto2="Mundo"
textFinal=texto1+" "+texto2
print(textFinal)
print("El saludo es: %s %s" %(texto1,texto2))

saludofinal = "El saludo es: {} {}".format(texto1,texto2)
print(saludofinal)

saludofinal = "El saludo es: {x} {y}".format(x=texto1,y=texto2)
print(saludofinal)