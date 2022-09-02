K = int(input())
V = list(map(int, input().split()))
l = len(V)
for i in range(1, K+1):
    L = V[l//(2**i)::l//(2**(i-1)) + 1]
    print(*L)