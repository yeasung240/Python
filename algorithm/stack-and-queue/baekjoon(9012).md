[Problem](https://www.acmicpc.net/problem/9012)


```python
T = int(input())
lis = []

for i in range(T):
    word = input()
    lis = []
    for x in word:
        if x == '(':
            lis.append(x)
            # 처음 오는거나, 다 사라지고 난 뒤에 나타는거면 리스트에 추가를 해준다. 
        elif x == ')':
            if len(lis) == 0:
                lis.append(x)
                break
            else:
                lis.pop()
    if len(lis) == 0:
        print('YES')
    else:
        print('NO')

```