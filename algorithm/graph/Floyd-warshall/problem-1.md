### [Floyd](https://www.acmicpc.net/problem/11404)

Difficulty : Gold 5

#### statement

There are n (2 ≤ n ≤ 100) cities. There are m (1 ≤ m ≤ 100,000) buses that start from one city and arrive at another city. Each bus has a cost for one use.

Write a program to find the minimum cost of traveling from city A to city B for all pairs of cities (A, B).

#### Input
The first line contains the number of cities, n, and the second line contains the number of buses, m. From the third line to the m+2 lines, the following bus information is given. First, the number of the departure city of the bus is given. The bus information consists of the starting city a, the destination city b, and the cost of one ride, c. The starting city and the destination city are never the same. The cost is a natural number less than or equal to 100,000.

There may not be just one route connecting the starting city and the destination city.


#### Output
You need to print n lines. The jth number printed on the ith line is the minimum cost required to go from city i to j. If it is impossible to go from i to j, print 0 in that place.



>**IDEA**

>**How I solve it**

```python
import sys
input = sys.stdin.readline

N = int(input())
M = int(input())

graph = [[sys.maxsize for i in range(N+1)] for j in range(N+1)]
for i in range(1, N+1):
    graph[i][i] = 0

for i in range(M):
    S,E,W = map(int, input().split())
    # There are several values for the W. The smallest values should be written. 
    if graph[S][E] > W:
        graph[S][E] = W

for K in range(1, N+1):
    for S in range(1, N+1):
        for E in range(1, N+1):
            if graph[S][E] > graph[S][K] + graph[K][E]:
                graph[S][E] = graph[S][K] + graph[K][E]
for i in range(1,N+1):
    for j in range(1,N+1):
        if graph[i][j] == sys.maxsize:
            print(0, end = ' ')
        else:
            print(graph[i][j], end = ' ')
    print()
```