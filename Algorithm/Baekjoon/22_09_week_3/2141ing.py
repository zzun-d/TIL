import sys

def input():
    return sys.stdin.readline().rstrip()

N = int(input())
p = {}
for _ in range(N):
    x, a = map(int, input().split())
    p[x] = a
p_k = sorted(list(p.keys()))
avg = p_k[0]*p[p_k[0]]


