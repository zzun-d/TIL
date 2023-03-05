import sys
sys.setrecursionlimit(10**6)

def find_length(p):
    global mx
    if tree_p.get(p):
        l = []
        for c in tree_p[p]:
            l.append(find_length(c) + weight[p])
        l.sort()
        mx = max(mx, sum(l[-2:])-weight[p]*2)
        weight[p] = max(l)
        return weight[p]
    else:
        return weight[p]

N = int(input())
mx = 0
tree_p = {}
tree_c = [0]*(N+1)
weight = [0]*(N+1)

for _ in range(N-1):
    p, c, d = map(int, input().split())
    tree_c[c] = p
    weight[c] = d
    if tree_p.get(p):
        tree_p[p].append(c)
    else:
        tree_p[p] = [c]
find_length(1)
print(mx)