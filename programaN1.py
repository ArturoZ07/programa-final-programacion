print("programa  1\n intercambio de variables\n")
def intercambio_variables():
	A = 7
	B = 0
	C = 0
	B = A
	C = B
	A = A
	return(A,B,C)
A,B,C = intercambio_variables()
print(A,B,C)