import sys

def input():
    return sys.stdin.readline().rstrip()

N = int(input())
coordi = []
for _ in range(N):
    x, y = map(int, input().split())
    coordi.append((y, x))
coordi.sort()
for y, x in coordi:
    print(x, y)