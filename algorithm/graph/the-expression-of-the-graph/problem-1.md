### [found a city on a specific street](https://www.acmicpc.net/problem/18352)

Difficulty : Silver 2 

#### statement

In a country there are cities numbered  1 to N and M one-way roads. The distance of all roads is 1.

Write a program that outputs the numbers of all cities that can be reached from a specific city X , and whose shortest distance is exactly K. Also , assume that the shortest distance from the starting city X to the starting city X is always 0.

For example, let's assume that the graph is structured as follows when N = 4, K = 2, and X = 1.

#### Input

The first line contains  the number of cities N , the number of roads M , distance information K , and the starting city X. (2 ≤ N  ≤ 300,000, 1 ≤  M  ≤ 1,000,000, 1 ≤  K  ≤ 300,000, 1 ≤  X  ≤  N ) From the second line, two natural numbers A and B are given, separated by a space, over M lines. This means that there is a one-way road  from city A to city B. (1 ≤ A , B  ≤  N ) However, A and B are different natural numbers.

#### Output
Starting from X , print the numbers of all cities that can be reached by the shortest distance K , one per line, in ascending order.

If there is no city among the cities reachable at this time whose shortest distance is K , output -1.



>**IDEA**

Use BFS. Firstly search all the connected values from the start. As we search, we add the number(starts from 1) to the visited list. When the value of K and the value of visited value, return the index value 


>**How I solve it**

```python

import sys
from collections import deque
input = sys.stdin.readline

N, M, K, X = map(int, input().split())  
A = [[] for _ in range(N + 1)]
answer = []
visited = [-1] * (N + 1)

def BFS(v):  # BFS search
    queue = deque()
    queue.append(v)
    visited[v] += 1
    while queue:
        now_Node = queue.popleft()
        for i in A[now_Node]:
            if visited[i] == -1:
                visited[i] = visited[now_Node] + 1
                queue.append(i)

for _ in range(M):
    S, E = map(int, input().split())
    A[S].append(E)

BFS(X)

for i in range(N + 1):
    if visited[i] == K:
        answer.append(i)
if not answer:
    print(-1)
else:
    answer.sort()
    for i in answer:
        print(i)
```