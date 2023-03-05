N = int(input())
drinks = list(map(int, input().split()))
drinks.sort()
print(sum(drinks[:-1])/2 + drinks[-1])