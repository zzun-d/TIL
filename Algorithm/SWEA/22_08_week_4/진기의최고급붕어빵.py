T = int(input())

for tc in range(1, T+1):
    N, M, K = map(int, input().split())
    T = list(map(int, input().split()))
    mx_t = 0

    for t in T:
        if t > mx_t:
            mx_t = t

    boong = [0] * (mx_t + 1)

    for i in range(1, mx_t+1):
        if i % M == 0:
            boong[i] += boong[i-1] + K
        else:
            boong[i] += boong[i-1]

    ans = 'Possible'
    for t in T:
        for i in range(t, mx_t+1):
            if boong[i] <= 0:
                ans = 'Impossible'
                break
            boong[i] -= 1
        if ans == 'Impossible':
            break

    print(f'#{tc} {ans}')

