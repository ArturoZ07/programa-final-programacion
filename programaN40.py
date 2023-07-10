print('programa-40- version del Programa  13 modificado a funcion, programa que resuelva una regla de 3 simple')

def funcion_mult(A,B,C):
	D =round(((B*C)/A),2)
	return D
A = float(input('INSERTE EL VALOR DE A: '))
B = float(input('INCERTE EL VALOR DE B: '))
C = float(input('INCERTE  EL VALOR DE C: '))
D = funcion_mult(A,B,C)
print("RESULTADO:",D)