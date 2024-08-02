[Problem](https://www.acmicpc.net/problem/11286)


```python
# Queue

from queue import PriorityQueue

N = int(input())
myQueue = PriorityQueue()

for i in range(N):
    request = int(input())
    if request == 0:
        if myQueue.empty():
            print('0\n')
        else:
            temp = myQueue.get()
            print(str((temp[1])+'\n'))
    else:
        myQueue.put((abs(request), request))

```