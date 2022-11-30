import sys

sys.setrecursionlimit(10*6)

def input():
    return sys.stdin.readline().rstrip()

N, M = map(int, input().split())
lst = [i for i in range(N+1)]

def find(n):

    if lst[n] != n:
        lst[n] = find(lst[n])
        
    return lst[n]

def union(a, b):
    lst[find(a)] = find(b)


for _ in range(M):
    O, A, B = map(int, input().split())
    if O == 0:
        union(A, B)
    elif O == 1:
        if find(A) == find(B):
            print('YES')
        else:
            print('NO')