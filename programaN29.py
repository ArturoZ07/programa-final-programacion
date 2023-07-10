print('Programa 29. n\ Programa que  determina la calificación n\ ')
def programa_29():
 value = 1
 while value <= 4:
     print(value)
     value += 1
     Valor = float(input('Escribe el valor: '))
     if Valor >= 90:
         print('Es A')        
     elif Valor >= 80 and Valor <90:
         print('Es B')
     if Valor >= 70 and Valor < 80:
         print('Es C')        
     elif Valor >= 60 and Valor < 70:
         print('Es D')
     if Valor < 60:
         print('Es F')        
programa_29()