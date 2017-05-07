# Uses python3
def edit_distance(str1, str2):
    rows = len(str2) + 1
    cols = len(str1) + 1
    T = [[0 for _ in range(cols)] for _ in range(rows)]

    for j in range(cols):
        T[0][j] = j

    for i in range(rows):
        T[i][0] = i

    for i in range(1, rows):
        for j in range(1, cols):
            if str2[i - 1] == str1[j - 1]:
                T[i][j] = T[i - 1][j - 1]
            else:
                T[i][j] = 1 + min(T[i - 1][j - 1], T[i - 1][j], T[i][j - 1])

    #print_edits(T, str1, str2)
    return T[rows - 1][cols - 1]

if __name__ == "__main__":
    print(edit_distance(input(), input()))
