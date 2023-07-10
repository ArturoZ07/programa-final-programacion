print('Programa 26. n\ Programa que clasifica triangulos segun sus lados n\ ')
def programa_26():
 LadoA = float(input('Escribe el valor 1: '))
 LadoB = float(input('Escriba el valor 2: '))
 LadoC = float(input('Escriba el valor 3: '))

 if LadoA == LadoB == LadoC:
     print('El tringulo es equilatero')
 elif LadoA == LadoB or LadoA == LadoC     or LadoB == LadoC:
     print('El tringulo es isoceles')
 else:
     print('El tiangulo es escaleno')
 print('Fin del programa')
programa_26()