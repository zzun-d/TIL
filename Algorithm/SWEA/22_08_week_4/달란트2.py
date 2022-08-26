T = int(input())

for tc in range(1, T+1):
    N, P = map(int, input().split())

    D = N // P
    d = N % P

    print(f'#{tc} {D**(P-d)*(D+1)**d}')

