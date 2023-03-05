n, m = map(int, input().split())


def f(num, i):
    cnt = 0
    while num > 0:
        cnt += num//i
        num //= i
    return cnt
# print(f(n, 2), f(m, 2), f(n-m, 2), f(n, 5), f(m, 5), f(n-m, 5))
print(max(min(f(n, 2) - f(m, 2) - f(n-m, 2), f(n, 5) - f(m, 5) - f(n-m, 5)), 0))