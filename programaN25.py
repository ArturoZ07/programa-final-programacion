print('Programa 25. n\ Programa que calcula descuentos n\ ')
def programa25():
 Producto = float(input('Escribe el valor del producto: '))
 Descuento = float(input('Escribe el porcentaje de descuento: '))
 def funcion_mult(Producto,Descuento):
	 D = round(((Descuento * Producto) / 100),2)
	 return D
 D = funcion_mult(Producto,Descuento)
 print("Descuento:",D)
 def funcion_resta(Producto,Descuento):
	 RD = round((Producto - Descuento),2)
	 return RD
 RD = funcion_resta(Producto,Descuento)
 print('El precio final es: ', RD)

 if RD < 50:
     print('Oferta Especial')
programa25()
