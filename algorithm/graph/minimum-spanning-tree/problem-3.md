### [in helping the underprivileged](https://www.acmicpc.net/problem/1414)

Difficulty : Gold 3

#### statement

Dasom thought about what she could do to help the underprivileged. She realized that she had a lot of LAN cables at home. Dasom, who felt that she didn't need that many LAN cables, decided to use them to volunteer in the community.

Dasom's house has N rooms. Each room has one computer. Each computer is connected with a LAN cable. When there are two computers, A and B, if A and B are connected with a LAN cable or connected through another computer, they can communicate with each other.

Dasom wants to connect all N computers in her house to each other.

Given the length of the LAN cable connecting N computers, write a program that outputs the maximum length of the LAN cable that Dasom can donate.

#### Input

The number of computers N is given in the first line. The length of the LAN cable is given from the second line. If the jth character of the ith line is 0, it means that there is no LAN cable connecting computer i and computer j. Otherwise, it means the length of the LAN cable. The length of the LAN cable is 1 to 26 for a to z, and 27 to 52 for A to Z. N is a natural number less than or equal to 50.



#### Output

In the first line, print the maximum length of the LAN cable that Dasom can donate. If not all computers are connected, print -1.


>**IDEA**


The whole goal of the problem is to minimize the amout of strings among full amout. <br>
The hardest part is changing adjacency graph to edge grap to use the algoritm. For alpabets, we use ord() function. 

>**How I solve it**

```python

import sys
from queue import PriorityQueue

N = int(input())
pq = PriorityQueue()
sum = 0
parent = [i for i in range(N)]
all = 0 

# Changing adjacency graph to edge graph(PriorityQueue)
for i in range(N):
    lis = list(input())
    for j in range(N):
        value = 0
        
        if 'a' <= lis[j] <= 'z':
            value = ord(lis[j])-96
        
        elif 'A' <= lis[j] <= 'Z':
            value = ord(lis[j])-38
            
        all += value
        if i != j and value != 0:
            pq.put((value, i, j))

def union(a,b):
    a = find(a)
    b = find(b)
    if a != b:
        if a > b:
            parent[a] = b
        elif a < b:
            parent[b] = a
        
def find(c):
    if c == parent[c]:
        return c
    else:
        parent[c] = find(parent[c])
        return parent[c]
        
sume = 0
answer = 0
while pq.qsize() > 0:
    value, i, j = pq.get()
    if find(i) != find(j):
        union(i,j)
        answer += value
        sume += 1

if sume == N-1:
    print(all - answer)
else:
    print(-1)
```
