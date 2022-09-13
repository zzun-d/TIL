def inorder(T):
    if T:
        inorder(c1[T])
        print(tree[T], end='')
        inorder(c2[T])

for tc in range(1, 11):
    N = int(input())
    tree = [''] * (N+1)
    c1 = [0]*(N+1)
    c2 = [0]*(N+1)

    for _ in range(N):
        info = input().split()
        if len(info) == 2:
            tree[int(info[0])] = info[1]
        elif len(info) == 3:
            tree[int(info[0])] = info[1]
            c1[int(info[0])] = int(info[2])
        else:
            tree[int(info[0])] = info[1]
            c1[int(info[0])] = int(info[2])
            c2[int(info[0])] = int(info[3])
    print(f'#{tc}', end=' ')
    inorder(1)
    print()