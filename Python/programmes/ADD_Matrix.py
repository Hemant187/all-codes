def Matrix(m,n):
    o =[]
    for i in range(m):
        row = []
        for j in range(n):
            c = int(input(f"Enter the number ({i},{j})"))
            row.append(c)
        o.append(row)
    return o

def Sum(A,B):
    output =[]
    for i in range(len(A)):#Number of rows
        row =[]
        for j in range(len(A[0])):# Number of columns
            c= A[i][j]+B[i][j]
            row.append(c)
        output.append(row)
    return output
            


m = int(input('Enter the value of m\n'))
n = int(input('Enter the value of n\n'))
print(f'Enter matrix {m}x{n}')
A = Matrix(m,n)
# print(A)

B = Matrix(m,n)
# print(B)

S = Sum(A,B)
print(A)
print(B)
print(S)

