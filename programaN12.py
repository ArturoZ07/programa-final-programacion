print('programa-12 Programa que calcule el interes a pagar por un prestamo')
def funcion_mult(M,T,P):
	F = round((M * T * P),2)
	return F
M = float(input('Escribe el valor de Monto del prestamo: '))
T = float(input('Escribe el valor de la Tasa mensual: '))
P = float(input('Escribe el valor de P: '))
F = funcion_mult(M,T,P)
print("EL INTERES A PAGAR ES:",F)