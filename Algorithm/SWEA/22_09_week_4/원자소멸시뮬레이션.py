from collections import defaultdict

D = [(0, 1), (0, -1), (-1, 0), (1, 0)]

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    info_coordi = defaultdict(list)
    energy = 0
    for _ in range(N):
        x, y, d, k = map(int, input().split())
        x *= 2
        y *= 2
        info_coordi[(x, y)].append((d, k))

    while info_coordi:
        nxt = defaultdict(list)
        for key, value in info_coordi.items():
            x, y = key
            d, k = value[0]
            if -2000 <= x+D[d][0] <= 2000 and -2000 <= y+D[d][1] <= 2000:
                nxt[(x+D[d][0], y+D[d][1])].append((d, k))
        for key in list(nxt.keys()):
            if len(nxt[key]) > 1:
                for value in nxt[key]:
                    energy += value[1]
                nxt.pop(key)
        info_coordi = nxt
    print(f'#{tc} {energy}')



