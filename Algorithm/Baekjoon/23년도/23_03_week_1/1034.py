import sys

def input():
    return sys.stdin.readline().rstrip()

r, c = map(int ,input().split())
arr = [input() for _ in range(r)]
cnt = int(input())

D = {}

for a in arr:
    if D.get(a):
        D[a][1] += 1
    else:
        D[a] = [a.count('0'), 1]
answer = 0
for c, ans in D.values():
    if cnt >= c and (cnt - c)%2 == 0:
        answer = max(answer, ans)
print(answer)
