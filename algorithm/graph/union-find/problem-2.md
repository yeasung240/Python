### [Let's go on a trip](https://www.acmicpc.net/problem/1976)

Difficulty : Gold 5

#### statement

Donghyuk is going to travel with his friends. There are N cities in Korea, and there may or may not be a road between any two cities. Given Donghyuk's travel itinerary, let's see if this travel route is possible. Of course, he can travel by passing through other cities in the middle. For example, if there are 5 cities, and the roads are AB, BC, AD, BD, and EA, and Donghyuk's travel plan is ECBCD, he can achieve his goal through a travel route called EABCBCBD.

Given the number of cities and whether the cities are connected, and the order of the cities in Dong-hyeok's travel plan, write a program to determine whether it is possible. It is also possible to visit the same city multiple times.

#### Input
The first line contains the number of cities N. N must be less than or equal to 200. The second line contains the number of cities M in the travel plan. M must be less than or equal to 1000. The next N lines contain N integers. The jth number in the ith line indicates the connection information between the ith city and the jth city. 1 means connected, and 0 means not connected. If A and B are connected, then B and A are also connected. The last line contains the travel plan. The cities are numbered sequentially from 1 to N.


#### Output
On the first line, print YES if possible, NO if not possible.



>**IDEA**

* Making comprehension list that expressing the information about connection point between cities. 
* Use union Find to clearfiy the problem
* Make a Index variable that expressing the first value of the parent list tha has through Find function and compare the vlaue with the rest.
  <br> if the value is equal, then output the Yes else, output the No

>**How I solve it**

```python
N = int(input())
M = int(input())
dosi = [[0 for j in range(N+1)] for i in range(N+1)]

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

for i in range(1, N+1):
    dosi[i] = list(map(int, input().split()))
    dosi[i].insert(0, 0)

route = list(map(int, input().split()))
route.insert(0, 0)

parent = [0]*(N+1)
for i in range(1, N+1):
    parent[i] = i

for i in range(1, N+1):
    for j in range(1, N+1):
        if dosi[i][j] == 1:
            union(i,j)

index = find(route[1])
isConnect = True
for i in range(2, len(route)):
    if index != find(route[i]):
        isConnect = False
        break

if isConnect:
    print("YES")
else:
    print("NO")

```

