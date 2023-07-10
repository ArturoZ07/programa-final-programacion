print('programa-39 Programa que calcula la suma de los números pares entre 1 y 20 y que el numero ingresado se sume a la suma de lo numeros pares')
def funcio_suma_de_numeros_pares():
 suma = float(input("Ingrese el numero: "))
 numero= 0
 while numero <= 20:
     if numero % 2 == 0:
         suma += numero
     numero += 1
 print("El resulatado de la suma de numeros pares es:", suma)
funcio_suma_de_numeros_pares()