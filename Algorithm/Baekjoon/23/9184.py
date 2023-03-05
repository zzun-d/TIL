def w(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return 1

    elif a > 10 or b > 10 or c > 10:
        return w(10, 10, 10)

    elif a < b and b < c:
        return w(a, b, c-1) + w(a, b-1, c-1) - w(a, b-1, c)
    
    else:
        return w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) -w(a-1, b-1, c-1)

a, b, c = map(int, input().split())
print(w(a, b, c))

# print(2**20)