print('program-16. n\Juan esta cursando una materia en la universidad y necesita conocer cual sera su nota final en la asignatura')
def funcion_mult(N1,N2,N3,N4,N5):
	NF = (N1 * 0.20) + (N2 * 0.15) + (N3 * 0.25) + (N4 * 0.10) + (N5 * 0.30)
	return NF
N1 = float(input('NOTA 1: '))
N2 = float(input('NOTA 2: '))
N3 = float(input('NOTA 3: '))
N4 = float(input('NOTA 4: '))
N5 = float(input('NOTA 5: '))
NF = funcion_mult(N1,N2,N3,N4,N5)
print("NOTA FINAL:",NF)