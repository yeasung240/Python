DFS basic algorithm

```python

def dfs(graph, v, visited):
    visited[v] = True
    print(v, end = ' ')
    # graph 각 인자의 인접 데이트 값 중에서 
    for i in graph[v]:
        
        if not visited[i]:
            dfs(graph, i, visited)    
graph = [
  [],
  [2, 3, 8], # 1번
  [1, 7], # 2번
  [1, 4, 5], # 3번
  [3, 5],
  [3, 4],
  [7],
  [2, 6, 8],
  [1, 7]
]

# 각 노드가 방문된 정보를 리스트 자료형으로 표현(1차원 리스트)
visited = [False] * 9

# 정의된 DFS 함수 호출
dfs(graph, 1, visited)

```

문제 응용

[연결 요소의 개수 구하기](https://www.acmicpc.net/problem/11724)
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
