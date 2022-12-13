import sys

def input():
    return sys.stdin.readline().rstrip()

W, N = map(int, input().split())
lst = [0]* 10001
for _ in range(N):
    m, p = map(int, input().split())
    lst[p] += m

ans = 0
bag = 0
for i in range(10000, 0, -1):
    if lst[i] == 0:
        continue
    elif lst[i] + bag >= W:
        ans += (W - bag) * i
        break
    else:
        ans += lst[i]*i
        bag += lst[i]
print(ans)