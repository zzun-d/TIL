from collections import defaultdict


N = int(input())
tree = defaultdict(list)
lines = [0]
for _ in range(N-1):
    a, b = map(int, input().split())
    lines.append((a, b))
    if tree[b] or b in list(tree.values()):
        tree[b].append(a)
    else:
        tree[a].append(b)

q = int(input())
for _ in range(q):
    cut, num = map(int, input().split())
    if cut == 1:
        sa = tree[num][:] 
        tree[num] = []
        v_lst = []
        for i in list(tree.values()):
            v_lst += i
        if len(list(set(tree.keys()) - set(v_lst))) > 1:
            print('yes')
        else:
            print('no')
        tree[num] = sa
    else:
        a, b = lines[num]
        if tree[a]:
            tree[a].remove(b)
            tmp = 'a'
        else:
            tree[b].remove(a)
            tmp = 'b'

        v_lst = []
        for i in list(tree.values()):
            v_lst += i
        if len(list(set(tree.keys()) - set(v_lst))) > 1:
            print('yes')
        else:
            print('no')
        if tmp == 'a':
            tree[a].append(b)
        else:
            tree[b].append(a)