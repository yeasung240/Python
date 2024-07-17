# Greedy Algoritm, finding the least number of coins. 
# 1st try
N, K = map(int, input().split())
lis = [0]*N
counter = 0 

for i in range(N):
    lis[i] = int(input())

    
 # i = 1, 5, 10 # K = 55
while K != 0:
    for i in reversed(lis):
        if i <= K:
            a = (K // i)
            counter = counter + (a)
            K = K - (a*i)
print(counter)

# Solution
N, K = map(int, input().split())
lis = [0]*N
counter = 0 

for i in range(N):
    lis[i] = int(input())
    
for i in reversed(lis):
    
    if i <= K:
        counter = counter + int(K/i)
        K = K % i
        counter
        
print(counter)
