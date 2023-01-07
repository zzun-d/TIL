import sys
def input():
    return sys.stdin.readline().rstrip()

N = int(input())
reserv = []
for _ in range(N):
    s, e = map(int, input().split())
    reserv.append([e, s])
reserv.sort()
r_e = reserv[0][0]
i = 1
result = 1
while i < N:
    if reserv[i][1] >= r_e:
        result += 1
        r_e = reserv[i][0]
    i += 1

print(result)