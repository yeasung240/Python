### [Almost a prime number](https://www.acmicpc.net/problem/1456)

Difficulty : Gold 5

#### statement
When a number is in the form of a prime number raised to the power of N (N ≥ 2), the number is said to be nearly prime.

Given two integers A and B, print how many approximate prime numbers are greater than or equal to A and less than or equal to B


#### Input

In the first line, the left range A and the right range B are given with one space between them.
#### Output
Print the total number of items on the first line.



>**IDEA**
Using while

>**How I solve it**

```python
# 1456
A, B = map(int, input().split())
lis = [0] * (10000001)
counter = 0 

for i in range(2, B+1):
    lis[i] = i

for i in range(2,int(math.sqrt(B))+1 ):
    if lis[i] == 0:
        continue
    for j in range(i+i, B+1 ,i):
        lis[j] = 0
for i in range(2, 10000001):
    if A[i] != 0:
        temp = A[i] # temp is prime number
        
        while A[i] <= (B / temp):
            if A[i] <= (A / temp):
                count += 1
            temp = temp * A[i]
            
print(count)
    

```