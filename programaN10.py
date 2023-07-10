print('program-10 Programa que convierta una cantidad')
A= float(input('VALOR DE METRO: '))
def funcion_mult(A):
	AR = round((A * 3.281),2)
	return AR
AR = funcion_mult(A)
print("EL RESULTADO DE METRO A PIES ES: ", AR)
def funcion_mult(A):
	BR = round((A * 39.37),2)
	return BR
BR = funcion_mult(A)
print("EL RESULTADO DE METRO A PULGADA ES: ", BR)