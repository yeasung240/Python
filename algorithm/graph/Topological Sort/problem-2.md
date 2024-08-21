### [Game Development](https://www.acmicpc.net/problem/1516)

Difficulty : Gold 3 

#### statement
The company decided to develop a new strategy simulation game called Sejun Craft. The core parts have been developed, and the only things left are the balance between races and the overall game time.

Since the time taken to play the game can vary depending on the situation, we decided to approximate it using the minimum time it takes to build all the buildings. Of course, the problem may not be simple because you may need to build other buildings first in order to build some buildings. For example, in Starcraft, you need to build a barracks first to build a bunker, so you need to build a barracks first and then a bunker. You can build multiple buildings at the same time.

For convenience, let's assume that we have infinite resources and that it takes no time to issue a command to build a building.


#### Input
The first line contains the number of building types N (1 ≤ N ≤ 500). The next N lines contain the time it takes to build each building and the numbers of buildings that must be built before building that building. Let the building numbers be from 1 to N, and let each line end with -1. The time it takes to build each building is a natural number less than or equal to 100,000. Only inputs that allow all buildings to be built are given.


#### Output
Print the minimum time it takes for each of N buildings to be completed.



>**IDEA**

Based on -1, make the list. 


>**How I solve it**

```python
from collections import deque

N = int(input())
A = [[] for _ in range(N + 1)]
indegree = [0] * (N + 1)  # 진입차수 리스트
selfBuild = [0] * (N + 1)  # 자기자신을 짓는데 걸리는 시간

for i in range(1, N + 1):
    inputList = list(map(int, input().split()))
    selfBuild[i] = (inputList[0])  # 건물을 짓는데 걸리는 시간
    index = 1
    while True:  # 인접리스트 만들기
        preTemp = inputList[index]
        index += 1
        if preTemp == -1:
            break
        A[preTemp].append(i)
        indegree[i] += 1  # 진입차수 데이터 저장

queue = deque()
for i in range(1, N + 1):
    if indegree[i] == 0:
        queue.append(i)

result = [0] * (N + 1)
while queue:  # 위상정렬 수행
    now = queue.popleft()
    for next in A[now]:
        indegree[next] -= 1
        result[next] = max(result[next], result[now] + selfBuild[now]) 
        # the reason using max = because duplicated value like 1-4, 1-3-4. We chose the biggest value
        if indegree[next] == 0:
            queue.append(next)

for i in range(1, N + 1):
    print(result[i] + selfBuild[i])

```


