import sys

P, N = map(int, input().split())
A = list(map(int, input().split()))

result = A[0]
for i in range(1, N):
    result = (result * P + A[i]) % 1000000007

print(result)
