T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    a_lst = list(map(int, input().split()))
    a_lst.sort()
    b_lst = list(map(int, input().split()))
    cnt = 0
    for b in b_lst:
        l = 0
        r = N - 1
        m = (N - 1 + l) // 2
        tmp = None
        while True:
            if a_lst[m] == b:
                cnt += 1
                break

            elif m == r:
                break

            elif a_lst[m] > b:
                if tmp == 'r':
                    break
                tmp = 'r'
                r = m - 1
                m = (l + r) // 2

            else:
                if tmp == 'l':
                    break
                tmp = 'l'
                l = m + 1
                m = (l + r) // 2

    print(f'#{tc} {cnt}')