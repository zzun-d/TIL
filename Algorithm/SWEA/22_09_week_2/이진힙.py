T = int(input())
for tc in range(1, T+1):
    N = int(input())
    lst = list(map(int, input().split()))
    tree = [0]
    for idx, l in enumerate(lst, start=1):
        tree.append(l)
        while True:
            if idx//2 and tree[idx//2] > l:
                tree[idx], tree[idx//2] = tree[idx//2], tree[idx]
                idx = idx//2
            else:
                break
    result = 0
    last_n = len(tree)-1
    while last_n:
        last_n = last_n//2
        result += tree[last_n]
    print(result)


