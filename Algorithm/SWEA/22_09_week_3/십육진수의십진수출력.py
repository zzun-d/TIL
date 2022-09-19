T = int(input())

for tc in range(1, T+1):
    num = input()
    num_10 = 0
    for i in range(len(num)):
        n = ord(num[i]) 
        if n - 64 > 0:
            num_10 += (n - 54) * (16**(len(num)-(i+1)))
        else:
            num_10 += (n - 48) * (16**(len(num)-(i+1)))


