import sys
from collections import defaultdict, deque

def input():
    return sys.stdin.readline().rstrip()

n = int(input())
if n > 1:
    tree_p = defaultdict(list)
    tree_c = {}
    result = [0] * (n+1)
    mx_weight = 0
    for _ in range(n-1):
        p, c, d = map(int, input().split())
        tree_p[p].append((c, d))
        tree_c[c] = [p, d]

    tree_parent = set(list(tree_p.keys()))
    tree_leaf = set(list(range(1, n+1))) - tree_parent
    tree_leaf = list(tree_leaf)
    while tree_leaf[0] != 1:
        n_leaf = set()
        for c in tree_leaf:
            p, d = tree_c[c]
            if result[c] + d + result[p] > mx_weight:
                mx_weight = result[c] + d + result[p]
            result[p] = max(result[c] + d, result[p])
            
            n_leaf.add(p)

        tree_leaf = list(n_leaf)

    root_value = []
    for c,d in tree_p[1]:
        root_value.append(result[c] + d)
    root_value.sort()
    result[1] = root_value[-1] + root_value[-2]

    print(max(max(result), mx_weight))
    
else:
    print(0)