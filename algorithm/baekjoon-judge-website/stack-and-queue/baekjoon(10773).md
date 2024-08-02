[Problem](https://www.acmicpc.net/problem/10773)

```python

K = int(input())
number = []

for i in range(K):
    x = int(input())
    if x != 0:
        number.append(x)
    elif x == 0:
        number.pop()
print(sum(number))

```