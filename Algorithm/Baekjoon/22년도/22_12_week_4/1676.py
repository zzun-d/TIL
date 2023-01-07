N = int(input())

n_fac = 1
i = 1
while N >= i:
    n_fac *= i
    i += 1
cnt = 0

while n_fac % 10 == 0:
    cnt += 1
    n_fac //= 10

print(cnt)