K, P, N = map(int, input().split())

num = K
for i in range(N):
    num *= P
    num %= 1000000007
print(num)