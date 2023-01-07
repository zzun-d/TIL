N = int(input())
ans = 0
for num in map(int, input().split()):
    if num < 2:
        continue
    for i in range(2, int(num**0.5)+1):
        if num%i == 0:
            break
    else:
        ans += 1
print(ans)