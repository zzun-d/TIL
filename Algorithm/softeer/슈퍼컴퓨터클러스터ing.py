def binary_search(l, r):
    global answer
    if l + 1 == r:
        answer = l
        return
    cost = 0
    m = (l+r) // 2
    for p in lst:
            
        if cost > B:
            binary_search(l, m)
            break
        if p < m:
            cost += (m - p)**2
    else:
        if cost <= B:
            binary_search(m, r)
        else:
            binary_search(l, m)
    return

N, B = map(int, input().split())
lst = list(map(int, input().split()))
lst.sort()
answer = 0
binary_search(0, 2*10**9)
print(answer)

