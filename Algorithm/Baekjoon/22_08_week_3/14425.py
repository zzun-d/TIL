import sys
def input():
    return sys.stdin.readline().rstrip()

N, M = map(int, input().split())
ans = 0
S = set(input() for _ in range(N))

for _ in range(M):
    if S & set([input()]):
        ans += 1
print(ans)