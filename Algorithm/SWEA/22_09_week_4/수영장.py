def f(m, cost):
    global mn
    if m >= 12:
        mn = min(mn, cost)
        return
    else:
        f(m+1, cost + fee[0] * use_days[m])
        f(m+1, cost + fee[1])
        f(m+3, cost + fee[2])


T = int(input())
for tc in range(1, T+1):
    fee = list(map(int, input().split()))
    use_days = list(map(int, input().split()))
    mn = fee[-1]
    f(0, 0)
    print(f'#{tc} {mn}')