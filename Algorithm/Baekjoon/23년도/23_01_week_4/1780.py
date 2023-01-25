import sys

def input():
    return sys.stdin.readline().rstrip()


def cut(x, y, n):
    std = arr[x][y]
    for i in range(x, x+n):
        for j in range(y, y+n):
            if arr[i][j] != std:
                b = n // 3
                for k in range(3):
                    for l in range(3):
                        cut(x + k * b, y + l * b, b)
                return
    
    answer[std] += 1


N = int(input())

arr = [list(map(int, input().split())) for _ in range(N)]

answer= [0, 0, 0]


cut(0, 0, N)
print(answer[-1])
print(answer[0])
print(answer[1])



# 시간초과 코드
# import sys

# def input():
#     return sys.stdin.readline().rstrip()

# def check(arr):
#     std = arr[0]
#     for a in arr:
#         if std != a:
#             return False
#     return True

# def div(arr):
#     if check(arr):
#         answer[arr[0]] += 1
#     elif len(arr) == 9:
#         for a in arr:
#             answer[a] += 1
#     else:
#         l = round(len(arr)**0.5)
#         b = l // 3
#         for i in range(0, 3*b, 3):
#             for j in range(b):
#                 div(arr[i*l+b*j:i*l+b*(j+1)] + arr[(i+1)*l+b*j:(i+1)*l+b*(j+1)] + arr[(i+2)*l+b*j:(i+2)*l+b*(j+1)])


# N = int(input())
# arr = []
# answer = [0, 0, 0]
# for _ in range(N):
#     arr += list(map(int, input().split()))

# div(arr)
# print(answer[-1])
# print(answer[0])
# print(answer[1])