from math import sqrt
S = 0
for i in range(1, 1 + 1):
	S += i**i

#print(str(S)[-10::])
'''
para darle vuelta a un string
"hola"[::-1] retorna "aloh"

si quiero los ultimos n caracteres de un string
"hola"[-2::] retorna "la"
en general string[-n::]

si quiero los primeros n caracteres de un string
"hola"[:2] retonra "ho"
en general string[:n]
'''
def divisores(numero):
	div = []
	for i in range(1, int(sqrt(numero)) + 1):
		if numero%i == 0:
			div.append(i)
			div.append(numero//i)
	return(sorted(div))


def Qamigables(numero):
	a = sum(divisores(numero)) - numero
	b = sum(divisores(a)) - a
	if numero != a and numero == b:
		return(True)
	else:
		return(False)

listaA = []
for a in range(1, 10000 + 1):
	if Qamigables(a):
		listaA.append(a)

print(sum(listaA))