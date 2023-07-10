print('programa-19 Programa que devuelve el valor total de los productos con y sin impuestos y el promedio de la compra sin impuesto')
P1 = float(input('valor del producto 1: '))
P2 = float(input('valor del producto 2: '))
P3 = float(input('valor del producto 3: '))
P4 = float(input('valor del producto 4: '))
P5 = float(input('valor del producto 5: '))
def funcion_suma(P1,P2,P3,P4,P5):
	TS = P1+P2+P3+P4+P5
	return TS
TS = funcion_suma(P1,P2,P3,P4,P5)
print("Total sin impuesto:",TS)
T = TS
def funcion_mult(TS):
	T = round(( TS * 1.07),2)
	return T
T = funcion_mult(TS)
print("Total con impuesto:",T)
def funcion_suma(P1,P2,P3,P4,P5):
	P = (P1+P2+P3+P4+P5)/5
	return P
P = funcion_suma(P1,P2,P3,P4,P5)
print("El promedio de la compra sin impuesto:",P)
	