A = [[1, 2], [2, 3]]
B = [[1, 2], [3, 4]]
C = [[0, 0], [0, 0]]

for i in range(len(A)):
    for j in range(len(B[0])):
        for k in range(len(B)):
            C[i][j] = C[i][j] + A[i][k] * B[k][j]

print(C)