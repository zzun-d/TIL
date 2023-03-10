import sys

def input():
    return sys.stdin.readline().rstrip()

def counting(x, y):
    for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        nx = x + dx
        ny = y + dy
        if N > nx >= 0 and M > ny >= 0 and arr[nx][ny] == 1:
            

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
