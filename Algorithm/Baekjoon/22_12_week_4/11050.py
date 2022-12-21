N, K = map(int, input().split())
fac_lst = [1, 1] + [0]*(N-1)

if K < 0 or K > N:
    print(0)
else:
    i = 2
    while i <= N:
        fac_lst[i] = fac_lst[i-1]*i
        i += 1
    print(fac_lst[N]//(fac_lst[K]*fac_lst[N-K]) % 10007)