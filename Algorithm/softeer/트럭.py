import sys
import heapq


def input():
    return sys.stdin.readline().rstrip()


N = int(input())

infos = []
costs = [0]*N
results = {}
sum_p = 0
for n in range(N):
    info = list(map(int, input().split()))
    for i in range(info[0]):
        s, p = info[i*2+1:i*2+3]
        heapq.heappush(infos, (s, p, n))

while infos:
    s, p, n = heapq.heappop(infos)
    if costs[n] >= p:
        continue
    elif costs[n] != 0:
        sum_p -= costs[n]
    costs[n] = p
    sum_p += p
    results[s] = sum_p

k = list(results.keys())
v = list(results.values())
l = len(k)
mx = v[-1]
mn = v[0]


def b_s(l, r, target):
    while l < r:
        m = (l+r)//2
        if v[m] >= target:
            r = m
        else:
            l = m+1
    return k[l]


Q = int(input())
q_list = list(map(int, input().split()))
ans_lst = []
for q in q_list:
    if q <= mn:
        ans_lst.append(k[0])
    elif q > mx:
        ans_lst.append(-1)
    else:
        ans_lst.append(b_s(0, l-1, q))

print(*ans_lst)
