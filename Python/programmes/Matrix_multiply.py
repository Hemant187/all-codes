A = [[1, 0, 3],
     [2, 0, 4],
     [5, 0, 2]]

B = [[1, 2],
     [0, 1],
     [2, 3]]

# A(3x3) B(3x2) --> C(3x2)
C = [[0, 0],
     [0, 0],
     [0, 0]]

for i in range(len(A)):
    for j in range(len(B[0])):
        for k in range(len(B)):  # i. 0-2   j. 0-1   k. 0-2
            C[i][j] += A[i][k] * B[k][j]
for row in C:
    print(row)
