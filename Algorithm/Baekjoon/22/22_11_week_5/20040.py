import sys

def input():
    return sys.stdin.readline().rstrip()

def find(n):
    
    while n != lst[n]:
        n = lst[n]
    return n

def union(x, y):
    x = find(x)
    y = find(y)
    if x < y:
        lst[y] = x
    else:
        lst[x] = y

N, M = map(int, input().split())
lst = [i for i in range(N)]
result = 0
for i in range(M):
    a, b = map(int, input().split())
    tmp_a = find(a)
    tmp_b = find(b)
    if tmp_a == tmp_b:
        result = i + 1
        break
    union(a, b)
print(result)