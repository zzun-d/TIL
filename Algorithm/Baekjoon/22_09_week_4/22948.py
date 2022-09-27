import sys


def input():
    return sys.stdin.readline().rstrip()


N = int(input())

tree = {}
tree[0] = [i for i in range(1, N+1)]
comp = {}
for _ in range(N):
    n, c, r = map(int, input().split())
    comp[n] = [c-r, c+r]
s, e = map(int, input().split())

for 