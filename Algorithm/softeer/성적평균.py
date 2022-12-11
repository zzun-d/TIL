N, K = map(int, input().split())
lst = [0] + list(map(int, input().split()))
for _ in range(K):
    s, e = map(int, input().split())
    print(f'{round(sum(lst[s:e+1])/(e - s + 1), 2):0.2f}')

