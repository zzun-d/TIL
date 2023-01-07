import sys


def input():
    return sys.stdin.readline().rstrip()


N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

for i in range(1, N):
    for j in range(N):
        arr[i][j] += arr[i-1][j]

for _ in range(M):
    ans = 0
    x1, y1, x2, y2 = map(int, input().split())
    if x1 != 1:
        for i in range(y1, y2+1):
            ans += arr[x2-1][i-1] - arr[x1-2][i-1]
    else:
        for i in range(y1, y2+1):
            ans += arr[x2-1][i-1]
    print(ans)
