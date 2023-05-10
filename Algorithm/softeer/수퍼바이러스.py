import sys

k, p, n = map(int, input().split())
n *= 10


def recur_f(x, y):
    result = 1
    while y > 0:
        if y % 2 == 1:
            result = (result*x) % 1000000007
        x = (x*x) % 1000000007
        y = y//2
    return result


print(k*recur_f(p, n) % 1000000007)
