def preorder(T):
    if T:
        print(T, end=' ')
        preorder(tree_c1[T])
        preorder(tree_c2[T])

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    lst = list(map(int, input().split()))
    tree_c1 = [0] * (N + 1)
    tree_c2 = [0] * (N + 1)
    for i in range(0, len(lst), 2):
        if tree_c1[lst[i]]:
            tree_c2[lst[i]] = lst[i+1]
        else:
            tree_c1[lst[i]] = lst[i+1]
    print(f'#{tc}', end=' ')
    preorder(1)
