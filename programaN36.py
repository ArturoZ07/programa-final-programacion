print('Programa 36. n\ Programa que se detiene al llegar a 9 en bucle de for n\ ')
def programa_36():
 i = 1
 for i in range (10):
     print(i)
     z = i + 1
     if z < 5:
             print('menor a 5')
     elif z > 5:
         print('mayor a 5')
     else:
         print('es igual a 5')
     if z ==9:
         break
programa_36()