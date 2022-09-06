import sys
def input():
    return sys.stdin.readline().rstrip()

N = int(input())
i_ord = list(map(int, input().split()))
p_ord = list(map(int, input().split()))
tree = {i:[0, 0] for i in range(1, N+1)}

