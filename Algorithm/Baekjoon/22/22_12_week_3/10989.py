import sys

def input():
    return sys.stdin.readline().rstrip()

lst = [0]*10001
N = int(input())
for _ in range(N):
    lst[int(input())] += 1
for i in range(1, 10001):
    for _ in range(lst[i]):
        print(i)