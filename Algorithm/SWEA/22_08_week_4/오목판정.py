T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [input() for _ in range(N)]
    ans = 'NO'
    i = j = 0

    while True:
        if i == N:
            break

        elif j == N:
            i += 1
            j = 0
            continue

        if arr[i][j] =='o':

            cnt = 1
            if j+4 < N:
                for d in range(1, 5):
                    if arr[i][j+d] == 'o':
                        cnt += 1
                    else:
                        break
            if cnt == 5:
                ans = 'YES'
                break

            cnt = 1
            if i+4 < N:
                for d in range(1, 5):
                    if arr[i + d][j] == 'o':
                        cnt += 1
                    else:
                        break
            if cnt == 5:
                ans = 'YES'
                break

            cnt = 1
            if j + 4 < N and i + 4 < N:
                for d in range(1, 5):
                    if arr[i + d][j + d] == 'o':
                        cnt += 1
                    else:
                        break
            if cnt == 5:
                ans = 'YES'
                break

            cnt = 1
            if 0 <= j - 4  and i + 4 < N:
                for d in range(1, 5):
                    if arr[i + d][j - d] == 'o':
                        cnt += 1
                    else:
                        break
            if cnt == 5:
                ans = 'YES'
                break
        j += 1

    print(f'#{tc} {ans}')
