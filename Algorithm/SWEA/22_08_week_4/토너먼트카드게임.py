def tourna(p1, p2):
    l1, l2 = len(p1), len(p2)

    if l1 + l2 <= 2:
        if l2:
            if p1[0][1]-p2[0][1] in [1, -2, 0]:
                w1 = p1[0]
            else:
                w1 = p2[0]

            return [w1]
        else:
            return [p1[0]]
    else:
        return tourna(tourna(p1[:(l1+1)//2], p1[(l1+1)//2:]), tourna(p2[:(l2+1)//2], p2[(l2+1)//2:]))

T = int(input())

for t in range(1, T+1):
    N = int(input())
    tou = [(i, j) for i, j in zip(range(1, N+1), list(map(int, input().split())))]
    print(f'#{t} {tourna(tou[:(N+1)//2], tou[(N+1)//2:])[0][0]}')