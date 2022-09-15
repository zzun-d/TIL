T = int(input())
for tc in range(1, T+1):
    E, N = map(int, input().split())
    c1 = [0]*(E+2)
    c2 = [0]*(E+2)
    lst = list(map(int, input().split()))
    for i in range(0, 2*E, 2):
        if c1[lst[i]]:
            c2[lst[i]] = lst[i+1]
        else:
            c1[lst[i]] = lst[i+1]
    cnt = 1
    node = [N]
    while node:
        n = node.pop(0)
        if c2[n]:
           node.append(c2[n])
           node.append(c1[n])
           cnt += 2
        elif c1[n]:
            node.append(c1[n])
            cnt += 1
    print(f'#{tc} {cnt}')
