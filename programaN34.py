print('programa-34 - programa para contar numeros impares y pares')
def programa_34():
 numero = 1
 while numero <= 20:
     if numero % 2 == 0:
         print("Número par:", numero)
     else:
         print("Número impar:", numero)
     numero += 1
programa_34()