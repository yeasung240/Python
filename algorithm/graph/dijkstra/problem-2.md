### [Shortest path](https://www.acmicpc.net/problem/1753)

Difficulty : Gold 5

#### statement

Given a directed graph, write a program that finds the shortest path from a given starting point to all other vertices. All edges have weights less than or equal to 10.

#### Input

The first line contains the number of vertices V and the number of edges E (1 ≤ V ≤ 20,000, 1 ≤ E ≤ 300,000). Assume that all vertices are numbered from 1 to V. The second line contains the number of the starting vertex K (1 ≤ K ≤ V). From the third line onwards, three integers (u, v, w) representing each edge are given in order over E lines. This means that there is an edge with weight w going from u to v. u and v are different and w is a natural number less than or equal to 10. Note that there may be multiple edges between two different vertices.

#### Output
From the first line, across V lines, print the path value of the shortest path to the i-th vertex on the i-th line. The starting point itself should be printed as 0, and if the path does not exist, print INF.



>**IDEA**

>**How I solve it**

```python
import sys
input = sys.stdin.readline
from queue import PriorityQueue

V, E = map(int, input().split())
K = int(input())
distance = [sys.maxsize] * (V + 1)
visited = [False] * (V + 1)
myList = [[] for _ in range(V + 1)]
q = PriorityQueue()

for _ in range(E):
    u, v, w = map(int, input().split()) 
    myList[u].append((v, w))

q.put((0, K))  # Priority criteria is the length of the time 
distance[K] = 0
while q.qsize() > 0:
    current = q.get()
    c_v = current[1]
    if visited[c_v]:
        continue
    visited[c_v] = True
    for tmp in myList[c_v]:
        next = tmp[0]
        value = tmp[1]
        if distance[next] > distance[c_v] + value:  # Update min value
            distance[next] = distance[c_v] + value
            q.put((distance[next], next))
for i in range(1, V + 1):
    if visited[i]:
        print(distance[i])
    else:
        print("INF")

```