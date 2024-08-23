# Priority queue
* Implement the function
  ```python
  from queue import PriorityQueue

  q = PriorityQueue()
  ```
* Put function

input the value in the priority queue

```python
# 1. Basic input based on numbers order
que.put(4)
que.put(1)
que.put(7)
que.put(3)



# 2. change in according to priority.
q.put((priority, value))

que.put((3, 'Apple'))
que.put((1, 'Banana'))
que.put((2, 'Cherry'))

print(que.get()[1])  # Banana
print(que.get()[1])  # Cherry
print(que.get()[1])  # Apple
```
* get

Delete the value and return the value

```python
que.put(4)
que.put(1)
que.put(7)
que.put(3)

print(que.get())  # 1
print(que.get())  # 3
print(que.get())  # 4
print(que.get())  # 7
```

* qsize

It is related to size of queue.