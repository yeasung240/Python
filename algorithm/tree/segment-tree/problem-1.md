### [finding the sum of intervals](https://www.acmicpc.net/problem/2042)

Difficulty : Gold 1

#### statement
Given some N numbers, but the numbers change frequently in the middle, and you want to find the sum of some parts in the middle. If there are numbers 1,2,3,4,5, and you change the third number to 6 and ask for the sum from the second to the fifth, you should output 17. And in that state, if you change the fifth number to 2 and ask for the sum from the third to the fifth, it will be 12.


#### Input
The first line contains N (1 ≤ N ≤ 1,000,000) numbers and M (1 ≤ M ≤ 10,000), K (1 ≤ K ≤ 10,000). M is the number of times the numbers change, and K is the number of times the sum of the intervals is found. Then, N numbers are given from the second line to the N+1th line. Then, three integers a, b, c are given from the N+2nd line to the N+M+K+1th line. When a is 1, change the b-th number (1 ≤ b ≤ N) to c, and when a is 2, find and print the sum of the b-th number (1 ≤ b ≤ N) to the c-th number (b ≤ c ≤ N).

All numbers given as input are integers greater than or equal to -2 63 and less than or equal to 2 63 -1.


#### Output
Print the sum of the sections obtained from the first line to the K lines. However, the correct answer is an integer greater than or equal to -2 63 and less than or equal to 2 63 -1



>**IDEA**

* Set the size of tree
* Index change
* put the values (to leaf nodes and parent node)
* Change the values
* 
* Summing up the values
  <br> Two values find parent node as expected. For selected cases, we include these to SUM variable and to parent node by -1 and +1

>**How I solve it**

```python

N, M, K = map(int, input().split())  # 수의 개수, 변경이 일어나는 횟수, 구간 합을 구하는 횟수
treeHeight = 0
lenght = N
# Finding the K (K = 3 with N = 5)
while lenght != 0:
    lenght //= 2
    treeHeight += 1
 
treeSize = pow(2, treeHeight + 1) # Set the tree size (2**3)*2
leftNodeStartIndex = treeSize // 2 - 1 # (Changing the index)
tree = [0] * (treeSize + 1) # why the tree is (treesize + 1) ? 

# Put the leaf node value
for i in range(leftNodeStartIndex + 1, leftNodeStartIndex + N + 1):
    tree[i] = int(input())

# Put the node from leaf node. 
def setTree(i):
    while i != 1:
        tree[i // 2] = tree[i //2] + tree[i]
        i -= 1
        # Fullfilling [1] index and get out

setTree(treeSize - 1)


# Change the values
# Set the differnce between changed vlaue and orginal value 
# Update from now indes to parent node. 
def changeVal(index, value):
    diff = value - tree[index]
    while index > 0: # if index == 0, couldn't go furthur
        tree[index] = tree[index] + diff
        index = index // 2

# 구간 합 계산 함수
def getSum(s, e):
    partSum = 0
    while s <= e:
        if s % 2 == 1:
            partSum += tree[s]
            s += 1
        if e % 2 == 0:
            partSum += tree[e]
            e -= 1
        s = s // 2
        e = e // 2
    return partSum

for _ in range(M + K):
    question, s, e = map(int, input().split())
    if question == 1:
        changeVal(leftNodeStartIndex + s, e)
    elif question == 2:
        s = s + leftNodeStartIndex
        e = e + leftNodeStartIndex
        print(getSum(s, e))
```