#Using python3

def matrices_multiply(matrices):
	matrices_length  = len(matrices)
	M = [[0 for _ in range(matrices_length)] for _ in range(matrices_length)]
	
	for gap in range(2,matrices_length):
		for i in range(0,matrices_length-gap):
			j = i+gap	
			M[i][j]=10000
			for k in range(i+1,j):
				temp = (M[i][k] + M[k][j]) + (matrices[i] * matrices[k] * matrices[j])
				print (i,j,k,temp) 
				if temp < M[i][j]:
					M[i][j] = temp

	print(M)
	print M[0][-1]


matrices_multiply([2,3,6,4,5])



