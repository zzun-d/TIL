import sys

def input():
    return sys.stdin.readline().rstrip()

N= int(input())
h_lst = [] 
w_lst = []
for _ in range(N):
    w, h = map(int, input().split())
    h_lst.append(h)
    w_lst.append(w)
ans = []
for i in range(N):
    rank = 1
    for j in range(N):
        if i != j and h_lst[j] > h_lst[i] and w_lst[j] > w_lst[i]:
            rank += 1
    ans.append(rank)
print(*ans)

