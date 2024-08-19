# Union Find

Union Find algorithm consists of Union function and Find function.

>**Union function**

Normally, it receives two values for the function. It decides which one is representing node. 
<br> A more bigger value is the index of representing node in the list and a more smaller one is value. For example, there is the list called lis and a = 1, b = 3 are given. After union function, the list is described as lis[b] = a

Basically, Union function is to compare values and to set the representing values based on the order. 

>**Find function**

 Find function is the most important part in the Union find algorithm. 
 <br> There are steps in the union function
 1. Check if the value in the list equals the index of the value in the list.

    1-1. if value = index, return the value

    1-2. if value != index, it is going back to the index that had different index as the value given.
    <br> It ultimatley finds the index is the same as the value of the index in the list. 
    <br> For example
```python
    def find(v):
        if v == list[v]:
            return v:
        else:
            list[v] = find[list[v]]
            return list[v]
    # in this recursive function, function is like stack and  when recursive function is called, it goes back to previous function with the value of current function.  
```
>**[Best example to understand Union find easily]()**


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
        parent[a] = find(parent[a])  # Recursive function form -> compress the paths.
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
