for tc in range(1, 11):
    N, S = map(int, input().split())
    lst = list(map(int, input().split()))
    tree = {}
    for i in range(0, N, 2):
        p, c = lst[i:i+2]
        if tree.get(p):
            tree[p].add(c)
        else:
            tree[p] = {c}
    call_lst = [S]
    called = set([S])
    while True:
        nxt = set()
        for s in call_lst:
            if tree.get(s):
                nxt |= tree[s]

        nxt -= called

        called |= nxt

        if not nxt:
            if post_called:
                print(f'#{tc} {max(post_called)}')
            else:
                print(f'#{tc} {S}')
            break
        post_called = set()|nxt
        call_lst = list(nxt)
