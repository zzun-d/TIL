import sys
def input():
    return sys.stdin.readline().rstrip()


N = int(input())
lst = []
for _ in range(N):
    a = int(input())
    lst.append(a)
lst.sort()
mx = lst[0] * N
for i in range(N-1):
    if lst[i+1] > lst[i]:
        mx = max(lst[i+1] * (N-i-1), mx)

print(mx)


