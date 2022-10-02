T = int(input())
for _ in range(T):
    N = int(input())
    lst = [0] + list(map(int, input().split()))
    visited = [0]*(N+1)
    cnt = 0
    for i in range(1, N+1):
        v_lst = []
        while not visited[i]:
            visited[i] = 1
            v_lst.append(i)
            i = lst[i]
        if i in v_lst:
            cnt += len(v_lst) - v_lst.index(i)
    print(N - cnt)