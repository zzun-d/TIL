import sys
def input():
    return sys.stdin.readline().rstrip()

T = int(input())
for t in range(1, T+1):
    problem = list(input())
    tmp = 0
    
    for char in problem:
        if char == '(':
            tmp += 1
        else:
            tmp -= 1
            if tmp < 0:
                break
    if tmp == 0:
        print('YES')
    else:
        print('NO')
        