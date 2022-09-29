def find_set(n):
    if kruscal[n] == n:
        return n
    else:
        return find_set(kruscal[n])
        

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    kruscal = [i for i in range(N+1)]
    lst = list(map(int, input().split()))
    ans = set()
    for i in range(0, M*2, 2):
        if kruscal[lst[i]] == lst[i]:
            kruscal[lst[i]] = find_set(lst[i+1])
        else:
            kruscal[lst[i+1]] = find_set(lst[i])

    for i in range(1, N+1):
        ans.add(find_set(i))
    print(f'#{tc} {len(ans)}')