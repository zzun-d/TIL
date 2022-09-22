T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    nlst = list(map(int, input().split()))
    mlst = list(map(int, input().split()))
    nlst.sort(reverse=True)
    mlst.sort(reverse=True)
    sm = 0
    i = 0
    j = 0
    while True:
        if mlst[i] >= nlst[j]:
            sm += nlst[j]
            i += 1
        j += 1
        if j >= N or i >= M:
            break
    print(f'#{tc} {sm}')
