print('programa-14 Programa que indica el costo total de la compra')
PG = float(input("PRECIO DE GASOLINA: "))
LG = float(input("LITROS DE GASOLINA: "))
def funcion_mult(PG,LG):
	CS = PG*LG
	return CS
CS = funcion_mult(PG,LG)
def funcion_mult(PG,LG):
	CT = round(((PG*LG)*1.07),2)
	return CT
CT = funcion_mult(PG,LG)
print("COSTO TOTAL SIN IMPUESTO:",CS)
print("COSTO TOTAL CON IMPUESTO:",CT)