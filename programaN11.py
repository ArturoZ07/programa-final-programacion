print('program-10-Programa que que resuelva una regla de 3 simple')
def funcion_mult(A,B,C):
	D =round(((B*C)/A),2)
	return D
A = float(input('ESCRIBA EL VALOR DE A: '))
B = float(input('ESCRIBA EL VALOR DE B: '))
C = float(input('ESCRIBA EL VALOR DE C: '))
D = funcion_mult(A,B,C)
print("RESULTADO:",D)