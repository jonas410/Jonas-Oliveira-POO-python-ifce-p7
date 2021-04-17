#!/usr/bin/env python3

import sys

print("Digite valores nao-nulos e positivos.")

try: 

	a = float(input("Entre com a medida do lado 1 do triangulo: "))
	b = float(input("Entre com a medida do lado 2 do triangulo: "))
	c = float(input("Entre com a medida do lado 3 do triangulo: "))

except ValueError:

	print("Digite somente numeros para as medidas 1, 2 e 3.")
	sys.exit(1)

if a>=b+c or b>=c+a or c>=a+b :
	print("false")
	quit()
	
if a<=0 or b<=0 or c<=0 :
	print("False")
	quit()

if a==b and b==c :
	print("verdadeiro. Triangulo equilatero.")

elif a==b or b==c or c==a :
	print("verdadeiro. Triangulo isosceles.")

else:
	print("verdadeiro. Triangulo escaleno.")
