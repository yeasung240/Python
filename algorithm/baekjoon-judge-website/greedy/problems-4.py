# 1744 (Gold 4)

# Try
import heapq

lis = []
answer = []

N = int(input())
for i in range(N):
    lis.append(int(input()))
heapq.heapify(lis)

while len(lis) > 3:
    mini_1 = heapq.heappop(lis)
    mini_2 = heapq.heappop(lis)
    
    
    if (mini_1 * mini_2) > (mini_1 + mini_2):
        answer.append(mini_1 * mini_2)
    else:
        answer.append(mini_1 + mini_2)
    
if len(lis) == 3:
    mini_1 = heapq.heappop(lis)
    answer.append(mini_1)
    mini_2 =  heapq.heappop(lis)
    mini_3 =  heapq.heappop(lis)
    if (mini_2 * mini_3) > (mini_2 + mini_3):
        answer.append(mini_2 * mini_3)
    else:
        answer.append(mini_2 + mini_3)
    
print(sum(answer+lis))



# solution

from queue import PriorityQueue
N = int(input())
plusPq = PriorityQueue()
mlusPq = PriorityQueue()
one = 0
zero = 0
for i in range(N):  # 4가지로 데이터 분리 저장
    data = int(input())
    if data > 1:
        plusPq.put(data * -1)   # 양수 내림차순 정렬을 위해 -1을 곱하여 저장
    elif data == 1:
        one += 1
    elif data == 0:
        zero += 1
    else:
        mlusPq.put(data)
sum = 0
while plusPq.qsize() > 1:   # 양수 처리
    first = plusPq.get() * -1
    second = plusPq.get() * -1
    sum += first * second
if plusPq.qsize() > 0:
    sum += plusPq.get() * -1

while mlusPq.qsize() > 1:   # 음수 처리
    first = mlusPq.get()
    second = mlusPq.get()
    sum += first * second
if mlusPq.qsize() > 0:
    if zero == 0:
        sum += mlusPq.get()
sum += one  # 1 처리
print(sum)