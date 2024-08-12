# Number theory



### Sieve of Eratosthenes (Prime number)
```python

#1929
import math
M, N = map(int, input().split())
A = [0] * (N+1)

for i in range(2, N+1):
    A[i] = i

for i in range(2, int(math.sqrt(n))+1):
    if A[i] == 0:
        continue
        # continue -> skip next line and go back to for loop. 
    for j in range(i+i, N+1, i):
        A[j] = 0
    
for i in range(M,N+1):
    if A[i] != 0:
        print(A[i])

```
> why we search until sqrt(n)

[Reason](https://nahwasa.com/entry/%EC%97%90%EB%9D%BC%ED%86%A0%EC%8A%A4%ED%85%8C%EB%84%A4%EC%8A%A4%EC%9D%98-%EC%B2%B4-%ED%98%B9%EC%9D%80-%EC%86%8C%EC%88%98%ED%8C%90%EC%A0%95-%EC%8B%9C-%EC%A0%9C%EA%B3%B1%EA%B7%BC-%EA%B9%8C%EC%A7%80%EB%A7%8C-%ED%99%95%EC%9D%B8%ED%95%98%EB%A9%B4-%EB%90%98%EB%8A%94-%EC%9D%B4%EC%9C%A0)


### Euler's totient

>[Example question](https://www.acmicpc.net/problem/11689)
```python
import math
N = int(input())
result = N
for p in range(2, int(math.sqrt(N)) + 1):  # 제곱근까지만 진행
    if N % p == 0:  # p가 소인수인지 확인
        result -= result / p  # 결괏값 업데이트
        while N % p == 0:  # 2의 7승*11이라면 2의 7승을 없애고 11만 남김
            N /= p
if N > 1:  # 반복문에서 제곱근까지만 탐색했으므로 1개의 소인수가 누락되는 케이스 처리
    result -= result / N
print(int(result))
```

### Euclidean-algorithm (greatest common divisor)
[Example question 1](https://www.acmicpc.net/problem/1934)

[Example question 2](https://www.acmicpc.net/problem/1850)


```python
def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)
gcd(a,b) 
# denominator should be more bigger than nominator
# greatest common multiple = (a*b) / gcd 
```