print('Programa-7 calcular el volumen de un prisma rectangular')
def funcion_mult(A,B,C):
	V = round((A * B * C),2)
	return V
A = float(input('VALOR DE LARGO: '))
B = float(input('VALOR DE ANCHO: '))
C = float(input('VALOR DE ALTURA: '))
V = funcion_mult(A,B,C)
print("EL VOLUMEN DE UN PRISMA RECTANGULAR ES:",V)