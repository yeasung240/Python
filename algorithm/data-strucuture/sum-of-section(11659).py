# 11659
# getting runtime error if you don't use the sys. 
N, M = map(int, input().split())
lis = list(map(int, input().split()))
new_lis = [0] + lis
SUM_lis = []
SUM = 0 
for i in new_liss:
    SUM += i
    SUM_lis.append(SUM)
    
for i in range(M):
    A,B = map(int, input().split())
    print(SUM_lis[B]-SUM_lis[A-1])
