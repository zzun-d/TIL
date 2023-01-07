import sys

def input():
    return sys.stdin.readline().rstrip()

N, M = map(int, input().split())
not_hear = set()
ans = []
for _ in range(N):
    not_hear.add(input())
for _ in range(M):
    name = input()
    if not_hear.intersection({name}):
        ans.append(name)
print(len(ans))
for name in sorted(ans):
    print(name)