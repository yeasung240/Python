```python
# union find
import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)
N, M = map(int, input().split())
parent = [0] * (N + 1)


def find(a):
    if a == parent[a]:
        return a
    else:
        parent[a] = find(parent[a])  # 재귀 형태로 구현 -> 경로 압축 부분
        return parent[a]


def union(a, b):
    a = find(a)
    b = find(b)
    if a != b:
        parent[b] = a


def checkSame(a, b):
    a = find(a)
    b = find(b)
    if a == b:
        return True
    return False


for i in range(0, N + 1):
    parent[i] = i

for i in range(M):
    question, a, b = map(int, input().split())
    if question == 0:
        union(a, b)
    else:
        if checkSame(a, b):
            print("YES")
        else:
            print("NO")

```


```python
N, M = map(int, input().split())
parent = [0] * (N+1)

def find(a):
    if a == parent[a]:
        return a
    else:
        parent[a] = find(parent[a])
        return parent[a]
    
def union(a,b):
    a = find(a)
    b = find(b)
    if a != b:
        if a < b:
            parent[b] = a
        else:
            parent[a] = b
            
def checkSame(a,b):
    a = find(a)
    b = find(b)
    if a == b:
        return ture
    return False
        
for i in range(1, N+1):
    parent[i] = i
    
for i in range(M):
    question, a, b = map(int, input().split())
    if question == 0:
        union(a,b)
    else:
        if checkSame(a,b):
            print('Yes')
        else:
            print('NO')

```

```python
# union find 

n, m = map(int, input().split())

A = [0] * (n+1)
for i in range(1, n+1):
    A[i] = i

def find(v):
    if A[v] = v:
        return v
    else:
        A[v] = find(A[v])
        return A[v]
    
def union(a,b):
    a = find(a)
    b = find(b)
    if a != b:  # if a and b is the same, no need to change the value
        if a < b:
            A[b] = a
        else:
            A[a] = b


def check

for i in range(m):
    question, a, b = map(int, input().split())
    if question == 0:
        union(a,b)
    else:
        check(a,b)
```

```python
# 1976
N = int(input()) 
M = int(input())
A = [[]]
parent = [0] * (N+1) # parent = [1,2,3]
for i in range(1, N+1):
    parent[i] = i
for i in range(M):
    a = list(map(int, input().split()))
    A.append(a) # A = [[],[0, 1, 0], [1, 0, 1], [0, 1, 0]]
B = list(map(int, input().split())) # [1,2,3]
C = B


def find(v):
    if parent[v] == v:
        return v
    else: 
        parent [v] = find(parent[v])
        return parent[v]

def union(a, b):
    a = find(a)
    b = find(b)
    if a != b:
        if a < b:
            parent[b] = a
        else:
            parent[a] = b
            
for i in range(1, M+1): #i = 1,2,3
    for j in range(N): # j = 0,1,2
        if A[i][j] == 1:
            union(i, j+1)

index = find(B[0])
iscorrect = True
for i in range(1, len(B)):
    if index != find(B[i]):
        iscorrect = False
        break
if iscorrect:
    print('YES')
else:
    print('NO')
        
    
    
    


```