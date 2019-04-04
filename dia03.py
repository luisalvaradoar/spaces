#recapitulando los ciclos
#ciclo for
'''
objetos iterables:
 - string ("hola")
 - listas ['a', 2, 2.0]
 - tuplas ()
 - parametros de diccionarios
 - range(i, j, p) --> [i, j) cada p
'''
for i in (1.2, 100, 'luis', [1,2]):
	print(i)

#condicional if
a = 7
if a%2 == 0:
	print("a es par")
elif a%3 == 0:
	print("a es multiplo de 3")
else:
	print("holi")

#ciclos while
j = 0
while j <= 100:
	j += 1

#paros
n = 10
while(True):
	n = n**3 - 1
	if n > 100000 or n%3 == 2:
		break
print(n)
