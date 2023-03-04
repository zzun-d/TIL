import sys
from collections import defaultdict
sys.setrecursionlimit(10**6)

def input():
    return sys.stdin.readline().rstrip()

def f(w):
    ans_lst = [0]
    for i in s_dict[w]:
        if not visited[i]:
            f(i)
        ans_lst.append(t_lst[i])
    t_lst[w] += max(ans_lst)
    visited[w] = True
    
T = int(input())

for _ in range(T):
    N, K = map(int, input().split())
    t_lst = [0] + list(map(int, input().split()))
    s_dict = defaultdict(list)
    visited = [False]*(N+1)

    for _ in range(K):
        x, y = map(int, input().split())
        s_dict[y].append(x)
    
    w = int(input())

    f(w)

    print(t_lst[w])

