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

* Make all necessary lists based on -1 and for loop that starts from 1 to N-1. 
* We use math.max function because the total time can be shown more than 1 time from each node. 
* We add up the time of each node at the last point without using weight in graph.


>**How I solve it**

```python
from collections import deque

N = int(input())
A = [[] for _ in range(N + 1)]
indegree = [0] * (N + 1) 
selfBuild = [0] * (N + 1)  

for i in range(1, N + 1):
    inputList = list(map(int, input().split()))
    selfBuild[i] = (inputList[0])  
    index = 1
    while True:  
        preTemp = inputList[index]
        index += 1
        if preTemp == -1:
            break
        A[preTemp].append(i)
        indegree[i] += 1  

queue = deque()
for i in range(1, N + 1):
    if indegree[i] == 0:
        queue.append(i)

result = [0] * (N + 1)
while queue:  # Topological sort
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


