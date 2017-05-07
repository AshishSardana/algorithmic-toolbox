#Using python3

def longest_common_substring(string1,string2):
	Y = len(string2)+1
	X = len(string1)+1

	memory = [[0 for x in range(X)] for y in range(Y)]
	longest=0
	common_substring=[]
	for y in range(1,Y):
		for x in range(1,X):
			if string1[x-1]==string2[y-1]:
				c = (memory[y-1][x-1])+1
				memory[y][x] = c
				if c > longest:
					common_substring = []
					longest = c
					common_substring.append(string2[y-c:y])
				elif c == longest:
					common_substring.append(string2[y-c:y])

	return 	common_substring		

if __name__ == '__main__':
	print (longest_common_substring('123456789012347','235679023479'))
	print (longest_common_substring('12341','4231'))


