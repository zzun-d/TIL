import sys

def input():
    return sys.stdin.readline().rstrip()

N = int(input())
coordi = []
for _ in range(N):
    coordi.append(list(map(int, input().split())))
coordi.sort()
for c in coordi:
    print(*c)