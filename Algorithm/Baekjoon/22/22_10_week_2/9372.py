import sys

def input():
    return sys.stdin.readline().rstrip()


T = int(input())

for _ in range(T):
    N, M = map(int, input().split())
    
    for _ in range(M):
        input()

    print(N-1)