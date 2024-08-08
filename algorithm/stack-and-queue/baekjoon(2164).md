[Problem](https://www.acmicpc.net/problem/2164)

```python
N = int(input())
lis = [0] * N

for i in range(N):
    lis[i] = i+1

while len(lis) != 1:
    lis.pop(0)

    lis.append(lis.pop(0))
    
    
print(lis[0])


```