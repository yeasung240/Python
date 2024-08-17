# What is BFS
Breadth-First-Search

* BFS means Breadth-First-Search and it searches the closest nodes firstly in the graph.
* BFS uses Queue data strucuture.
1. Input start doe on the queue and mark it is visited
2. Popleft the node and input all the cloest nodes that are not visited. After that, mark these are visited
3. Repeat second process until we don't have any data on the queue. 
   

```python

from collections import deque

# BFS 함수 정의
def bfs(graph, start, visited):
    # 큐(Queue) 구현을 위해 deque 라이브러리 사용
    queue = deque([start])
    # 현재 노드를 방문 처리
    visited[start] = True
    # 큐가 빌 때까지 반복
    while queue:
        # 큐에서 하나의 원소를 뽑아 출력
        v = queue.popleft()
        print(v, end=' ')
        # 해당 원소와 연결된, 아직 방문하지 않은 원소들을 큐에 삽입
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

# 각 노드가 연결된 정보를 리스트 자료형으로 표현(2차원 리스트)
graph = [
  [],
  [2, 3, 8],
  [1, 7],
  [1, 4, 5],
  [3, 5],
  [3, 4],
  [7],
  [2, 6, 8],
  [1, 7]
]

# 각 노드가 방문된 정보를 리스트 자료형으로 표현(1차원 리스트)
visited = [False] * 9

# 정의된 BFS 함수 호출
bfs(graph, 1, visited)

```

> BFS and DFS code in a different way. 
> 
```python
from collections import deque
N, M, V = map(int, input().split())
graph = [[] for _ in range(N+1)]
visited1 = [False] * (N+1)
visited2 = [False] * (N+1)

for i in range(M):
    S, E = map(int, input().split())
    graph[S].append(E)
    graph[E].append(S)
for i in graph:
    i.sort()

def DFS(v):
    
    visited1[v] = True
    print(v, end = ' ')
    for i in graph[v]:
        if not visited1[i]:
            DFS(i)
DFS(V) 
print()

def BFS(v):
    
    visited2[v] = True
    queue = deque()
    queue.append(v)
    while queue:
        value = queue.popleft()
        print(value, end = ' ')
        for i in graph[value]:
            if not visited2[i]:
                queue.append(i)
                visited2[i] = True
BFS(V)
  
                       
```
