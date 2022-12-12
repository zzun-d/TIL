import sys

def input():
    return sys.stdin.readline().rstrip()


N = int(input())
lst = []
for i in range(N):
    lst.append(int(input()))
lst.sort()
print(round(sum(lst)/N))
print(lst[N//2])

cnt = []
i = 0
while i < N:
    c = 1
    i += 1
    while i < N and lst[i] == lst[i-1]:
        c += 1
        i += 1
    cnt.append((c, -lst[i-1]))
cnt.sort(reverse=True)
if len(cnt) > 1 and cnt[0][0] == cnt[1][0]:
    print(-cnt[1][1])
else:
    print(-cnt[0][1])
print(max(lst) - min(lst))
