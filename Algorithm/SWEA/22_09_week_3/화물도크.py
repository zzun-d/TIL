from heapq import heappop, heappush


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    lst = []
    for _ in range(N):
        s, e = map(int, input().split())
        heappush(lst, (e, -s))
    E = 0
    cnt = 0
    while lst:
        e, s = heappop(lst)
        if -s >= E:
            E = e
            cnt += 1
    print(f'#{tc} {cnt}')