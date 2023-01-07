N, K = map(int, input().split())
lst = list(map(int, input().split()))
s = 0
odd = 0
mx = 1

while True:
    if lst[s] % 2 == 0:
        break
    s += 1
e = s + 1

while e < N:
    while lst[e] % 2 == 1:
        if odd < K:
            odd += 1
            e += 1
        else:
            while (odd >= K or lst[s] % 2 == 1) and s < e:
                if lst[s] % 2:
                    odd -= 1
                s += 1
            mx = max(mx, e-s+1-odd)
    mx = max(mx, e-s+1-odd)
    e += 1
print(mx)
