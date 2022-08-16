n = int(input())

if n // (7 * 4):
    print((n // 7) + 4) if n % 7 else print((n // 7) + 3)
else:
    i = 1
    s_i = 1
    while s_i < n:
        s_i = sum(range(1, i+1))
        i += 1
    print(i - 1) if n > 1 else print(i)
