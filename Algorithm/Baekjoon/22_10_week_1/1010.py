T = int(input())
for tc in range(1, t+1):
    N, M = map(int, input().split())
    lst = [0]*N
    k = 0
    cnt = 0
    for i in range(N):
        for j in range(i+1, M)