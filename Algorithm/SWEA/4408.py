def max(lst, n):
    ans = lst[0]
    for i in range(n):
        if lst[i] > ans:
            ans = lst[i]
    return ans

T = int(input())
for t in range(1, T+1):
    N = int(input())
    room = [0] * 401
    for _ in range(N):
        l, r = map(int, input().split())
        
        if l > r:
            l, r = r, l

        for i in range(l, r+1):
            room[i] += 1
    ans = max(room, 401)
    print(f'#{t} {ans}')
    