#-*-coding:utf8 -*-
from math import sqrt
''' Este programa resuelve una ecuación cuadrática
Entradas: a, b y c los coeficientes de x^2, x y el término independiente
Salidas: Las raíces de la ecuación cuadrática
'''
a = int(input("Ingrese a: "))
b = int(input("Ingrese b: "))
c = int(input("Ingrese c: "))

def formula_cuadratica(a, b, c):
	x1 = (-b + sqrt(b**2 - 4 * a * c)) / (2 * a)
	x2 = (-b - sqrt(b**2 - 4 * a * c)) / (2 * a)
	return((x1, x2))

xs = formula_cuadratica(a,b,c)
print("Las raíces son {} y {}".format(xs[0], xs[1]))