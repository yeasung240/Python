### [A set of strings](https://www.acmicpc.net/problem/14425)

Difficulty : Silver 5

#### statement

A set S consisting of N strings is given.

Write a program that calculates how many of the M strings given as input are contained in the set S.

#### Input

The first line contains the number of strings N and M (1 ≤ N ≤ 10,000, 1 ≤ M ≤ 10,000).

The next N lines contain strings contained in the set S.

The next M lines contain strings to be tested.

The string given as input consists only of lowercase letters of the alphabet and its length does not exceed 500. There is no case where the same string is given multiple times in the set S.

#### Output

In the first line, print how many of the M strings are contained in the set S.


>**IDEA**

It is more complicated to make the logic and we can solve easily with set
>**How I solve it**

```python
import sys
input = sys.stdin.readline
n, m = map(int, input().split())
textList = set([input() for _ in range(n)])
count = 0
for _ in range(m):
    subText = input()
    if subText in textList:
        count += 1
print(count)
```