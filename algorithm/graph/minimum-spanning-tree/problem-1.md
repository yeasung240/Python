
### [Minimum spanning tree](https://www.acmicpc.net/problem/1197)

Difficulty : Gold 5

#### statement


Given a graph, write a program to find the minimum spanning tree of the graph.

A minimum spanning tree is a tree that connects all vertices of a given graph and has the minimum sum of weights among the subgraphs.



#### Input

The first line contains the number of vertices V (1 ≤ V ≤ 10,000) and the number of edges E (1 ≤ E ≤ 100,000). The next E lines contain three integers A, B, and C, which represent information about each edge. This means that vertex A and vertex B are connected by an edge with weight C. C may be negative, and its absolute value does not exceed 1,000,000.

The vertices of the graph are numbered from 1 to V, and there is a path between any two vertices. Only data whose weights of the minimum spanning tree are greater than or equal to -2,147,483,648 and less than or equal to 2,147,483,647 are given as input.

#### Output

The first line prints the weights of the minimum spanning tree


>**IDEA**

The basic example is related to minimum-spanning tree. 


>**How I solve it**

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
