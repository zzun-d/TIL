N = int(input())
has = set(map(int, input().split()))
M = int(input())
for n in map(int, input().split()):
    if has.intersection({n}):
        print(1, end=' ')
    else:
        print(0, end=' ')