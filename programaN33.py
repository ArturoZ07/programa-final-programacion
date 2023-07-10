print('programa-33- programa que genera las tablas  de multiplicar')
def programa_33():
 for i in range (1, 13):
     print('Tabla de multiplicar del : ',i)
     print('=========================')
     for j in range (1, 13):
         resultado = i * j
         print(i, 'x', j, '=', resultado)
     print()
programa_33()