### [Bipartite graph](https://www.acmicpc.net/problem/1707)

Difficulty : Gold 5

#### statement

When the set of vertices of a graph can be divided into two such that the vertices in each set are not adjacent to each other, such a graph is specifically called a bipartite graph.

Given a graph as input, write a program to determine whether the graph is a bipartite graph or not.


#### Input
The input consists of several test cases, and the number of test cases K is given on the first line. The first line of each test case contains the number of vertices V and the number of edges E of the graph, separated by a blank space. Each vertex is numbered from 1 to V. Then, information about the edges is given on the second and subsequent E lines, and each line contains the numbers u and v (u ≠ v) of two adjacent vertices, separated by a blank space.


#### Output
If the graph given as input is a bipartite graph across K lines, print YES, otherwise print NO in that order.



>**IDEA**
1. The definition of bipartite graph<br>seperating the graph with two clusters like A, B, A not like A, B, A, A (joint parts should be different.)

2. When the node has the same value between 1 and 2 with the nodes that we visited, we print out the False.

>**How I solve it**

```python

# 1707
# answer
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
N = int(input())
IsEven = True

def DFS(node):
    global IsEven
    visited[node] = True
    for i in A[node]:
        if not visited[i]:
            check[i] = (check[node]+1)%2
            # when the node(previous) is 0 then, check is 1
            # when the node(previous) is 1 then, check is 0
            # by using this property, we type 0,1 in the check list
            DFS(i)
        elif check[node] == check[i]:
            IsEven = False


for _ in range(N):
    V, E = map(int, input().split())
    A = [[] for _ in range(V + 1)]
    visited = [False] * (V + 1)
    check = [0] * (V + 1)
    IsEven = True

    for i in range(E):
        Start, End = map(int, input().split())
        A[Start].append(End)
        A[End].append(Start)

    for i in range(1, V + 1):
        if IsEven:
            DFS(i)
        else:
            break

    check[1] = 0
    if IsEven:
        print("YES")
    else:
        print("NO")

```