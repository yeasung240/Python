### [Time machine](https://www.acmicpc.net/problem/11657)

Difficulty : Gold 5

#### statement
There are N cities. And there are M buses that start from one city and arrive at another city. Each bus can be represented as A, B, and C, where A is the starting city, B is the destination city, and C is the time it takes to travel by bus. There are cases where the time C is not positive. When C = 0, it is a case of teleportation, and when C < 0, it is a case of going back in time with a time machine.

Write a program to find the fastest time to travel from city 1 to the remaining cities.


#### Input
The first line contains the number of cities N (1 ≤ N ≤ 500) and the number of bus routes M (1 ≤ M ≤ 6,000). The second and subsequent M lines contain information about bus routes A, B, C (1 ≤ A, B ≤ N, -10,000 ≤ C ≤ 10,000). 


#### Output

If it is possible to go back in time infinitely from city 1 to any city, print -1 on the first line. Otherwise, print the fastest times to go from city 1 to city 2, city 3, ..., city N in order, over N-1 lines. If there is no route to that city, print -1 instead.


>**IDEA**

The basic question about Belman Ford algoritm. 
>**How I solve it**

```python
import sys
input = sys.stdin.readline
N, M = map(int, input().split())
edges = []
distance = [sys.maxsize]*(N+1)
for i in range(M):  # 에지 데이터 저장
    start, end, time = map(int, input().split())
    edges.append((start, end, time))

# 벨만포드 수행
distance[1] = 0
for _ in range(N-1):
    for start, end, time in edges:
        if distance[start] != sys.maxsize and distance[end] > distance[start] + time:
            distance[end] = distance[start] + time

# 음수 사이클 확인
mCycle = False
for start, end, time in edges:
    if distance[start] != sys.maxsize and distance[end] > distance[start] + time:
        mCycle = True

if not mCycle:
    for i in range(2, N+1):
        if distance[i] != sys.maxsize:
            print(distance[i])
        else:
            print(-1)
else:
    print(-1)

```