### [Finding the path](https://www.acmicpc.net/problem/11403)

Difficulty : silver 5

#### statement
Given an unweighted directed graph G, write a program to determine whether there is a positive path from i to j for all vertices (i, j).


#### Input
The first line contains the number of vertices N (1 ≤ N ≤ 100). The second and subsequent N lines contain the adjacency matrix of the graph. If the jth number of the ith line is 1, it means that there is an edge from i to j, and if it is 0, it means that there is no edge. The ith number of the ith line is always 0.


#### Output

The answer to the problem is printed in the form of an adjacency matrix over a total of N lines. If there is a path with a positive length from vertex i to j, the jth number in the ith line should be printed as 1, otherwise it should be printed as 0.


>**IDEA**

This problem examines if solvers can change Floyd Warshall theory based on the questions. I still did not understand how it works exactly in every details

>**How I solve it**

```python
N = int(input())
distance = [[0 for j in range(N)] for i in range(N)]


for i in range(N):
    distance[i] = list(map(int, input().split()))

# Changed Floyd Warshall
for k in range(N):
    for i in range(N):
        for j in range(N):
            if distance[i][k] == 1 and distance[k][j] == 1:
                distance[i][j] = 1

for i in range(N):
    for j in range(N):
        print(distance[i][j], end=' ')
    print()
```