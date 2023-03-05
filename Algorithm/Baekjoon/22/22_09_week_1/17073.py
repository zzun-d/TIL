from collections import defaultdict
import sys
def input():
    return sys.stdin.readline().rstrip()

N, W = map(int, input().split())
tree = defaultdict(list)
for _ in range(N-1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)
cnt = 0

for v in tree.values():
    if len(v) == 1:
        cnt += 1
if len(tree[1]) == 1:
    cnt -= 1

print(W/cnt)