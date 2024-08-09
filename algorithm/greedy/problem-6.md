### [Meeting Room Allocation](https://www.acmicpc.net/problem/1931#)

Difficulty : Silver 1

#### statement
There is one meeting room available, and there are 
$N$ meetings that want to use it. For each meeting, a start time and an end time are given. The goal is to find the maximum number of meetings that can use the meeting room without any overlap. Once a meeting starts, it cannot be interrupted, and a new meeting can start immediately after the previous one ends. Note that the start and end times of a meeting can be the same, which means the meeting starts and ends instantly.


#### Input

The first line provides the number of meetings 
$N$ (
$1 \le N \le 100\,000$). From the second line to the 
$N+1$-th line, the information of each meeting is given, separated by a space, indicating the start and end times of the meetings. The start and end times are natural numbers or 0, less than or equal to 
$2^{31}-1$.

#### Output
Print the maximum number of meetings that can be held in the first line.
  


>### Idea
The idea to solve this question to find the earliest meeting ending time.-> related to greedy. Sort the data based on that.


>**How I solve it**

```python

N = int(input())
A = [[0] * 2 for _ in range(N)]
for i in range(N):
    S, E = map(int, input().split())
    A[i][0] = E  # 종료시간 우선 정렬이 우선이기 때문에 0번째에 종료시간을 먼저 저장.
    A[i][1] = S

A.sort()
count = 0
end = -1
for i in range(N):
    if A[i][1] >= end:  # 겹치지 않는 다음 회의가 나온 경우
        end = A[i][0]  # 종료 시간 업데이트
        count += 1
print(count)
```


>**First try**

```python
N = 11
lis = [[1,4],[3,5],[0,6],[5,7],[3,8],[5,9],[6,10],[8,11],[8,12],[2,13],[12,14]]
compare = 0


for i in range(N):
    if (N-lis[i][1]) > compare: 
        compare = (N-lis[i][1])
a = N-compare

compare = 0 
for i in range(N):
    if lis[i][0] > a:
        if (N-lis[i][1]) > compare: 
            compare = (N-lis[i][1])
a = N-compare  

compare = 0 
for i in range(N):
    if lis[i][0] > a:
        if (N-lis[i][1]) > compare: 
            compare = (N-lis[i][1])
a = N-compare  

print(a)

compare = 0 
for i in range(N):
    if lis[i][0] > a:
        if (N-lis[i][1]) > compare: 
            compare = (N-lis[i][1])
a = N-compare  
print(a)

```


