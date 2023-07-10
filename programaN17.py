print('Programa 17. Convertir unidades de medida')
def Programa_17():
    kg = float(input('Ingresa los kg: '))
    g = kg * 1000
    print('La cantidad en Gramos es =', g)

    g = float(input('Ingresa los  g: '))
    kg = g * 0.001
    print('La cantidad en Kilogramos es =', kg)

    m = float(input('Ingresa los m: '))
    cm = m * 100
    print('La cantidad en centímetros es =', cm)

    cm = float(input('Ingresa los cm: '))
    m = cm * 0.01
    print('La cantidad en metros es =', m)

    print('Fin del Programa')
Programa_17()