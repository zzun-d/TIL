import sys
def input():
    return sys.stdin.readline().rstrip()

N = int(input())
lst = []
for _ in range(N):
    lst.append(int(input()))
lst.sort(reverse=True)

tip = 0
cnt = 0
while cnt < N and lst[cnt]- cnt > 0:
    tip += lst[cnt] - cnt
    cnt += 1
print(tip)
    
