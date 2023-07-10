print('programa- 13 Programa que calcule el salario neto')
SB = float(input('Valor de Salario bruto: '))
CP = round((50),2)
def funcion_mult(SB):
	SS = round((SB * 0.0514),2)
	return SS
SS = funcion_mult(SB)
def funcion_mult(SB):
	SE = round((SB * 0.02),2)
	return SE
SE = funcion_mult(SB)
def funcion_resta(SB):
	SN = round((SB-SS-SE-CP),2)
	return SN
SN = funcion_resta(SB)
print("SALARIO NETO DE SEGURO SOCIAL ES:",SS)
print("SALARIO NETO DE SEGURO EDUCATIVO ES:",SE)
print("LA CUOTA DE PRESTAMO ES:",CP)
print("EL SALARIO NETO ES:",SN)