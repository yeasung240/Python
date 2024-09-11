### [tree ](https://www.acmicpc.net/problem/1068)

Difficulty : Gold 5

#### statement
In a tree, a leaf node is a node that has 0 children.

Given a tree, one node will be deleted. Write a program to find the number of leaf nodes in the remaining tree. When a node is deleted, that node and all of its descendants are removed from the tree.






#### Input

The first line contains the number of nodes in the tree, N. N is a natural number less than or equal to 50. The second line contains the parent of each node from node 0 to node N-1. If there is no parent, -1 (root) is given. The third line contains the number of the node to be deleted.

#### Output

In the first line, output the number of leaf nodes when the node given as input is deleted from the tree given as input.


>**IDEA**

* First make adjacency list to excute DFS from the input data
* The logic is to add up the number of child nodes until it meets the end node.
* Reset cNode when the recursion occurs again. 

>**How I solve it**

```python
# 재귀 함수를 위해 충분히 큰수로 한계 값 설정

N = int(input())
visited = [False] * (N)
tree = [[] for _ in range(N)]
answer = 0
p = list(map(int, input().split()))
for i in range(N):
    if p[i] != -1:
        tree[i].append(p[i])
        tree[p[i]].append(i)
    else:
        root = i


# DFS 탐색 함수
def DFS(number):
    global answer
    visited[number] = True
    cNode = 0
    for i in tree[number]:
        if not visited[i] and i != eleteNode:  
            # 삭제 노드가 아닐 때도 탐색 중지
            cNode += 1
            DFS(i)
    if cNode == 0:
        answer += 1  # 자식 노드가 0개이면 리프노드이므로 정답 값 층가


deleteNode = int(input())
if deleteNode == root:
    print(0)
else:
    DFS(root)
```
