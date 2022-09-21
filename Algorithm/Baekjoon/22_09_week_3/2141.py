import sys

def input():
    return sys.stdin.readline().rstrip()

N = int(input())
p = {}
for _ in range(N):
    x, a = map(int, input().split())
    p[x] = a
p_k = sorted(list(p.keys()))
v = sum(p.values())
sm = 0
i = 0
while sm*2 < v:
    sm += p[p_k[i]]
    i += 1
print(p_k[i-1])
