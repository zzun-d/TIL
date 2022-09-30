T = int(input())
for tc in range(1, T+1):
    N = int(input())
    x = int(N**(1/3))
    ans = -1
    if x**3 == N:
        ans = x
    elif (x-1)**3 == N:
        ans = x-1
    elif (x+1)**3 == N:
        ans = x+1
    print(f'#{tc} {ans}')