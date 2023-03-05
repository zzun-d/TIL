N, M = map(int, input().split())

a = b = 1
for i in range(M):
    a *= N-i
    b *= i+1
print(a//b)