print('programa-20  Programa que devuelve el salario neto a pagar')
SB = float(input('SALARIO BRUTO: '))
def funcion_mult(SB):
	SS= round((SB * 0.08),2)
	return SS
SS = funcion_mult(SB)
print("SEGURO SOCIAL:",SS)
def funcion_mult(SB):
	SE = round((SB * 0.02),2)
	return SE
SE = funcion_mult(SB)
print("SEGURO EDUACATIVO :",SE)
def funcion_mult(SB):
	I =round((SB * 0.15),2)
	return I
I =funcion_mult(SB)
print("IMPUESTOS:",I)
P = 100
print("PRESTAMO:",P)
def funcion_resta(SB,SS,SE,I,P):
	SN = round((SB-SS-SE-I-P),2)
	return SN
SN = funcion_resta(SB,SS,SE,I,P)
print("SALARIO NETO:",SN)