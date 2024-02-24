import math
import os
os.system("cls || clear")

#calcular el area de un circulo
radio = int(input("ingrese el radio del circulo: "))
area = math.pi * pow(radio, 2)
#Imprimir el resultado con 2 decimales
print ("El area del circulo es: {:.2f} ".format(area))