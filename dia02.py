#ciclos for

S = 0
for i in range(1, 1000 + 1):
	S += i

for c in "rubi":
	print(c)

lista = ['a', 1, (2.3,1)]
for i in lista:
	print(i)

S = 0
for n in range(1, 1000 + 1):
	if n%5 == 0:
		S += n

print(S)

#la suma de los multiplos de cinco y tres abajo de 10**6
S = 0
for g in range(1, 10**3 + 1):
	if g%3 == 0:
		S += g
	if g%5 == 0:
		S += g
	if g%15 == 0:
		S -= g
print(S)

M = 1000
suma = 0

# suma todos los multiplos de 3 que no son divisibles por 5
for n in range( M // 3 + 1 ):
	m3 = 3 * n
	if m3 % 5 != 0:
		suma += m3
# suma todos los multiplos de 5.
for n in range( M // 5 ):
	m5 = 5 * n
	suma += m5
	
print(suma)
