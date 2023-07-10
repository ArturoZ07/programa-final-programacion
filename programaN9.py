print('programa-9 Programa que resuelva ecuaciones con multiples variables')
A = float(input('VALOR DE A: '))
B = float(input('VALOR DE B: '))
C = float(input('VALOR DE C: '))
def funcion_mult(A,B):
	R1 = round((4 * A) + (3 * B) ,2)
	return R1
R1 = funcion_mult(A,B)
print("RESPUESTA LA ECUACION A ES:",R1)

def funcion_mult(A,B):
	 R2 = round((1 * A) - 18 + ( 8 * B) - 5 ,2)
	 return R2
R2 = funcion_mult(A,B)
print("RESPUESTA LA ECUACION B ES:",R2)

def funcion_mult(A,B):
	 R3 = round((4 * A) + (3 * B) + 7 ,2)
	 return R3
R3 = funcion_mult(A,B)
print("RESPUESTA LA ECUACION C ES:",R3)

def funcion_mult(A,B,C):
	 R4 = round((2* A) + (3 * B) - (C**5) ,2)
	 return R4
R4 = funcion_mult(A,B,C)
print("RESPUESTA LA ECUACION D ES:",R4)

def funcion_mult(A,B,C):
	R5= round((2 * A) + (3*B) - (C**2) ,2)
	return R5
R5 = funcion_mult(A,B,C)
print ("RESPUESTA LA ECUACION E ES:",R5)