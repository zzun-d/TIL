from collections import deque

n, s, a, b = 6, 4, 6, 2
fares = [[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]

graph = [[0]*(n+1) for _ in range(n+1)]
dp = [[0]*(n+1) for _ in range(n+1)]

for fare in fares:
    c, d, f = fare
    graph[c][d] = f
    graph[d][c] = f

for i in range(1, n+1):
    for j in dp[i]:
        pass