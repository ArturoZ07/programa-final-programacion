print('programa-22 programa que indica el nivel de temperatura')
def programa_22():
 temperatura = float(input('Escriba la temperatura: '))
 if temperatura < 20:
  if temperatura < 10:
	      print('Nivel azul')
  else: 
        print('Nivel verde')
 else:
     if temperatura < 30:
           print('Nivel naranja')
     else:
  	     print('Nivel rojo')
programa_22()