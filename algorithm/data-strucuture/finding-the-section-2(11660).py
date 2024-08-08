n, m = map(int, input().split())
A = [[0] * (n+1)]
B = [[0] * (n+1) for _ in range(n+1)] # making matrix 


for i in range(n):
    A_row = [0] + [int(x) for x in input().split()] # making input values to matrix
    print(A_row)
    A.append(A_row)
    
    
for i in range(1, n+1):
    for j in range(1, n+1):
        D[i,j] = D[i][j-1] + D[i-1][j] - D[i-1][j-1] + A[i][j]
        
for i in range(m):
    x1, y1, x2, y2 = map(int, input().split())
    result = D[x2][y2] - D[X2][y-1] - D[X1-1][y-2] + D[x-1][y-1]
print(A)
print(B)
