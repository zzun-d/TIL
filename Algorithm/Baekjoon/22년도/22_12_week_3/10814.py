import sys

def input():
    return sys.stdin.readline().rstrip()

N = int(input())
lst = []
for i in range(N):
    age, name = input().split()
    age = int(age)
    lst.append((age, i, name))
lst.sort()
for age, _, name in lst:
    print(age, name)