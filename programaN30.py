print('Programa 30. n\ Programa que indica nuemros mayores, menores y cero n\ ')
def programa_30():
 value = 1
 while value <= 3:
     print(value)
     value += 1
     Valor = float(input('Escribe el nuemro: '))

     if Valor == 0:
         print('Es cero')
        
     elif Valor < 0:
         print('Es negativo')
        
     else:
         print('Es positivo')
programa_30()
