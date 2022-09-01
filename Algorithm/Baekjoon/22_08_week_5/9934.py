K = int(input())
V = list(map(int, input().split()))
print(V[(2**K - 1)//2])
