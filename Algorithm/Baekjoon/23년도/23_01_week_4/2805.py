def bs(l, r):
    global answer
    # print(l, r)
    if l+1 >= r:
        return

    cut_tree = 0
    m = (l+r)//2
    for tree in trees:

        if tree <= m:
            continue
        cut_tree += tree - m

    if cut_tree >= M:
        answer = m
        return bs(m, r)
    else:
        bs(l, m)


answer = 0
N, M = map(int, input().split())
trees = list(map(int, input().split()))
bs(0, max(trees)+1)
print(answer)
