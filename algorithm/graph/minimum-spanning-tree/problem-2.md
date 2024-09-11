### [Building a bridge 2]()

Difficulty : Gold 1

#### statement

There is a country made up of islands, and we want to connect all the islands with bridges. The map of this country can be represented as a two-dimensional grid of size N×M, where each square in the grid is either land or sea.

An island is a mass of connected land connected up, down, left, and right. The picture below is a country made up of four islands. The colored squares are land.



Bridges can only be built on the sea, and the length of a bridge is the number of squares the bridge occupies in the grid. We are trying to connect all islands by connecting bridges. When you can go from island A to island B through a bridge, we say that islands A and B are connected. Both ends of the bridge must be on the sea adjacent to the island, and the direction of one bridge cannot change in the middle. Also, the length of the bridge must be at least 2.

Since the direction of the bridge cannot change in the middle, the direction of the bridge can only be horizontal or vertical. A bridge that is horizontal must have both ends of the bridge horizontally adjacent to the island, and a bridge that is vertical must have both ends of the bridge vertically adjacent to the island.

If a bridge connecting islands A and B passes through the sea adjacent to island C in the middle, then island C is not connected to A and B. 

The figure below shows the two correct ways to connect all the islands, with the bridges colored in gray. The islands are identified by integers, and the bridges by capital letters.

	
Total leg length: 13

D is a bridge connecting 2 and 4, and is not connected to 3.

Total leg length: 9 (minimum)

Here are three incorrect methods:

		
C's direction changed in the middle	The length of D is 1.	The horizontal bridge A is not horizontally connected to 1.
There may be cases where the bridges intersect. When calculating the length of the intersecting bridges, each cell must be included in the length of each bridge. Below are two examples of cases where the bridges intersect and other cases.

	
The length of A is 4, and the length of B is also 4.

Total length of the legs: 4 + 4 + 2 = 10

Bridge A: Connects 2 and 3 (length 2)

Bridge B: Connects 3 and 4 (length 3)

Bridge C: Connects 2 and 5 (length 5)

Bridge D: Connects 1 and 2 (length 2)

Total length: 12

Given the information about a country, let's find the minimum length of bridges connecting all islands.

#### Input
The first line contains the vertical size N and horizontal size M of the map. The second line and subsequent N lines contain information about the map. Each line consists of M numbers, which are 0 or 1. 0 means sea, and 1 means land.


#### Output

Print the minimum bridge length connecting all islands. If it is impossible to connect all islands, print -1.


>**IDEA**

Do BFS searching to find islands and do minimum-spanning tree calcaulation. 

>**How I solve it**

```python
import copy
import sys
from collections import deque
from queue import PriorityQueue
input = sys.stdin.readline

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

N, M = map(int, input().split())
myMap = [[0 for j in range(M)] for i in range(N)]
visited = [[False for j in range(M)] for i in range(N)]

for i in range(N):
    myMap[i] = list(map(int, input().split()))

sNum = 1
sumlist = list([])
mlist = []

def addNode(i, j, queue):
    myMap[i][j] = sNum
    visited[i][j] = True
    temp = [i, j]
    mlist.append(temp)
    queue.append(temp)

def BFS(i, j):
    queue = deque()
    mlist.clear()
    start = [i, j]
    queue.append(start)
    mlist.append(start)
    visited[i][j] = True
    myMap[i][j] = sNum
    while queue:
        r, c = queue.popleft()
        for d in range(4):
            tempR = dr[d]
            tempC = dc[d]
            while r + tempR >= 0 and r + tempR < N and c + tempC >= 0 and c + tempC < M:
                if not visited[r + tempR][c + tempC] and myMap[r + tempR][c + tempC] != 0:
                    addNode(r + tempR, c + tempC, queue);
                else:
                    break;
                if tempR < 0:
                    tempR -= 1
                elif tempR > 0:
                    tempR += 1
                elif tempC < 0:
                    tempC -= 1
                elif tempC > 0:
                    tempC += 1
    return mlist

for i in range(N):
    for j in range(M):
        if myMap[i][j] != 0 and not visited[i][j]:
            tempList = copy.deepcopy(BFS(i, j))  # 깊은 복사로 해주어야 주소를 공유하지 않음
            sNum += 1
            sumlist.append(tempList)

pq = PriorityQueue()
for now in sumlist:
    for temp in now:
        r = temp[0]
        c = temp[1]
        now_S = myMap[r][c]
        for d in range(4):
            tempR = dr[d]
            tempC = dc[d]
            blenght = 0
            while r + tempR >= 0 and r + tempR < N and c + tempC >= 0 and c + tempC < M:
                if myMap[r + tempR][c + tempC] == now_S:  # 같은 섬이면 에지를 만들 수 없음
                    break
                elif myMap[r + tempR][c + tempC] != 0:  # 같은 섬도 아니고 바다도 아니면
                    if blenght > 1:  # 다른 섬 → 길이가 1 이상일 때 에지로 더하기
                        pq.put((blenght, now_S, myMap[r + tempR][c + tempC]))
                    break
                else:  # 바다이면 다리의 길이 연장
                    blenght += 1
                if tempR < 0:
                    tempR -= 1
                elif tempR > 0:
                    tempR += 1
                elif tempC < 0:
                    tempC -= 1
                elif tempC > 0:
                    tempC += 1


def find(a):
    if a == parent[a]:
        return a
    else:
        parent[a] = find(parent[a])
        return parent[a]


def union(a, b):
    a = find(a)
    b = find(b)
    if a != b:
        parent[b] = a


parent = [0] * sNum
for i in range(len(parent)):
    parent[i] = i

useEdge = 0
result = 0
while pq.qsize() > 0:
    v, s, e = pq.get()
    if find(s) != find(e):
        union(s, e)
        result += v
        useEdge += 1

if useEdge == sNum - 2:
    print(result)
else:
    print(-1)
```
