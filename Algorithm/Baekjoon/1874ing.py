import sys
def input():
    return sys.stdin.readline().rstrip()

n = int(input())
lst = [i for i in range(1, n+1)]
for _ in range(n):
    1