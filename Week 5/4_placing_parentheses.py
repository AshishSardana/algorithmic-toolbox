# Uses python3
import re

def evalt(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    else:
        assert False

def min_and_max(M, m, ops, i, j):
    # it seems that we cannot import math.inf here
    minimum = 1000000000
    maximum = -100000000

    for k in range(i, j):
        a = evalt(M[i][k], M[k + 1][j], ops[k])
        b = evalt(M[i][k], m[k + 1][j], ops[k])
        c = evalt(m[i][k], M[k + 1][j], ops[k])
        d = evalt(m[i][k], m[k + 1][j], ops[k])

        minimum = min(minimum, a, b, c, d)
        maximum = max(maximum, a, b, c, d)
    return minimum, maximum

def get_maximum_value(dataset):
    #write your code here
    digits = list(int(digit) for digit in re.findall(r"(\d+)+", dataset))
    operations = re.findall(r"([\+|\-|\\|\*])+", dataset)

    m = []
    M = []
    n = len(digits)
    for i in range(0, n):
        m.append(list(0 for j in digits))
        M.append(list(0 for j in digits))
    for i in range(0, len(m)):
        m[i][i] = digits[i]
        M[i][i] = digits[i]

    for s in range(1, n):
        for i in range(0, n - s):
            j = i + s
            res = min_and_max(M, m, operations, i, j)
            m[i][j], M[i][j] = res

    return M[0][len(digits) - 1]

def print_value(value):
  print("Value is " + str(len(value[0])) + "x" + str(len(value)) + " matrix")
  for i in range(0, len(value)):
    string = ""
    for j in range(0, len(value[i])):
      string += "{:>3}".format(value[i][j]) + " "
    print(string)

if __name__ == "__main__":
    # string = "5-8+7*4-8+9"
    # print(get_maximum_value(string))
    print(get_maximum_value(input()))

# print("k = " + str(k) + " M[i][k] = " + str(M[i][k]) + " M[k + 1][j] = " + str(M[k + 1][j]))

# print("i = " + str(i) + " j = " + str(j) + " M[i] = " + str(M[i]) )

# print("We set m[i][j], M[i][j] = " + str(res[0]) + " " + str(res[1]))