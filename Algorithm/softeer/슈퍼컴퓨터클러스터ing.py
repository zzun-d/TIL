from collections import defaultdict

def binary_search(s, e):
    global ans
    if e - s <= 1:
        sm = 0
        for i in range(1, e+1):
            if c_dict[i] != 0:
                sm += (e-i)**2 * c_dict[i]
        if sm <= K:
            ans = e
        else:
            ans = s
            
        return
    m = (s+e)//2
    sm = 0
    i = 1
    while sm < K and i < m:
        if c_dict[i] != 0:
            sm += (m-i)**2 * c_dict[i]
        i += 1
    if i == m and sm < K:
        binary_search(m, e)
    else:
        binary_search(s, m)


N, K = map(int, input().split())

c_dict = defaultdict(int)

for n in map(int, input().split()):
    c_dict[n] += 1

ans = 0

binary_search(0, 2000000000)

print(ans)


