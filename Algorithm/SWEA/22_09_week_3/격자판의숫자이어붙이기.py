def f(i, j, k, num):
    if k == 7:
        ans.add(num)
    else:
        for di, dj in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            ni = i + di
            nj = j + dj
            if 0 <= ni < 4 and 0 <= nj < 4:
                f(ni, nj, k+1, num+arr[ni][nj])


T = int(input())


for tc in range(1, T+1):
    arr = [input().split() for _ in range(4)]
    ans = set()

    for i in range(4):
        for j in range(4):
            nums = arr[i][j]
            f(i, j, 1, nums)
    print(f'#{tc} {len(ans)}')
