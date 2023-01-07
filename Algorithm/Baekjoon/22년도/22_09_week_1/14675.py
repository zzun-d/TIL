from collections import defaultdict
import sys
def input():
    return sys.stdin.readline().rstrip()


N = int(input())
tree = defaultdict(list)
line_idx = [0]
for _ in range(N-1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)
    line_idx.append((a, b))
for _ in range(int(input())):
    q, n = map(int, input().split())
    if q == 1:
        if len(tree[n]) > 1:
            print('yes')
        else:
            print('no')
    
    else:
        print('yes')