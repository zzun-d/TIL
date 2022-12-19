def f(n):
    if n < 2:
        return 1

    else:
        return n * f(n-1)

N, K = map(int, input().split())

if K < 0 or K > N:
    print(0)
else:
    print(round(f(N)/(f(K)*f(N-K))))
    