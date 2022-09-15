for tc in range(1, 11):
    N = int(input())
    tree = [0]*(N+1)
    c1 = [0]*(N+1)
    c2 = [0]*(N+1)
    cor = ['+', '-', '*', '/']
    for _ in range(N):
        info = input().split()
        if len(info) > 2:
            tree[int(info[0])] = info[1]
            c1[int(info[0])] = int(info[2])
            c2[int(info[0])] = int(info[3])
        else:
            tree[int(info[0])] = int(info[1])


    while tree[1] in cor:

        for n in range(1, N+1):
            if c1[n] and c2[n] and tree[c1[n]] not in cor and tree[c2[n]] not in cor:
                if tree[n] == '+':
                    tree[n] = tree[c1[n]] + tree[c2[n]]
                elif tree[n] == '-':
                    tree[n] = tree[c1[n]] - tree[c2[n]]
                elif tree[n] == '*':
                    tree[n] = tree[c1[n]] * tree[c2[n]]
                else:
                    tree[n] = tree[c1[n]] / tree[c2[n]]
                c1[n] = 0
                c2[n] = 0
                if tree[1] not in cor:
                    break
    print(f'#{tc} {int(tree[1])}')