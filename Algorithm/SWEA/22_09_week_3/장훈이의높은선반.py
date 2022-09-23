def f(i, h):
    global gap
    if h >= B:
        gap = min(gap, h-B)

    elif i >= len(H):
        return

    else:
        f(i+1, h+H[i])
        f(i+1, h)


T = int(input())
for tc in range(1, T+1):
    N, B = map(int, input().split())
    H = list(map(int, input().split()))
    gap = 10000
    f(0, 0)
    print(f'#{tc} {gap}')