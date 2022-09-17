import sys
def input():
    return sys.stdin.readline().strip()

N = int(input())
lst = []
for _ in range(N):
    lst.append(int(input()))
lst.sort(reverse=True)
sm = sum(lst)
sale = sum([lst[i] for i in range(2, N, 3)])
print(sm - sale)