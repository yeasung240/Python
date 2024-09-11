### [Tree](https://www.acmicpc.net/problem/11725)

Difficulty : Silver 3

#### statement
Given a rootless tree, write a program to find the parent of each node when the root of the tree is set to 1.


#### Input
The first line contains the number of nodes N (2 ≤ N ≤ 100,000). From the second line, N-1 lines contain two vertices connected in the tree.


#### Output
Starting from the first line, print the parent node number of each node in order from node 2 on N-1 lines.



>**IDEA**

* first node is parents' node 
* Use DFS to find the parents'node

>**How I solve it**

```python
import sys
# Restrict the number of recursion times. 
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N = int(input())
visited = [False]*(N+1)
tree = [[] for _ in range(N+1)]
answer = [0]*(N+1)
for _ in range(1, N):
    n1, n2 = map(int, input().split())
    tree[n1].append(n2)
    tree[n2].append(n1)

# Excuting the DFS. 
def DFS(number):
    visited[number] = True
    for i in tree[number]:
        if not visited[i]:
            answer[i] = number 
            DFS(i)

DFS(1)  
for i in range(2, N+1):
    print(answer[i])
```
