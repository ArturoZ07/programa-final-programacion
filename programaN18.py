print('Programa 18. Calcula el interés compuesto')
def Programa_18():
    ci = float(input('Ingrese el capital inicial: '))
    i = float(input('ingrese la tasa de interés: '))
    n = float(input('ingrese el número de periodos: '))

    Cf = ci * (1 + i) * n
    CF = round(Cf, 2)

    print('La capital final es =', CF)
    
    print('Fin del Programa')
Programa_18()