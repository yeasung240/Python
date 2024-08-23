### [Line up](https://www.acmicpc.net/problem/2252)

Difficulty : Gold 3 

#### statement
 I want to line up N students in order of height. It would be easy to measure each student's height and then arrange them, but since there is no good way, I decided to use a method of comparing the heights of two students. Even then, I did not compare all the students, but only some of them.

Given the results of comparing the heights of some students, write a program to line them up.


#### Input

The first line contains N (1 ≤ N ≤ 32,000) and M (1 ≤ M ≤ 100,000). M is the number of times the keys were compared. The next M lines contain the numbers A and B of the two students whose keys were compared. This means that student A must stand in front of student B.

Students' numbers are from 1 to N.

#### Output

The first line prints the result of lining up the students from the front. If there are multiple answers, print any one of them.


>**IDEA**

Use the deque and store data like stack when we do topological sorrting

>**How I solve it**

**First try**
```python

N, M = map(int, input().split())
lis = [[] for _ in range(N+1)]
answer = [0] * (N+1)
array = []

for i in range(M):
    A, B = map(int, input().split())
    lis[A].append(B)
for i in lis:
    if i:
        for j in i:
            answer[j] += 1

# answer = [0, 1, 1, 0, 0]
# lis = [[],[],[],[1],[2]]
while answer != ([0]* (N+1)):
    for i in range(1, len(answer)):
        if answer[i] == 0 and not answer[i] in array:
            array.append(i)
    for j in array:
        for x in lis[j]:
            answer[x] -= 1
            if answer[x] == 0:
                array.append(x)
            
    
for i in array:
    print(i, end = ' ')
```
**answer**

```python

# 2252 topological sorting
from collections import deque

N, M = map(int, input().split())
graph = [[] for i in range(N+1)]
degree = [0] * (N+1)

for i in range(M):
    A, B = map(int, input().split())
    graph[A].append(B)
    degree[B] += 1 

queue = deque()

for i in range(1, N+1):
    if degree[i] == 0:
        queue.append(i)
while queue:
    value = queue.popleft()
    print(value, end = ' ')
    
    for i in graph[value]:
        degree[i] -= 1
        if degree[i] == 0:
            queue.append(i)
# In the output case 2, the output from the code is 3,4,1,2.
# even though we have different values from the case 2, it is okay
# because in topological sorting, there are not unique answers. 
```
