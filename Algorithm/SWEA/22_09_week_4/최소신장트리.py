def find_set(n):
    if kruskal[n] == n:
        return n
    else:
        return find_set(kruskal[n])


def union_set(a, b):
    if kruskal[b] != b:
        union_set(a, kruskal[b])
    kruskal[b] = find_set(a)






T = int(input())

for tc in range(1, T+1):
    V, E = map(int, input().split())
    kruskal = [i for i in range(V+1)]
    lst = []
    for _ in range(E):
        lst.append(list(map(int, input().split())))
    lst.sort(key=lambda x: x[2])

    ans = cnt = idx = 0
    while cnt < V:
        n1, n2, w = lst[idx]
        if find_set(n1) != find_set(n2):
            union_set(n1, n2)
            ans += w
            cnt += 1
        idx += 1
    print(f'#{tc} {ans}')