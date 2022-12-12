N = int(input())
x = 1
cnt = 1
while N > x:
    x += 6*cnt
    cnt += 1
print(cnt)