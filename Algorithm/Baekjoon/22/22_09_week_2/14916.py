N = int(input())
b_c = N // 5
while True:
    if b_c < 0:
        print(-1)
        break
    if (N - (5*b_c)) % 2:
        b_c -= 1
    else:
        print(b_c + (N-5*b_c)//2)
        break