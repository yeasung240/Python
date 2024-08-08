[Finding the number of connection points](https://www.acmicpc.net/problem/11724)


**Problem**

Given an undirected graph, write a program to find the number of connected components.

**Input**


On the first line, the number of vertices, N, and the number of edges, M, are given. (1 ≤ N ≤ 1,000, 0 ≤ M ≤ N×(N-1)/2) In the second line, we are given two endpoints u and v of a trunk line in M lines. (1 ≤ u, v ≤ N, u ≠ v) The same trunk line is given only once.

**The output**
Print the number of connected elements on the first line.

**Example Input 1** 

6 5

1 2

2 5

5 1

3 4

4 6

Example Output 

1 
2 








code

```python


n, m = map(int, input().split())
A = [[] for _ in range(n+1)]
visited = [False] * (n+1)

def dfs(v):
    visited[v] = True
    for i in A[v]:
        if not visited[i]:
            dfs(i)
for _ in range(m):
    s, e = map(int, input().split())
    A[s].append(e) # 양방향 에지이므로 양쪽에 에지를 더하기
    A[e].append(s)
count = 0 
for i in range(1, n+1):
    if not visited[i]:# 연결 노드 중 방문하지 않았던 노드만 탐색
        count +=1
        dfs(i)


```