### [Exercise 5. Lost parentheses](https://www.acmicpc.net/problem/1541#)

Difficulty : silver 2

#### statement

Sejun has created an expression using positive numbers, +, −, and parentheses. Then, Sejun removed all the parentheses.

After that, Sejun wants to add parentheses appropriately to minimize the value of this expression.

Write a program that minimizes the value of this expression by adding parentheses appropriately.

#### Input

The first line contains the expression. The expression consists only of digits (0 through 9), +, and -, and the first and last characters are digits. There are no two consecutive operators, and there are no more than five consecutive digits. Numbers can start with 0. The length of the expression given as input is less than or equal to 50.

#### Output

Print the answer on the first line.



>**How I solve it**

```python

answer = 0
A = list(map(str, input().split("-")))

# def to get the sum is seperated above
def mySum(i):
    sum = 0
    temp = str(i).split("+")
    for i in temp:
        sum += int(i)
    return sum

for i in range(len(A)):
    temp = mySum(A[i])

    if i == 0:
        answer += temp # add the first value
    else:
        answer -= temp # subtract other values
print(answer)
```