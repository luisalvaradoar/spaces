from math import sqrt, factorial

suma_1 = 0 #suma de los cuadrados de los naturales
suma_2 = 0 #suma de los naturales

for i in range(1, 100 + 1):
	suma_1 += i**2
	suma_2 += i

#print(suma_2**2 - suma_1)

#esta funcion comprueba que un numero es primo por medio de la criba de eratostenes
def criba(numero):
	if numero == 1:
		return(False)
	elif numero == 2:
		return(True)

	for n in range(2, int(sqrt(numero)) + 1):
		if numero%n == 0:
			return(False)

	return(True)

Sp = 0 #suma de los primos
for i in range(1, 200):
	if criba(i):
		Sp += i

#print(Sp)


#el primer primo arriba de dos millones
contador = 0
for i in range(1, 2):
	if criba(i):
		contador += 1
		if contador == 3:
			print(i)
			break

cienfac = factorial(100)
S = 0
for d in str(cienfac):
	S += int(d)
#print(S)

#problema 4
def Qpalindromo(numero):
	if str(numero) == str(numero)[::-1]:
		return(True)
	else:
		return(False)

listaP = []
for m1 in range(999, 99, -1):
	for m2 in range(m1, 99, -1):
		m = m1*m2
		if Qpalindromo(m):
			listaP.append((m,m1,m2))

#print(max(listaP))

#problema 29
lista_ab = []
for a in range(2, 100 + 1):
	for b in range(2, 100 + 1):
		n = a**b
		if not n in lista_ab:
			lista_ab.append(n)

print(len(lista_ab))

