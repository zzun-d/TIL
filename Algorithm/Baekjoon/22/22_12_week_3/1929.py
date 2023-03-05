a, b = map(int, input().split())
a = max(2, a)
for num in range(a, b+1):
    for i in range(2, int(num**0.5) + 1):
        if num%i == 0:
            break
    else:
        print(num)
