T = int(input())
for tc in range(1, T+1):
    lst = list(map(int, input().split()))
    cnt = 0
    now = 1
    nxt = now + lst[now]
    while nxt < lst[0]:

        for i in range(now+1, nxt+1):
            nxt = max(i + lst[i], nxt)

        cnt += 1
    print(f'#{tc} {cnt}')