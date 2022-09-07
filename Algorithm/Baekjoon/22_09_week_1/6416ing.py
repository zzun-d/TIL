import sys
from collections import defaultdict
def input():
    return sys.stdin.readline().rstrip()


tc = 1
while True:
    tree = defaultdict(list)
    TMP = True
    while True:
        n_lst = list(map(int, input().split()))
        for i in range(0, len(n_lst), 2):
            tree[n_lst[i]].append(n_lst[i+1])
        if tree[0]:
            break
        if tree[-1]:
            TMP = False
            break
    if TMP:
        if len(tree) == 1:
            print(f'Case {tc} is a tree.')
            continue

        v_lst = []
        for i in list(tree.values()):
            v_lst += i
        # print(v_lst)
        v_set = set(v_lst)
        k_set = set(tree.keys()) - set([-1])
        tmp = True
        # print(k_set)
        # print(v_set)
        if len(k_set - v_set) != 1 or len(v_lst) != len(v_set):
            tmp = False
        if tmp:
            print(f'Case {tc} is a tree.')
        else:
            print(f'Case {tc} is not a tree.')
        tc += 1
    else:
        break
    