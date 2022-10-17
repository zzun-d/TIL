def binary_search(s, e):
    global ans
    if e - s <= 1:
        ans = s
        return
    m = (s+e)//2
    sm = 0
    i = 1
    while sm < K and i < m:
        if c_lst[i] != 0:
            sm += (m-i)**2 * c_lst[i]
        i += 1
    if i == m and sm < K:
        binary_search(m, e)
    else:
        binary_search(s, m)


N, K = map(int, input().split())
c_lst = [0]*(1000000001)

for n in map(int, input().split()):
    c_lst[n] += 1
ans = 0
binary_search(0, 1000000000)
print(ans)