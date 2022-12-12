T = int(input())

for _ in range(T):
    k = int(input())
    n = int(input())
    f = [i for i in range(1, n+1)]
    nf = [0]*n
    for _ in range(k):
        for i in range(n):
            nf[i] = sum(f[:i+1])
        f = nf[:]
    print(nf[-1])