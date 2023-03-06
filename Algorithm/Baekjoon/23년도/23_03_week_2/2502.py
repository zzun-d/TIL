def f(n):
    if n == 1:
        return 1
    if n == 2:
        return 1
    return f(n-1) + f(n-2)


D, K = map(int, input().split())

x = f(D-1)
y = f(D-2)
r = K % x
while True:
    if r % y == 0 and r > x:
        break
    r += x

print(r//y)
print((K-r)//x)




 