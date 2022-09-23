T = int(input())

direct = [(-1, 0), (1, 0), (0, -1), (0, 1)]

for tc in range(1, T+1):
    N, M, K = map(int, input().split())
    info = {}
    for _ in range(K):
        i, j, n, d = map(int, input().split())
        info[(i, j)] = [(n, d)]

    for _ in range(M):
        nxt = {}
        for k in info.keys():
            i, j = k
            n, d = info[k][0]
            ni = i + direct[d-1][0]
            nj = j + direct[d-1][1]
            if ni == 0 or nj == 0 or ni == N-1 or nj == N-1:
                n //= 2

                if d % 2:
                    d += 1
                else:
                    d -= 1

            if nxt.get((ni, nj)):
                nxt[(ni, nj)].append((n, d))
            else:
                nxt[(ni, nj)] = [(n, d)]

        for k in nxt.keys():
            if len(nxt[k]) > 1:
                sm = 0
                mxd = mxn = 0
                for n, d in nxt[k]:
                    if n > mxn:
                        mxn = n
                        mxd = d
                    sm += n
                nxt[k] = [(sm, mxd)]
        info = nxt

    ans = 0
    for n in info.values():
        ans += n[0][0]
    print(f'#{tc} {ans}')