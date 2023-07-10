print('Programa-6 calcular el Area de un trapecio')
def funcion_mult(B1,B2,A):
	T = round((B1 + B2)*A)/ 2
	return T
B1= float(input('VALOR DE B1: '))
B2= float(input('VALOR DE B2: '))
A= float(input('VALOR DE A: '))
T = funcion_mult(B1,B2,A)
print("EL AREA DE UN TRAPECIO ES:",T)