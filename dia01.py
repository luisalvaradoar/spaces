#-*-coding:utf8 -*-

# esta es la primera
# hola hola

'''
asdasd
asda
'''

#aritmetica
1 + 2
1 - 2
3 * 8
4 / 9
4 // 9 #cociente
4 % 9 # modulo
4 ** (1/3)
5 ** (0.5)

#importaciones
#import math 
import math as m
#math.sqrt(5)
#from math import sqrt, pow
m.factorial(12)

#tipos de datos
'''
string, letras-caracteres ("hola")
int, enteros (1,23)
float, punto flotante (3.14, 1.0)
listas, [1,2,3,4, "hola"]
tuplas, (1,2,3)
diccionarios, {1:"a", 2:"b", [1,2]:(3,2)}
bool, 1,0, True, False
'''

#variables
a = 2
b = 3
c = a
a * b

#imprimir
print('"Hola mundo"')
print(a*b)
print(a**b)
print(a//b)
print("Hola \nMundo")
print("\\n")
print("{},{},{}".format(a*b, a**b, a//b))
v1 = "hola"
v2 = "mundo"
n1 = 12
print(v1 + " " + v2 + str(n1))

n2 = "1.23"
print(n1 + float(n2)) #int()
'''
file = open("input.txt","r")
for linea in file:
	print(linea)
'''
#funciones
def f(x):
	a = x**2
	a += 1
	return(a)

def g(x):
	return(f(x+1))

print(f(2))
print(g(2))