import sys
def input():
    return sys.stdin.readline().rstrip()

N = int(input())
coordi = []

for i in range(1, N+1):
    x, r = map(int, input().split())
    coordi.append((x-r, -i))
    coordi.append((x+r, i))
coordi.sort()
stack = []
ans = 'YES'
for c in coordi:
    if c[1] > 0:
        if stack and stack.pop()[1] == -c[1]:
            continue
        else:
            ans = 'NO'
            break
    else:
        if stack and stack[-1][0] == c[0]:
            ans = 'NO'
            break
        else:
            stack.append(c)
print(ans)