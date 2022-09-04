import sys

def input():
    return sys.stdin.readline().rstrip()

case = []
while True:
    n_lst = list(map(int, input().split()))
    if n_lst[-1] == 0:
        case.append()
        tmp = input()
        if tmp:
            break
    case


