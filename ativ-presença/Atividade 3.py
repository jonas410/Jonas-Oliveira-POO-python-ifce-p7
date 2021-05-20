import random
numeros = [];
for x in range(1,7):
	sorteio = random.randint(1,60)
	numeros.append(sorteio);
	(numeros.sort())
	print(numeros)
print("foram estes os numeros sorteados")
