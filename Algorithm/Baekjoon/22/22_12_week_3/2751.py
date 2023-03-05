import sys

def input():
    return sys.stdin.readline().rstrip()

N = int(input())
lst = []
for _ in range(N):
    lst.append(int(input()))
lst.sort()
for l in lst:
    print(l)