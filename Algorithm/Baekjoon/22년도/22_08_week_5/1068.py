from collections import defaultdict

N = int(input())
lst = list(map(int, input().split()))
cut = [int(input())]
tree = defaultdict(list)
for i in range(N):
    if lst[i] >= 0:
        tree[lst[i]].append(i)
leaf = N -len(tree)

if len(tree[lst[cut[0]]]) == 1:
    leaf += 1

while cut:
    n_cut = []
    for c in cut:
        if tree[c]:
            n_cut += tree[c]
        else:
            leaf -= 1

    cut = n_cut[:]

print(leaf)


