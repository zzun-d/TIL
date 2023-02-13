N = int(input())

arr = [list(map(int, list(input()))) for _ in range(N)]
ans = []

x = y = 0
while x < N:
    if y >= N:
        x += 1
        y = 0
        continue

    if arr[x][y] == 0:
        y += 1
        continue
    cnt = 1
    q = [(x, y)]
    arr[x][y] = 0
    while q:
        i, j = q.pop()
        for di, dj in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            ni = i + di
            nj = j + dj
            if N > ni >= 0 and N > nj >= 0 and arr[ni][nj] == 1:
                q.append((ni, nj))
                arr[ni][nj] = 0
                cnt += 1
    ans.append(cnt)

print(len(ans))
ans.sort()
for n in ans:
    print(n)