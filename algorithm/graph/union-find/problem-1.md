### [The expression of sets](https://www.acmicpc.net/problem/1717)

Difficulty : Gold 4

#### statement
In the beginning
$n+1$A collection of dogs
$\{0\}, \{1\}, \{2\}, \dots , \{n\}$Here we have a union operation and an operation to check if two elements are in the same set.

Write a program to represent a set.


#### Input

In the first line
$n$,
$m$This is given.
$m$is the number of operations given as input. Next
$m$Each line of the dog is given an operation. The union is
$0$ 
$a$ 
$b$The input is given in the form of
$a$A set that contains,
$b$It means merging sets that contain . The operation to check whether two elements are included in the same set is
$1$ 
$a$ 
$b$The input is given in the form of
$a$and
$b$It is an operation to check whether something is included in the same set.
#### Output

For inputs starting with 1
$a$and
$b$If it is included in the same set, print " YES" or " yes", otherwise print " NO" or " ", one per line.no


>**IDEA**

Union Find concept. 

>**How I solve it**

```python
# union find
import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)
N, M = map(int, input().split())
parent = [0] * (N + 1)


def find(a):
    if a == parent[a]:
        return a
    else:
        parent[a] = find(parent[a])  # Recursive function form -> compress the paths.
        return parent[a]


def union(a, b):
    a = find(a)
    b = find(b)
    if a != b:
        parent[b] = a


def checkSame(a, b):
    a = find(a)
    b = find(b)
    if a == b:
        return True
    return False


for i in range(0, N + 1):
    parent[i] = i

for i in range(M):
    question, a, b = map(int, input().split())
    if question == 0:
        union(a, b)
    else:
        if checkSame(a, b):
            print("YES")
        else:
            print("NO")


```

