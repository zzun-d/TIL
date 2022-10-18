from math import inf


def combi(sm, mn, i):
    global ans
    if i >= 6:
        return
    elif mn < ans:
        return
    elif sm > D:
        return
    elif sm == D:
        ans = mn
    
    combi(lst[i][0] + sm, min(mn, lst[i][1]), i+1)
    combi(sm, mn, i+1)

D, P = map(int, input().split())
lst = [tuple(map(int, input().split())) for _ in range(P)]
lst.sort(reverse=True)
ans = 0

combi(0, inf, 0)

print(ans)
