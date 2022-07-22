# 유클리드 호제법

t = int(input())

for _ in range(t):
    a, b = map(int, input().split())
    ori_a, ori_b = a, b
    while a%b != 0:
        a, b = b, a%b
    print((ori_a*ori_b)//b)