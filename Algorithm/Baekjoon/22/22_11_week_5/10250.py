T = int(input())
for _ in range(T):
    H, W, N = map(int, input().split())
    Y = N%H if N%H != 0 else H
    X = N//H if N%H == 0 else N//H + 1

    if X // 10 == 0:
        print(f'{Y}0{X}')
    else:
        print(f'{Y}{X}')

