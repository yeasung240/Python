### [Oh Min-sik's worries](https://www.acmicpc.net/problem/1219)

Difficulty : Platinum 5

#### statement

Oh Min-sik is a salesman. Oh Min-sik's company president told him to sell as many items as possible to maximize his profit.

Oh Min-sik was troubled.

How can I maximize my profits?

There are N cities in this country. The cities are numbered from 0 to N-1. Oh Min-sik's journey begins in city A and ends in city B.

There are several modes of transportation that Oh Min-sik can use. Oh Min-sik knows the departure and arrival cities of all modes of transportation, and also knows the cost. In addition, Oh Min-sik knows the amount of money he can earn each time he visits each city. This amount is different for each city, and the amount is fixed. In addition, he earns that amount each time he visits a city.

When Min-sik Oh arrives at his destination city, he wants to maximize the amount of money he has. Write a program to find this maximum.

If O Min-sik spends more money than he earns, the amount of money he has when he arrives at the destination city may be negative. Also, he can visit the same city multiple times, and he earns money each time he visits the city. All transportation methods can only be used in the direction given as input, and can be used multiple times.

#### Input

The first line contains the number of cities N, the starting city, the destination city, and the number of transportation means M. The second line and the M lines contain information on transportation means. The information on transportation means is in the format of “starting and ending prices.” The last line contains the maximum amount of money that Oh Min-sik can earn in each city, starting from city 0.

N and M are non-negative integers less than or equal to 50, and the maximum value of money and the price of transportation are non-negative integers less than or equal to 1,000,000.

#### Output

In the first line, print the maximum amount of money that Oh Min-sik has when he arrives at the destination city. If it is impossible for Oh Min-sik to arrive at the destination city, print "gg". And, if Oh Min-sik can have infinite money when he arrives at the destination city, print "Gee".


>**IDEA**

>**How I solve it**

```python
# First try
mport sys
input = sys.stdin.readline
maxe = sys.maxsize
N, depart, arrive, M = map(int, input().split())
graph = [] 
distance = [-maxe] * (N)


for _ in range(M):
    S,E,W = map(int, input().split())
    graph.append((S,E,W))
money = list(map(int, input().split()))

distance[0] = 0 
distance[0] = money[0]

for x in range(N-1):  
    for S,E,W in graph:
        
        if distance[S] != maxe and distance[E] < (distance[S] - W + money[E]):
            distance[E] = distance[S] - W + money[E]
            
checker = False
for S,E,W in graph:
        if distance[S] != maxe and distance[E] < (distance[S] - W + money[E]):
            distance[E] = distance[S] - W + money[E]
            checker = True
            
            
if distance[arrive] == -maxe:
    print('gg')
    
elif checker == False and distance[arrive] != -maxe:
    print(distance[arrive])

elif checker == True and distance[arrive] != (-maxe):
    print('Gee')
```

```python
# Answer
mport sys
input = sys.stdin.readline
N, sCity, eCity, M = map(int, input().split())
edges= []
distance = [-sys.maxsize] * N  # 최단거리 배열 초기화

for _ in range(M):
    start, end, price = map(int, input().split())
    edges.append((start, end, price))

cityMoney = list(map(int, input().split()))

# 변형된 벨만포드 수행
distance[sCity] = cityMoney[sCity]  # 출발 초기화
# 양수 사이클이 전파 되도록 충분히 큰 수로 반복
for i in range(N+101):
    for start, end, price in edges:
        if distance[start] == -sys.maxsize:
            continue
        elif distance[start] == sys.maxsize:
            distance[end] = sys.maxsize
        elif distance[end] < distance[start] + cityMoney[end] - price:
            distance[end] = distance[start] + cityMoney[end] - price
            if i >= N-1:
                distance[end] = sys.maxsize

if distance[eCity] == -sys.maxsize:
    print("gg")
elif distance[eCity] == sys.maxsize:
    print("Gee")
else:
    print(distance[eCity])

```