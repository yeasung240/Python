Bubble sort (데이터의 인접 요소끼리 비교하고, swap 연산을 수행하며 정렬하는 방식)


Bublle sort
``` python 

N = int(input())
num = []
for i in range(N):
    num.append(int(input()))
    
for i in reversed(range(0, N)):
    for x in range(0, i):
        if num[x] > num[x+1]:
            temp = num[x+1]
            num[x+1] = num[x]
            num[x] = temp
        else:
            continue
for i in num:
    print(i)

```


Selection sort

```python 
#내림차순

N = list(input())
length = len(N)

for i in range(length):
    max_value = i
    
    for x in range(i+1, length):
        
        if N[max_value] < N[x]:
            max_value = x
        
    temp = N[max_value]
    N[max_value] = N[i]
    N[i] = temp

for i in N:
    print(i, end ='')

#오름차순
N = list(input())
length = len(N)
min_value = 0

for i in range(length):
    min_value = i 
    for x in range(i+1, length):
        if N[min_value] > N[x]:
            min_value = x
    temp = N[min_value]
    N[min_value] = N[i]
    N[i] = temp
    
print(N)

```




insertion sort 

```python
N = int(input())
A = list(map(int, input().split()))
S = [0] * N

for i in range(1, N):
    insert_point = i
    insert_value = A[i]
    
    for j in range(i-1, -1, -1):
        if A[j] < A[i]:
            insert_point = j +1
            break
        if j == 0:
            insert_point = 0
    for j in range(i, insert_point, -1):
        A[j] = A[j-1]
    A[insert_point] = insert_value

print(A)
        

# 합배열
lis = [1,2,3,3,4]
N = len(lis)
Sum = [0] * N 
Sum[0] = lis[0]
multiple = 0

# 합 배열 만들기
for i in range(1, N):
    Sum[i] = Sum[i-1] + A[i]
    
# 합 배열 만든 후 
for i in range(N):
    multiple += Sum[i]
print(multiple)

```


quick sort
```python

array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

def quick_sort(array, start, end):
    if start >= end: # 원소가 1개인 경우 종료
        return
    pivot = start # 피벗은 첫 번째 원소
    left = start + 1
    right = end
    while(left <= right):
        # 피벗보다 큰 데이터를 찾을 때까지 반복 
        while(left <= end and array[left] <= array[pivot]):
            left += 1
        # 피벗보다 작은 데이터를 찾을 때까지 반복
        while(right > start and array[right] >= array[pivot]):
            right -= 1
        if(left > right): # 엇갈렸다면 작은 데이터와 피벗을 교체
            array[right], array[pivot] = array[pivot], array[right]
        else: # 엇갈리지 않았다면 작은 데이터와 큰 데이터를 교체
            array[left], array[right] = array[right], array[left]
    # 분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬 수행
    quick_sort(array, start, right - 1)
    quick_sort(array, right + 1, end)

quick_sort(array, 0, len(array) - 1)
print(array)


```




merge sort
```python

def mergelr(x, y):
    re = []
    i, j = 0, 0
    
    
    while i < len(x) and j < len(y):
         
        if x[i] < y[j]:
            re.append(x[i])
            i += 1
        else:
            re.append(y[j])
            j += 1
        
    if i == len(x):
        while j < len(y):
            re.append(y[j])
            j += 1
    elif j == len(y):
        while i < len(x):
            re.append(x[i])
            i += 1
    return re

    
def mergesort(x):
    if len(x) <= 1:
        return x
    
    # 나누기
    div = (len(x) // 2)
    left = mergesort(x[:div])
    right = mergesort(x[div:])
    
    # 합치기
    x = mergelr(left, right)
    return x

lis = [3,4,5,8,1,7,2,9,6,5]

lis = mergesort(lis)
print(lis)

```

countring sort
```python



n = int(input())
count = [0] * 10001

for i in range(N):
    count[int(input())] += 1

for i in range(10001):
    if count[i] != 0:
        for _ in range(count[i]):
            print(i)

```