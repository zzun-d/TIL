N = int(input())
if N != 1:
    i = 2
    while i <= N**0.5:
        if N % i == 0:
            print(i)
            N = N // i
            continue
        i += 1
    print(N)
