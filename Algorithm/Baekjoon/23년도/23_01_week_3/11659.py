import sys

def input():
    return sys.stdin.readline().rstrip()

N, M = map(int, input().split())
# lst = [0] + list(map(int, input().split()))
lst = [0]*(N+1)
for i, n in enumerate(map(int, input().split())):
    lst[i+1] = lst[i] + n

for _ in range(M):
    s, e = map(int, input().split())
    print(lst[e] - lst[s-1])
