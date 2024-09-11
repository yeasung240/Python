# Combination
Recurrence relation 

D[i][j] = D[i-1][j] + D[i-1][j]

Let's say you pick 3 balls out of 5 balls. 4 balls are already decided so the probaility depends on the 5th ball. 
* When 5th ball is a last ball

5C2
* When 5th ball is not a last ball

5C3

The condition. 


```python

# D[i][j] = D[i-1][j-1] + D[i-1][j]
N, K = map(int, input().split())
lis = [[0]*(N+1) for i in range(N+1)]

for i in range(N+1):
    lis[i][1] = i
    lis[i][0] = 1
    lis[i][i] = 1 


for i in range(N+1):
    for j in range(N+1):
        if j <= i and lis[i][j] == 0:
            lis[i][j] = lis[i-1][j] + lis[i-1][j-1]
print(lis[N][K])

```

```python
# D[i][j] = D[i-1][j-1] + D[i-1][j]
N, K = map(int, input().split())
lis = [[0]*(N+1) for i in range(N+1)]

for i in range(N+1):
    lis[i][1] = i
    lis[i][0] = 1
    lis[i][i] = 1 


for i in range(2, N+1):
    for j in range(1, i):
            lis[i][j] = lis[i-1][j] + lis[i-1][j-1]
print(lis[N][K])
```