print ("Programa 4. que calcula el area de una triangulo \n")
def funcion_mult(B,A):
	Area = (B * A) / 2
	return Area
A = float(input('la altura de A es: '))
B = float(input('la base de B es: '))
Area = funcion_mult(B,A)
print(Area)