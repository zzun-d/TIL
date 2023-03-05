import sys

input = sys.stdin.readline

def dfs(sm, n):
    global cnt
    if n == N:
        return

    sm += l[n]

    if sm == S:
        cnt += 1

    dfs(sm, n + 1)
    dfs(sm - l[n], n+1)

N, S = map(int, input().split())
l = list(map(int, input().split()))

cnt = 0
dfs(0, 0)

print(cnt)