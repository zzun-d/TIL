T = int(input())
for _ in range(T):
    x, y = map(int, input().split())
    l = y - x

    k = int((l ** 0.5))
    cnt = k * 2 - 1
    remain = l - k**2

    while remain > 0:
        if remain >= k:
            remain -= k
            cnt += 1
            continue
        else:
            remain = 0
            cnt += 1

    print(cnt)
        