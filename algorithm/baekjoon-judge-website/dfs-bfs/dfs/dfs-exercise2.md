[Finding interesting prime numbers](https://www.acmicpc.net/problem/2023)

**The problem**


Subin's favorite thing in the world is prime numbers, and his favorite hobby is playing with them. The prime number he is most interested in right now is 7331.

7331 is a prime number, but interestingly, 733 is also a prime number, 73 is also a prime number, and 7 is also a prime number. In other words, from left to right, 1, 2, 3, and 4 digits are all prime numbers! Subin named these numbers as "strange prime numbers".




```python
# 2023
N = int(input())

# check if num is prime number or not. 
def prime(num):
    for i in range(2, int(num / 2 + 1)):
        if num % i == 0:
            return False
    return True

def dfs(number):
    if len(str(number)) == N:
        print(number) # when it finishes, move to dfs(3)
    
    else:
        for i in range(1,10):
            if i % 2 == 0: # exclude even numbers
                continue
            if prime(number * 10 + i):
                dfs(number * 10 + i)  # append the number         
dfs(2)
dfs(3)
dfs(5)
dfs(7)

```