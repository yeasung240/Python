# baekjoon 2875 (intern or competition)

N, M, K = map(int, input().split())

for i in range(K):
    if (N//2) >= M:
        N-=1
    if (N//2) < M:
        M-=1
    print(min(N//2,M))
