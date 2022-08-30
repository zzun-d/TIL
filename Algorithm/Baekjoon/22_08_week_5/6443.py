from collections import deque


def dfs(n, s, old_a):
    



N = int(input())
for _ in range(N):
    senten = list(input())
    senten.sort()
    stack = deque(senten)
    old_s = None
    ans = []
