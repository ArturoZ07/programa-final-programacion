print('Programa-5 calcular el perimetro de un rectangulo')
def funcion_suma(A,B,C,D):
	P = round (A + B + C +D)
	return P
A= float(input('VALOR DE A: '))
B= float(input('VALOR DE B: '))
C= float(input('VALOR DE C: '))
D= float(input('VALOR DE D: '))
P = funcion_suma(A,B,C,D)
print (P)