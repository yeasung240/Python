[Problem](https://www.acmicpc.net/problem/1874)




```python
n = int(input())
lis = [0]*n
for i in range(n):
    lis[i] = int(input())

    
for i in range(n-1):
    print('+' * lis[i], '-')
    if lis[i] > lis[i+1]:
        print('-' * (lis[i+1]-lis[i]))
        
    if lis[i] < lis[i+1]:


```