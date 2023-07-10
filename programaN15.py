print('Programa-15 Programa que devuelve el valor total de los productos a comprar')
A  = float(input('VALOR DE ARTICULO 1: '))
B  = float(input('VALOR DE ARTICULO 2: '))
C  = float(input('VALOR DE ARTICULO 3: '))
def funcion_suma(A,B,C):
	DS = A+B+C
	return DS
DS = funcion_suma(A,B,C)
def funcion_mult(A,B,C):
	D = round(((A+B+C)*1.07),2)
	return D
D = funcion_mult(A,B,C)
print("TOTAL SIN IMPUESTOS :",DS)
print("TOTAL A PAGAR CON IMPUESTOS:",D)