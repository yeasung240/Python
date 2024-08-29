### [Tree traversal](https://www.acmicpc.net/problem/1991)

Difficulty : 

#### statement
Write a program that inputs a binary tree and outputs the results of preorder traversal, inorder traversal, and postorder traversal.


#### Input
The first line contains the number of nodes in the binary tree, N (1 ≤ N ≤ 26). Each node and its left child node and right child node are given in N lines starting from the second line. The names of the nodes are given in alphabetical order starting from A, with A always being the root node. If there are no child nodes, they are represented by a .


#### Output
Print the results of preorder traversal on the first line, inorder traversal on the second line, and postorder traversal on the third line. Print N alphabets on each line without spaces.



>**IDEA**

Use recursion concept. 
<br> Important to understand when the value is printed with the location of 'return'


>**How I solve it**

```python
N = int(input())
tree = {}

for _ in range(N):
    root, left, right = input().split()
    # tree[root] = key, [left, right] = value
    tree[root] = [left, right]

def preorder(value):
    if value == '.':
        return
    print(value, end = '')
    preorder(tree[value][0])
    preorder(tree[value][1])

def middleorder(value):
    if value == '.':
        return
    middleorder(tree[value][0])
    # Not skip to C right away, go through Print function.
    print(value, end = '')
    middleorder(tree[value][1])

def afterorder(value):
    if value == '.':
        return
    afterorder(tree[value][0])
    afterorder(tree[value][1])
    print(value, end = '')



preorder('A')
print()
middleorder('A')
print()
afterorder('A')
```