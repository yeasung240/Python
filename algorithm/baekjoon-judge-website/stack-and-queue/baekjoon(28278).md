[Problem](https://www.acmicpc.net/problem/28278)


```python

import sys

N = int(sys.stdin.readline())
stack = []


for i in range(N):
    value = sys.stdin.readline().split()
    
    if value[0] == '1':
        stack.append(value[1])
    
    if value[0] == '2':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack.pop())
        
    if value[0] == '3':
        print(len(stack))
    
    if value[0] == '4':
        if len(stack) == 0:
            print(1)
        else:
            print(0)
            
            
    if value[0] == '5':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])

```