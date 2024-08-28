[Minimum spanning tree](https://www.acmicpc.net/problem/1197)
17472, 1414
```python
# 1197 

from queue import PriorityQueue
V, E = map(int, input().split())
edges = PriorityQueue()
parent = [i for i in range(0, V+1)]

for _ in range(E):
    s,e,w = map(int, input().split())
    # PriorityQueue sorting based on the first number
    edges.put((w,s,e))

SUM = 0
Repeat = 0

def union(a,b):
    a = find(a)
    b = find(b)
    # If a == b, there is nothing to do. 
    if a != b:
        if a > b:
            parent[a] = b
        elif a < b:
            parent[b] = a
    
def find(c):
    if c == parent[c]:
        return c
    else:
        parent[c] = find(parent[c])
        return parent[c]
        
while SUM < (V-1):

    w,s,e = edges.get() # output like input 
    if find(s) != find(e):
        union(s,e)
        SUM += 1
        Repeat += w


print(Repeat)
```
